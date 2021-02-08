#提取PTT 电影版的网页原始码（HTML）
#on github python-learn branch caih-crawler
import urllib.request as req
url="https://www.ptt.cc/bbs/movie/index.html"
#建立一个 request 物件，附加 request Headers 的资讯，看起来像一个正常使用者。
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
#print(data)
#解析原始码，取得每篇文章的标题。
import bs4
root=bs4.BeautifulSoup(data, "html.parser") #BeautifulSoup 协助我们解析 HTML 格式文件。
titles=root.find_all("div",class_="title") #寻找所有 class="title" 的 div 标籤
for title in titles:
    if title.a != None:   #如果标题包含 a 标籤（没有被删除） 印出来。
        print(title.a.string)
#print(titles)
