import requests

url_yahoo="https://tw.yahoo.com/"
url_momo = "https://www.momoshop.com.tw/"
url_git="https://github.com/hajimimi20/first_repository"
headers_s = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/139.0.0.0 Safari/537.36",
    "Accept-Language": "zh-TW,zh;q=0.9,en;q=0.8"
}

response = requests.get(url_yahoo, headers=headers_s)


#print(response.status_code)
#print("呼叫的結果(網頁內容)：",response.text)

with open("C://PythonProject/News/Yahoo_News.html","w",encoding="utf-8") as f:
    f.write(response.text)
