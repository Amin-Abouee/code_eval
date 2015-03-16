import sys
with open(sys.argv[1],'r') as test_cases:
	for test in test_cases:
		a,b = test.split('|')
		a_num = [x for x in a.split()]
		b_num = [x for x in b.split()]
		res = [int(a) * int(b) for a,b in zip(a_num,b_num)]
		print ' '.join(map(str, res))