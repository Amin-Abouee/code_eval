import sys
import collections
with open(sys.argv[1],'r') as test_cases:
	for test in test_cases:
		nums = [x for x in test.split()]
		c = collections.Counter(nums)
		print c
		check = False
		for key, values in sorted(c.iteritems()):
			if values == 1:
				print nums.index(key)+1
				check = True
				break
		if check == False:
			print 0

