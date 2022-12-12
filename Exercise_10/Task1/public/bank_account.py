#!/usr/bin/env python3
# add imports, if necessary
from currency_converter import convert
from exchange_rates import EXCHANGE_RATES

class BankAccount:

    def __init__(self, currency="CHF"):
        self.__ALL_CURRENCY = EXCHANGE_RATES.keys()
        if not currency in self.__ALL_CURRENCY:
            raise Warning("Given currency does not exist.")
        self.__currency = currency
        self.__balance = 0

    def get_currency(self):
        return self.__currency

    def get_balance(self):
        return self.__balance
        
    def deposit(self, amount, currency="CHF"):
        if not (isinstance(amount,int) or isinstance(amount,float)):
            raise Warning("Invalid input type for amount.")
        if not isinstance(currency,str):
            raise Warning("Invalid input type for currency.")
        if not currency in self.__ALL_CURRENCY:
            raise Warning("Given currency does not exist.")
        if amount <= 0:
            raise Warning("ValueError")
        if self.__currency == currency:
            self.__balance += amount
        else:
            self.__balance += convert(amount,currency,self.__currency)
    
    def withdraw(self, amount, currency="CHF"):
        if not (isinstance(amount,int) or isinstance(amount,float)):
            raise Warning("Invalid input type for amount.")
        if not isinstance(currency,str):
            raise Warning("Invalid input type for currency.")
        if not currency in self.__ALL_CURRENCY:
            raise Warning("Given currency does not exist.")
        if amount <=0:
            raise Warning("ValueError")
        
        if currency == self.__currency:
            if self.__balance < amount:
                raise Warning("ValueError")
            else:
                self.__balance -= amount
        else:        
            converted = convert(amount,currency,self.__currency)
            if self.__balance<converted:
                raise Warning("ValueError")
            else:
                self.__balance -= converted