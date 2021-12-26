import numpy as np
from numpy.polynomial import polynomial as p

def polymul(A,B,P,q=2):
    return np.floor(p.polydiv(p.polymul(A,B),P)[1]%q)

def polyadd(A,B,q=2):
    return np.floor(p.polyadd(A,B)%q)

def polysub(A,B,q=2):
    return p.polysub(A,B)%q

def polydiv(A,B,P,q=2):
    return np.floor((p.polydiv(A,B),P)[1]%q)

def togf(A,q=2):
    res = 0
    pow = 1
    for i in A:
        res += pow*i
        pow = pow*q
    return np.floor(res)
    
def topoly(nr,q=2):
    pow = 1
    result = []
    ind = 0
    while nr > 0:
        rem = nr%q
        nr = (nr - rem)//q
        result.append(rem)
    return np.floor(result)

def gfmul(a,b,p,q=2):
    A = topoly(a,q)
    B = topoly(b,q)
    P = topoly(p,q)
    res_poly = polymul(A,B,P,q)
    res_gf = togf(res_poly,q)
    return int(res_gf)

def gfadd(a,b,q=2):
    A = topoly(a)
    B = topoly(b)
    res_poly = polyadd(A,B,q)
    res_gf = togf(res_poly,q)
    return int(res_gf)
