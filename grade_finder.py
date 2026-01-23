#Using if-elif-else, write a program to grade #marks: 90–100 → A 75–89 → B 50–74 → C below
#50 → Fail

mark = int(input("\nEnter Your mark ?\n\n"))

if 100 >= mark >=90:
	print("Your Are Grade A")
elif 89>= mark >=75:
	print("Your Grade is B")
elif 74>= mark >= 50 :
	print("Your Grade Is C")
elif 100 < mark:
	print("You Enter A wrong Mark")
else :
	print("Your Are Failed")