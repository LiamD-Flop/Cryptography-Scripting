import array
import struct
from time import time
import operator
import random

def left_half(x):
    return ((x >> 32) & 0xFFFFFFFF)

def right_half(x):
    return (x & 0xFFFFFFFF)

def sep_byte(x, i):
    return ((x >> (8 * i)) & 0xFF)

def combine_bytes(b3, b2, b1, b0):
    return (((b3 << 24) | (b2 << 16) | (b1 << 8) | (b0)) & 0xFFFFFFFF)

def combine_halves(x, y):
    return (((x << 32) | (y & 0xFFFFFFFF)) & 0xFFFFFFFFFFFFFFFF)

# FEAL-4 Rotation
def rot(x):
    return ((x<<4) | (x>>4)) & 0xff

# FEAL-4 G-Box
def g_box(a, b, mode):
    return rot((a + b + mode) & 0xff)

# FEAL-4 round function ('f-box')
def f_box(x):
    x0 = sep_byte(x, 0)
    x1 = sep_byte(x, 1)
    x2 = sep_byte(x, 2)
    x3 = sep_byte(x, 3)

    t0 = (x2 ^ x3)
    y1 = g_box(x0 ^ x1, t0, 1)
    y0 = g_box(x0, y1, 0)
    y2 = g_box(y1, t0, 0)
    y3 = g_box(y2, x3, 1)
    return combine_bytes(y3, y2, y1, y0)


ifdiff = 0x80800000
#ifdiff = 0x02000000
ofdiff1 = None
OK = True
for i in range(0,256):
    arg = random.randint(1, 256**4-1)
    res1 = f_box(arg)
    arg = operator.xor(arg,ifdiff)
    res2 = f_box(arg)
    ofdiff2 = operator.xor(res1,res2)
    if (ofdiff1 != None) and (ofdiff1 != ofdiff2):
        OK = False
        break
    else:
        ofdiff1 = ofdiff2
if OK:
    print ("OK F", hex(ifdiff))
else:
    print ("not OK F", hex(ifdiff))
    
        


