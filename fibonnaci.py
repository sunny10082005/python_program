def fibo(n):
    a = 0
    b = 1

    for _ in range(n):
        print(a,end=" ")

        temp = a
        a = b
        b =  temp + b

fibo(10)




#Second Way
def fibo(n):
    a = 0
    b = 1

    for _ in range(n):
        print(a,end=" ")

        a,b = b,a+b

fibo(10)