
# This code checks if Fermat's Last Theorem is true.
# Fermat's Last Theorem says that there are no positive
# integers a, b, c such that an + bn == cn.

def check_fermat(a, b, c, n):
                 if an + bn == cn:
                     print(false)
                 else:
                     print(true)
a = 5
b = 3
c = 4
n = 6

an = (a ** n)
bn = (b ** n)
cn = (c ** n)

false = "Holy smokes, Fermat was wrong!"
true = "No, that doesn't work."

print(check_fermat(a, b, c, n))
