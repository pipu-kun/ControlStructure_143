n = int(input("Masukkan nilai: "))


for i in range(n):
    if i % 2 == 0:
        print(f"{i} adalah bilangan genap")
    else:
        print(f"{i} adalah bilangan ganjil")