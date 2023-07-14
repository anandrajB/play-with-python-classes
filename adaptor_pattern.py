from abc import ABC, abstractmethod
from dataclasses import dataclass


# in this class type u need to call

# self.attrs.username and so on , 

# i recommend this for small class functionality  , use classmethod inorder to overcome this issue



@dataclass
class Base:
    username: Optional[str] = None
    password: Optional[str] = None
    dob: Optional[int] = None
    address: Optional[str] = None


class Base2Adapter(ABC):
    @abstractmethod
    def main(self):
        pass


class Base2(Base2Adapter):
    def __init__(self, attrs: Base, some: Optional[int] = None):
        self.attrs = attrs
        self.some = some

    def sub(self):
        print("The username is", self.attrs.username)

    def main(self):
        print("the name is " , self.attrs.username)


# Usage example
base_instance = Base(username="anand", password="123", dob=223, address="test")
base2_instance = Base2(attrs=base_instance)
base2_instance.sub()