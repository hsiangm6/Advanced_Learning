#抓取PTT八卦版的網頁原始碼(HTML)
import urllib.request as req
def getData(url):
    #建立一個Request物件，附加Request Headers資訊
    request=req.Request(url,headers={
        "cookie":"over18=1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    #解析原始碼，取得每篇文章標題
    import bs4
    root=bs4.BeautifulSoup(data,"html.parser")       #讓BeautifulSoup協助我們解析HTML文件
    titles=root.find_all("div",class_="title")       #尋找所有class="title"的div標籤
    for title in titles:
        if title.a != None:                          #如果標題包含a標籤(代表文章沒有被刪除)，印出來
            print(title.a.string)
    #抓取上一頁的連結
    nextLink=root.find("a",string="‹ 上頁")          #找到內文是 < 上頁 的a標籤
    return nextLink["href"]

#抓取多個頁面的標題
pageUrl="https://www.ptt.cc/bbs/Gossiping/index.html"
count=0
range=int(input("請輸入您想要搜尋的最新頁碼範圍:"))
while count<range:
    pageUrl="https://www.ptt.cc"+getData(pageUrl)
    count+=1


