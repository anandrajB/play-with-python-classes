
from dataclasses import dataclass

@dataclass
class base:

    a : int

    @staticmethod
    def static_fun():
        return a + 5

    def main(self):
        return self.static_fun(a = self.a)