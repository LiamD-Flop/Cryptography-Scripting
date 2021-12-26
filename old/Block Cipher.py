from operator import xor

C1 = int(input("What is C1? "), 16)
C2 = int(input("What is C2? "), 16)
D1 = int(input("What is D1? "), 16)
D2 = int(input("What is D2? "), 16)
P1 = int(input("What is P1? "), 16)
P2 = int(input("What is P2? "), 16)

Q1 = xor(xor(D1, C1), P1)
Q2 = xor(xor(D2, C2), P2)

print("Q1 = ", hex(Q1))
print("Q2 = ", hex(Q2))
