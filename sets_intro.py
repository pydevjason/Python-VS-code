# set is an unordered mutable data structure that prohibits duplicate values
# any duplicates from the following sets have been removed by Python
# sets do not support indexing because indexing implies order.  If order is needed a list is the best choice

stocks = {"MSFT", "FB", "IBM", "FB"}
print(stocks)

prices = {1, 2, 3, 4, 5, 3, 4, 2}
print(prices)

lottery_numbers = {(1, 2, 3), (4, 5, 6), (1, 2, 3)}
print(lottery_numbers)

print()

print(len(stocks))
print(len(prices))
print(len(lottery_numbers))

print()

print("MSFT" in stocks)
print("IBM" in stocks)
print("GOOG" in stocks)
print()

# sets are iterable but you should not assume that they will come out in order, it's purely coincidental 

for i in stocks:
	print(i)
print()

for value in lottery_numbers:
	for k in value:
		print(k)
print()
# sets also support set comprehensions similar to list and dictionary comprehensions

sqaures = {pow(number, 2) for number in [-5, -4, -3, 3, 4, 5]}
print(sqaures)
print(len(sqaures))