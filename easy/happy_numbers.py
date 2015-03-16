import sys
with open(sys.argv[1],'r') as test_case:
	for test in test_case:
		test = test.rstrip()
		find_num = []
		while True:
			num = sum([int(x)*int(x) for x in test])
			# print num
			if num == 1:
				print 1
				break
			elif num in find_num:
				print 0
				break
			else:
				find_num.append(num)
				test = str(num)
