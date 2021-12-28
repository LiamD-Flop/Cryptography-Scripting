import old.permute as permute
import ast
from operator import xor
from modules.calculate import Calculate

class BlockCipher(Calculate):
  def __init__(self) -> None:
    super().__init__()
    self.requirements = ["sbox", "key", "permutation sequence"]

  def calculate(self, args):
    super().calculate(args)
    
    sbox = int(args["sbox"],16)
    key = int(args["key"],16)
    permutation = ast.literal_eval(args["permutation sequence"])

    per = permute.permute(sbox, permutation)
    cipher = hex(xor(per, key))

    result = {
        "cipher": cipher
    }

    return result