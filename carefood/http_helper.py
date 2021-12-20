from carefood.config import Config
import requests
from typing import Dict
import random


def get_proxy(url: str) -> Dict[str, str] or None:
    """ Функция для получения прокси к источнику
    Input : https://carefood.kz/
    Output : {'http://': '37.235.24.166:5678', 'https://': '37.235.24.166:5678'}
    """
    proxy_list = Config.PROXIES
    if not bool(proxy_list):
        return
    random_proxy = random.choice(proxy_list)
    for i in range(len(proxy_list)):
        try:
            r = requests.get(url, proxies=random_proxy, timeout=10)
            if r.status_code == 200:
                return random_proxy
        except Exception as e:
            print(e)
            random_proxy = random.choice(proxy_list)
    else:
        return None
