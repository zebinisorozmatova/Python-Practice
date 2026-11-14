A = int(input("Uch xonali son kiriting: "))
a = A // 100
b = (A // 10) % 10
c = A % 10
print((a < b and b < c) or (a > b and b > c))
