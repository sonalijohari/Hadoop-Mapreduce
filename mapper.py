import sys

for line in sys.stdin:
	line = line.strip()
	for i in line:
		if i == '.':
			continue
		print '%s\t%s' % (i,'1')
