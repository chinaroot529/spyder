from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import requests
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException
import certifi
import httpx
import time
save_folder = "C:\dataset\中国人民法院典型案例"
# 设置ChromeDriver的路径
chrome_path = r"C:\chromedriver-win32\chromedriver.exe"
# 设置ChromeDriver的执行路径
chrome_service = ChromeService(chrome_path)
headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
}
# 定义函数来保存案例为HTML文件
def save_case_to_html(title, content, date):
    filename = os.path.join(save_folder, f"{title}.html")
    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"<h1>{title}</h1>")
        file.write(f"<p>Date: {date}</p>")
        file.write(content.decode("utf-8"))  # 解码字节码为字符串

# 定义函数提取详细内容并保存为HTML文件
def extract_detail_and_save(case_link, case_title):
    # 发送GET请求获取案例详情页
    case_response = httpx.get(url=case_link, headers=headers, timeout=10, verify=False)
    case_soup = BeautifulSoup(case_response.text, "html.parser")

    # 提取标题
    title = case_title

    # 提取日期
    date_element = case_soup.find('span', class_='date')
    date = date_element.get_text() if date_element else "未知日期"

    # 提取内容
    detail_content = case_soup.find('div', class_='wzinfo')
    content = detail_content.encode_contents() if detail_content else "没有内容"
    # 保存为HTML文件
    save_case_to_html(title, content, date)

# 创建Chrome浏览器实例
chrome_options = Options()
chrome_options.add_argument("--headless")  # 无头模式，不显示浏览器界面
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# 发送GET请求
url = 'http://alk.12348.gov.cn/LawSelect/SearchIndex?checkDatabaseID=74%2C75%2C76%2C77'
driver.get(url)

def getElement():
    # 等待元素出现，最长等待时间为10秒
    wait = WebDriverWait(driver, 10)
    sortlist_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'sortlist')))

    # 获取sortlist元素下所有的tr元素
    tr_elements = sortlist_element.find_elements(By.TAG_NAME, 'tr')

    # 遍历tr元素，提取href和title属性
    for tr_element in tr_elements:
        try:
            # Adjusted XPath to locate the 'a' element
            a_element = tr_element.find_element(By.XPATH, './/td[1]/a')
            case_link = a_element.get_attribute('href')
            case_title = a_element.get_attribute('title')
            
            # 提取详细内容并保存为HTML文件
            extract_detail_and_save(case_link, case_title)
            print(f'{case_title}爬取成功')
            time.sleep(1)
        except:
            # Handle the case where 'a' element is not found in the current 'tr'
            print("")

# 循环遍历页面
while True:
    try:
        getElement()
        # 尝试找到下一页按钮
        next_page_button = driver.find_element(By.CLASS_NAME, 'page-next')
        # 点击下一页按钮
        next_page_button.click()
        time.sleep(2)
        # 等待下一页元素出现，最长等待时间为10秒
        wait = WebDriverWait(driver, 10)
        sortlist_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'sortlist')))
    except NoSuchElementException:
        print("爬取完毕")
        break  # 结束循环

# 关闭浏览器
driver.quit()

