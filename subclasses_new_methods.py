class Employee():
	def do_work(self):
		print("I'm working!")

class Manager(Employee):
	def waste_time(self):
		print("Love putting my feet up on the desk!")

class Director(Manager):
	def fire_employee(self):
		print("You're fired!")



employee = Employee()
manager = Manager()
director = Director()

employee.do_work()
manager.do_work()
manager.waste_time()
# employee.waste_time()

director.do_work()
director.waste_time()
director.fire_employee()