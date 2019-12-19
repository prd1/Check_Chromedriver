from setuptools import setup, find_packages
import os

with open("./Check_Chromedriver/README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="check_chromedriver",
    version="0.1.1",
    description="Check and update chromedriver for selenium automatically",
    author="cuzai",
    author_email="cuzai@naver.com",
    url="https://github.com/cuzai/Check_Chromedriver.git",
    install_requires=["bs4", "requests", "selenium"],
    packages=find_packages(exclude=[".vscode", "README.md"]),
    keywords="selenium chromdriver auto download",
    python_requires=">=3",
    long_description=long_description,
    long_description_content_type="text/markdown",
)

