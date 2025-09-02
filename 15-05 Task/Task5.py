# Manually calculate the Method Resolution Order (MRO) for:

class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass

# D=D+merge(B,C,BC)
# D=D+merge(BA,CA,BC)
# D=DB+merge(A,CA,C)
# D=DBC+merge(A,A)
# D=DBCA

# B=B+merge(A,A)
# B=BA

# C=C+merge(A,A)
# C=CA