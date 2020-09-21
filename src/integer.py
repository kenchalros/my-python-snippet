from pysnit import snippet

@snippet(description="Calculate gcd.")
def gcd(x,y):
    while y: x,y = y,x%y
    return x

@snippet(description="Calculate lcm (require `gcd`).")
def lcm(x,y):
    return x*y//gcd(x,y)

@snippet(prefix="ed",
         description="Return a tuple list of divisor of n.")
def enumerate_divs(n):
    return [(i,n//i) for i in range(1,int(n**0.5)+1) if n%i==0]

@snippet(prefix="gp",
         description="Return a list of prime numbers n or less.")
def get_primes(n=10**3):
    is_prime = [True]*(n+1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5)+1):
        if not is_prime[i]:
            continue
        for j in range(i*2, n+1, i): is_prime[j] = False
    return [i for i in range(n+1) if is_prime[i]]

@snippet(prefix="pf",
         description="Return a list of prime factorization numbers of n.")
def prime_factor(n):
    res = []
    for i in range(2,int(n**0.5)+1):
        while n%i==0: res.append(i); n //= i
    if n != 1: res.append(n)
    return res

@snippet(prefix="mc",
         description="Calculate n_C_r with mod.")
def mod_cmb(n, r, mod):
    x, y = 1, n
    for i in range(2,r+1):
        x *= i; y *= n-i+1;
        x %= mod; y %= mod
    return y * pow(x, mod-2, mod) % mod

@snippet(prefix="egcd",
         description="Extended Euclidean algorithm.")
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y

def isPrime(n):
    if n == 1: return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0: return False
    return True
