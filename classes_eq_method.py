class Student():
	def __init__(self, math, history, writing):
		self.math = math
		self.history = history
		self.writing = writing

	@property
	def grades(self):
		return self.math + self.history + self.writing

	def __eq__(self, other_student):
		return self.grades == other_student.grades

	def __gt__(self, other_student):
		return self.grades > other_student.grades

	def __le__(self, other_student):
		return self.grades <= other_student.grades

	def __add__(self, other_student):
		return self.grades + other_student.grades

	def __sub__(self, other_student):
		return self.grades - other_student.grades

bob = Student(math = 90, history = 90, writing = 90)
rob = Student(math = 100, history = 80, writing = 90)
cob = Student(math = 40, history = 50, writing = 70)

print(bob == rob)
print(bob == cob)
print()
print(bob > cob)
print(rob > bob)
print(bob <= rob)
