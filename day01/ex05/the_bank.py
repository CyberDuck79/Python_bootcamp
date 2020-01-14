# in the_bank.py
class Account(object):
	ID_COUNT = 1
	def __init__(self, name, **kwargs):
		self.id = self.ID_COUNT
		self.name = name
		self.__dict__.update(kwargs)
		if hasattr(self, 'value'):
			self.value = 0
		Account.ID_COUNT += 1
	def transfer(self, amount):
		self.value += amount

# in the_bank.py
class Bank(object):
	"""The bank"""
	def __init__(self):
		self.account = []
	def add(self, account):
		self.account.append(account)
	
	def check_account(self, account: Account, name: str):
		if not isinstance(account, Account):
			raise TypeError("the account is not a account instance.")
		attributes = dir(account)
		if not len(attributes) % 2:
			raise ValueError(f"{name} account is corrupted : even number of attributes.")
		for attr in attributes:
			if attr.startswith('b'):
				raise ValueError(f"{name} account is corrupted : an attribute start with b.")
			elif attr.startswith("zip") or attr.startswith("addr"):
				check_arg = 1
		if not check_arg:
			raise ValueError(f"{name} account is corrupted : missing mandatory attributes.")
		if "name" not in attributes or "id" not in attributes or "value" not in attributes:
			raise ValueError(f"{name} account is corrupted : missing mandatory attributes.")
	
	def transfer(self, origin, dest, amount):
		"""
			@origin: int(id) or str(name) of the first account
			@dest:    int(id) or str(name) of the destination account
			@amount: float(amount) amount to transfer
			@return         True if success, False if an error occured
		"""
		self.check_account(origin, "origin")
		self.check_account(dest, "dest")
		if amout < 0:
			raise ValueError("Amount is negative.")
		if origin.amount < amount:
			print("Error: insufficient fund in origin account.")

	def fix_account(self, account):
		"""
			fix the corrupted account
			@account: int(id) or str(name) of the account
			@return         True if success, False if an error occured
		"""


