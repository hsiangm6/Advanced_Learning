def revNum(num,rem=0):
    if num==0:
        return rem
    elif num<10:
        return revNum(num//10,(rem+num%10))
    else:
        return revNum(num//10,(rem+num%10)*10)

count=0   
num=int(input("Please enter the numbers: "))
num2=num
while num2%10==0:
    num2//=10
    count+=1
print("Reversed positive integer number: \n"+"0"*count+str(revNum(num)))