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


def check_driver():
    try:
        ver_path = "C:/Program Files (x86)/Google/Chrome/Application"
        read_ver = deal_txt.read_version(driver_mother_path)
        for i in os.listdir(ver_path):
            local_ver = deal_reg.reg_dir(i)
            re_read_ver = deal_reg.reg_dir(read_ver)
            if local_ver == re_read_ver:
                print("your_ver : {}".format(i))
                print("latest_ver : {}".format(read_ver))
                return True
    except Exception as e:
        print(e)
        return False


def make_dir():
    try:
        os.makedirs(driver_mother_path)
    except OSError as e:
        if e.errno != 17:
            raise


def main():
    if check_driver():
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

