import sys
import re
with open(sys.argv[1],'r') as test_cases:
	for test in test_cases:
		a,b = test.split(':')
		nums = [x for x in a.split()]
		elemets = re.findall('\d+',b)
		for i in xrange(0,len(elemets),2):
			nums[int(elemets[i])] , nums[int(elemets[i+1])] = nums[int(elemets[i+1])] , nums[int(elemets[i])]
		print ' '.join(nums)
