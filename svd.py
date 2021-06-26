from PIL import Image
import imageio
import numpy as np
import os

def svd(path, k):
    #Check input
    try:
        img = imageio.imread("in/" + path)
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
    
    dirout = "out/" + path
    im.save(dirout)

    sizeawal = os.path.getsize("in/"+path)
    sizeakhir = os.path.getsize(dirout)
    print("Persentase ukuran memori gambar yang dikompresi terhadap gambar original: " + "{:.3f}".format(sizeakhir/sizeawal*100) + "%")
    return "Berhasil Compress"