text = input("Enter Value \n\n")

text2 = text.split() # create a list of each word 

word_count = 0

for wc in text2:
	if wc.isalpha():  #ignore numers like 123 or kan123
		word_count +=1 
		
print(word_count)
			