import requests
from bs4 import BeautifulSoup
import pandas as pd

try : 
    from libs import deal_reg
except Exception :
    from Check_Chromedriver.libs import deal_reg


BASE_URL = "https://chromedriver.chromium.org/downloads"
BASE_URL2 = "https://googlechromelabs.github.io/chrome-for-testing/"


def get_to_URL(url):
    req = requests.get(url)
    if req.status_code == 200 and req.ok:
        return req
    else:
        print("request error")


def parse_driver_version():
    base_req = get_to_URL(BASE_URL)
    base_soup = BeautifulSoup(base_req.content, "html.parser")

    atags = base_soup.select("a")

    return atags

def parse_driver_version2():
    reqs = requests.get(BASE_URL2)
    soup = BeautifulSoup(reqs.text, 'html.parser')

    tables = soup.find_all('table')

    table_list = []
    for table in tables:
        df = pd.read_html(str(table))[0]
        table_list.append(df)

    # table_list now contains all tables from the website as pandas DataFrames.
    df = pd.concat(table_list).query('Binary=="chromedriver" & Platform=="win64"')
    df = df[df['HTTP status'] == 200]
    df['version'] = [u.split('/')[-3] for u in df['URL'].values]
    df['version_short'] = [u.split('.')[0] for u in df['version']]

    return df

def parse_download_URL2(local_browser_ver_code):
    version_df = parse_driver_version2()
    for version_code in version_df['version_short']:
        if version_code==local_browser_ver_code:
            download_url = version_df.query('version_short==@version_code')['URL'].iloc[0]
            return download_url, version_code


def parse_download_URL(local_browser_ver_code):
    atags = parse_driver_version()

    for a in atags:
        # print(a.text)
        version = deal_reg.reg_from_atags(a.text)
        if deal_reg.is_version(version):
            version_code = deal_reg.reg_version_code(version)
            if version_code == local_browser_ver_code:
                download_url = "/".join(
                    [
                        "https://chromedriver.storage.googleapis.com",
                        version,
                        "chromedriver_win32.zip",
                    ]
                )
                return download_url, version


# def parse_driver_version(soup):
#     # print(soup)
#     li = soup.select(".sites-layout-tile.sites-tile-name-content-1 > div li")
#     href = li[0].select_one("a")["href"]
#     version = deal_reg.regrex_version(href)
#     # https://chromedriver.storage.googleapis.com/78.0.3904.105/chromedriver_win32.zip
#     return version
