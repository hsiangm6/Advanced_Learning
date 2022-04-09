"""#zip版
def verify_twid_v2(idstr):
    #Verify Taiwan ID number. Return True if valid； False otherwise
    
    #check lengh
    if len(idstr)!=10:
        return False
    
    #check first letter
    code1=ord(idstr[0])
    if (code1<65 or code1>90):
        return False
    
    #check the remaining letters
    for i in range(1,10):                 #注意是1~9而不是1~10
        code2=ord(idstr[i])
        if code2<48 or code2>57:
            return False
    
    #check the second character           #id的第2個字元只會是1或2
    code2=ord(idstr[1])
    if code2<49 or code2>50:
        return False
    
    #convert first English character to two-digit number.
    cmap=[10,11,12,13,14,15,16,17,\
      34,18,19,20,21,22,35,23,24,\
      25,26,27,28,29,32,30,31,33]
    num1=cmap[code1-65]
    newid=str(num1)+idstr[1:]             #注意記得加str，否則num1的型態會是int
    print("newid:"+newid)

    #calculate checksum
    weight=[1,9,8,7,6,5,4,3,2,1,1]
    checksum=0
    for appair in zip(newid,weight):      #此迴圈是與第1版不同之處
        checksum+=appair[1]*int(appair[0])
    if checksum%10==0:
        return True
    else:
        return False

#id1=input("Enter your ID number:")
#print(verify_twid_v2(id1))
print(verify_twid_v2("A123456789"))
"""

#zip、lambda、map版
def verify_twid_v3(idstr):
    #Verify Taiwan ID number. Return True if valid； False otherwise
    
    #check lengh
    if len(idstr)!=10:
        return False
    
    #check first letter
    code1=ord(idstr[0])
    if (code1<65 or code1>90):
        return False
    
    #check the remaining letters
    for i in range(1,10):                 #注意是1~9而不是1~10
        code2=ord(idstr[i])
        if code2<48 or code2>57:
            return False
    
    #check the second character           #id的第2個字元只會是1或2
    code2=ord(idstr[1])
    if code2<49 or code2>50:
        return False
    
    #convert first English character to two-digit number.
    cmap=[10,11,12,13,14,15,16,17,\
      34,18,19,20,21,22,35,23,24,\
      25,26,27,28,29,32,30,31,33]
    num1=cmap[code1-65]
    newid=str(num1)+idstr[1:]             #注意記得加str，否則num1的型態會是int
    print("newid:"+newid)

    #calculate checksum
    weight=[1,9,8,7,6,5,4,3,2,1,1]
    
    out1=map(lambda appair: appair[1]*int(appair[0]),zip(newid,weight))    #out1和checksum是與第二輪不一樣的地方
    checksum=sum(out1)
    if checksum%10==0:
        return True
    else:
        return False

#id1=input("Enter your ID number:")
#print(verify_twid_v3(id1))
print(verify_twid_v3("A123456789"))
