한국어, english

# Check_Chromedriver
It is always annoying to know that your Chromedriver is expired especially when you want to use Selenium.

I found that this happends because chrome browser updates itself automatically for its security's sake.

Rather than making it not to update by itself, I made a module that checks and updates [Chromedirver](https://chromedriver.chromium.org/)'s version.
※ It only works on Windows
## Install
1. Clone the repository
```bash
$ git clone https://github.com/cuzai/Check_Chromedriver.git
```
2. Simply import the module
```python
from Check_Chromedriver.Check_Chromedriver import Check_Chromedriver
```
## Sample Usage
1. Check and Download
This will automatically check not only whether your Chromedriver exists in your directory but also whether it is good to use. It downloads latest stable version of Chromedriver in your root directory. (./chromedriver/chromedriver.exe)
```python
cc = Check_Chromedriver()
cc.main()
```
if you want to make your own directory, you can say...
```python
cc = Check_Chromedriver("./your own path")
cc.main()
```
2. Just Check
If you just want to check whether the driver works so that you can download whatever the version you want, you can say. If it says True, it is good to go.
```python
cc = Check_Chromedriver()
isUsable = cc.check_driver()
print(isUsable)
```
# Check_Chromedriver
셀레니움을 사용하려고 할 때 기존에 받아 놓은 크롬 드라이버 버전이 만료되어있다면, 새로 다운받는 것이 여간 귀찮은 일이 아니다.

이는 크롬 브라우저가 보안 등의 이유로 자동으로 브라우저 업데이트를 진행하기 때문인데, 필자는 이 보안 업데이트를 막음으로써 위 문제를 해결하기보다는, 간단한 모듈을 통해 [크롬드라이버](https://chromedriver.chromium.org/)를 자동으로 다운받게 함으로써 항상 최신 버전을 유지할 수 있도록 했다.
※ 윈도우에서만 작동 가능
## 설치
1. Repository 클론
```bash
$ git clone https://github.com/cuzai/Check_Chromedriver.git
```
2. 모듈 import
```python
from Check_Chromedriver.Check_Chromedriver import Check_Chromedriver
```
## 사용 예
1. 버전 체크 및 자동 다운로드
현재 루트에 크롬드라이버가 존재하는지 또는 존재한다면 사용가능한지 체크한 후 안정적인 최신 버전의 크롬드라이버를 다음 루트에 다운로드한다.(./chromedriver/chromedriver.exe)
```python
cc = Check_Chromedriver()
cc.main()
```
./chromedriver/chromedriver.exe 루트가 아닌 자신만의 루트를 만들고싶다면 아래와 같이 작성...
```python
cc = Check_Chromedriver("./your own path")
cc.main()
```
2. 버전만 체크
현재 버전이 사용가능한지 체크만 하고 다운로드는 직접 하고싶다면 다음과 같이 작성한다.
True가 반환된다면 사용 가능하다는 의미
```python
cc = Check_Chromedriver()
isUsable = cc.check_driver()
print(isUsable)
```