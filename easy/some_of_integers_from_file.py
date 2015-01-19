import sys
with open(sys.argv[1],'r') as test_case:
	sum = 0
	for test in test_case:
		sum += int(test)
	print sum 