# *args
def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
print(add(1,3,4,5,7,8,96,4))

 # **kwargs
def greet(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")
print(greet(name="John", age=30, city="New York"))