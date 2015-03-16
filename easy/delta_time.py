import sys
from datetime import datetime
with open('sample.txt','r') as test_cases:
	for test in test_cases:
		t1 , t2 = test.split()
		FMT = '%H:%M:%S'
		if t2 > t1:
			time_delta = datetime.strptime(t2, FMT) - datetime.strptime(t1, FMT)
		
		else:
			time_delta = datetime.strptime(t1, FMT) - datetime.strptime(t2, FMT)

		print "%2d:%2d:%2d:" % (time_delta.hour, time_delta.minute, time_delta.second)
