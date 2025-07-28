"""
# print number from 1 to 100 
i = 1
while i <= 100:
    print(i)
    i += 1
    
#print number from 100 to 1
i = 100
while i >= 1:
      print(i) 
      i -= 1   
    

# multiplication table of n number    
n = int(input("Enter number u want to print table") )  
i = 1
while ( i <= 10)  :
    table = n * i 
    print(n,"*",i,"=",table)
    i += 1
 
#print list using while loop    
list = []

i = 1
while  i <= 10:
    list.append(i*i)
    i += 1
print(list)    


#search number x in tuple using while loop
tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = int(input(" Enter number u want to search in tuple"))

i = 0
while i < len(tup):
      tup.index(x)
      break
      i += 1
print("number found",tup.index(x))    


#or
tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = int(input(" Enter number u want to search in tuple"))

i = 0
while i < len(tup):
    if tup[i] == x:
        print("number found at index",i)
        break
    else:
        i += 1
  
"""
#print tuple
tup = ("potato","brijal","ladyfinger")

for i in tup:
    print(i)
  
print("\n")  
 
for i in tup:
    print(i)
else:
    print("End")  
    
list = []    

for i in range(1,11):
    list.append(i*i)
    
print(list) 

# find the x element in tuple using for loop   
idx = 0
tup= (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = int(input("Enter number u want to search in tuple"))
for i in tup:
    if(i == x):
        print("number found at index",idx)
        idx += 1


#print number 1 to 100 using for loop and range function
for i in range(1,101):
    print(i)        
        

#print number 100 to 1 using for loop and range function
for i in range(100,0,-1):
    print(i)        
                
                

# multiplication table of n number using for loop

n = int(input("Enter number u want to print multiplication table"))
for i in range(1,11):
    print(n,"*",i,"=",n*i)
    
#sum of n number using while loop
n = int(input("Enter number u want to print sum"))
sum = 0
i = 1
while i <= n:
    sum = sum + i
    i = i + 1
print("Sum of number is",sum)
    
#factorial of first n numbers using for loop
n = int(input("Enter number u want to print factorial"))
fact = 1
for i in range(1,n+1):
    fact = fact * i
print("Factorial of number is",fact)