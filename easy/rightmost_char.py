import sys
with open(sys.argv[1],'r') as test_case:
	for test in test_case:
		test = test.rstrip()
		a,b = test.split(',')
		print a.rfind(b)