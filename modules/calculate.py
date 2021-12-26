class Calculate:
  def __init__(self) -> None:
      pass

  def hasRequirements(self, given):
    if len(given.keys()) == len(self.requirements):
      for k in given.keys():
        if k not in self.requirements:
          return False
      return True
    return False

  def calculate(self, args):
    if len(args.items()) == 0:
      for requirement in self.requirements:
        args[requirement] = input("Give the argument {requirement} = ".format(requirement = requirement))