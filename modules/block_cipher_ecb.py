import old.permute as permute
import ast
from operator import xor
from modules.calculate import Calculate

class BlockCipherECB(Calculate):
  def __init__(self) -> None:
    super().__init__()
    self.requirements = ["sbox", "subkey1", "subkey2", "permutation sequence"]

  def calculate(self, args):
    super().calculate(args)
    
    sbox = int(args["sbox"],16)
    subkey1 = int(args["subkey1"],16)
    subkey2 = int(args["subkey2"],16)
    permutation = ast.literal_eval(args["permutation sequence"])
    first = xor(sbox, subkey1)
    per = permute.permute(first, permutation)
    cipher = hex(xor(per, subkey2))

    result = {
        "cipher": cipher
    }

    return result