#past sales
"""salesStr=input("Sales: ")"""
salesStr="14 23 26 17 17 12 24 19 10 18 22 31 19 16 22 28 20 27 20 32"
sales=salesStr.split()
for i in range(len(sales)):
    sales[i]=int(sales[i])

#given information
stgCost=2  #缺貨成本
invCost=1000*0.073/365  #inventory cost(存貨成本) 是一個東西買要一千塊。 放在庫房裡一天晚上要浪費掉的錢的利率是 0.073 除以 365，因為 7.3% 是年利率
Q=30   #訂貨量
I=20   #起始存貨

#finding the best R
bestR=0
costOfBestR=1000000
for R in range(Q):
    totalStgCost=0
    totalInvCost=0

    #finding the total cost of this R
    for s in sales:
        I-=s
        if I<0:
            totalStgCost+= (-I)*stgCost
            I+=Q
        elif I<R:
            I+=Q
            totalInvCost+=I*invCost     #此處的I成立在I為正數的情況下，也就是需求量沒有大過Q，否則不成立
    
    totalCost=totalStgCost+totalInvCost
    #update best R in necessary
    if totalCost<costOfBestR:
        bestR=R
        costOfBestR=totalCost
    print(R,totalStgCost,totalInvCost,totalCost)

print(bestR)
