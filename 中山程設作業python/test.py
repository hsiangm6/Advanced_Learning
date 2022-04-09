import sys 
data = {
    'n1': 0,
    'n2': 10
}

while True: 
    inputs = input('Please input your operation:')
    inputs = inputs.split(' ')
    
    # using unpacking to get each parameters
    if len(inputs) == 1: # printall, delall
        op = inputs[0]
    elif len(inputs) == 2: # del, new
        op = inputs[0]
        key= inputs[1]
        # unpacking inputs to op and name variables
    elif len(inputs) == 3: # add, mul
        op = inputs[0]
        key= inputs[1]
        if key not in data:
            print("Your search is not in dict!")
            continue
        try: #avoid enter string to be number
            num= int(inputs[2])
        except:
            print("Your enter is not number!")
            continue
    elif len(inputs) == 4: # sum of geometric sequence(geoSeq NAME numberOfItems commonRatio)
        op = inputs[0]
        key= inputs[1]
        if key not in data:
            print("Your search is not in dict!")
            continue
        try: #avoid enter string to be number
            n= int(inputs[2])
            r= int(inputs[3])
        except:
            print("Your enter is not number!")
            continue

    # handle operation logic
    if op == 'printall':
        print(data)
    elif op == 'delall':
        for value in data:
                data[value]=0
    elif op == 'del':
        if key not in data:
            print("Your search is not exist!")
            continue
        del data[key]
    elif op == 'new':
        data[key]=0
    elif op == 'add':
        print(f"{data[key]} + {num} = {data[key]+num}")
        data[key]+=num
        # calculate
        # print "old_num + number = new_num"
    elif op == 'mul':
        print(f"{data[key]} * {num} = {data[key]*num}")
        data[key]*=num
        # same as add
    elif op == 'geoSeq':
        a1=data[key]
        for i in range(n-1):
            print(f"{a1}+",end="")
            a1*=r
        print(f"{a1}={data[key]*(1-r**n)/(1-r):.1f}")
        data[key]=data[key]*(1-r**n)/(1-r)
    elif op == 'end':
        break
    else:
        print("Your instruction is error!")