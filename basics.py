import sys,math

def isPrime(n) :
    if n==2 or n==3 : return True
    for i in range(2,int(math.sqrt(n)+1)) :
        if n%i==0 :
            return False
    return True

n = int(input())
if isPrime(n) :
    print('no', end = '')
else :
    print('yes', end='')
