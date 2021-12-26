import modules.euclidean as Euclidean
import modules.block_cipher as BlockCipher
import os

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

possibilities = {
  "Multiplicative Inverse": Euclidean.MultiplicativeInverse(),
  "Extended Euclidean": Euclidean.ExtendedEuclidean(),
  "Greatest Common Devider": Euclidean.GreatestCommonDevider(),
  "Block Cipher (AES)": BlockCipher.AESBlockCipher(),
}

possible_modules = []
arguments = {}

def UnknownModule():
  input_str = "Give an argument (example: n=1) "

  i = input(input_str)

  while i != "":
    i = i.split("=")

    i[0] = i[0].strip()
    i[1] = i[1].strip()

    arguments[i[0]] = i[1]

    i = input(input_str)

  i = 0
  print("\nSelect the number of the module you want to run")
  for k, module in possibilities.items():
    possible = module.hasRequirements(arguments)
    if (possible):
      print(i, k)
      possible_modules.append(module)
      i += 1

def ChooseModule():
  i = 0
  for k, module in possibilities.items():
    print(i, k)
    possible_modules.append(module)
    i += 1

def init():
  arguments = {}
  clearConsole()
  todo = input("What do you want to do:\n1: Select a module\n2: Derrive a module from arguments\nSelect: ")
  clearConsole()
  if todo == "1":
    print("Select a module:")
    ChooseModule()
  else:
    print("")
    UnknownModule()

  module_to_run = input("Module: ")

  print("\n", possible_modules[int(module_to_run)].calculate(arguments))
  
  if input("Continue? (Y/n)").lower() == "n":
    print("Goodbye...")
    exit()
  else:
    init()

init()
