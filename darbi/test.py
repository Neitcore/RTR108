#Python 2.7 -> print vars()
from math import cos as cos_v1
#print(vars())
a = 10
#print("%s"%(vars()))
print(cos_v1(a))

from cmath import cos as cos_v2
"""
cmath ir biblieoteka kas strada
ar kompleksiem skaitļiem.
"""
print(cos_v2(a))
