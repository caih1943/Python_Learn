# import urllib.request as request
# src="https://www.toutiao.com/"
# with request.urlopen(src) as response:
#     data=response.read().decode("utf-8")
# print(data)
#on github python-learn branch caih-crawler
import urllib.request as request
import json
#籉北市學習型機構是给json api 存取列表，网址如下：
src="https://data.taipei/api/v1/dataset/24c9f8fe-88db-4a6e-895c-498fbc94df94?scope=resourceAquire"  #臺北內湖科技園區廠商名錄.json
with request.urlopen(src) as response:
    data=json.load(response)
#print(data)
#将o_tlc_agency_name的key的值列表出来
clist=data["result"]["results"]
with open("data.txt","w", encoding="utf-8") as f:
# print(clist)
    for name in clist:
        f.write(name["o_tlc_agency_name"]+"\n")
        print(name["o_tlc_agency_name"])
