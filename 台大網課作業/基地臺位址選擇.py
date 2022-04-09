"""
基地臺位址選擇:
有一家電信公司正在研擬一個新服務區域的無線基地臺設置計畫。在這個區域裡，一共有 n 個城鎮，編號為 1、2 直到 n，而城鎮 i 的人口數是 Pi。
公司將此區域以一公里為單位，畫出了一個二維座標系，並且以 (xi, yi) 表示城鎮 i 的位置。"""
#使n,p,d能夠同時輸入到同一列
#一共有 n 個城鎮，編號為 1、2 直到 n
#在此區域的 n 個城鎮中挑選 p 個城鎮設置基地臺，以求能覆蓋最多的人口數。
#如果一個基地臺跟一個城鎮的距離在 d 公里以內，我們就說這個基地臺可以「覆蓋」這個城鎮
'''
2≤n≤1000
2≤p≤n
−100≤x ≤100
−100≤y ≤100
1≤Pi ≤100
不會有兩個城鎮落在同一個地點。
讀入這些資料之後，請根據題目指定的演算法，求出應該在哪 pp 個城鎮設置基地臺，然後依照選擇的先後順序由先而後印出這些城鎮的編號，最後輸出被覆蓋的總人數。任兩個城鎮編號間，用一個空白隔開。
'''
#town為城鎮數，base為基地台數，radius為基地台覆蓋範圍的半徑
town,base,radius=map(int,input().split())  #town:8  base:3  radius:3

#[x座標，y座標，人口數pop]
data=[]
for i in range(town):                    #i是y座標
    data.append(input().split())
    for j in range(3):                   #j是x座標
        data[i][j]=int(data[i][j])
rangeList1 = range(town)         #城鎮清單:[0,1,2,3,4,5,6,7] 

#The algorism
dst=0.0                    # dst:兩個地點間的距離
nowPop=0                   #階段覆蓋人數
maxPop=0                   #最多覆蓋人數的基地台的人數
totalPop=0                 #總覆蓋人數
mayBuilt=[]                #可能設立基地台城鎮代號的累積清單:一輪中曾經是範圍內人數最多的清單
hasBuilt=[]                #設立基地台的城鎮
nowCovered=[]              #現在的指定基地台所覆蓋的城鎮代號
roundcovered=[]            #此回合被覆蓋的確切城鎮
covered=[]                 #所有覆蓋的城鎮代號
for rounds in range(base):
    for i in rangeList1:
        
        for j in rangeList1:
            dst=((data[i][0]-data[j][0])**2+(data[i][1]-data[j][1])**2)**0.5
            #print(dst)
            if dst<=radius :
                nowPop+=data[j][2]          #將i點為圓心的覆蓋人數與城鎮找出來並累積在nowCovered清單中
                nowCovered.append(j)        
            dst=0
        if nowPop>maxPop:                   #update
            maxPop=nowPop                   #人數更新
            mayBuilt.append(i)              #基地台的可能選址增加
            #print(mayBuilt)
            roundcovered=list(nowCovered)   #有更好的城鎮選擇就update覆蓋之城鎮清單
            #print(roundcovered)
        
        nowPop=0                            #記得歸零
        nowCovered=[]                       #階段覆蓋城鎮清單之暫存清空
    
    totalPop+=maxPop                        #把每一輪的最大覆蓋人數加到總覆蓋人數上
    maxPop=0                                #記得歸零
    covered+=roundcovered                   #a清單+=b清單:b清單銜接a清單後面
    #print(covered)
    roundcovered=[]                         #回合覆蓋城鎮清單之暫存清空
    hasBuilt.append(mayBuilt[len(mayBuilt)-1])   #更新到最後可能建造基地台的城鎮＝最佳建造基地台的城鎮
    mayBuilt=[]                             #建造基地台的可能選擇清單之暫存清空
    
    rangeList1=list(set(rangeList1).difference(set(covered)))   #把已經覆蓋過的城鎮和基地台城鎮從接下來的選擇中刪掉

print(hasBuilt)
print(totalPop)
final=[z+1 for z in hasBuilt]               #轉換成從1開始的城鎮代號
final2=str(final)[1:-1]                     #將[ ]移除
final3=final2.replace(",","")               #將 , 移除

print("=====================================")
print(str(final3)+" "+str(totalPop))
