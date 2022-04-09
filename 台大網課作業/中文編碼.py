#-*-coding:utf8-*-
code="21830, 31649, 31243, 24335, 35373, 35336"
codeList=code.split(", ")
msg=""
for i in codeList:
    msg+=chr(int(i))   #
print("msg=",msg)