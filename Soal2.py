x = int(input("Masukkan nilai x: "))
y = int(input("Masukkan nilai y: "))
z = int(input("Masukkan nilai z: "))

if x > y and x > z:
    print(f"{x} Adalah nilai terbesar")
elif y > x and y > z:
     print(f"{y} Adalah nilai terbesar")
else:
    print(f"{z} Adalah nilai terbesar")1