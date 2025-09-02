# formula of calculating MRO=class +merge(parent class_1,class_2...class_n,[list of parent class])
class A:
    def greet(self):
        print("Hello from A")

class B(A):
    def greet(self):
        print("Hello from B")

class C(A):
    def greet(self):
        print("Hello from C")

class D(B, C):
    def greet(self):
        print("Hello from D")

class E(C,B):
    def greet(self):
        print("Hello from E")

class F(D, E):
    def greet(self):
        print("Hello from F")
        
print(F.mro())
#F=F+merge(D,E,DE)
#F=F+merge(DBCA,ECBA,DE)
#F=FD+merge(BCA,ECBA,E)
#F=FDE+merge(BCA,CBA)
#F=FDEC+merge(BA,BA)
#F=FDECBA

#D=D+merge(B,C,BC)
#D=D+merge(BA,CA,BC)
#D=DB+merge(A,CA,C)
#D=DBC=merge(A,A)
#D=DBCA

#E=E+merge(C,B,CB)
#E=E+merge(CA,BA,CB)
#E=EC+merge(A,BA,B)
#E=ECB+merge(A,A)
#E=ECBA

#B=B+merge(A,A)
#B=BA

#C=C+merge(A,A)
#C=CA