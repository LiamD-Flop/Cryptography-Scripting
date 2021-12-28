from operator import xor
from modules.calculate import Calculate

class AESBlockCipher(Calculate):
  def __init__(self) -> None:
    super().__init__()
    self.requirements = ["c", "d", "p"]

  def calculate(self, args):
    super().calculate(args)
    
    c = int(args["c"], 16)
    d = int(args["d"], 16)
    p = int(args["p"], 16)

    nonce = hex(xor(xor(d, c), p))
    result = {
      "nonce": nonce,
    }

    return result