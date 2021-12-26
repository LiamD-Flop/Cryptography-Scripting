import euclidean
import primes
import math



def rsa_example():
    print("Calculating primes... This may take a while...")
    p = primes.findAPrime(pow(2, 2047), pow(2, 2048))
    print("Found p:", p)
    q = primes.findAPrime(pow(2, 2047), pow(2, 2048))
    print("Found q:", q)
    print("Found primes.")
    solve_rsa(p=p, q=q, e=65537, P=123456789123456789)


def solve_rsa(p, q, e, P):
    n = p * q
    print("n =", n)
    totient_n = (p - 1) * (q - 1)
    print("Totient of n:", totient_n)
    if validate_rsa(totient_n, e):
        d = euclidean.mulinv(e, totient_n)
        print("Private key:", d)
        print("Plain text:", P)
        C = pow(P, e, n)
        print("Cipher text:", C)
        M = pow(C, d, n)
        print("Decrypted text:", M)
        if P == M:
            print("This is a valid RSA key.")
        else:
            print("This is not a valid RSA key. The cipher text cannot be decrypted to its original form.")
    else:
        print("(n,e) is not a valid RSA key.")
    exit(0)


def decrypt_rsa(C, e, n):
    print("Prime factorisation...")
    p, q = prime_factors(n)
    print("Primes found!", n, "=", p, "*", q)
    totient = (p - 1) * (q - 1)
    print("Totient:", totient)
    d = euclidean.mulinv(e, totient)
    print("Private key:", d)
    M = pow(C, d, n)
    print("The decrypted message is:", M)


def calculate_private_key(e, n):
    print("Prime factorisation...")
    p, q = prime_factors(n)
    print("Primes found!", n, "=", p, "*", q)
    totient_n = (p - 1) * (q - 1)
    print("Totient:", totient_n)
    if euclidean.gcd(e, totient_n) == 1:
        d = euclidean.mulinv(e, totient_n)
        print("Private key:", d)
    else:
        print("The totient and public key are not relatively prime.")
        exit(1)


def get_totient_primes(N):
    p = math.floor(math.sqrt(N))
    while N % p != 0:
        p -= 2
    q = int(N / p)
    print("The prime numbers are", p, "and", q)


def prime_factors(n):
    print("If it crashes here, your number was not the product of two prime factors.")
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def validate_rsa(totient_n, e):
    return euclidean.gcd(totient_n, e) == 1


inp = int(input("Do you want to encrypt your own values(0), decrypt a cipher text(1), calculate a private key(2), "
                "or crack key totient with same modulus(3)? [0/1/2/3] "))
if inp == 0:
    p = int(input("Please input prime number p: "))
    q = int(input("Please input prime number q: "))
    e = int(input("Please input public key e: "))
    P = int(input("Please input your plaintext message: "))
    solve_rsa(p, q, e, P)
elif inp == 1:
    C = int(input("Please input cipher text C: "))
    e = int(input("Please input public key e: "))
    n = int(input("Please input modulus n: "))
    decrypt_rsa(C, e, n)
elif inp == 2:
    e = int(input("Please input public key e: "))
    n = int(input("Please input modulus n: "))
    calculate_private_key(e, n)
elif inp == 3:
    N = int(input("Please input modulus n: "))
    get_totient_primes(N)
else:
    rsa_example()
