# For each word in words, add ‘d’ to the end of the word if the word ends in “e” to make it past tense. Otherwise, add ‘ed’ to make it past tense. Save these past tense words to a list called past_tense.

words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]


def past_tense(str_list):
	past_tense = []
	for i in words:
		if "e" in i[-1]:
			i += "d"
			past_tense.append(i)
		else:
			i += "ed"
			past_tense.append(i)
	return past_tense

print(past_tense(words))

print()
# For each string in the list words2, find the number of characters in the string. If the number of characters in the string is greater than 3, add 1 to the variable num_words so that num_words should end up with the total number of words with more than 3 characters.

words2 = ["water", "chair", "pen", "basket", "hi", "car"]

def str_more_than_three(str_list):
	num_words = 0
	for i in str_list:
		if len(i) > 3:
			num_words += 1
	return num_words

print(str_more_than_three(words2))
print()

# Write code that will count the number of vowels in the sentence s and 
# assign the result to the variable num_vowels. For this problem, vowels are 
# only a, e, i, o, and u. Hint: use the in operator with vowels.

s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"

def vowel_count(string):
	vowels = ["a", "e", "i", "o", "u"]
	num_vowels = 0
	for i in string:
		if i in vowels:
			num_vowels += 1
	return num_vowels
print(vowel_count(s))
print()

# Write code that counts the number of words in sentence that contain either 
# an “a” or an “e”. Store the result in the variable num_a_or_e.
# Note 1: be sure to not double-count words that contain both an a and an e.
# HINT 1: Use the in operator.
# HINT 2: You can either use or or elif.
# Hard-coded answers will receive no credit.

sentence = "Python is a high level general purpose programming language that can be applied to many different classes of problems."

def a_or_e_count(string):
	split_str = string.split(" ")
	num_a_or_e = 0
	for i in split_str:
		if "a" in i or "e" in i:
			num_a_or_e += 1
	return num_a_or_e

print(a_or_e_count(sentence))