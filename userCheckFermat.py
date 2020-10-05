
# This code requests input from the user to check if Fermat's Last Theorem is true.
# Fermat's Last Theorem says that there are no positive
# integers a, b, c such that an + bn == cn.

def check_fermat(a, b, c, n):
                 if an + bn == cn:
                     print(false)
                 else:
                     print(true)

value1 = input('Enter a value for a:\n')
#print(value1)      testing code
a = int(value1)

value2 = input('Enter a value for b:\n')
#print(value2)      testing code
b = int(value2)

value3 = input('Enter a value for c:\n')
#print(value3)      testing code
c = int(value3)

value4 = input('Enter a value for n:\n')
#print(value4)      testing code
n = int(value4)

an = (a ** n)
bn = (b ** n)
cn = (c ** n)

false = "Holy smokes, Fermat was wrong!"
true = "No, that doesn't work."

print(check_fermat(a, b, c, n))
