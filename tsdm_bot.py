import httpx
import re
import urllib.parse
import time
from bs4 import BeautifulSoup

def tsdm_check_in(cookie):
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Cookie": cookie,
        "Referer": "https://www.tsdm39.com/forum.php"
    }

    with httpx.Client(headers=headers) as client:
        response = client.get("https://www.tsdm39.com/forum.php")
        match = re.search(r'formhash=(.+?)"', response.text)
        if not match:
            print("formhash 获取失败，跳过")
            return
        formhash = urllib.parse.quote(match.group(1))
        payload = {
            "formhash": formhash,
            "qdxq": "kx",
            "qdmode": "3",
            "todaysay": "",
            "fastreply": "1"
        }
        response = client.post(
            "https://www.tsdm39.com/plugin.php?id=dsu_paulsign%3Asign&operation=qiandao&infloat=1&sign_as=1&inajax=1",
            data=payload
        )
        print("签到完成")

def tsdm_work(cookie):
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'cookie': cookie,
        'referer': 'https://www.tsdm39.net/plugin.php?id=np_cliworkdz:work',
        'x-requested-with': 'XMLHttpRequest',
        'content-type': 'application/x-www-form-urlencoded'
    }

    with httpx.Client(headers=headers) as client:
        response = client.get("https://www.tsdm39.com/plugin.php?id=np_cliworkdz%3Awork&inajax=1")
        if "您需要等待" in response.text:
            print("打工冷却中")
            return
        for i in range(6):
            client.post("https://www.tsdm39.com/plugin.php?id=np_cliworkdz:work", data={"act": "clickad"})
            print(f"🛠打工中... 第 {i+1} 次")
            time.sleep(3)
        client.post("https://www.tsdm39.com/plugin.php?id=np_cliworkdz:work", data={"act": "getcre"})
        print("打工完成")
