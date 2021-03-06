# n! = n*(n-1)!   5! = 5*4*3*2*1

def fact_rec(n):
    if n==0 or n==1:
        return 1
    return n * fact_rec(n-1)

def fact_iter(n):
    fact = 1
    for i in range(2,n+1):
        fact*=i
    return fact

if __name__ == '__main__':
    print(fact_iter(5))