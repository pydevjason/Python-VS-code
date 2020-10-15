employee_salaries = {
	"Guido": 100_000,
	"James": 500_000,
	"Brandon": 900_000,
}

extra_employee_salaries = {
	"Yukihiro": 1_000_000,
	"Guido": 333_333,
}

# mutating method .update()
employee_salaries.update(extra_employee_salaries)
print(employee_salaries)