# Tutorial Multiple window dan Tabel menggunakan PyQt5

1. (QtWidget) digunakan untuk menangani multiple window (_Apabila berhasil login maka akan dibawa ke halaman selanjutnya_)
2. (QTableWidget) digunakan untuk menampilkan data kedalam tabel
3. (pushButton) digunakan untuk penambahan dan penghapusan data didalam QTableWidget

## Konsep sederhana
1. `main.py` adalah core aplikasi
2. folder layout berisi layout diantaranya adalah `login_layout.py` dan `main_layout.py`

## Cara menjalankan
1. Run aplikasi :
```
python main.py
```
2. Login dengan mengakomodasi layout `login_layout.py` apabila berhasil login maka akan masuk kedalam `main_layout.py`
3. di `main_layout.py` user dapat menambahkan dan mengurangkan biodata pada (QtTableWidget)
