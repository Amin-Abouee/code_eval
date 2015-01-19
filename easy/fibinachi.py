import sys

def fib(n):
    a,b = 0,1
    for x in xrange(n):
        a,b = b,a+b
    return a


test_cases = open('sample.txt', 'r')
for test in test_cases:
    # ignore test if it is an empty line
    # 'test' represents the test case, do something with it
    # ...
    # ...
    print fib(int(test))
    
test_cases.close()