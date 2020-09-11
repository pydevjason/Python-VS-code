def feet_to_meters(feet, inches):
	total_inches = (feet * 12) + inches
	return f"{total_inches * 0.0254:.2f}"

print(feet_to_meters(5, 11))

stats = {
	"feet": 5,
	"inches": 11,
}

print(feet_to_meters(**stats))