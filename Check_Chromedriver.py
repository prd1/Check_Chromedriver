import os
import re
import zipfile
from urllib import request
import platform

from bs4 import BeautifulSoup
import requests

from libs import deal_parse, deal_reg, deal_zip


def check_os():
    return platform.system()


def check_driver():
    try:
        read_ver = read_version()
        if new_version != read_ver:
            return False
        return True
    except Exception:
        return False


def make_dir():
    try:
        os.makedirs(driver_mother_path)
    except OSError as e:
        if e.errno != 17:
            raise


def write_version(latest_version):
    with open(driver_mother_path + "/version.txt", "wt") as f:
        f.write(latest_version)


def read_version():
    with open(driver_mother_path + "/version.txt", "rt") as f:
        result = f.read()
    return result


def main():
    if check_driver():
        # print chromedriver version
        return
    make_dir()
    download_path = os.path.join(driver_mother_path, "chromedriver.zip")
    print("Downloading...")
    request.urlretrieve(down_url, download_path)
    print("Download Complete!")
    deal_zip.unzip(download_path)
    deal_zip.remove_zip(download_path)
    write_version(new_version)


os_name = check_os()
driver_mother_path = "./chromedriver/"
temp = deal_parse.parse_download_URL(os_name)
down_url = temp[0]
new_version = temp[1]

if __name__ == "__main__":
    check_driver()
