#一開始的計算過程
def histogram(seq):
    d=dict()
    for element in seq:         #element是dictionary中的key
        if element not in d:
            d[element]=1
        else:
            d[element]+=1
    return d
h=histogram('brontosaurus')     #此列不能放第1列，可推測只能呼叫前面建立過的函數
print(h)                        #第一種輸出方式

#第二種輸出方式的轉換過程
def print_hist(hist):
    for key in hist:
        print(key,hist[key])
#print_hist(h)                   #第二種輸出的第一種程式內容

#此圖的程式用途與第2種輸出方式相同，只是不同的程式表示法
def print_hist2(hist):
    for key, value in hist.items():
        print(key,value)
#print_hist2(h)                  #第二種輸出的第二種程式內容

#按照英文字母排序的轉換過程，可說是第三種輸出方式
def print_hist3(hist):
    keys=hist.keys()
    for key in sorted(keys):     #sorted()是對key進行排序
        print(key,hist[key])
#print_hist3(h)                  #第三種輸出:排序後

#反向對應:從value找到key:幾個相同字母對到那些英文字母
def invert_dict(d):
    inv=dict()
    for key in d:
        val=d[key]               #此列的d[key]是h中的value
        print("val:",val)
        if val not in inv:
            inv[val]=[key]       #val是h中的value，但卻也是inv中的key
        else:
            inv[val].append(key)
    return inv
inverted=invert_dict(h)
print(inverted)


