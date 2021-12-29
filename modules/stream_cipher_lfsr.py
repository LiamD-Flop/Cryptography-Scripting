from operator import xor
from modules.calculate import Calculate
import old.permute

class StreamCipherLFSR(Calculate):
  def __init__(self) -> None:
    super().__init__()
    self.requirements = ["input", "stream", "mask"]

  def calculate(self, args):
    super().calculate(args)
    
    stream = int(args["stream"], 16)
    mask  = int(args["mask"], 16)
    result = old.permute.lfsr(stream, mask, 256)
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
      

    