from tsdm_bot import tsdm_work
from utils import get_cookies_from_env

cookies = get_cookies_from_env()
for idx, cookie in enumerate(cookies, start=1):
    print(f"\n📌 正在为账号 {idx} 打工...")
    tsdm_work(cookie)
