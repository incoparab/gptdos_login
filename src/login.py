'''
Author: fwz
e-mail: wz-fu@qq.com
Date: 2023-03-18 16:38:08
LastEditTime: 2023-03-27 26:28:31
Description: 自动签到gptdos
'''
import requests
import json
import sys


def login():
    url = "https://gptdos.com/api/user/info"
    refer = "https://gptdos.com/chat"
    cookie = sys.argv[1]
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
    requests.get(url=refer,
                 headers={
                     'cookie': cookie,
                     'refer': refer,
                     'user-agent': user_agent
                 })

    response = requests.get(url=url,
                            headers={
                                'cookie': cookie,
                                'refer': refer,
                                'user-agent': user_agent
                            })
    jsonData = json.loads(response.text)
    try:
        msg = jsonData['data']['userInfo']['tokens_available']
    except Exception:
        msg = 'cookie失效'

    key = sys.argv[2]
    title = 'GPTDOS消息'
    msg = str(msg)
    sendurl = f'http://www.pushplus.plus/send?token={key}&title={title}&content={msg}'
    requests.get(url=sendurl)


if __name__ == "__main__":
    login()
