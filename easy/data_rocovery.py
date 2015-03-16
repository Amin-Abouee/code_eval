import sys
with open(sys.argv[1],'r') as test_cases:
	for test in test_cases:
		a , b = test.rstrip().split(';')
		word = [x for x in a.split()]
		print word
		num = [int(x) for x in b.split()]
		print num
		for x in xrange(1,len(word)+1):
			# print x
			if x in num:
				print word[num.index(x)],
			else:
				print word[len(word)-1],
		print 

		# list1, list2 = (list(t) for t in zip(*sorted(zip(num, word))))
