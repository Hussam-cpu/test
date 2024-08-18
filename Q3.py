def Fib(x):   #Q3
    if x == 1:
        return 1
    if x == 2:
        return 5
    return Fib(x-1)+Fib(x-2)
x = int(input("Enter any number :"))
print(Fib(x))