#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 10:44:26 2024

@author: zhuidexiaopengyou
"""

from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:8000"}})

def create_db_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='xjhxjhxjh520',
            database='hjai',
        )
        return connection
    except Error as e:
        print(f"The error '{e}' occurred")



@app.route('/api/leftPageData', methods=['GET'])
def get_left_page_data():
    connection = create_db_connection()
    if connection is not None:
        cursor = connection.cursor(dictionary=True)
        try:
            # 查询标题和对应的内容
            cursor.execute("SELECT Title, Content FROM Cases")  # 'Cases' 是你的表名
            rows = cursor.fetchall()
            # 从数据库中提取所有标题和内容
            titles_and_contents = [{'title': row['Title'], 'content': row['Content']} for row in rows]
        except Error as e:
            print(f"An error occurred: {e}")
            titles_and_contents = []  # 如果查询失败，使用空列表作为回退
        finally:
            cursor.close()
            connection.close()
    else:
        titles_and_contents = []  # 如果数据库连接失败，也使用空列表作为回退

    # 构建和返回期望的JSON结构，包括静态数据和动态查询到的标题及内容数据
    return jsonify({
        'accessFrequency': 1200,
        'peakFlow': 300,
        'trafficSitua': {
            'timeList': ['9:00', '12:00', '15:00', '18:00', '21:00', '00:00'],
            'outData': [502.84, 205.97, 332.79, 281.55, 398.35, 214.02],
            'inData': [281.55, 398.35, 214.02, 179.55, 289.57, 356.14],
        },
        'recommendSitua': {
            'data': [{'title': row['Title'], 'content': row['Content']} for row in rows]  # 包含标题和内容的列表
        }
    })


# 为了简化示例，省略了更新和删除接口的实现

if __name__ == '__main__':
    app.run(debug=True)
