"""練習題2:
今天有一群人在為n面牆壁漆油漆，一開始都是顏色1，經過著色後會被覆蓋，變成其他顏色。今天如果有10面牆壁，然後替第2到5面牆壁漆顏色2
，那麼總共會有6面牆壁顏色1，4面牆壁顏色2。若再替牆壁3到6漆顏色3，那麼會有5面牆壁顏色1，1面牆壁顏色2，4面牆壁顏色3。

現在給定如下的資料輸入格式：
第一行輸入牆壁n面和m次油漆，接下來的m行每行依順序輸入漆的牆壁的起點號碼、漆的牆壁的終點號碼，以及顏色代碼，都是合理的整數。
輸出共有m段，於第 i 段輸出在全部油漆動作都完成後，第 i 次油漆之顏色的牆壁面數、一個空格，與該顏色代碼。段與段之間用一個分號隔開。所有牆壁在最初都是顏色 1。舉例來說：
Input :
10 2
2 5 2
3 6 3

Output
1 2;4 3

現在如果是
15 4
2 3 3
5 13 2
3 5 1
5 5 4

那麼輸出會是？請注意第三次的油漆動作，我們會把第 3 到 5 面牆壁漆成最初的 1 號色。
"""
str_list=input()
list=str_list.split(' ')
walls=int(list[0])
frequency=int(list[1])
#print(walls)
#print(frequency)
d={}                                 #牆壁顏色字典
walls_number={}    #相同顏色的牆壁數字典
for i in range(1,walls+1):
    d[i]=1
    #print(d)

#漆油漆的過程
for i in range(frequency):
    initial_wall,last_wall,color_number=map(int,input().split())
    walls_number[color_number]=0
    #print('walls number:',walls_number)
    for j in range(initial_wall,last_wall+1):
        d[j]=color_number
    #print('d:',d)
print('d(牆壁代碼:顏色代碼):',d)
#計算油漆的牆壁數
for d_key in d:
    walls_number[d[d_key]]+=1
    #print(walls_number)
print('walls_number(顏色代碼:刷此顏色的牆壁數):',walls_number)

#轉換成指定格式
for key in walls_number:
    print(walls_number[key],key,end='')
    if key+1 in walls_number:
        print(';',end='')

