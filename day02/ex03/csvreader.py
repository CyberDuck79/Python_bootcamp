

class CsvReader():
	def __init__(self, filename, sep=',', header=False, skip_top=0, skip_bottom=0):
		try:
			self.file = open(filename, 'r')
		except FileNotFoundError:
			self.error = 1
			return
		self.error = 0
		self.data = []
		if header:
			self.header = self.file.readline().split(sep=sep)
			# ajouter le cleaning
			self.size = len(self.header)
			if skip_top:
				self.file.readline()
			buffer = self.file.readlines()
			for line in buffer[:-1]:
				zipdata = zip(self.header, line.split(sep=sep))
				self.data.append(dict(zipdata))
				if (self._check_corrupt()):
					return
			if not skip_bottom:
				zipdata = zip(self.header, buffer[-1].split(sep=sep))
				self.data.append(dict(zipdata))
		else:
			if (skip_top):
				self.file.readline()
			buffer = self.file.readline().split(sep=sep)
			self.size = len(buffer)
			self.data.append(buffer.copy())
			buffer = self.file.readlines()
			for line in buffer[:-1]:
				self.data.append(line.split(sep=sep))
				if (self._check_corrupt()):
					return
			if not skip_bottom:
				self.data.append(buffer[-1].split(sep=sep))

	def __enter__(self):
		if self.error:
			return None
		return self

	def __exit__(self, type, value, traceback):
		self.file.close

	def __check_corrupt(self):
		if len(self.data[-1]) != self.size:
			self.error = 1
			return True
		else:
			return False

	def getdata(self):
		return self.data

	def getheader(self):
		if hasattr(self, "header"):
			return self.header
		return None

with CsvReader('good.csv', header=True) as file:
	data = file.getdata()
	header = file.getheader()
print(header)
for elem in data:
	print(elem)