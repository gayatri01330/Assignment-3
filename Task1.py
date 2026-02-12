def factorial(num):
    if num < 0:
        print("fctorial does not exist")
    elif num ==0 or num == 1 :
        return 1
    else:
        return   num*factorial(num-1)
    
num = int(input("enter a number: "))
result = factorial(num)
print(f"factorial of {num} is : {result}")    


    
