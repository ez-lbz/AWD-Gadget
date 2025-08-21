import requests
def shellcode(flag):

    url = 'https://ctf.bugku.com/pvp/submit.html?token=53315c5e6d630d542017c41e13f85b98&flag=' + flag

    response = requests.post(url)

    return response.status_code
