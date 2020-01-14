import time

def get_bar(percent):
	progress_len = int(percent/4)
	bar = '=' * progress_len
	bar += '>'
	return bar

def ft_progress(list):
	total = len(list)
	start = time.time()
	estimation = 0
	for count, elem in enumerate(list, 1):
		elapsed = time.time() - start
		percent = int((count / total) * 100)
		if (count == 2):
			estimation = elapsed
		estimated = estimation * (total - count)
		bar = get_bar(percent)
		print(f"ETA: {estimated: >5.2f}s [{percent: >3}%][{bar:<26}] {count}/{total} | elapsed time {elapsed:.2f}s", end="\r")
		yield elem

# for testing the function
listy = range(1000)
ret = 0
for elem in ft_progress(listy):
	ret += (elem + 3) % 5
	time.sleep(0.01)
print()
print(ret)
