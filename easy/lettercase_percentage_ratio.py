import sys
with open(sys.argv[1],'r') as test_cases:
	for test in test_cases:
		test = test.rstrip()
		low_cnt = 0
		high_cnt = 0
		for c in test:
			if c.islower():
				low_cnt += 1
			else:
				high_cnt += 1

		cz = float(len(test))
		print "lowercase: %.2f uppercase: %.2f" % ((low_cnt * 100 /cz),(high_cnt * 100 /cz))