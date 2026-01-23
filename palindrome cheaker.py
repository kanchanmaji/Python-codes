text = input("Enter Value \n\n")

text2 = ""

for char in text:
	text2 = char + text2
if text == text2:
	print("This is Palindrome")
else:
	print("Normal Text")