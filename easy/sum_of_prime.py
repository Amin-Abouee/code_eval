import sys
def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False

    return True

sum = 0
cnt = 0
for x in xrange(2,1000000):
	if isPrime(x):
		cnt += 1
		sum += x
		if cnt == 1000:
			break

print sum

