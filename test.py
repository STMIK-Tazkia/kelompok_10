#tugas uts Bagian 1 soal No 1
import numpy as np

# Matriks A dan B diberikan
A = np.array([
    [10, 23, 21, 11],
    [55, 5, 7, 88],
    [34, 22, 21, 32],
    [10, 14, 11, 15]
])

B = np.array([
    [1, 0, 8, 1],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [1, 8, 0, 1]
])

# Perkalian matriks A x B
C = np.dot(A, B)

# Menampilkan hasil
print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

print("\nHasil A x B:")
print(C)

#tugas uts Bagian Dua Soal No 1
def irisan_himpunan(himpunan_a, himpunan_b):
    # Konversi ke set untuk menghapus duplikasi
    set_a = set(himpunan_a)
    set_b = set(himpunan_b)
    
    # Cari irisan
    irisan = set_a.intersection(set_b)
    
    return irisan

# Data himpunan
A = {3, 4, 5, 17, 2, 3, 5, 14, 3, 19}
B = {4, 2, 5, 17, 2, 3, 6, 15, 6, 4, 20}

# Panggil fungsi
hasil_irisan = irisan_himpunan(A, B)
print("Irisan dari A dan B adalah:", hasil_irisan)


# tugas uts Bagian 3 Soal no 1:Mengurutkan Himpunan A dengan algoritma bubble sort
def Mengurutkan(tugas):
    n = len(tugas)
    for i in range(n):
        for j in range(0, n-i-1):
            if tugas[j] > tugas[j+1]:
                tugas[j], tugas[j+1] = tugas[j+1], tugas[j]  
    return tugas

#tugas uts Bagian 3 Soal no 2:Mencari Nilai x(300) dalam Himpunan A
def mencari(tugas, x):
    for i in range(len(tugas)):
        if tugas[i] == x:
            return i  
   
# Himpunan A
A = [109, 222, 120, 150, 200, 321, 410, 120, 230, 300, 111, 89, 70, 45, 57, 31, 39, 900, 21, 378, 400, 101, 201, 301, 1]
mengurutkanA = Mengurutkan(A.copy())  
print("Himpunan A yang sudah diurutkan:", mengurutkanA)

# Mencari Nilai x (300)
x = 300
urutan = mencari(A, x)
if urutan:
    print(f"Selamat Nilai {x} akhirnya telah ditemukan pada urutan ke-{urutan + 1}.")
else:
    print(f"Nilai {x} sayangnya tidak ditemukan dalam himpunan A.")
