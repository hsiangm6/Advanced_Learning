#First, we get the given data ready
#set up the distance matrix(矩陣)
#法1-先行設定地點和地點間的距離
numLoc=5   #number of locations
dst=[[0,9,6,7,4],     #2-dim list(二維空間清單)
     [9,0,5,9,6],     #dst[i][j] is the distance between locations i and j
     [6,5,0,3,1],     #此清單從左上到右下劃一條準線會發現是對稱的，意思是現在有5個地點代碼分別是0~4
     [7,9,3,0,4],     #代碼0地點到代碼3地點的距離就是橫向第一列、直向第4行的數字7。代碼1地點到代碼2地點的距離就是橫向第2列、直向第3行的數字5。
     [4,6,1,4,0]]
"""
#法2-自行設定地點和地點間的距離
numLoc=int(input("How many places do you want to go?"))
dst=[]
for i in range(numLoc):
    dst.append(input().split())     #每一次要讓使用者輸入一串 數字，也就是五個數字，然後中間用四個空白鍵隔開，它一打完，我們就馬上把這段數字切開，切完了以後的東西是一個 list
    for j in range(numLoc):
        dst[i][j]=int(dst[i][j])
"""

#set up the origine
origine=0             #起點

#Second,we prepare two lists tour and unvisisted
#tour: a list that will contain the solution
#torLen: the total distance of the solution
#unvisistrd: a list that will contains those unvisisted locations at any time
tour=[origine]     # tour 裡面 一開始的時候呢，它只有一個東西，只有一個數字，就是 origin 的 index，等一下會在回圈子中，慢慢長，
                   #每一次我決定下一步我要去哪裡的時候 ，我就會把下一步的 next location 存到 tour 裡面去，最後我看 tour 我就會知道我要怎麼走
tourLen=0          #tourLen 表示我 整個走一圈，用我們的演算法要花多長的距離
unvisisted=[]
for i in range(numLoc):
    unvisisted.append(i)
unvisisted.remove(origine)
print(tour,tourLen)  #just take a look:[0] 0 :代表從代號0的地點出發，目前走過的距離為0
#print(unvisisted)    #[1, 2, 3, 4]

#The algorism
cur=origine                #現在位置
for i in range(numLoc-1):  #為甚麼要-1?因為起點本身的地點數不用算
    #find the next location to visit
    next=-1                #下一個地點的代碼數，是看x軸而非y軸
    minDst=10000000        #這個值可以隨便設定，只要確定接下來的所有距離都不會比此數小就好
    for j in unvisisted:
        if dst[cur][j]<minDst:
            next=j
            minDst=dst[cur][j]
    
    #move "next" from unvisisted to tour
    unvisisted.remove(next)
    tour.append(next)
    tourLen+=minDst

    print(tour,tourLen)  #just take a look:會顯示過程中的地點代碼和走過的總距離
    #print(unvisisted)

    #run the next interation from the next location
    cur=next

#complete the tour       #最後印結果之前，要記得，我們從 01234 我們這樣子繞了一圈以後 最後我要把 origin 再加回去我們的這一圈裡面，
                         #也就是加進 tour 這個 solution 的 list 的最後面。從最後的 current 移回去 的這個距離也是要加的
tour.append(origine)
tourLen+=dst[cur][origine]

#print out the solution
print(tour,tourLen)