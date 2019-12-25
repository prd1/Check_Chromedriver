import os
import re
import zipfile
from urllib import request
import platform
import datetime

from bs4 import BeautifulSoup
import requests

from libs import deal_parse, deal_reg, deal_zip, deal_txt


def check_os():
    return platform.system()


def check_local_driver():
    try:
        ver_path = "C:/Program Files (x86)/Google/Chrome/Application"
        for i in os.listdir(ver_path):
            local_ver = deal_reg.reg_dir(i)
            print("chrome_browser_ver : {}".format(i))
            return local_ver
    except Exception:
        print("You do not have Chrome browser.")


def compare_driver():
    local_ver = check_local_driver()
    read_ver = deal_txt.read_version(driver_mother_path)
    re_read_ver = deal_reg.reg_dir(read_ver)
    print("chromedriver_ver : {}".format(read_ver))
    if re_read_ver == local_ver:
        return True


def make_dir():
    try:
        os.makedirs(driver_mother_path)
    except OSError as e:
        if e.errno != 17:
            raise


def main():
    if compare_driver():
        # print chromedriver version
        return
    make_dir()
    download_path = os.path.join(driver_mother_path, "chromedriver.zip")
    print("Downloading...")
    request.urlretrieve(down_url, download_path)
    print("Download Complete!")
    deal_zip.unzip(driver_mother_path, download_path)
    deal_zip.remove_zip(download_path)
    deal_txt.write_version(driver_mother_path, new_version)


os_name = check_os()
driver_mother_path = "./chromedriver/"
temp = deal_parse.parse_download_URL(os_name)
down_url = temp[0]
new_version = temp[1]

if __name__ == "__main__":
    # check_driver()
    main()
    # check_local_driver()

