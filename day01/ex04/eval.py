class Evaluator:
	def zip_evaluate(coefs: list, words: list):
		if not isinstance(coefs, list) or not all(isinstance(n, float) for n in coefs):
			raise TypeError("Coefs type error")
		if not isinstance(words, list) or not all(isinstance(n, str) for n in words):
			raise TypeError("Words type error")
		if len(coefs) != len(words):
			return -1
		evaluation_list = zip(coefs, words)
		evaluation_sum = 0
		for elem in evaluation_list:
			evaluation_sum += elem[0] * len(elem[1])
		return evaluation_sum

	def enumerate_evaluate(coefs: list, words: list):
		if not isinstance(coefs, list) or not all(isinstance(n, float) for n in coefs):
			raise TypeError("Coefs type error")
		if not isinstance(words, list) or not all(isinstance(n, str) for n in words):
			raise TypeError("Words type error")
		if len(coefs) != len(words):
			return -1
		evaluation_sum = 0
		for i, coef in enumerate(coefs):
			evaluation_sum += coef * len(words[i])
		return evaluation_sum

words = ["Le", "Lorem", "Ipsum", "n'", "est", "pas", "test"]
coefs = [1.0, 2.0, 1.0, 4.0, "test"]
print(Evaluator.zip_evaluate(coefs, words))