import requests
import json
import sys

if len(sys.argv) < 2:
    print("Missing command-line argument")
    sys.exit()
try:
    num = float(sys.argv[1])
except ValueError:
    print("Command-line argument is not a number")
    sys.exit()

try:
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=7fcfa00d62a74eeb8a5beebaae943064d73a30e760589ec8558d923bab24742c")
    crypto = response.json()
    data = crypto["data"]
    price = num * float(data["priceUsd"])
except requests.RequestException:
    sys.exit()

print(f"${price:,.4f}")