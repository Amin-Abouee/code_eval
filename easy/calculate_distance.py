import sys
import re
import math
with open(sys.argv[1]) as test_cases:
	for test in test_cases:
		t = re.findall("[+-]?\d+", test)
		nums = [int(x) for x in t]
		print int(math.sqrt((nums[0]-nums[2]) * (nums[0]-nums[2]) + (nums[1]-nums[3]) * (nums[1]-nums[3])))