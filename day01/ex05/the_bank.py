# in the_bank.py
class Account(object):

	ID_COUNT = 1
	LAST_ERROR = 0

	def __init__(self, name, **kwargs):
		self.id = self.ID_COUNT
		self.name = name
		self.__dict__.update(kwargs)
		if hasattr(self, 'value'):
			self.value = 0
		Account.ID_COUNT += 1

	def receive(self, amount):
		self.value += amount

	def send(self, amount):
		self.value -= amount

	def __str__(self):
		string = f"Name : {self.name}\n"
		string += f"ID : {self.id}\n"
		if (hasattr(self, 'value')):
			string += f"Amount : {self.value}\n"
		if (hasattr(self, 'address')):
			string += f"Address : {self.address}\n"
		return string

# in the_bank.py
class Bank(object):
	"""The bank"""

	ERRORS = ["no_error", "even", "start_b", "missing addr", "mandatory"]

	def __init__(self):
		self.account = []

	def add(self, account):
		self.account.append(account)

	def check_account(self, account: Account, name: str):
		attributes = dir(account)
		if not len(attributes) % 2:
			Account.LAST_ERROR = 1
			raise ValueError(f"{name} account is corrupted : even number of attributes.")
		addr_check = 0
		for attr in attributes:
			if attr.startswith('b'):
				Account.LAST_ERROR = 2
				raise ValueError(f"{name} account is corrupted : an attribute start with b.")
			elif attr.startswith("zip") or attr.startswith("addr"):
				addr_check = 1
		if not addr_check:
			Account.LAST_ERROR = 3
			raise ValueError(f"{name} account is corrupted : missing an address attibute.")
		if not hasattr(account, 'name') or not hasattr(account, 'id') or not hasattr(account, 'value'):
			Account.LAST_ERROR = 4
			raise ValueError(f"{name} account is corrupted : missing mandatory attributes.")

	def get_account(self, search_id):
		if isinstance(search_id, str):
			for account in self.account:
				if account.name == search_id:
					return account
		elif isinstance(search_id, int):
			for account in self.account:
				if account.id == search_id:
					return account
		raise TypeError("Erreur, ID ou nom inconnu")


	def transfer(self, origin, dest, amount: int):
		"""
			@origin: int(id) or str(name) of the first account
			@dest:    int(id) or str(name) of the destination account
			@amount: float(amount) amount to transfer
			@return         True if success, False if an error occured
		"""
		origin_account = self.get_account(origin)
		dest_account = self.get_account(dest)
		try:
			self.check_account(origin_account, "origin")
		except ValueError:
			try:
				print(f"{origin_account.name} account corrupted, launch fixing...")
			except AttributeError:
				print(f"{origin_account.id} account corrupted, launch fixing...")
			self.fix_account(origin_account)
		try:
			self.check_account(dest_account, "dest")
		except ValueError:
			try:
				print(f"{dest_account.name} account corrupted, launch fixing...")
			except AttributeError:
				print(f"{dest_account.id} account corrupted, launch fixing...")
			self.fix_account(dest_account)
		if not isinstance(amount, int) or amount < 0:
			raise ValueError("Error : amount is negative or not number")
		if origin_account.value < amount:
			print("Error: insufficient fund in origin account.")
		else:
			origin_account.send(amount)
			dest_account.receive(amount)

	def fix_account(self, account):
		"""
			fix the corrupted account
			@account: int(id) or str(name) of the account
			@return         True if success, False if an error occured
		"""
		print(f"Fixing Account {account.name}")
		if Account.LAST_ERROR == 1:
			print("even attributes error")
			if hasattr(account, "dummy"):
				del account.dummy
			else:
				account.dummy = 0
		elif Account.LAST_ERROR == 2:
			print("start with b attribute error")
			for attr in dir(account):
				if attr.startswith('b'):
					delattr(account, attr)
		elif Account.LAST_ERROR == 3:
			print("Missing address error")
			account.address = input("enter an address: ")
		elif Account.LAST_ERROR == 4:
			if not hasattr(account, "name"):
				print("Missing name error")
				account.name = input("enter a new name: ")
			if not hasattr(account, "id"):
				for i, account_search in enumerate(self.account, 1):
					if i != account_search.id:
						account.id = i
				if not account.id:
					account.id = Account.ID_COUNT
					Account.ID_COUNT += 1
			while not hasattr(account, "value"):
				print("Missing amount error")
				try:
					new_value = int(input("enter the new fixed amount: "))
					account.value = new_value
				except ValueError:
					print("Error: please enter a number.")
		print(f"{account.name} account fixing OK")
		Account.LAST_ERROR = 0

the_bank = Bank()
patrick_account = Account("Patrick",value=0,address="4 rue du temple")
patrick_account.receive(1000)
print(patrick_account)
robert_account = Account("Robert",value=0,address="8 rue du chat")
robert_account.receive(100)
print(robert_account)
the_bank.add(patrick_account)
the_bank.add(robert_account)
the_bank.transfer("Patrick", "Robert", 100)
print(patrick_account)
print(robert_account)
paul_account = Account("Paul",value=0)
paul_account.receive(500)
print(paul_account)
the_bank.add(paul_account)
the_bank.transfer("Patrick", "Paul", 100)
the_bank.transfer("Paul", "Robert", 5000)
print(paul_account)
the_bank.transfer("Paul", "Alphonse", 5000)
# OK je suis debile y'a deja des fichiers de test : a tester plus tard
