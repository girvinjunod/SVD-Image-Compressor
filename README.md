# Cara Menggunakan Program
1. Jalankan perintah `python main.py` di terminal
2. Masukkan nama gambar yang ingin di-compress. Pastikan gambar sudah ada di dalam folder in. Contoh input: `momo.jpg`
3. Pilih jenis algoritma yang ingin dipakai (input 1 untuk SVD, input 2 untuk Huffman)
4. Untuk algoritma SVD, masukkan jumlah singular value yang ingin dipakai dengan minimal 1.
5. Hasil kompresi dapat dilihat di dalam folder out

# Penjelasan Singkat Tentang Algoritma SVD
Algoritma SVD adalah salah satu algoritma yang dapat dipakai dalam _image compression_. Algoritma ini bekerja dengan membagi Matriks A<sub>mxn</sub> menjadi matriks U<sub>mxm</sub>, matriks S<sub>mxn</sub>, dan matriks V<sub>nxn</sub>. Matriks U dan V adalah matriks ortogonal. Matriks U terdiri dari eigenvector matriks AA<sup>T</sup>. Matriks V terdiri dari eigenvector matriks A<sup>T</sup>A. Matriks S adalah matriks diagonal yang berisi akar dari eigenvalue A<sup>T</sup>A atau AA<sup>T</sup> yang bernilai di atas 0 yang dikenal juga dengan nama _singular value_. Banyaknya nilai tidak nol di S menunjukkan rank dari A.

Dari ketiga matriks ini, matriks awal dapat direkonstruksi melalui rumus A<sub>mxn</sub> = U<sub>mxm</sub> . S<sub>mxn</sub> . V<sup>T</sup><sub>nxn</sub>

![image](https://user-images.githubusercontent.com/68438200/123517041-50f5f900-d6c9-11eb-9f4e-6ccac26f644d.png)


Penggunaannya dalam kompresi gambar adalah SVD dapat digunakan untuk merekonstruksi gambar dengan rank yang lebih rendah untuk merepresentasikan gambar. Karena itu kompresi melalui algoritma SVD ini disebut _lossy_ karena kedekatan gambar hasil kompresi dengan gambar aslinya tergantung banyaknya singular value yang digunakan dalam rekonstruksi. 

![image](https://user-images.githubusercontent.com/68438200/123517202-df6a7a80-d6c9-11eb-8fc7-f4ae6e4b52fa.png)


Dapat dilihat di gambar di atas bahwa kita dapat merekonstruksi gambar dengan banyak _singular value_ k dengan mengambil kolom sebanyak k dari U dan V serta _singular value_ sebanyak K dari S terurut dari yang terbesar. Tentunya semakin banyak k yang dipakai semakin dekat gambar dengan gambar asli, namun semakin banyak data yang dipakai. Kita cenderung dapat mendapatkan aproksimasi gambar yang mirip dengan gambar asli dengan k yang jauh lebih kecil dari jumlah total _singular value_ karena kebanyakan informasi disimpan di _singular values_ awal karena terurut mengecil. k juga berkaitan dengan rank matriks karena banyaknya singular value yang diambil dalam matriks S adalah rank dari matriks hasil. Maka itu matriks hasil rekonstruksi dari SVD akan memiliki rank yang lebih kecil dari matriks aslinya jika menggunakan k yang lebih kecil dari total _singular values_.

Jadi, dapat dibilang algoritma SVD bermanfaat dalam kompresi gambar karena kemampuannya untuk menghasilkan gambar dengan rank yang lebih kecil dari gambar aslinya namun tetap mempertahankan informasi-informasi pentingnya. Ini dapat dilihat dari strukturnya tepatnya di matriks S yang isi diagonalnya terurut mengecil, sehingga kebanyakan informasi penting di gambar akan ada di _singular values_ awal yang memungkinkan rekonstruksi gambar yang dekat dengan gambar asli dengan rank yang lebih kecil dari gambar asli sehingga gambar memiliki ukuran yang lebih kecil.


# Referensi
http://timbaumann.info/svd-image-compression-demo/
https://www.frankcleary.com/svdimage/
https://machinelearningmastery.com/singular-value-decomposition-for-machine-learning/
https://stackoverflow.com/questions/58894191/image-compression-in-python - Untuk kompresi menggunakan Huffman Coding

# Library
Program dibuat menggunakan bahasa Python
- Numpy -> Untuk manipulasi array, matriks, dan algoritma SVD
- imageio -> Untuk membaca gambar menjadi array
- Pillow -> Untuk rekonstruksi gambar dari array dan menyimpannya
