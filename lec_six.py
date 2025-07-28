def sum (a,b):
    sum = a + b
    print(sum)
    return sum
    
sum(2,3)    
    
sum(10,3)   

#Average of three number

def average (a,b,c):
    avg = (a + b + c)/3
    print(avg)
    return avg

average(10,20,30)


#lenght function
def len_list(list):
    length = len(list)
    print(length)
    return length


len_list([4,7,8,2,7,4,6])


list = [4,7,8,2,7,4,6]

print(list)

#factorial function
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    print(fact)
    return fact
       
factorial(5)


#USD to INR
def usd_to_inr(usd):
    inr = usd * 83
    print(inr)
    return inr

usd_to_inr(100)
        
#EVEN ODD NUMBER
def even_odd(num):
    if num % 2 == 0:
        print("Even Number")
    else:
        print("Number is odd")
    

even_odd(4)       


#Recursion
def show(n):
    if n == 0:
        return
    print(n)
    show(n-1)


show(5)        


#factorial using recursion

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))    
    
#natural number sum using recursion 
def natural_sum(n):
    if n == 1:
        return 1
    else:
        return n + natural_sum(n-1)

print(natural_sum(5))

#print list element using recursion
def print_list(lst):
    if len(lst) == 0:
        return
    print(lst[0])
    print_list(lst[1:])

num = [1, 2, 3, 4, 5]    
print_list(num)