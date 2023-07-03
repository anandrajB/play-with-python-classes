class base:

    __slots__ = ['a' , 'b']

    def __init__(self,a,b):
        self.a = a 
        self.b = b

    def main(self):
        return self.a 


ins = base(a = 2 , b = 1)
print(ins)