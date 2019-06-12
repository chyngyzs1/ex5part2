a = int(input('Perviy klass:'))
b = int(input('Vtoroy klass:'))
c = int(input('Tretiy klass:'))
if a % 2 == 1:
    a = (a/2) + 0.5
else:
    a = a/2
if b % 2 == 1:
    b = (b/2) + 0.5
else:
    b = b/2
if c % 2 == 1:
    c = (c/2) + 0.5
else:
    c = c/2
print(a + b + c)