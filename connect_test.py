#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 10:52:21 2024

@author: zhuidexiaopengyou
"""

import requests

API_URL = "http://127.0.0.1:5000/api/items"
API_URLs = "http://127.0.0.1:5000/api/leftPageData"

def test_get_items():
    response = requests.get(API_URL)
    if response.status_code == 200:
        print("GET Request Successful")
        print(response.json())
    else:
        print("GET Request Failed", response.status_code)


def test():
    response = requests.get(API_URLs)
    if response.status_code == 200:
        print("GET Request Successful")
        print(response.json())
    else:
        print("GET Request Failed", response.status_code)

if __name__ == "__main__":
    test()  # 测试GET请求
    

