# 载入 pandas 模块
import pandas as pd
#建立 Series
data=pd.Series([3,10,20,5,-12])
#print(data[2])
#观察资料
# print("data 类型：",data.dtype)
# print("资料尺寸：",data.size)
# print("资料索引：",data.index)
#各种数学、统计运算
print("总和：",data.sum())
print("标准差：",data.std())
print("最大三个数：",data.nlargest(3),sep="\n")
#print(data.sum(),data.max()，data.prod())
#print(data.mean(),data.median()，data.std())
#print(data.nlargest(3),data.nsmalles(2))
# print("最大值:", data.max())
# print("中位数:",data.median())
# data=data*2
# print(data)
# data=data==20
# print(data)
#============================
#import pandas as pd
data=pd.Series(["Python","Pandas","你好"])
print(data)
#print(data.str.cat(sep=","))
#各种字串操作，定义在str底下
#print(data.str.lower(), data.str.upper(),data.str.len())
print(data.str.cat(sep="-"), (data.str.contains("P")),sep="\n")
#print(data.str.replace("你好","Hello"))
print(data.str.len()) #算出每个字串长度
print("====================================")
print("====================================")
#建立 DataFrame
data=pd.DataFrame({
    "name":["amy","John","Bob"],
     "salary":[30000,50000,40000]
 },index=["0","1","2"])
#观察资料
print("资料数量",data.size)
print("资料形状",data.shape)
print("资料索引",data.index)
#基本 DataFrame 操作
#取得特定的栏位
# print(data["name"])
# print(data["salary"])
#print(data)
#资料索引
print("=================")
print("data数量",data.size)
print("资料形式(Row-列,Column-栏",data.shape)
print("资料索引",data.index)
print("取出横向第2行（列）-Row1",data.iloc[1], sep="\n")  # 印出横向Row1即第二行（列）的资料-
print("=================")
print("取出索引（列）-Row2",data.loc["2"], sep="\n") # 印出索引Row2即第三行（列）的资料。
print("=================")
print(data.loc["1"])
print("=================")
print("取出栏位(column)名称=列资料",data["name"],sep="\n") #Seies 形态资料 栏位名称=列表资料 column名称
name=data["name"]  # 取得单维度的 Series 资料
print("把 name 全部转大写", name.str.upper(), sep="\n") #双维度的资料取得特定的栏或列就变成单维度资料Series,应可结合起来用
salaries=data["salary"]
print("薪水平均值：",salaries.mean())
print("=================")
#建立新的栏位column
data["revenue"]=[500000,400000,300000] # data[新栏位的名称]=列表
data["rank"]=pd.Series([3,6,1],index=["0","1","2"]) # data [新栏位的名称】=Series 的资料
data["cp"]=data["revenue"]/data["salary"]
print(data)