import sys
with open(sys.argv[1],'r') as test_cases:
	for test in test_cases:
		test = test.rstrip()
		if int(test[-1]) % 2 == 0:
			print 1
		else:
			print 0