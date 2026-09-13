import requests
print("===== CURRENCY CONVERTER =====") 
from_currency = input("Enter currency to convert from: ").upper() 
to_currency = input("Enter currency to convert to: ").upper() 
amount = float(input("Enter amount: ")) 
url = "https://api.frankfurter.dev/v1/latest" 
params = {    
    "base": from_currency,    
    "symbols": to_currency 
} 
response = requests.get(url, params=params, timeout=10) 
if response.status_code == 200:    
    data = response.json()    
    rate = data["rates"][to_currency]    
    converted_amount = amount * rate    
    print("\n===== CONVERSION RESULT =====")    
    print("Exchange Rate:", rate)    
    print(amount, from_currency, "=", round(converted_amount, 2), to_currency) 
else:    
    print("Unable to get exchange rate.")