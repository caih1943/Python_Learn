import pandas as pd
#读取资料
data=pd.read_csv("googleplaystore.csv") #把 csv 格式的档案读取成一个DataFrame
#观察资料
# print(data)
# print("资料数量：",data.shape)
# print("资料栏位：",data.columns)
print("======================================")
#分析资料：评分的各种统计数据#
# condition=data["Rating"]<=5
# data=data[condition]
#print(data)
# print("平均数",data["Rating"].mean())
# print("中位数",data["Rating"].median())
# print("取得前100个应用程序的平均数：",data["Rating"].nlargest(1000).mean())
# print(data["Installs"])
#print(data["Installs"][10472])
# data["Installs"]=pd.to_numeric(data["Installs"].str.replace("[,+]","").replace("Free",""))
# #print(data["Installs"])
# print("平均数：",data["Installs"].mean())
# condition=data["Installs"]>100000
# print("安装数量大于100000 的应用程序有几个",data[condition].shape[0])
#基于资料的应用：关键字搜索的应用程序的名称
keyword=input("请输入关键字：")
condition=data["App"].str.contains(keyword, case=False) #忽略大小写
print(data[condition]["App"]) #列出应用程序App名
#print("包含关键字的应用程序数量：",data[condition]["App"].shape[0])