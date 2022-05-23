# What is the object here? PyChanger
#
# An object has: properties/attributes, methods
#
# property: base_currency
# method: set_currency()
#
# Think about a car; a car has 4 wheels(attribute) but a car can be started, start() (method)
#
# at what point does the attribute exist?
#
# Compare with Python's own tooling: string.uppercase()
#
# Init is a constructor. It allows default methods to run whenever a class is instantiated or when the context requires
# additional values to be passed to the object.
#
#
#
class PyChanger:
    amount = 100

    def __init__(self, base_currency="kes", exchange_rate=28):
        self.exchange_rate = None
        self.exchanged_currency = 'ugx'

        print('We are going to exchange money')

        # Method 1: override an attribute with externally provided value. This value is provided to constructor directly
        self.base_currency = base_currency

        # Method 2: override the attribute using a setter method.
        self.__set_exchange_rate(exchange_rate)

    def __set_exchange_rate(self, exchange_rate):
        self.exchange_rate = exchange_rate
        pass

    # Method 3: chaining methods. most flexible and recommended way for larger codebases. Returns self.
    def set_exchanged_currency(self, currency="gbp"):
        self.exchanged_currency = currency
        return self

    def convert(self):
        converted_amount = self.amount * self.exchange_rate

        print(str(self.amount) + " " + str(self.base_currency) + " converted to " + str(converted_amount) + " " + str(
            self.exchanged_currency))
