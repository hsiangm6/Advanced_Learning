#抓取PTT電影版的網頁原始碼(HTML)
import urllib.request as req
url="https://www.ptt.cc/bbs/movie/index.html"

#建立一個Request物件，附加Request Headers資訊，使得程式看起來像一般瀏覽者
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
})
#print(request)

with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
#print(data)

#解析原始碼，取得每篇文章的標題
import bs4          #beautifulsoup僅限解析html資料
root=bs4.BeautifulSoup(data,"html.parser")
titles=root.find_all("div",class_="title")
for title in titles:
    if title.a != None:
        print(title.a.string)
