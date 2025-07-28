class Student:
    def __init__(self,name):
        self.name = name
  

s1 = Student("sanika")

print(s1.name)# Output: sanika
del s1.name
print(s1.name)

class Car():
    color = "blue"
    brand =  "mercedes"
    
c1 = Car()
print(c1.color)    
print(c1.brand)

#class
class Students:
   @staticmethod
   def hello():
        print("Hello, World!")
        
   def __init__(self, name, marks):
        self.name = name
        self.marks = marks   

   def get_avg(self):
         sum = 0
         for i in self.marks:
             sum += i
         print("hi",self.name,"your avg score is:",sum/3)
    


s1 =  Students("SANIKA",[90,87,98])
s1.get_avg()
s1.hello()

#Abstraction
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
    
    def start(self):
        self.clutch = True
        self.acc = True
        print("car started")
        
car1 = Car() 
car1.start()

class Account:
    def __init__(self, balance , acc_no):
        self.balance = balance
        self.acc_no = acc_no
    
    #debit method
    def debit(self, amount):
        self.balance -= amount
        print("Debited amount:", amount)
        print("total amount",self.get_balance())
        
    #credit method
    def credit(self, amount):
        self.balance += amount
        print("Credited amount:", amount)
        print("total amount",self.get_balance())
        
        
    #get balance
    def get_balance(self):
        return self.balance
    
            

s1 = Account(6000,12345678)    
s1.debit(1000)
s1.credit(14000)
s1.debit(500)
