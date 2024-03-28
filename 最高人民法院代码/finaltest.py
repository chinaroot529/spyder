import os
import requests
from bs4 import BeautifulSoup
import certifi
import time
# 设置初始页面链接和保存文件夹
base_url = "https://www.court.gov.cn/zixun/gengduo/104.html"
save_folder = "典型案例"
next_page_num = 2
save_folder = "/Volumes/xiejunhao/学习资料/数据处理/最高法测试数据集"
# 创建保存文件夹
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

# 定义函数来保存案例为HTML文件
def save_case_to_html(title, content, date):
    filename = os.path.join(save_folder, f"{title}.html")
    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"<h1>{title}</h1>")
        file.write(f"<p>Date: {date}</p>")
        file.write(content.decode("utf-8"))  # 解码字节码为字符串
    print(f'{case_title}写入完毕')

# 定义函数提取详细内容并保存为HTML文件
def extract_detail_and_save(case_link,case_title):
    # 发送GET请求获取案例详情页
    case_response = requests.get(case_link, verify=certifi.where())
    case_soup = BeautifulSoup(case_response.text, "html.parser")
    print(f'{case_title}获取成功')
    # 提取标题
    title = case_title if case_title else '未命名'

    # 提取日期
    date_element = case_soup.find('span', class_='date')
    date = date_element.get_text() if date_element else "未知日期"

    # 提取内容
    detail_content = case_soup.find('div', class_='detail')
    content = detail_content.encode_contents() if detail_content else "没有内容"
    # 保存为HTML文件
    save_case_to_html(title, content, date)

# 循环遍历页面
while base_url:
    # 发送GET请求
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, "html.parser")
    # 找到当前页面的所有案例链接
    case_links = [a["href"] for a in soup.select("div.sec_list > ul > li > a")]
    case_titles = [a["title"] for a in soup.select("div.sec_list > ul > li > a")]
    # 遍历并保存每个案例
    for index, (case_link, case_title) in enumerate(zip(case_links, case_titles), start=1):
        case_link = "https://www.court.gov.cn" + case_link
        case_title = case_title.replace(':', '').replace('\n', '').replace('\\', '').replace(' ', '').replace('\t', '')
        print(case_title)
        # 提取详细内容并保存为HTML文件
        extract_detail_and_save(case_link,case_title)
        #每爬取一个网页停一秒
        time.sleep(1)

    # 获取下一页链接
    next_page = soup.find("li", class_="next")
    if next_page:
        # 提取当前页面的数字部分并自增
        base_url = f"https://www.court.gov.cn/zixun/gengduo/104_{next_page_num}.html"
        next_page_num += 1
        print(base_url, '开始爬取')
    else:
        base_url = None
    #爬完一页停两秒
    time.sleep(2)
print("爬取完成！")
