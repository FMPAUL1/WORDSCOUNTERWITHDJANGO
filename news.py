# def news(**p):
#     for j,s in p.items():
#      print(j,s)
    
    

# print(news(first='abel',last='paul',firsts='tamunoboma',lasts='mary'))


# p=lambda x,y:x+y

# print(p(20,20))
# def myFun(arg1, **kwargs):
#     for key, value in kwargs.items():
#         print("%s =+ %s" % (key, value))
 
 
# # Driver code
# myFun("Hi", first='Geeks', mid='for', last='Geeks')

# class car():
#     # args receives unlimited no. of arguments as an array
#     def __init__(self, *args):
#         # access args index like array does
#         self.speed = args[0]
#         self.color = args[1]
 
 
# # creating objects of car class
# audi = car(200, 'red')
# bmw = car(250, 'black')
# mb = car(190, 'white')
 
# # printing the color and speed of the cars
# print(audi.color)
# print(bmw.speed)


# obi= lambda *x:x

# print(obi('abel','paul','tamunoboma'))


# find_sum = lambda n: sum([int(x) for x in str(n)])
# print("find_sum():", find_sum(15))

# l = ["1", "2", "9", "0", "-1", "-2"]


# # print("Operation on each item using lambda and map()",
# #       list(map(lambda x: str(int(x) + 10), l)))
# # print( list(map(lambda x:str(int(x)+10),l)))
# numbers=list(filter(lambda x: int(x) % 2 ==0,l))

# print(numbers)

def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()


def all(me):
    paul=me('I,Am hello atp')
    print(paul)
    
def add(x):
    def int(y):
        return x*y
    return int

# adds=add(5)
# print(adds(10))
# def outerFunction(text):
 
#     def innerFunction():
#         print(text)
 
#     innerFunction()
 
 
# if __name__ == '__main__':
#     outerFunction('Hey!')

# def outerFunction(text):
 
#     def innerFunction():
#         print(text)
 
#     # Note we are returning function
#     # WITHOUT parenthesis
#     return innerFunction 
 
# if __name__ == '__main__':
#     myFunction = outerFunction('Hey!')
#     myFunction()

# def keys(text):
#     def news():
#         print(text.upper())
#     news()
    

# if __name__=='__main__':
#     keys('atp')
import time
import math
 
# decorator to calculate duration
# taken by any function.
# def calculate_time(func):
#     def inner1(*args, **kwargs):
#         begin = time.time() 
#         func(*args, **kwargs)
#         end = time.time()
#         print("Total time taken in : ", func.__name__, end - begin)
 
#     return inner1
 
# @calculate_time
# def factorials(num):
#     time.sleep(2)
#     print(math.factorial(num))
# factorials(12)
# def shout(text):
#     return text.upper()
 
# def whisper(text):
#     return text.lower()
 
# def greet(func):
#     # storing the function in a variable
#     greeting = func("""Hi, I am created by a function passed as an argument.""")
#     print (greeting)
 
# greet(shout)
# greet(whisper)


# import time,math
# def decorator(funct):
#     def inner(*args, **kwargs):
#         begin=time.time()
#         funct(*args, **kwargs)
#         end=time.time()
#         print('hello,the function is :',funct.__name__,end-begin)
        
#     return inner


# @decorator
# def Abelpaul(num):
#     time.sleep(2)
#     print(math.factorial(num),'the first')
# Abelpaul(5)        

# def cal(func):
#     def cal(*args, **kwargs):
#           add= func(*args, **kwargs)
#           print('ddd')
#           return add +add
       
#     return cal
# @cal
# def yea(num):
#     return num * num

# print(yea(5))

# memory={}
# def words(f):
    
#     def num(nums):
#         if nums not in memory:
#             memory[nums]=f(nums)
#             print(' result saved in memmory')
#         else:
#             print('restoring')
#         return memory[nums]
#     return num

# @words
# def factoria(item):
#     if item ==1:
#         return 1
#     else:
#         return item * factoria(item-1)
    

# print(factoria(6))
# print(factoria(6))
        

# class Dog:
#     attr1="maam"
#     attr2='dig'
#     def fun(self):
#         print('the stud is ',self.attr1 + self.attr2)

# print(Dog().fun())
# class Profile:
#     def __init__(f,name,age):
#         f.name=name
#         f.age=age
#     def check(self):
#         print('my name is ',self.name + ' i am ', str(self.age) , ' years old ')
    

# obj=Profile('abel',27)
# print(obj.check())

# class Man:
#     def __init__(atp,name,age):
#         atp.name=name
#         atp.age=age
#     def __str__(atp):
#         return f" hello myname is {atp.name} and i am {atp.age} years old"
    
# news=Man('abel',27)
# print(news) 
        
# class Yam:
#     def __init__(self,name):
#         self.name=name
#     def show(self):    
#       return f"my name is {self.name} "
# class Employee:
 
#     # Initializing
#     def __init__(self):
#         print('Employee created.')
 
#     # Deleting (Calling destructor)
#     def __del__(self):
#         print('Destructor called, Employee deleted.')
 
# obj = Employee()
# del obj

# class Person:
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id
#     def back(self):
#         print(self.name,self.id)


# class Emp(Person):
#     def news(self):
#         print('hello news')
# new=Emp('atp',27)       
# new.news()
# new.back()
    
# class Person:
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id
#     def display(self):
#         print(self.name)
#         print(self.id)
        
# class Employee(Person):
#     def __init__(self,name,id,salary,post):
#         self.salary=salary
#         self.post=post
#         super().__init__()
#         Person.__init__(self,name,id)
# a=Employee('abel',1,200000,'helloworld')

# a.display() 

from datetime import date

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    @classmethod
    def get_max_age(cls,name,year):
        return cls(name,date.today().year -year)
    @staticmethod
    def isAdult(age):
        return age>18

somebody1=Person('abel',27)
all=somebody1.get_max_age('atp',1995)

print(somebody1.name)
print(all.name) 
# print(Person.get_max_age('atp',1995))

# print(Person.isAdult(22))
        
   
        