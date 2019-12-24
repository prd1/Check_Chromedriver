import requests
from bs4 import BeautifulSoup

from libs import deal_reg

BASE_URL = "https://chromedriver.chromium.org/"


def get_to_URL(url):
    req = requests.get(url)
    if req.status_code == 200 and req.ok:
        return req
    else:
        print("request error")


def parse_download_URL(os_name):
    if os_name == "Linux":
        down_name = "chromedriver_linux64.zip"
    else:
        down_name = "chromedriver_win32.zip"
    base_req = get_to_URL(BASE_URL)
    base_soup = BeautifulSoup(base_req.content, "html.parser")

    driver_version = parse_driver_version(base_soup)
    download_url = "/".join(
        ["https://chromedriver.storage.googleapis.com", driver_version, down_name,]
    )
    return download_url, driver_version


def parse_driver_version(soup):
    # print(soup)
    li = soup.select(".sites-layout-tile.sites-tile-name-content-1 > div li")
    href = li[0].select_one("a")["href"]
    version = deal_reg.regrex_version(href)
    # https://chromedriver.storage.googleapis.com/78.0.3904.105/chromedriver_win32.zip
    return version
