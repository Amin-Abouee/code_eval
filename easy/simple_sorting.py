import sys
with open(sys.argv[1],'r') as test_cases:
	for test in test_cases:
		num = sorted([float(x) for x in test.split()])
		print ' '.join(['%.3f' % x for x in num])