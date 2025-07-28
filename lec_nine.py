#private
class Account:
    def __init__(self, account_number, account_pass):
        self.account_number = account_number
        self.__account_pass = account_pass
    
    def  reset_pass(self):
     print(self.__account_pass)

s1 = Account(123450,"abcd")
print(s1.account_number)
print(s1.reset_pass())


#polymorphism
print(1 + 2) #3
print("1" + "2") #12
print([1,2,3] + [4,5,6]) #merge

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    def add(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)
        
    def showNumber(self):
        print(self.real, "i +", self.imag, "j")

num1 = Complex(1,3)
num2 = Complex(2,4)
print(num1.add(num2).showNumber())

class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def Area(self):
     return 3.14 * self.radius**2
 
    def Circumference(self):
        return 2 * 3.14 * self.radius

r = Circle(21)        
print(r.Area())
print(r.Circumference())


class Employee:
    def __init__(self, role, dep, salary):
        self.role = role
        self.dep = dep
        self.salary = salary
        
    def showDetail(self):
     print("Role:", self.role)
     print("Department:", self.dep)
     print("Salary:", self.salary)
     
class Engineer(Employee):
    def __init__(self, name, age):
        super().__init__("Engineer", "IT", 50000)
        self.name = name
        self.age = age
        
#e1 = Employee("ee","dd",2000)
#e1.showDetail()

engg1 = Engineer("Rahul", 25)
engg1.showDetail()


class Order:
    def __init__(self,item,price):
        self.item = item
        self.price = price
        
    def __gt__(self,ord2):
        return self.price > ord2.price
        

ord1 = Order("chips",15)     
ord2 = Order("choco",8)   
print(ord1 > ord2)

        
