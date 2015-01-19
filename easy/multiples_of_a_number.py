import sys
test_cases = open('sample.txt', 'r')
for test in test_cases:
    # ignore test if it is an empty line
    # 'test' represents the test case, do something with it
    # ...
    # ...
    num = [int(x) for x in test.split(',')]
    a = num[0]
    b = num[1]
    cnt = 0
    while a > b:
    	a -= b
    	cnt += 1

    # print cnt
    print (cnt+1) * b
test_cases.close()