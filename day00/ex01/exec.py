import sys

words_list = []
for arg in sys.argv[1:]:
	for word in arg.split():
		words_list.append(word[::-1].swapcase())
words_list.reverse()
print(' '.join(words_list))
