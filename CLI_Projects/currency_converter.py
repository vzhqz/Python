import os
import requests
from dotenv import load_dotenv
import time


def convert_currency(convert_from, convert_to, amount):
    base_url = f"https://v6.exchangerate-api.com/v6/{CURRENCY_API_KEY}/latest/{convert_from}"
    response = requests.get(base_url)
    
    if response.status_code == 200:
        currency_data = response.json()
        if convert_to in currency_data["conversion_rates"]:
            return currency_data["conversion_rates"][convert_to]
        else:
            print(f"\n❌ Invalid \"convert to\" currency: {convert_to}")
            return None
    else:
        print(f"\n❌ ERROR CONVERTING CURRENCY. Error Code: {response.status_code}\n")
        return None

## Retrieving the API key
load_dotenv()
CURRENCY_API_KEY = os.getenv('CURRENCY_API_KEY')

while True:
    print("==========================")
    print("💱  Currency Converter CLI")
    print("==========================")
    
    from_currency = input("🌍 From Currency: ").upper()
    to_currency = input("💱 To Currency: ").upper()
    amount = float(input("💵 Amount: "))

    if from_currency and to_currency and amount > 0:
        converstion_rate = convert_currency(from_currency, to_currency, amount)
        if converstion_rate:
            converted_currency = round(converstion_rate * amount, 1)
            print("\n🔄 Processing Conversion...")
            time.sleep(1.5)
            print("--------------------------")
            print(f"💵 {amount} {from_currency} = {converted_currency} {to_currency}")
            print(f"🔑 Exchange Rate: 1 {from_currency} = {converstion_rate} {to_currency}\n")
            print("--------------------------")

            user_continue = input("Would you like to convert another amount? (Y/n): ").lower()
            if user_continue == "y":
                os.system("cls")
                continue
            else:
                print("\n👋 Thank you for using the Currency Converter!")
                break
        else:
            input("⏪ Press Enter to try again...")
            os.system("cls")
            continue

    else:
        print("❌ Invalid Currency/Amount.")
        input("⏪ Press Enter to try again...")
        os.system("cls")

# ( im too lazy to add comments )