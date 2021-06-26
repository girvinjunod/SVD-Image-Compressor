from PIL import Image
import imageio
import numpy as np
import time
import os

def svd(path, k):
    #Check input
    try:
        img = imageio.imread(path)
    except:
        return "File tidak ditemukan"

    #print(img.shape)
    #img dimensions
    height = img.shape[0]
    width = img.shape[1]

    #RGB
    red = img[:,:,0]
    green = img[:,:,1]
    blue = img[:,:,2]
    rgb = [red,green,blue]

    res = []
    #SVD for each color
    for i in rgb:
        # Calulating the SVD, nanti diganti pakai algo sendiri
        U, s, VT = np.linalg.svd(i)


        #print(f'u.shape:{U.shape},s.shape:{s.shape},v.shape:{VT.shape}')
        Sigma = np.zeros((height, width))

        # fill Sigma with diagonal s
        
        if (height < width):
            Sigma[:height, : height] = np.diag(s)
        else:
            Sigma[:width, : width] = np.diag(s)
        
        Sigma = Sigma[:, :k]
        VT = VT[:k, :]

        # reconstruct
        B = U.dot(Sigma.dot(VT))

        res.append(B)

    #Reconstruct RGB
    r1 = res[0]
    g1 = res[1]
    b1 = res[2]
    hasil = []
    for i in range(len(r1)):
        temp = []
        for j in range(len(r1[i])):
            temprgb = []
            temprgb.append(r1[i][j])
            temprgb.append(g1[i][j])
            temprgb.append(b1[i][j])
            temp.append(temprgb)
        hasil.append(temp)
    hasil = np.array(hasil)

    #Save
    hasil = hasil/255
    hasil = np.clip(hasil,0,1)
    im = Image.fromarray(np.uint8(hasil*255))
    #im.show()
    
    dirout = "out/" + namaimg
    im.save(dirout)

    sizeawal = os.path.getsize(path)
    sizeakhir = os.path.getsize(dirout)
    print("Persentase ukuran memori gambar yang dikompresi terhadap gambar original: " + "{:.3f}".format(sizeakhir/sizeawal*100) + "%")
    return "Berhasil Compress"

def huffman(path):
    return "Berhasil Compress"


#main
#Read image
dirin = "in/"
namaimg = input("Masukkan path file gambar(in/): ")
path = dirin+namaimg
print("Pilih algoritma:")
print("1. SVD")
print("2. Huffman")

try:
    alg = int(input("Input(1/2): "))
    if alg == 1:
        valid = False
        try:
            k = int(input("Masukkan tingkat kompresi-> \nPilih jumlah singular values: "))
            valid = True
        except:
            print("Error Input")
        if valid:
            start = time.time()
            print(svd(path, k))
            end = time.time()
            print("Runtime program: " + "{:.3f}".format(end - start) + " detik")
    elif alg == 2:
        start = time.time()
        print(huffman(path))
        end = time.time()
        print("Runtime program: " + "{:.3f}".format(end - start) + " detik")
    else:
        print("Error Input")
except:
    print("Error Input")










    
    





