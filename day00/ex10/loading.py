import time

def get_bar(percent):
	progress_len = int(percent/4)
	bar = '=' * progress_len
	bar += '>'
	return bar

def ft_progress(list):
	total = len(list)
	count = 1
	start = time.time()
	estimation = 0
	for elem in list:
		elapsed = time.time() - start
		percent = int((count / total) * 100)
		if (count == 2):
			estimation = elapsed
		estimated = estimation * (total - count)
		bar = get_bar(percent)
		print("ETA: {: >5.2f}s [{: >3}%][{:<26}] {}/{} | elapsed time {:.2f}s".format(estimated, percent, bar, count, total, elapsed), end="\r")
		count += 1
		yield elem

