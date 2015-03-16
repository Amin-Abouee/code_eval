import sys
with open(sys.argv[1],'r') as test_case:
	for test in test_case:
		a,b = test.split(';')
		n = [int(x) for x in a.split(',')]
		m = [int(x) for x in b.split(',')]
		res = [item for item in n if item in m]
		print ','.join(map(str,res))