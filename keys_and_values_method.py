cryptocurrency_prices = {
	"Bitcoin": 400_000,
	"Etherium": 7_000,
	"Litecoin": 10,
}

print(cryptocurrency_prices.keys())
print(cryptocurrency_prices.values())
print()

for currency in cryptocurrency_prices.keys():
	print(f"The next currency is {currency}")
print()

for price in cryptocurrency_prices.values():
	print(f"The price is {price}")
print()

for types, prices in cryptocurrency_prices.items():
	print(f"{types} is currently selling for {prices}")
print()

print("Bitcoin" in cryptocurrency_prices.keys())
print("Ripple" in cryptocurrency_prices.keys())



