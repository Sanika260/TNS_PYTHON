"""
import os

f = open("demo.txt","r")
#data = f.read()
#data = f.read(5)
data = f.readline()
print(data)
print(type(data))
f.close()

os.remove("demo.txt")
"""

with open("practice.txt","w") as f:
    f.write("Hi eveyone\nWe are learning File I/O\n")
    f.write("using python.\nI like programming in python")


with open("practice.txt","r") as f:
    data = f.read()
    
new_data = data.replace("python" , "java")    
print(new_data)


with open("practice.txt","w") as f:
    f.write(new_data)
 
 
word = "learning"
    
with open("practice.txt","r") as f:
    data = f.read()
    if(data.find(word) != -1):
        print("found")
    else:
        print("not found")    
    