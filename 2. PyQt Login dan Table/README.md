# Tutorial Multiple window dan Tabel menggunakan PyQt5

1. (QtWidget) digunakan untuk menangani multiple window (_Apabila berhasil login maka akan dibawa ke halaman selanjutnya_)
2. (QTableWidget) digunakan untuk menampilkan data kedalam tabel
3. (pushButton) digunakan untuk penambahan dan penghapusan data didalam QTableWidget

## Konsep sederhana
1. `main.py` adalah core aplikasi
2. folder layout berisi layout diantaranya adalah (_login_layout.py dan main_layout.py_)

## Cara menjalankan
1. Run aplikasi :
```
python main.py
```
2. Login dengan mengakomodasi layout (_login_layout.py_) apabila berhasil login maka akan masuk kedalam (_main_layout.py_)
3. di (_main_layout.py_) user dapat menambahkan dan mengurangkan biodata pada (QtTableWidget)
