#Write a Python program to print the multiplication table of a number entered by the user.

num=int(input("Enter your Number."))

for i in range(0,11):
	print(num,"X",i,"=",num*i)
	