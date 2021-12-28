from operator import xor
from modules.calculate import Calculate
import old.permute as permute
import ast

def byte(number, i):
    return (number & (0xff << (i * 8))) >> (i * 8)

class Permute(Calculate):
  def __init__(self) -> None:
    super().__init__()
    self.requirements = ["s", "permutation"]

  def calculate(self, args):
    super().calculate(args)
    # example: b = 0x1234567890, s = [3,2,4,1,0]
    # this produces result = 0x5612347890
    # Position 0 is the rightmost position, position 1 is the position at the left, etc
    # So, the first byte (0x12) should come at position 3 which is the leftmost position but one
    # The second byte (0x34) should come at position 2, which is in the middle
    # The third byte (0x56) should come at positon 4 which is at the leftmost position
    # The fourth byte (0x78) should come at position 1, which is the rightmost position but one
    # The fifth byte (0x90) should come at position 0, which is the rightmost position

    b = int(args["s"], 16)
    permutation = ast.literal_eval(args["permutation"])

    if int((len(hex(b).rstrip("L")) - 1)/2) > len(permutation):
        raise ValueError('byte length %s too big for sequence with length %s' %((len(hex(b)) - 1)/2, len(permutation)))
    else:
        result = 0
        index = 0
        s = list(permutation)
        s.reverse()
        for l in s:
            result = result + pow(2,l*8)*byte(b,index)
            index = index + 1
        return hex(result)

