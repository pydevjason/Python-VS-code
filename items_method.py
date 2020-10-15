# the items method returns an iterator object which can be iterated over

# example 1

college_courses = {
	"History": "Mr. Washington",
	"Math": "Mr. Newton",
	"Science": "Mr. Einstein",
}

for key, value in college_courses.items():
	print(f"The course {key} is being taught by {value}.")