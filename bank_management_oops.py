class BankAccount:
	def __init__(self,acc_no,holder_name,balance):
		self.acc_no = acc_no
		self.holder_name = holder_name
		self.__balance = balance
		
	def user_info(self):
		info = f"Holder name = {self.holder_name}\nAccount no. = {self.acc_no}\n Balance = {self.__balance} "            
		return info
		
	def deposit_money(self,amount):
		if amount > 0:
			self.__balance += amount
			return f"{amount} deposit sucessfully "
		else :
			return "something went wrong"
			
	def withdraw_money(self,amount):
		if self.__balance>=amount>0:
			self.__balance -= amount
			return f"{amount} Withdrawn successfully"
		else :
			return "Something went wrong"
	@property
	def balance(self):
		return self.__balance
		
class SavingAccount(BankAccount):
					def __init__(self,acc_no,holder_name,balance,intrest_rate):
						super().__init__(acc_no,holder_name,balance)
						self.intrest_rate = intrest_rate
						
					def add_intrest(self):
						intrest = self.balance * (self.intrest_rate/100)
						self.deposit_money(intrest)
						return f"{intrest} added succecfully"
						
class CurrentAccount(BankAccount):
		def __init__(self,acc_no,holder_name,balance,overdraft):
			super().__init__(acc_no,holder_name,balance)	
			self.overdraft = overdraft
				
		def withdraw_money(self,amount):
			if (self.balance + self.overdraft)>=amount>0:
				self.balance -= amount
				return "Withdrawn success"
			else :
				return "Overdraft used"


			