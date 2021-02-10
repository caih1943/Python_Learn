#提取PTT 电影版的网页原始码（HTML）
#on github python-learn branch caih-crawler
import urllib.request as req
url="https://medium.com/_/graphql"
#建立一个 request 物件，附加 request Headers 的资讯，看起来像一个正常使用者。
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
#print(data)
#解析json 原始码，取得每篇文章的标题。
import json
#data=data.replace("])}while(1);</x>","") # 将while等前缀替换为空字窜。
data=json.load(data) # 把原始的json 资料解析成字典、列表表示形式。
#取得 JSON 资料中的文章标题。
#posts=data["patload"]["reference"]["post"]
post=data["webRankedModules"]["modules"]["metadata"]["post"]
for key in posts:
    post=posts[key]
    print(post["title"])
#由于medium 的结构改变，现在找不到homefeed,只有graphgl内有标题信息。会出现
# urllib error : HTTP error:Http Error 403: Forbidden,

