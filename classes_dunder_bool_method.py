class Emotion():
	def __init__(self, positivity, negativity):
		self.positivity = positivity
		self.negativity = negativity

	def __bool__(self):
		return self.positivity > self.negativity

emotional_state = Emotion(positivity = 100, negativity = 50)
print(emotional_state)

if emotional_state:
	print("This will print")