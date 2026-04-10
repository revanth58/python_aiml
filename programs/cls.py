class Account:

	def __init__(self, acc_no, owner_name):
		self.acc_no = acc_no
		self.balance = 0
		self.owner_name = owner_name
		self.branch = "vzm"

	def __init__(self, acc_no, balance, owner_name, branch)
		self.acc_no = acc_no
		self.balance = balance
		self.owner_name = owner_name
		self.branch = branch

	def deposit(self, amount):
		self.balance += amount
		return 1

	def withdraw(self, amount):
		if self.balance < amount :
			print("insifficient balance")
			return -1
		self.balance -= amount
		return 1

def transaction(sender, reciever, amount):
	x = sender.withdraw(amount)
	reciever.deposit(amount)
	return x

rollno1 = Account(1,"mukesh")
rollno2 = Account(2,"samad")

rlno3 = Account(3,10000,"michael","hyd")

print(rollno1.owner_name)
print(rollno2.balance)

rollno1.deposit(10000)
rollno1.withdraw(9000)
rollno1.withdraw(1200)