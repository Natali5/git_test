import math

y = input("Enter Y: ")
x = input("Enter X: ")

part1 = math.sqrt((2 + y) ** 2 + math.sqrt(math.sin(y + 5)))
part2 = math.log10(x + 1) - y ** 3

print(part1 / part2)

**************2********
import math

variables = input("Enter x,y,z,a,b,c,d: ")
x, y, z, a, b, c, d = variables

while (a > b and c > d):
    variables = input("a >= b and c >= d; Enter x,y,z,a,b,c,d: ")
    x, y, z, a, b, c, d = variables


if x in [q for q in range(c, d)] and\
    y in [q for q in range(c, d)] and\
    z in [q for q in range(c, d)]:
        V = max(x, y, z)
elif not(x in [q for q in range(c, d)] and
    y in [q for q in range(c, d)] and
    z in [q for q in range(c, d)]):
        V = math.sqrt(x ** 2 + y ** 2)
else:
    V = min(x ** 2, y ** 2, z ** 2)

print "Result: ", V

*********3*****
import math

variables = input("Enter x, a, eps: ")
x, a, eps = variables

k = 0
fk, lnax, stk = 1, 1, 1
d = math.sin(2) / 3
s = d
while (math.fabs(d) > eps):
    k += 1
    fk += k
    lnax *= (a + x) ** 2
    d = math.log(lnax, 10) / (stk + fk)
    s += d

print ("Result: ", s)
print ("Count: ", k)
******4*******
variables = input("Enter A(n x m): ")
n, m = variables

while n > 100 or m > 10:
    variables = input("Enter A(n x m): ")
    n, m = variables

print "Make random numbers in A from {} to {}".format(n, m)

A = [number for number in range(n * m)]
Z = max(min(A[0:m]), min(A[m + 1:2 * m]), min(A[n - 1: n * m]))

print "Result is {}".format(Z)
********5*******
sentence = "Hello, there, how are you doing? TheLongWordinthesentense :) TheLongWordinthesentense"

prepared_sentense = ""
for char in sentence:
    prepared_sentense += char if char.isalpha() else " "

sentence = sentence.replace(max(prepared_sentense.split(), key=len), "")
print "Max word is: {} ".format(max(prepared_sentense.split(), key=len))
print "New text: {} ".format(sentence)
