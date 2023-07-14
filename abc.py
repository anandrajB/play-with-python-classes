from abc import abstractmethod , ABC


class base(ABC):

    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def get_base_data(self):
        pass


class Main(base):
    def __init__(self,a):
        self.a = a

    @property
    def get_data(self):
        return self.a

    def get_base_data(self):
        return self.a


obj = Main(a = 5).get_base_data()
print(obj)