import sys
with open(sys.argv[1]) as test_data:
	for test in test_data:
		test = test.rstrip()
		num = test.split(',')
		# print num
		sz = len(num)/2
		unique_nums = set(num)
		# print unique_nums
		find = False
		for n in unique_nums:
			if num.count(n) > sz:
				find = True
				print n
				break
		if find == False:
			print "None"