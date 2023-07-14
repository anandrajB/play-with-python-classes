from dataclasses import dataclass
from typing import Optional

# type 1

@dataclass
class Base:
    username : str
    password : str 

    def sub(self):
        return self.username


@dataclass
class Main:

    var = Base

    def sub(self):
        return self.var.username

obj = Base(username = "anand" , password = "123")
Main(var = obj).sub()



# TYPE 2

# using astuple


@dataclass
class Base:
    username : str
    password : str 

    def sub(self):
        return self.username



@dataclass
class Main:
    class_attrs : Base
    username : Optional[str] = None
    password : Optional[str] = None

    def __post_init__(self):
        (
            self.username,
            self.password
        ) = astuple(self.class_attrs)[:2]

    
    def sub(self):
        return self.username

obj = Base(username = "anand" , password = "123")
Main(class_attrs = obj).sub()



# type 3 
# using clsmethod


@dataclass
class Base:
    dob: int
    address: str
    username: str
    password: str
    

    def main(self):
        return self.username


@dataclass
class Base2:
    attrs : Base
    some : Optional[int] = None
    username: Optional[str] = None
    password: Optional[str] = None

    # type 1 with required
    @classmethod
    def from_base(cls, base: Base):
        return cls( attrs = base , username = base.username, password =  base.password)


    @classmethod
    def from_base(cls, base: Base):
        # base.username goes for attr some , base.password for username
        return cls( attrs = base ,  base.username,  base.password)

    def sub(self):
        print("The username is",)
        return None

base_instance = Base(username="anand", password="123", dob=223, address="test")
base2_instance = Base2.from_base(base_instance)
base2_instance.sub()

