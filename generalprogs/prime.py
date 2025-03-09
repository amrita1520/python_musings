n=1
def is_prime(n):
    is_prime=True
    for i in range(2,n):
        if n%i==0:
            is_prime=False
            break
    if n==1 or n==0:
        is_prime=False
    return is_prime
for i in range(1,101):
    if is_prime(i):
        print(i)   