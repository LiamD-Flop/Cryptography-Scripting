import modules.euclidean as Euclidean
from modules.calculate import Calculate

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

class Encrypt(Calculate):
  def __init__(self) -> None:
    super().__init__()
    self.requirements = ["p", "q", "e", "plain"]

  def calculate(self, args):
    super().calculate(args)
    n = int(args["p"]) * int(args["q"])
    totient_n = (int(args["p"]) - 1) * (int(args["q"]) - 1)
    if Euclidean.GreatestCommonDevider().calculate({"b": int(args["e"]), "n": totient_n}):
        d = Euclidean.MultiplicativeInverse().calculate({"b": int(args["e"]), "n": totient_n})
        C = pow(int(args["plain"]), int(args["e"]), n)
        M = pow(C, d, n)
        if int(args["plain"]) == M:
            print("This is a valid RSA key.")
            return {
              "Private Key": d,
              "n": n,
              "Totient of n": totient_n,
              "Plain text": int(args["plain"]),
              "Cipher text": C,
              "Decrypted text": M,
            }
        else:
            print("This is not a valid RSA key. The cipher text cannot be decrypted to its original form.")
    else:
        print("(n,e) is not a valid RSA key.")

class Decrypt(Calculate):
  def __init__(self) -> None:
    super().__init__()
    self.requirements = ["p", "q", "e", "cipher", "n"]

  def calculate(self, args):
    super().calculate(args)
    if (args["n"] == ""):
      p = int(args["p"])
      q = int(args["q"])
      n = p * q
    else:
      p, q = prime_factors(int(args["n"]))
      n = int(args["n"])
    totient = (p - 1) * (q - 1)
    d = Euclidean.MultiplicativeInverse().calculate({"b": int(args["e"]), "n": totient})
    M = pow(int(args["cipher"]), d, n)
    print("The decrypted message is:", M)
    return {
      "First prime (p)": p,
      "Second prime (q)": q,
      "n": n,
      "Totient": totient,
      "Private key": d,
      "Decrypted message": M,
    }

