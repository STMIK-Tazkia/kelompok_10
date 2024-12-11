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