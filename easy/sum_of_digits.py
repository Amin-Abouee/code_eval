import sys
test_cases = open('sample.txt', 'r')
for test in test_cases:
    # ignore test if it is an empty line
    # 'test' represents the test case, do something with it
    # ...
    # ...
    sum = 0
    test = test.rstrip()
    for n in test:
    	# print n
    	sum += int(n)
    print sum
    
test_cases.close()