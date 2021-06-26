from PIL import Image
import imageio
import numpy as np

# Pohon node
class NodeTree(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)

#cari kode dari pohon huffman
def huffmanTree(node, kode):
    #basis, kalau udh sampe ujung return dict kunci : kode binary
    if type(node) is np.uint8:
        return {node: kode}
    #rekursi
    (l, r) = node.children()
    d = dict()
    d.update(huffmanTree(l, kode + '0'))
    d.update(huffmanTree(r, kode + '1'))
    return d

def huffman(path):
    img = imageio.imread("in/" + path)

    #RGB
    red = img[:,:,0]
    green = img[:,:,1]
    blue = img[:,:,2]
    rgb = [red,green,blue]
    res=  []
    freq = {}
    for i in rgb:
        # Hitung frekuensi
        for col in i:
            for c in col:
                if c in freq:
                    freq[c] += 1
                else:
                    freq[c] = 1

    #Sort
    freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    nodes = freq

    while len(nodes) > 1:
        #ambil kedua terkecil
        (key1, count1) = nodes[-1]
        (key2, count2) = nodes[-2]
        #sisa kecuali dua terkecil
        nodes = nodes[:-2]
        #buat node baru di tree
        node = NodeTree(key1, key2)
        #masukin lagi hasil jumlahnya kedua terkecil
        nodes.append((node, count1 + count2))
        #Sort lagi
        nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

    huffmanCode = huffmanTree(nodes[0][0], "")
    bitmap = ""
    for i in img:
        for j in i:
            for k in j:
                bitmap += huffmanCode[k]

    idx = path.index(".")
    nama = path[:idx]
    nama += "huffman.txt"
    f = open("out/" + nama, "w")
    f.write(bitmap)
    f.close()

    print('Kode Huffman:')
    for key in sorted(huffmanCode):
        print(key, end=" | ")
        print(huffmanCode[key])

    height = img.shape[0]
    width = img.shape[1]

    bitin = height * width * 8 * 3 #Jumlah bit per pixel = 8x3 (RGB), dikali banyaknya pixel
    bitout = len(bitmap)
    print("Perbedaan jumlah bit awal dan akhir: " + str(bitout/bitin*100) + "%")
    return "Berhasil Compress"