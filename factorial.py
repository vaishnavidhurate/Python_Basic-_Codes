def factorial(num):
    if num<0:
        return 0
    elif num==1 or num==0:
        return 1
    else:
        fact=1
        while(num>1):
            fact=fact*num
            num=num-1
        return fact
    
num=int(input("enter the no"))
print("Fcatorial of ",num," is ",factorial(num))
