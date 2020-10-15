# example 1

release_dates = {
	"Python": 1991,
	"Ruby": 1995,
	"Java": 1995,
	"Go": 2007,
}

year = release_dates.pop("Java")

def release_date(dictionary):
	dictionary = {}
	for k,v in dictionary.items():
		print(k,v)
	return dictionary

print(release_date(release_dates))
print()





	


