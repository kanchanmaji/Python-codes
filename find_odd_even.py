
def odd_even(nums): # define funtion

	result = [] # create a balack list for data
	
	for num in nums: # loop for cheaking all num one by one form list "nums"
	
		if num%2==0: # cheak remainder =0
			result.append(f"{num} is even")
		else : 
			result.append(f"{num} is odd")
	return result

numin=[1, 2, 3 ,4 ,5] #input logic
nums=[]
for i in numin:
	nums.append(int(input(f"Enter {i} :")))
x = odd_even(nums) 
for s in x: # take out result from list
	print (s)
	
