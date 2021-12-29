from operator import xor
from modules.calculate import Calculate

class StreamCipherLFSR(Calculate):
  def __init__(self) -> None:
    super().__init__()
    self.requirements = ["input", "stream", "mask"]

  def calculate(self, args):
    super().calculate(args)

    stream = int(args["stream"], 16)
    mask  = int(args["mask"], 2)

    nbits = mask.bit_length()
    result = stream
    seed = stream
    all_ones = pow(2,nbits) - 1
    length_so_far = nbits
    while length_so_far < 256:
        newbit = bin(mask&seed).count('1')%2
        seed = (seed<<1 & all_ones) + newbit
        result = (result<<1) + newbit
        length_so_far += 1

    plain = int(args["input"], 16)
    cipher = xor(plain, result)

    result = {
      "stream": hex(stream),
      "mask": hex(mask),
      "plain": hex(plain),
      "lfsr": hex(result),
      "cipher": hex(cipher),
      "plain length": len(hex(plain)),
    }

    return result
      

    