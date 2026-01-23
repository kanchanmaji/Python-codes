#for taking input
text = input("Enter the value \n\n")

#define which are vowels
vowels = "aeiouAEIOU"

#set vowel count to "0"
vowel_count =0
const_count =0

#creating a for loop for chaking 1 by 1
for char in text:
	if char.isalpha():
		if char in vowels:
			vowel_count +=1
		else:
			const_count+=1

#printing all the data counts
print(f"\n => Vowel count {vowel_count}")
print(f"\n => Consonant count {const_count}")
