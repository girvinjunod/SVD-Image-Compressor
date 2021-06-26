import time
from svd import *
from huffman import *

#main
namaimg = input("Masukkan path file gambar(in/): ")
print("Pilih algoritma:")
print("1. SVD")
print("2. Huffman")
try:
    alg = int(input("Input(1/2): "))
    if alg == 1:
        valid = False
        try:
            k = int(input("Masukkan tingkat kompresi-> \nPilih jumlah singular values: "))
            if k >=1:
                valid = True
            else:
                print("Jumlah singular value minimal 1")
        except:
            print("Error Input")
        if valid:
            start = time.time()
            print(svd(namaimg, k))
            end = time.time()
            print("Runtime program: " + "{:.3f}".format(end - start) + " detik")
    elif alg == 2:
        start = time.time()
        print(huffman(namaimg))
        end = time.time()
        print("Runtime program: " + "{:.3f}".format(end - start) + " detik")
    else:
        print("Error Input")
except:
    print("Error Input")










    
    





