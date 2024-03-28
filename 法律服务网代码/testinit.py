import httpx
from bs4 import BeautifulSoup
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
}

res = httpx.get(url='http://alk.12348.gov.cn/LawSelect/Detail?dbID=49&dbName=RTQT&sysID=24574', headers=headers, timeout=10, verify=False)
# soup = BeautifulSoup(res.text, "html.parser")
# case_links = [a["href"] for a in soup.select("div.sortlist > table > tbody > tr > td > a")]
# print(case_links)

soup = BeautifulSoup(res.text, 'html.parser')

wzinfo_content = soup.find('div', class_='wzinfo')
print(wzinfo_content.prettify())

# print(res.text)