def factorial(n):
    if n == 1:
        #print(n)
        return 1
    else:
        #print(n)
        return n*factorial(n-1)

i= input("Enter the number : ")
print(f"Factorial of {i} is :",factorial(int (i)))