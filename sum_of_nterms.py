#Write a program using for loop to calculate the sum of first N natural numbers 

num=int(input("\nEnter Your Number\n\n"))
total=0
for i in range ( 0, num+1):
	total +=i
print("\nTotal sum =", total)
