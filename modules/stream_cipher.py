from operator import xor
from modules.calculate import Calculate
import random

class StreamCipher(Calculate):
  def __init__(self) -> None:
    super().__init__()
    self.requirements = ["input"]

  def calculate(self, args):
    super().calculate(args)
    random.seed(1000)
    stream = hex(random.getrandbits(1000))
    plain = int(args["input"], 16)
    parts = int(stream[:len(hex(plain))], 16)
    cipher = xor(plain, parts)

    result = {
      "stream": stream,
      "plain": hex(plain),
      "parts": hex(parts),
      "cipher": hex(cipher),
      "plain length": len(hex(plain)),
    }

    return result

    