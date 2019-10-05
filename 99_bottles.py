# Beginner project 99 bottles from https://github.com/jorgegonzalez/beginner-projects#99-bottles
# Create a program that prints out every line to the song "99 bottles of beer on the wall."
# Do not use a list for all of the numbers, and do not manually type them all in. Use a built in function instead.
# Besides the phrase "take one down," you may not type in any numbers/names of numbers directly into your song lyrics.
# Remember, when you reach 1 bottle left, the word "bottles" becomes singular.

for x in reversed(range(1,100)):
	if x > 2:
		print (
			str(x) + " bottles of beer on the wall "
			+ str(x) + " bottles of beer."
			+ " Take one down, pass it around. "
			+ str(x-1) + " bottles of beer on the wall."
			)
	elif x == 2:
		print (
			str(x) + " bottles of beer on the wall "
			+ str(x) + " bottles of beer."
			+ " Take one down, pass it around. "
			+ str(x-1) + " bottle of beer on the wall."
			)
	else:
		print (
			str(x) + " bottle of beer on the wall "
			+ str(x) + " bottle of beer."
			+ " Take one down, pass it around. "
			+ str(x-1) + " bottles of beer on the wall."
			)
