# Below are a set of scores that students have received in the past semester. 
# Write code to determine how many are 90 or above and assign that result to the value a_scores.

scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"

def ninety_or_above(string):
	string = string.split(" ")
	a_scores = 0
	for i in string:
		if int(i) >= 90:
			a_scores += 1
	return a_scores

print(ninety_or_above(scores))

print()

def ninety_or_above2(string):
	string = string.split(" ")
	a_scores = []
	for k in string:
		if int(k) >= 90:
			a_scores.append(k)
	return a_scores

print(ninety_or_above2(scores))
print()

'''
Write code that uses the string stored in org and creates an acronym which is assigned to the
variable acro. 

Only the first letter of each word should be used, each letter in the acronym 
should be a capital letter, and there should be nothing to separate the letters of the acronym.

Words that should not be included in the acronym are stored in the list stopwords.
For example, if org was assigned the string “hello to world” then the resulting acronym 
should be “HW”.
'''

stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"



def acronym(string):
	string = string.split(" ")
	acro = ""
	for j in string:
		if j not in stopwords:
			acro += j[0].upper()
	return acro

print(acronym(org))
print()


'''
Write code that uses the string stored in sent and creates an acronym which is assigned to 
the variable acro. The first two letters of each word should be used, each letter in the acronym 
should be a capital letter, and each element of the acronym should be separated 
by a “. ” (dot and space). Words that should not be included in the acronym are stored 
in the list stopwords. For example, if sent was assigned the string “height and ewok wonder” 
then the resulting acronym should be “HE. EW. WO”.
'''

stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"

# acro = '. '.join(word[:2].upper() for word in sent.split() if word not in stopwords)
# print(acro)

def acronym2(string):
	# string = string.split(". ")
	acro = ""
	for x in string.split(". "):
		if x not in stopwords:
			# ", ".join(x[:2].upper())
			acro += x[:2].upper()
	return acro

print(acronym2(sent))