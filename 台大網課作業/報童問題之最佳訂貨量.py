"""報童問題之最佳訂貨量
第一列的整數是單位進貨成本 c、第二列的整數是單位零售價格 r、第三列的整數是需求的可能個數 N、第四列開始的小數則依序是賣出零份
、一份直到 N 份報紙的機率（也就是說對於 i = 4, 5, ..., N + 4，第 i 列記錄的是賣出 i - 4份報紙的機率）。"""
cost=int(input()) #cost是進貨成本
price=int(input()) #price是銷售價
n=int(input()) #預計單日需求
#q=int(input()) #訂貨量
sum=float()  #期望值
max=0.0  #最佳利潤
bestq=0  # 最佳訂貨量
d=float() #累積機率
p = [] #p是此需求量的機率
p.append(float(input()))
p.append(float(input()))
p.append(float(input()))
p.append(float(input()))
p.append(float(input()))
p.append(float(input()))
p.append(float(input()))
p.append(float(input()))
p.append(float(input()))
for q in range(n+1):  #q是訂貨量
    sum=0      #!!!記得歸0
    d=0.0      #!!!記得歸0                 
    for i in range(q+1):  #i是單日需求量   
        if i != q:
            d+=p[i]
            sum=sum+(price*i-cost*q)*p[i]
        else:
            sum=sum+(price*i-cost*q)*(1-d) #因為機率加起來一定要是1，所以需求量超出訂貨量的機率必須歸到需求量和訂貨量相等時的機率
            break
    if sum>max:
        max=sum
        bestq=q
integer=int(max)   #把小數無條件捨去到整數位
print(bestq,integer)