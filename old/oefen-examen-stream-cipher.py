import binascii
from operator import xor
import random

seed = int(input("Enter the seed: "))
bits = int(input("Enter amount of bits: "))
random.seed(seed)
stream = random.getrandbits(bits)
stream = hex(stream)
print("Stream:", stream)
what_to_do = str(input("encryptie of decryptie [e/d]? "))

def encryptie():
    string = str(input("Enter your message here: "))
    s_number = 0
    for c in string:
        ascii_code = ord(c)
        s_number = s_number*256 + ascii_code
    #print(s_number)
    s_number = hex(s_number)
    #print(s_number)
    lengte_string = len(s_number[2:])
    stream_to_xor = stream[:lengte_string+2]
    print("Lengte message in hex:", lengte_string)
    print("Message in hex:", s_number)
    print("Stream in hex met juiste lengte:", stream_to_xor)
    s_number = int(s_number[2:], 16)
    stream_to_xor = int(stream_to_xor[2:], 16)
    encrypted = xor(s_number, stream_to_xor)
    print("Encryptie in hex:", hex(encrypted))

def decryptie():
    encrypted = int(input("Enter encrypted message: "), 16)
    encrypted = hex(encrypted)
    print("Encrypted message:", encrypted)
    lengte_string = len(encrypted[2:])
    stream_to_xor = stream[:lengte_string+2]
    encrypted = int(encrypted[2:], 16)
    stream_to_xor = int(stream_to_xor[2:], 16)
    decrypted = xor(encrypted, stream_to_xor)
    print("Decrypted message:", hex(decrypted))

if what_to_do == "e":
    encryptie()
elif what_to_do == "d":
    decryptie()





