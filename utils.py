import os
import re
import sys

def get_cookies_from_env(env_key="COOKIE"):
    if env_key in os.environ:
        cookie_list = re.split(r'\n|&&', os.environ[env_key].strip())
        cookie_list = [ck.strip() for ck in cookie_list if ck.strip()]
        return cookie_list
    else:
        print(f"❌未检测到环境变量：{env_key}")
        sys.exit(0)
