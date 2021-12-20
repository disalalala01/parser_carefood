from carefood import producer
import requests
from bs4 import BeautifulSoup as BS
from carefood.config import Config
from carefood.http_helper import get_proxy
from pprint import pprint
import time


def parse_product_page(session: requests.Session, url: str, sausage: bool) -> None:
    try:
        time.sleep(1)
        resp = session.get(url)
        if resp.status_code != 200:
            raise Exception(f"Status : {resp.status_code}, url: {url}")
        print(f"Send product url: {resp.url}")
        soup = BS(resp.text, "lxml")
        product_name = soup.select_one("h1.pagetitle").text.strip()
        info = soup.select_one("div.c-gruppedprops__group-props").select(
            "span.c-gruppedprops__prop"
        )

        obj = Config.OBJ

        obj["product_unit"] = soup.select_one(
            "span.c-quantity__measure.js-measurename"
        ).text.strip()
        obj["product_price"] = float(
            soup.select_one("span.c-prices__value.js-prices_pdv_Розн.Маг.Алматы")
            .text.replace(" ", "")
            .replace("тг.", "")
        )
        try:
            obj["provider"] = (
                info[0].select_one("span.c-gruppedprops__prop-value").text.strip()
            )
        except IndexError:
            obj["provider"] = product_name
        try:
            obj["composition"] = (
                info[-2].select_one("span.c-gruppedprops__prop-value").text.strip()
            )
        except IndexError:
            obj["composition"] = (
                "" if not sausage else "курица" if "кур" in product_name.lower() else ""
            )
        obj["thermal_state"] = (
            ""
            if sausage
            else "охлажденное"
            if "охл" in product_name.lower()
            else "замороженное"
        )
        obj["package"] = (
            ""
            if sausage
            else "на подложке"
            if "подлож" in product_name.lower()
            else "монолит"
        )
        obj["product_name"] = product_name

        print("SEND data: ")
        pprint(obj)
        producer.send(Config.TOPIC, obj)
        print("-" * 50)
    except Exception as e:
        print(e)


def parse_category_page(session: requests.Session, url: str, sausage: bool) -> None:
    try:
        resp = session.get(url)
        if resp.status_code != 200:
            raise Exception(f"Status : {resp.status_code}, url: {url}")
        if Config.EMPTY_MSG in resp.text:
            raise Exception(f"Empty category msg: {Config.EMPTY_MSG}, url : {url}")
        soup = BS(resp.text, "lxml")
        products = soup.find("div", id="view-showcase").find_all("div")
        for product in products:
            href = product.select_one("div.list-showcase__name").find("a").get("href")
            parse_product_page(
                session=session, url=Config.DOMAIN + href, sausage=sausage
            )
    except Exception as e:
        print(e)


def parse_collections(session: requests.Session, url: str, sausage: bool) -> None:
    """
    :param session:
    :param url:
    :param sausage:
    :return:
    """
    try:
        resp = session.get(url)
        if resp.status_code != 200:
            raise Exception(
                f"ERROR collection page: {resp.url}, status: {resp.status_code}"
            )
        soup = BS(resp.text, "lxml")
        categories = soup.select_one("ul.row.list-unstyled").select(
            "li.section.col-xs-4.col-md-3.col-lg-5rs"
        )
        for category in categories:
            parent = category.select_one("a.parent")
            if "ptitsa" in url:
                if parent.text == "Птица":
                    href = parent.get("href")
                    parse_category_page(
                        session=session, url=Config.DOMAIN + href, sausage=sausage
                    )
            else:
                href = parent.get("href")
                parse_category_page(
                    session=session, url=Config.DOMAIN + href, sausage=sausage
                )
    except Exception as e:
        print(e)


def main() -> None:
    try:
        with requests.Session() as session:
            session.headers = Config.HEADERS
            session.proxies = get_proxy(Config.DOMAIN + "/")
            r = session.get(Config.DOMAIN + "/")
            if r.status_code != 200:
                raise Exception(f"Status : {r.status_code}, URL : {Config.DOMAIN}")
            resp = session.get(Config.DOMAIN + "/catalog/")
            if resp.status_code != 200:
                raise Exception(f"Status : {r.status_code}, URL : {Config.DOMAIN}")
            soup = BS(resp.text, "lxml")
            categories = soup.select_one("div.top-nav-catalog-block-list").select("li")

            for li in categories:
                category_name = li.select_one(
                    "div.top-catalog-nav-menu-title-inner."
                    "top-nav-parent-link.has-subsection.more-sections-view"
                ).text.strip()
                if category_name == "Мясо, птица":
                    href = li.find("a").get("href")
                    url = Config.DOMAIN + href
                    parse_collections(session=session, url=url, sausage=False)
                elif category_name == "Колбасы, ветчина, сосиски, сардельки":
                    href = li.find("a").get("href")
                    url = Config.DOMAIN + href
                    parse_collections(session=session, url=url, sausage=True)
                else:
                    pass
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
