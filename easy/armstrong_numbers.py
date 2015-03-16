import sys
with open(sys.argv[1],'r') as test_case:
	for test in test_case:
		test = test.strip()
		size = len(test)
		print int(test) == sum([int(x) ** size for x in test])