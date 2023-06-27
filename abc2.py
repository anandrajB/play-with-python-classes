from abc import ABC, abstractmethod

class CurrencyABC(ABC):
    @abstractmethod
    def get_finance_currency(self):
        pass

    @abstractmethod
    def set_finance_currency(self, value):
        pass

@dataclass
class Currency(CurrencyABC):
    finance_currency: str
    base_currency: str
    
    @property
    def get_finance_currency(self):
        return self.finance_currency

    def set_finance_currency(self, value):
        self.finance_currency = value


# Usage example:
currency = Currency(finance_currency="USD", base_currency="USD")

# Accessing the finance currency through the abstraction layer
print(currency.get_finance_currency)  # Output: USD

# Modifying the finance currency through the abstraction layer
currency.set_finance_currency("EUR")
print(currency.get_finance_currency)  # Output: EUR
