# If a class defines neither a __bool__ nor a __len__ magic method, will the object be considered truthy or falsy? Provide some code to prove your case.


class Mouse():
	def __init__(self, color, kind):
		self.color = color
		self.kind = kind

mouse = Mouse("white", "bluetooth")
print(mouse.__len__("white"))
# print(mouse.__bool__())
