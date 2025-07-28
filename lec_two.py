str1 = "apna"
str2 = "college"
print("The original string  is : ", str1+str2)
print(len(str1))
ch = str1[3]
print(ch)
slicing = str1[ :len(str1)]
print(slicing)

str = "i am studying python from apna college"
print(str.endswith("app")) 
print(str.capitalize())
print(str.replace("apna" , "self"))
print(str.find("python"))
print(str.count("from"))

"""
#name and length
name = input("Enter ur name:")
length = len(name)
print("The length of ur name is: ", length)

occur = "He$llo $ w$orld"
print(occur.count("$"))


age = 21
if age >= 18:
    print("Eligible to vote")
elif age == 17:
    print("Eligible to vote in 1 year")
else:
    print("Not eligible to vote")


# Numberis even or odd

num = int(input("Enter number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")



# Greatest of three number

num1 = int(input("Enter first number: "))    
num2  = int(input("Second number: "))
num3 = int(input("Third number: "))

if ((num1 >= num2) and (num1 >= num3)):
    print("The greatest number is: ", num1)
elif(num2 >= num3):
    print("The greatest number is: ", num2)
else:
    print("The greatest number is: ", num3)
    
"""

# multiple of 7 or not
num = int(input("Enter number: "))
if num % 7 == 0:
    print("Multiple of 7")
else:
    print("not multiple of 7")