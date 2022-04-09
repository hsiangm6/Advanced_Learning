Q=int(input("Order quantity Q: "))
R=int(input("Reorder point R: "))
I=int(input("Initial inventory I: "))
print("Inventory: "+str(I))
while True:                             #無窮迴圈 True的首字母T一定要大寫 要解決無限迴圈就到powershell中的terminal kill，再到左上角的terminal按new terminal
    sale=int(input("Sales in a day: "))
    I= (I-sale) if (I-sale)>=0 else 0
    print("Inventory: "+str(I))
    if I<R:
        print("Order!")
        I+=Q
        print("Inventory: "+str(I))
