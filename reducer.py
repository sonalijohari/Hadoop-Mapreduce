from operator import itemgetter
import sys

current_digit = None
current_count = 0
digit = None

for line in sys.stdin:
	line = line.strip()
	digit, count = line.split('\t', 1)
	
	try:
		count = int(count)

	except ValueError:
		continue

	if current_digit == digit:
		current_count += count
	else:
		if current_digit:
			print '%s\t%s' % (current_digit, current_count)
		current_count = count
		current_digit = digit

if current_digit == digit:
	print '%s\t%s' % (current_digit, current_count)
