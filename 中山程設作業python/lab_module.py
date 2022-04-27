def print_multiplication_table(n):
    for i in range(1,n+1,1):
        for j in range(1,n,1):
            print(f'{i*j:3}',end=" ")
        print(f'{i*n:3}')