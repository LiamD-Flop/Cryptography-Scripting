import binascii
from operator import xor

key_string = input("Please input your key: ")
key_string = bytes(key_string, encoding='utf-8')
key = binascii.hexlify(key_string)
encrypted_password = str(input("Please enter the encrypted message: "))
if " " in encrypted_password:
    encrypted_password = encrypted_password.split(" ")[1]
offset = str(input("Is there an offset [y/n] (in a Cisco password there is an offset): "))
if offset == "y":
    offset, encrypted_password = encrypted_password[:2], encrypted_password[2:]
    offset = int(offset, 16)
    key = key[offset * 2:]
length_to_decrypt = len(encrypted_password)
encrypted_password = int(encrypted_password, 16)
key_part = int(key[:length_to_decrypt], 16)
decrypted_password = xor(key_part, encrypted_password)
decrypted_password_hex = hex(decrypted_password)
password = binascii.unhexlify(decrypted_password_hex[2:])

print()
print("--------------------------------------------")
print("Key string:", key_string)
print("Key (offset deleted if present):", key)
print("Key part used to decrypt:", key_part)
print("--------------------------------------------")
if offset != "n":
    print("Offset:", offset)
    print("--------------------------------------------")
print("Encrypted message:", encrypted_password)
print("Decrypted message in hex:", decrypted_password_hex)
print("Message:", password)
print("--------------------------------------------")
