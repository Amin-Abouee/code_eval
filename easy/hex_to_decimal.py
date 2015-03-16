import sys
with open(sys.argv[1],'r') as test_case:
	for test in test_case:
		print int(test,16)