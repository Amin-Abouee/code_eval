import sys
with open(sys.atgv[1],'r') as test_case:
	for test in test_case:
		num = [int(x) for x in test.split(',')]
		s = set(num)
		print ','.join(map(str, s))