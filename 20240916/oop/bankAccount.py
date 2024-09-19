class Account:
    def __init__(self, number, name, initial_amount=1000):
        self.__number = number
        self.__name = name
        self.__balance = initial_amount
    def __repr__(self):
        return f'[number={self.__number}, name={self.__name}, balance={self.__balance}]'
    def __str__(self):
        return self.__repr__()
    def deposit(self, amount):
        self.__balance += amount
    def withdraw(self, amount):
        if amount > self.__balance:
            print('No enough balance')
            return
        self.__balance -= amount
    #end def
#end class
sahithya_ac = Account(name='sahithya',number='1344000000777',initial_amount=3000)
print(sahithya_ac)
sahithya_ac.deposit(200000)
print(sahithya_ac)
sahithya_ac.deposit(100000)
print(sahithya_ac)
sahithya_ac.withdraw(50000)
print(sahithya_ac)
#print(sahithya_ac.__dict__)
#print(sahithya_ac.__balance)
sahithya_ac.withdraw(200000)
print(sahithya_ac)

