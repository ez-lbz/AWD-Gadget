import requests
import json

def shellcode(flag):
    headers = {
        'Accept': 'application/json',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Content-Type': 'application/json',
        'Csrf-Token': 'a1754d87ee3340c16233a90bb675ae97d429e8496b71e3459060db3b36cef0a9',
        'Origin': 'https://buuoj.cn',
        'Priority': 'u=0',
        'Referer': 'https://buuoj.cn/challenges',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:141.0) Gecko/20100101 Firefox/141.0',
    }

    cookies = {
        'session': '30b07e92-56c0-4145-95d9-54367f8d6167.IW3DcCfdqrnlmU0k4YnbuPI9Ejk',
        'mydas_next_url': 'https://buuoj.cn/challenges?',
        'next': '/challenges?',
    }

    data = json.dumps({
        "challenge_id": 1929,
        "submission": flag
    }, indent=4)

    url = 'http://buuoj.cn/api/v1/challenges/attempt'

    response = requests.post(url, headers=headers, cookies=cookies, data=data)

    return response.status_code
