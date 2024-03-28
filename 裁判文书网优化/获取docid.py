import json
import requests
import execjs
import re

cookies1 = {
    '_bl_uid': 'szlC2nLak6dcRzzhtry6n6C5tzb3',
    'UM_distinctid': '18beab1fc05581-007861c8782bcc-4c657b58-144000-18beab1fc06a64',
    'wzws_sessionid': 'oGVdvfuAMjIyLjIwMC4yNTQuMTk5gmQyOTQ3Y4FjMDJmY2E=',
    'HOLDONKEY': 'NjA1MzY3NzYtZWM3NS00YzVlLWExMzQtYTQ2MzVlNjUwMjg0',
}

headers1 = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': '_bl_uid=szlC2nLak6dcRzzhtry6n6C5tzb3; UM_distinctid=18beab1fc05581-007861c8782bcc-4c657b58-144000-18beab1fc06a64; wzws_sessionid=oGVdvfuAMjIyLjIwMC4yNTQuMTk5gmQyOTQ3Y4FjMDJmY2E=; HOLDONKEY=NjA1MzY3NzYtZWM3NS00YzVlLWExMzQtYTQ2MzVlNjUwMjg0',
    'Origin': 'https://account.court.gov.cn',
    'Referer': 'https://account.court.gov.cn/app?back_url=https%3A%2F%2Faccount.court.gov.cn%2Foauth%2Fauthorize%3Fresponse_type%3Dcode%26client_id%3Dzgcpwsw%26redirect_uri%3Dhttps%253A%252F%252Fwenshu.court.gov.cn%252FCallBackController%252FauthorizeCallBack%26state%3D40df2b58-ed46-4d66-968e-23db05405826%26timestamp%3D1700792512778%26signature%3D961846AAF245CA7BAAEBB3541AEB674FF09694C9C3ACD87FA7E0A16272AF7E1E%26scope%3Duserinfo',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data1 = {
    'username': '15696827069',
    'password': 'JwVcSqb5%2BKHLEjAESbK3RBqGsJPoWN4opzCBe2kUTpnhoe3RjTUvK6ET5hbdM7gn4KkFWF4JlmwObOtA0RtDzQwzw%2FF2Fv1s5HMHpc7Y5iJ96EyiTdvwf%2Bizjzppa0jElJ22VS3Cj0amwgzhGlRGvdu7Jr76rXaJUhhPiQQHlR1aluiGrRoiYM%2FD4xNfL8ppx1vbBJxwsAZlvAbYWAzIEhYfd7Vkq%2FTCj8bo4MbSHMsEhpMyelMMnJDWQFHVatYN0edfgBrku3%2B5CWHTSWyLuT8YfXy5HSD3znvDYsWuK77bRQebwPDqUyB30M5Gcg7l9NLiJAYFRpJZXdWDK8rJkw%3D%3D',
    'appDomain': 'wenshu.court.gov.cn',
}

##response1 = requests.post('https://account.court.gov.cn/api/login', cookies=cookies1, headers=headers1, data=data1)

##print((response1.text))
##模拟登录

