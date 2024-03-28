from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import os
import requests
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException
import certifi
import httpx
save_folder = "C:\dataset\中国人民法院典型案例"
# 设置ChromeDriver的路径
chrome_path = r"C:\chromedriver-win32\chromedriver.exe"
# 设置ChromeDriver的执行路径
chrome_service = ChromeService(chrome_path)

# 创建Chrome浏览器实例
chrome_options = Options()
# chrome_options.add_argument("--headless")  # 无头模式，不显示浏览器界面
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# 发送GET请求
url = 'http://alk.12348.gov.cn/LawSelect/SearchIndex?checkDatabaseID=48%2C49'
driver.get(url)

def findelement():
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
            print(case_title)
            time.sleep(1)
        except:
            # Handle the case where 'a' element is not found in the current 'tr'
            print("")
# 循环遍历页面
while True:
    findelement()
    # 尝试找到下一页按钮
    next_page_button = driver.find_element(By.CLASS_NAME, 'page-next')
    # 点击下一页按钮
    next_page_button.click()
    time.sleep(2)
    # 等待下一页元素出现，最长等待时间为10秒
    wait = WebDriverWait(driver, 10)
    sortlist_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'sortlist')))
    if not next_page_button:
        # 如果找不到下一页按钮，说明已经到达最后一页
        print("爬取完毕")
        break  # 结束循环

# 关闭浏览器
driver.quit()

