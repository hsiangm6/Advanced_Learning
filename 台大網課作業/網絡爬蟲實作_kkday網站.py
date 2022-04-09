#抓取kkday的網頁資料
import urllib.request as req
url="https://www.kkday.com/zh-tw/home/ajax_get_homepage_setting?csrf_token_name=682f52e60086b43bc106b316ae1c54bd"

#建立一個Request物件，附加Request Headers資訊，使得程式看起來像一般瀏覽者
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
})
#print(request)

with req.urlopen(request) as response:
    data=response.read().decode("utf-8")    # 根據觀察，取得的資料是 JSON 格式
#print(data)

#解析json格式的資料，取得每篇文章的標題
import json
data=json.loads(data)                       # 根據觀察，取得的資料是 JSON 格式
#print(data)

#取得JSON資料中的文章標題
posts=data["data"]["homepage_product_group"]
#print(posts)

for key in posts:
    print(key["title"])