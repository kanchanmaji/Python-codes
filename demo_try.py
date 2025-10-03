print("*"*30)
print("sum Of two digit")
print("*"*30)
def funtion(a,b):
    ''' This Funtion for Adding two numbers'''
    total = a + b
    return total

value=["num 1","num 2"]
digits=[]

for i in value:
    digit=int(input(f"Enter {i} :- \n"))
    digits.append(digit)

total = funtion((digits[0]),(digits[1]))
print("*"*30)
print("Your Sum is ",total)
print("*"*30)