a, b, c = (
    int(input("Masukan nilai ke-1: ")),
    int(input("Masukan nilai ke-2: ")),
    int(input("Masukan nilai ke-3: "))
)
if a < b and a < c:
    if b < c:
        print("Urutan Bilangan : ", a, b, c)
    else:
        print("Urutan Bilangan : ", a, b, c)
elif b < a and b < c:
    if a < c:
        print("Urutan Bilangan : ", b, a, c)
    else:
        print("Urutan Bilangan : ", b, c, a)
else:
    if a < b:
        print("Urutan Bilangan : ", c, a, b)
    else:
        print("Urutan Bilangan : ", c, a, b)
