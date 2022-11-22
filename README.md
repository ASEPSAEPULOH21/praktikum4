# praktikum4
lab2
latihan1
membuat program sederhana dengan menginput 2 buah bilangan untuk menentukan bilngan terbesar menggunakan statement if 
source code & ouput (hasil running program) berikut adalah source code latihan 1 :
a = int(input("bilangan a : "))
b = int(input("bilangan b : "))

if a > b:
    print(f"terbesar adalah {a}")
elif b > a :
    print(f"terbesar adalah {b}")
    ![image1.png](Shreenshot/Screenshot%20(34).png)

latihan2
membuat program untuk menurutkan data berdasarkan input sejumlah data (minimal 3 variable input atau lebih), kemudian menampilkan hasil dengan urut dari data kecil
source code & ouput (hasil running program) berikut adalah source code latihan 2 :
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
! [image.png](Shreenshot/Screenshot%20(35).png)

lab3
latihan1
program membuat dengan perulangan bertingkat (nested) kode sumber & keluaran (program menjalankan hasil)
start = 0;
stop = 10;
for i in range(10):
    for j in range(start,stop):
        print(j, sep=" ", end=" ")
        if j < 10 :
            print('{0:>2}'.format(""), end="")
        else :
             print('{0:>1}'.format(""), end="")
    start+=1
    stop+=1
    print("")
! [image.png](Shreenshot/Screenshot%20(36).png
latihan2
menampilkan n bilangan acak yang lebih kecil dari 0.5 dan nilai n diisi pada saat runtime menggunakan kombinasi while dan for 
program membuat dengan perulangan bertingkat (nested) kode sumber & keluaran (program menjalankan hasil)
import random
jumlah = int(input("Masukan Jumlah Nilai :"))
for i in range(jumlah):
    i=random.uniform(0.0,0.5)
    print("Data Ke:", i)
    print("SELESAI")
! [image.png](Shreenshot/Screenshot%20(37).png