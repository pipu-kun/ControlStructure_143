num = int(input("Masukkan nilai: "))

x = 0
y = 1

for i in range(num):
    print(x)
    z = x + y
    x = y
    y = z