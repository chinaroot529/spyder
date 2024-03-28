import os
import pymysql
from datetime import datetime
from bs4 import BeautifulSoup

# 数据库连接参数
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'xjhxjhxjh520',
    'database': 'hjai',
}

# 创建数据库连接
conn = pymysql.connect(**db_config)

# 创建游标对象
cursor = conn.cursor()

# 表名
cases_table = 'Cases'
editors_table = 'Editors'

# 数据来源
data_source = "最高人民法院"

# 文件夹路径
folder_path = "/Volumes/xiejunhao/学习资料/数据处理/最高法测试数据集"  # 替换为实际文件夹路径

# 遍历文件夹中的 HTML 文件
for filename in os.listdir(folder_path):
    if filename.endswith(".html"):
        file_path = os.path.join(folder_path, filename)

        # 从文件中读取 HTML 内容并解析所需信息
        with open(file_path, "r", encoding="utf-8") as file:
            html_content = file.read()

        soup = BeautifulSoup(html_content, 'lxml')

        # 示例：从 HTML 解析标题（根据实际 HTML 结构调整选择器）
        title = soup.find('h1').text.strip() if soup.find('h1') else '未知标题'

        # 示例：从 HTML 解析法庭名称（根据实际 HTML 结构调整选择器）
        court_name = soup.find('div', class_='court-name').text.strip() if soup.find('div', class_='court-name') else '未知法庭'

        # 示例：从 HTML 解析关键词（根据实际 HTML 结构调整选择器）
        keywords = soup.find('div', class_='keywords').text.strip() if soup.find('div', class_='keywords')else '未知关键词'

        editor_name = soup.find('div', class_='editor-name').text.strip() if soup.find('div', class_='editor-name') else '未知编辑'

        # 查找包含发布时间的 <li> 元素
        time_element = soup.find('li', class_='fl', string=lambda text: '发布时间' in text)
        if time_element:
            # 提取时间字符串
            case_date = time_element.text.replace('发布时间：', '').strip()
        else:
            case_date = datetime.now().strftime('%Y-%m-%d')

        # 获取当前时间戳
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # 插入编辑信息到编辑信息表（如果不存在）
        try:
            editor_insert_query = f"INSERT INTO {editors_table} (EditorName) VALUES (%s) ON DUPLICATE KEY UPDATE EditorName=VALUES(EditorName)"
            cursor.execute(editor_insert_query, (editor_name,))
            conn.commit()
        except Exception as e:
            print(f"Error inserting editor {editor_name} into the database: {e}")

        # 获取刚插入的编辑的ID
        cursor.execute(f"SELECT EditorID FROM {editors_table} WHERE EditorName = %s", (editor_name,))
        editor_id = cursor.fetchone()[0]

        # 插入案例信息到案例表
        try:
            case_insert_query = f"INSERT INTO {cases_table} (Title, Date, Source, Content, CourtName, Keywords, EditorID, CreateTime, UpdateTime) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(case_insert_query, (title, case_date, data_source, html_content, court_name, keywords, editor_id, current_time, current_time))
            conn.commit()
            print(f"Inserted case '{title}' from '{filename}' into the database.")
        except Exception as e:
            print(f"Error inserting case from '{filename}' into the database: {e}")

cursor.close()
conn.close()