### PENGERJAAN MyVintageChoice

1. Membuat proyek Django baru:` django-admin startproject e_commers . `
2. Membuat repository baru
3. mengclone repository tersebut ke komputer
4. pada directori asal, membuat virtual python dengan command
  `python -m venv env`
5. Mengaktifkan virtual environment yang telah dibuat sebelumnya dengan menjalankan perintah:
   `env/Scripts/activate`
6. Mempersiapkan requirement dengan command   
	`nvim requirment.txt `   
		dan kemudian mengisi file requirements.txt 
7. menginstall requirement dengan pip
   `python -m pip install -r requirement.txt`
9. Membuat aplikasi main: `python manage.py startapp main`
10. Melakukan routing proyek dengan membuka settings.py dan menambahkan 'main' ke INSTALLED_APPS  
   `   INSTALLED_APPS = [
       ...  
       'main',
   ]`   
   kemudian membuka urls.py dan menambahkan
   `path('', include('main.urls')), `
11. Membuat model product yaitu dengan cara menambahkan   
![image](https://github.com/user-attachments/assets/b6ce191b-eed1-4555-9b89-bb949f37e890)  
pada code tersebut saya memberikan batasan batasan dari entri yang akan dimasukkan
12. Membuat fungsi view dengan melengkapi entri sesuai dengan variable yang digunakan di model dan file htmlnya         
![image](https://github.com/user-attachments/assets/23dc9375-eaec-4f3f-80d1-6d572999bc13)
13. Membuat template HTML dengan membuat folder template di dalam folder main   
![image](https://github.com/user-attachments/assets/4c164072-4a79-4756-bc5c-9153ef16c692)  
pada code saya akan menampilkan: header, nama, harga, deskripsi singkat produk, era, kondisi, dan banyak stock yang tersisa
14. Melakukan migrasi ke database:  
`python manage.py makemigrations` dan `python manage.py migrate`
15. untuk menjalankan server lokal untuk tes saya menjalankan `python manage.py runserver`

### BAGAN DJANGO
![WhatsApp Image 2024-09-10 at 21 56 08_78e7244c](https://github.com/user-attachments/assets/e403eeeb-2dd6-4c7b-844a-e9204a4828bf)   
1. Proses dimulai saat klien mengakses web melalui browser dengan mengirimkan HTTP ke server 
2. Django menerima permintaan tersebut dengan menggunakan file urls.py untuk memetakan antara URL yang diminta dengan fungsi view. Jika URL cocok maka permintaan akan diteruskan ke fungsi view  di view.py
3. Django memanggil fungsi view yang relevan, view bertanggung jawab memproses logika aplikasi. View juga dapat mengambil, mengubah, atau menyimpan data sesuai kebutuhan
4. Jika view membutuhkan basis data, dia akan berinteraksi dengan model.py, model berkomunukasi dengan basis data untuk mengambil, menyimpan, atau memodifikasi data sesuai kebutuhan view
5. Setelah data diproses oleh view, data tersebut kemudian akan dikirim ke template HTML untuk dirender menjadi halaman web
6. Template yang telah dirender dikirimkan kembali sebagai respons HTTP ke pengguna

### FUNGSI GIT
1. Version Control   
	Berfungsi untuk mencatat setiap perubahan yang terjadi pada kode dan jika terjadi kesalahan pada perubahan terbaru,
	memungkinkan pengembang untuk kembali ke versi awal 
2. Collaboration   
		memfasilitasi kerja tim supaya lebih efisien dan agar terdapat sinkronisasi perubahan kode dari
		pengembang yang berbeda
3. Backup   
		Repositori Git berfungsi sebagai cadangan yang dapat di akses kapanpun
4. Audit Trail  
		Menyimpan riwayat lengkap dari setiap perubahan yang dilakukan

### WHY DJANGO???
Menurut saya mengapa django dipilih untuk menjadi permulaan dalam pembelajaran
pengembangan perangkat lunak karena terbilang lebih mudah dipahami dibandingkan
framework lainnya. Django juga menggunakan bahasa python yang di mana sudah dipelajari 
pada DDP1 sebelumnya. Django juga didukung oleh dokumentasi yang lengkap dan 
komunitas besar yang aktif sehingga memudahkan pemula untuk menemukan tutorial atau bantuan. 

### KENAPA DJANGO ORM
ORM adalah Object-Relational Mapping di mana bagian dari kerangka Django 
yang bertanggung jawab untuk memetakan objek python ke struktur basisis data relational,
memungkinkan pengembang untuk berinteraksi dengan basis data menggunkan objek python tanpa perlu menulis kueri SQL langsung. Sehingga dengan Django ORM memudahkan pengembang karena menyediakan antarmuka yang mudah digunakan untuk berinteraksi langsung
dengan basis data, sehingga proses pengembangan menjadi lebih cepat











