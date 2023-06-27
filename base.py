from dataclasses import  dataclass
from typing import Optional as opt

@dataclass
class main:
    a : int
    b : str

    def func(self):
        return self.a
    

    @property
    def objc(self):
        return "some" , self.a

@dataclass
class sub:

    subs : main
    
    def fun1(self):
        print("the object is " ,self.subs.objc)
        return "the data is " ,self.subs.func()





obj1 = main(a = 5 , b = "data")
print(obj1.b)

sub(subs = obj1).fun1()