##获取docid
cookies = {
    'UM_distinctid': '18beab1fc05581-007861c8782bcc-4c657b58-144000-18beab1fc06a64',
    'wzws_sessionid': 'gDIyMi4yMDAuMjU0LjIwMII2ZjY5MDGBYzAyZmNhoGVdvfo=',
    'SESSION': 'c0f12763-05e3-4d63-af86-3c7bfe6ee882',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'UM_distinctid=18beab1fc05581-007861c8782bcc-4c657b58-144000-18beab1fc06a64; wzws_sessionid=gDIyMi4yMDAuMjU0LjIwMII2ZjY5MDGBYzAyZmNhoGVdvfo=; SESSION=c0f12763-05e3-4d63-af86-3c7bfe6ee882',
    'Origin': 'https://wenshu.court.gov.cn',
    'Referer': 'https://wenshu.court.gov.cn/website/wenshu/181217BMTKHNT2W0/index.html?pageId=92221103155552bc91fbc4735f52aed6&s38=J00&fymc=%E5%B9%BF%E4%B8%9C%E7%9C%81%E9%AB%98%E7%BA%A7%E4%BA%BA%E6%B0%91%E6%B3%95%E9%99%A2',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
m = 1

while m<10:
    i = 0
    data = {
        'pageId': '92221103155552bc91fbc4735f52aed6',
        's38': 'J00',
        'fymc': '广东省高级人民法院',
        'sortFields': 's50:desc',
        'ciphertext': '1100110 110111 1111001 1100100 1000101 1011000 1010010 1010010 1101111 1101001 1100111 1101111 1101010 1111001 1010010 1000100 1010010 1001101 1010100 1001101 1100010 110110 1000011 1000111 110010 110000 110010 110011 110001 110000 110010 110100 110111 1000011 1101110 110010 1010001 1100010 110001 1110100 1001101 1000110 1000010 1110000 1100100 1110101 1000101 1100111 1111001 111000 1111010 1101100 1001101 1110111 111101 111101',
        'pageNum': m,
        'pageSize': '5',
        'queryCondition': '[{"key":"s38","value":"J00"}]',
        'cfg': 'com.lawyee.judge.dc.parse.dto.SearchDataDsoDTO@queryDoc',
        '__RequestVerificationToken': '2I7Xcn6vQ27IxHW4DdBub0Gh',
        'wh': '750',
        'ww': '1488',
        'cs': '0',
    }

    response = requests.post('https://wenshu.court.gov.cn/website/parse/rest.q4w', cookies=cookies, headers=headers, data=data)
    a = "20231024"
    with open('./js测试.js', 'r', encoding='utf-8') as f:
        js_file = f.read()

    ctx = execjs.compile(js_file).call('decrypt',response.json()["result"],response.json()["secretKey"],a)
    data = json.loads(ctx)
    queryResult = (data['queryResult'])
    resultLitst = (queryResult['resultList'])



    while i<5:
        rowkey = resultLitst[i].get('rowkey')
        i = i+1

#发送用户名文件post

        cookies = {
            'UM_distinctid': '18beab1fc05581-007861c8782bcc-4c657b58-144000-18beab1fc06a64',
            'wzws_sessionid': 'gDIyMi4yMDAuMjU0LjIwMII2ZjY5MDGBYzAyZmNhoGVdvfo=',
            'SESSION': 'c0f12763-05e3-4d63-af86-3c7bfe6ee882',
        }

        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'Cookie': 'UM_distinctid=18beab1fc05581-007861c8782bcc-4c657b58-144000-18beab1fc06a64; wzws_sessionid=gDIyMi4yMDAuMjU0LjIwMII2ZjY5MDGBYzAyZmNhoGVdvfo=; SESSION=c0f12763-05e3-4d63-af86-3c7bfe6ee882',
            'Origin': 'https://wenshu.court.gov.cn',
            'Referer': 'https://wenshu.court.gov.cn/website/wenshu/181107ANFZ0BXSK4/index.html?docId=DJhb2Ojc+NL8s5xhi0GEiDtHqUJk+vJbHbXqOvIA6YKxgNt3FIy4hPUKq3u+IEo4wmPlPV9lomLT7ekz5XaM1rSpRY2UzxVuYpVg/IeRyx5hIDjsW2IJUjtRDleKzjJY',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        data = {
            'docId': rowkey,
            'cfg': 'com.lawyee.wbsttools.web.parse.dto.AppUserDTO@currentUser',
            '__RequestVerificationToken': 'YeaTajWwkfDcqRpCEsDTfStV',
            'wh': '750',
            'ww': '723',
            'cs': '0',
        }

        send_user = requests.post('https://wenshu.court.gov.cn/website/parse/rest.q4w', cookies=cookies, headers=headers, data=data)

        cookies = {
            'UM_distinctid': '18beab1fc05581-007861c8782bcc-4c657b58-144000-18beab1fc06a64',
            'wzws_sessionid': 'gDIyMi4yMDAuMjU0LjIwMII2ZjY5MDGBYzAyZmNhoGVdvfo=',
            'SESSION': 'c0f12763-05e3-4d63-af86-3c7bfe6ee882',
        }

        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'Cookie': 'UM_distinctid=18beab1fc05581-007861c8782bcc-4c657b58-144000-18beab1fc06a64; wzws_sessionid=gDIyMi4yMDAuMjU0LjIwMII2ZjY5MDGBYzAyZmNhoGVdvfo=; SESSION=c0f12763-05e3-4d63-af86-3c7bfe6ee882',
            'Origin': 'https://wenshu.court.gov.cn',
            'Referer': 'https://wenshu.court.gov.cn/website/wenshu/181107ANFZ0BXSK4/index.html?docId=DJhb2Ojc+NL8s5xhi0GEiDtHqUJk+vJbHbXqOvIA6YKxgNt3FIy4hPUKq3u+IEo4wmPlPV9lomLT7ekz5XaM1rSpRY2UzxVuYpVg/IeRyx5hIDjsW2IJUjtRDleKzjJY',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        data = {
            'docId': rowkey,
            'ciphertext': '1001011 110001 110111 110001 110101 1101010 1101001 1111010 1010000 1101010 1101111 1100010 111001 1110101 1100111 1001010 1111001 1101001 1101101 1000111 1100110 1100101 1110000 1110111 110010 110000 110010 110011 110001 110000 110010 110100 1111001 1101010 110010 1011001 110101 1101010 1010111 1010101 1010110 110001 1010101 1010100 1001100 1110011 1110001 1100110 1010011 111001 1001100 1010101 1100010 1010001 111101 111101',
            'cfg': 'com.lawyee.judge.dc.parse.dto.SearchDataDsoDTO@docInfoSearch',
            '__RequestVerificationToken': 'YeaTajWwkfDcqRpCEsDTfStV',
            'wh': '750',
            'ww': '723',
            'cs': '0',
        }

        response3 = requests.post('https://wenshu.court.gov.cn/website/parse/rest.q4w', cookies=cookies, headers=headers, data=data)
        a = "20231024"

        with open('./js测试.js', 'r', encoding='utf-8') as f:
            js_file = f.read()

        ctx = execjs.compile(js_file).call('decrypt',response3.json()["result"],response3.json()["secretKey"],a)
        sulute = re.sub('\<.*?\>', "", ctx)
        sulute = re.sub('&nbsp;', "\n", ctx)
        sulute = re.sub('&ensp;', "\n", ctx)
        print(sulute)
        count = 0
        count = count+1
    m = m+1

print(count)
