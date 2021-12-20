import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    TOPIC = os.getenv("TOPIC")
    KAFKA_IP = os.getenv("IP")
    PROXIES = [
        {"http://": "72.195.34.59:4145", "https://": "72.195.34.59:4145"},
        {"http://": "8.210.163.246:50050", "https://": "8.210.163.246:50050"},
        {"http://": "77.232.154.223:5678", "https://": "77.232.154.223:5678"},
        {"http://": "77.65.163.72:4153", "https://": "77.65.163.72:4153"},
        {"http://": "41.190.57.57:5678", "https://": "41.190.57.57:5678"},
        {"http://": "37.235.24.166:5678", "https://": "37.235.24.166:5678"},
        {"http://": "41.215.10.6:4145", "https://": "41.215.10.6:4145"},
        {"http://": "45.116.114.21:5678", "https://": "45.116.114.21:5678"},
        {"http://": "36.94.83.71:5678", "https://": "36.94.83.71:5678"},
    ]
    DOMAIN = "https://carefood.kz"
    HEADERS = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ru,en;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Cookie": "_gcl_au=1.1.789826651.1634487095; PHPSESSID=e98bdis9effgla8d51v9lkjjj1; BITRIX_SM_GUEST_ID=631388; BITRIX_SM_SALE_UID=03fa7a7cbdcc3b700247a46bfec98476; BITRIX_CONVERSION_CONTEXT_s1=%7B%22ID%22%3A6%2C%22EXPIRE%22%3A1634493540%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D; _ym_uid=1634487096634505031; _ym_d=1634487096; _ym_isad=2; BX_USER_ID=d1be9a41fe4676779a401769c916b13d; _ga=GA1.2.517084633.1634487096; _gid=GA1.2.2017179756.1634487096; _fbp=fb.1.1634487096391.393305624; BITRIX_SM_LAST_VISIT=17.10.2021+22%3A11%3A52",
        "Host": "carefood.kz",
        "Pragma": "no-cache",
        "sec-ch-ua": '";Not A Brand";v="99", "Chromium";v="94"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Linux"',
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36",
    }
    EMPTY_MSG = (
        "В данном разделе товары отсутствуют. Товары появятся в ближайшее время."
    )
    OBJ = {
        "city": "Almaty",
        "shop_name": "carefood.kz",
        "shop_type": "Интернет-магазин",
        "shop_category": "",
        "stationary_view": "",
        "provider": "",
        "channel": "KA",
        "product_name": "",
        "composition": "",
        "product_unit": "",
        "package": "",
        "thermal_state": "",
        "product_price": "",
    }
