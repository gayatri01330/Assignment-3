def fact(num):
    fact = 1
    for i in range(1,num+1):
        fact = fact * i
    print(f"the factorial of {num} is {fact}")
fact(5)
