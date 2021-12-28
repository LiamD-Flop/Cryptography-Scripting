from modules.calculate import Calculate

class ExtendedEuclidean(Calculate):
  def __init__(self) -> None:
    super().__init__()
    self.requirements = ["b", "n"]

  def calculate(self, args):
    # We calculate gcd(b,n)
    # At each iteration we perform the following steps:
    # the new value of b is the old value of n
    # the new value of n is the remainder of b/n
    # we call the quotient q = b/n
    #
    # For the extended euclidean algorithm, we also
    # calculate these formula's:
    # x(i) = x(i-2) - q(i) * x(i-1)
    # y(i) = y(i-2) - q(i) * y(i-1)
    #
    # x0 is x(i-2), y0 is y(i-2)
    # x1 is x(i-1), y1 is y(i-1)
    # q is q(i)
    #
    # the final values of x0, y0 are the resulting x, 
    super().calculate(args)

    b = int(args["b"])
    n = int(args["n"])

    x0, x1, y0, y1 = 1, 0, 0, 1
    while n != 0:
        q, b, n = b // n, n, b % n
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
        #print q, b, n, x1, y1
    return  b, x0, y0

class GreatestCommonDevider(Calculate):
  def __init__(self) -> None:
    super().__init__()
    self.requirements = ["b", "n"]

  def calculate(self, args):
    super().calculate(args)

    g, x, y = ExtendedEuclidean().calculate(args)
    return g

class MultiplicativeInverse(Calculate):
  def __init__(self) -> None:
    super().__init__()
    self.requirements = ["b", "n"]

  def calculate(self, args):
    # the extended euclidean algorithm also
    # calculates x, y such that gcd(b,n) = b*x + n*y
    #
    # if we calculate in modulo n
    # gcd (b,n) = b*x + n*y = b*x
    # and we know b and n are relatively prime,
    # so gcd(b,n) = 1 = b*x
    # so x = multiplicative inverse of b modulo n
    #
    super().calculate(args)

    n = int(args["n"])

    g, x, y = ExtendedEuclidean().calculate(args)
    if g == 1:
      return x % n
    else:
      raise ValueError('multiplicative inverse is not possible if values are not relatively prime ')
    