#!/usr/bin/env python3
# add imports, if necessary
from exchange_rates import EXCHANGE_RATES

def convert(amount, from_currency, to_currency):
    if isinstance(amount,int) or isinstance(amount,float):
        if not (isinstance(from_currency,str) and isinstance(to_currency,str)):
            raise Warning("Invalid input type for currency.")
        if from_currency == "" or to_currency == "":
            raise Warning("ValueError")
        
        currencies_list = EXCHANGE_RATES.keys()
        
        if from_currency in currencies_list and to_currency in currencies_list:
            try: 
                converted = amount * EXCHANGE_RATES[from_currency][to_currency]
                return converted
            except:
                converted = amount / EXCHANGE_RATES[to_currency][from_currency]            
                return converted
        else:
            raise Warning("Invalid currency to convert.")

    else:
        raise Warning("Invalid input type for amount.")
