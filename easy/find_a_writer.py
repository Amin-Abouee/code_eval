import sys
with open(sys.argv[1],'r') as test_cases:
	for test in test_cases:
		a,b = test.split('|')
		num = [int(x) for x in b.split()]
		print ''.join([a[p-1] for p in num])