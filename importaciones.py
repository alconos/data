import math
import random
#print(math.pi)
#print(math.sin(math.pi/2))

random.seed(42)
n1 = 0
n2 = 0
n3 = 0
n4 = 0
n5 = 0
n6 = 0
m1 = 0
m2 = 0
m3 = 0
m4 = 0
m5 = 0
m6 = 0
for i in range(1, 50):
    n = random.randint(1, 6)
    m = random.randint(1, 6)
    print(n, m)
    if n == 1:
        n1 += 1
    elif n == 2:
        n2 += 1
    elif n == 3:
        n3 += 1
    elif n == 4:
        n4 += 1
    elif n == 5:
        n5 += 1
    elif n == 6:
        n6 += 1

    if m == 1:
        m1 += 1
    elif m == 2:
        m2 += 1
    elif m == 3:
        m3 += 1
    elif m == 4:
        m4 += 1
    elif m == 5:
        m5 += 1
    elif m == 6:
        m6 += 1
print(n1, n2, n3, n4, n5, n6)
print(m1, m2, m3, m4, m5, m6)






