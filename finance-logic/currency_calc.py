import urllib.request
import json

def get_live_rates():
    try:
        url = "https://open.er-api.com/v6/latest/USD"
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read())
            return data['rates']
    except:
        # These are our "Safety" rates if the internet fails
        return {"USD": 1, "ZAR": 18.50, "EUR": 0.92, "GBP": 0.79}

rates = get_live_rates()

print("--- 🌍 Universal Currency Converter ---")

# Step 1: Now including ZAR as an option!
base_currency = input("Select your input currency (USD, EUR, GBP, or ZAR): ").upper().strip()

# Step 2: Get the amount
amount = float(input(f"Enter the amount in {base_currency}: "))

# Step 3: Math (The USD "Bridge")
usd_value = amount / rates[base_currency]

# Converting to all four target currencies
price_zar = round(usd_value * rates['ZAR'], 2)
price_eur = round(usd_value * rates['EUR'], 2)
price_gbp = round(usd_value * rates['GBP'], 2)
price_usd = round(usd_value, 2)

# RESULTS
print(f"\nResults for {amount} {base_currency}:")
print(f"🇿🇦 ZAR: R{price_zar}")
print(f"🇪🇺 EUR: €{price_eur}")
print(f"🇬🇧 GBP: £{price_gbp}")
print(f"🇺🇸 USD: ${price_usd}")