"""有n個工作，m台機器，每個工作有其需要完成的時間，如何分配工作到每個機器使全部工作完成的makespan最少"""
# read and prepare n,m and p
n=int(input("Number of jobs: "))                                                                              #if n為10
m=int(input("Number of machines: "))                                                                          #if m為3
p=input("Processing times: ")
"""pStr=input("Processing times: ")                                                                               #if pStr為['3', '3', '3', '4', '4', '5', '5', '6', '7', '8']
p=pStr.split()
for i in range(n):
    p[i]=int(p[i])"""                                                                                             #p為[3 3 3 4 4 5 5 6 7 8]，每一項工作的所需時間
#machine completion times
load=[0]*m        #所有machine，目前為止被分配到的 job 會分別耗機器多少時間                                         #[0(第0台機器的load) 0(第1台機器的load) 0(第2台機器的load)]
assignment=[0]*n  #它等一下要記的是工作安排給第幾台機器                                                            #[0 0 0 0 0 0 0 0 0 0]

#in interation j; assign job j to the least loaded machine
for j in range(n):  # 每一個迴圈我們要分配一個工作， 那換句話說，如果我有 n 個工作，我這個迴圈就要跑 n 次              #0 1 2 3 4 5 6 7 8 9
    #fnd the least loaded machine
    leastLoadedMachine=0   #我們先假設它是第 0 臺機器
    leastLoad=load[0]   #因此我們就說， 那它的最小load 就是第 0 臺 machine 的 loads
    for i in range(1,m):#為什麼range要從1開始?因為第0台已被設為最小值。此迴圈的意義是要找出現在哪台機器的load為最小值   #range---[1(第1台機器) 2(第2台機器)]
        if load[i]<leastLoad:
            leastLoadedMachine=i 
            leastLoad=load[i]
    #schedule a job
    load[leastLoadedMachine]+=p[j]
    assignment[j]=leastLoadedMachine+1
    #to check the process
    print(str(p[j])+":"+str(load))


#the result
print("Job assignment:",str(assignment))
print("Machine load:",str(load))