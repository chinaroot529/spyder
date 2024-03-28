import os
import pymysql
from datetime import datetime


# 数据库连接参数
db_config = {
    'host': '183.56.242.219',
    'user': 'collect_group',
    'password': 'lab-123456',
    'database': 'huge_law',
    'port': 9030,
}

# 创建数据库连接
conn = pymysql.connect(**db_config)

# 创建游标对象
cursor = conn.cursor()

# 表名
table_name = 'data_collecting_test'

# 数据来源
data_source = "裁判文书网"

# 文件夹路径
folder_path = "/Applications/学习资料/数据处理/最高人民法院典型案例"  # 替换为实际文件夹路径
id = 1

# 遍历文件夹中的 HTML 文件
for filename in os.listdir(folder_path):
    if filename.endswith(".html"):
        file_path = os.path.join(folder_path, filename)

        # 从文件中读取 HTML 内容
        with open(file_path, "r", encoding="utf-8") as file:
            html_content = file.read()

        # 获取当前时间戳
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # 插入 HTML 内容到数据库中
        try:
            # 使用参数化查询
            insert_query = f"INSERT INTO {table_name} (id, data_source, document_content_1, create_time, update_time) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(insert_query, (id, data_source, html_content[:50000], current_time, current_time))
            
            # 如果内容长度超过50000，插入第二块
            if len(html_content) > 50000:
                insert_query_2 = f"UPDATE {table_name} SET document_content_2 = %s WHERE id = %s"
                cursor.execute(insert_query_2, (html_content[50000:], id))
            
            conn.commit()
            print(f"Inserted {filename} into the database.")
            id += 1
        except Exception as e:
            print(f"Error inserting {filename} into the database: {e}")

# 关闭游标和连接
cursor.close()
conn.close()
