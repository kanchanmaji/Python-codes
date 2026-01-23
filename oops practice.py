
#"""Level 1 """


class student:
	def __init__(self , name , age , grade):
		self.name= name
		self.age = age
		self.grade =grade
		
	def get_info(self):
		return f"student name {self.name} of age {self.age} have grade {self.grade}"
		
s = student("Jhon Doe" , 10 , 85)
p = s.get_info()
print(p)



#"""Level 2 """


class Employee:
	company = "Forxcode"
	
	def __init__(self,name,sallary):
		self.name = name
		self.sallary = sallary
	
	def work(self):
		return f"{self.name} is the emplyoee of {Employee.company} is currently Working"

class Developer(Employee):
	def work(self):
		return f"{self.name} is currently writting code"
class Manager(Employee):
	def work(self):
		return f" {self.name} is managing team"
	
Employees =[
		Developer("Jhon" , 32000),
		Manager("Bob", 40000),
		Employee("Kiko" , 30000)
]

for emp in Employees:
	print(emp.work()) 
	

	
#"""Level 3 """


class BankAccount:
    def __init__(self, balance):
        # Encapsulation: make balance a "protected" attribute
        self._balance = balance

    # Property getter
    @property
    def balance(self):
        return self._balance

    # Property setter (validation)
    @balance.setter
    def balance(self, value):
        if value < 0:
            print("❌ Balance cannot be negative!")
        else:
            self._balance = value

    # Deposit and Withdraw
    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            print("❌ Insufficient funds!")
        else:
            self._balance -= amount

    # Operator overloading for +
    def __add__(self, other):
        total = self._balance + other._balance
        return BankAccount(total)

    def __str__(self):
        return f"Bank Balance = ₹{self._balance}"


# --- Test the class ---
acc1 = BankAccount(1000)
acc2 = BankAccount(500)
acc3 = acc1 + acc2  # Calls __add__

print(acc1)  # Bank Balance = ₹1000
print(acc2)  # Bank Balance = ₹500
print(acc3)  # Bank Balance = ₹1500