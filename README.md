## TUGAS 2
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

## TUGAS 3

### Data Delivery 
Data delivery penting dalam pengeimplementasian sebuah platform karena dapat memastikan bahwa informasi atau data yang diperlukan dapat diakses secara cepat sehingga pengguna atau sistem dapat mengakses informasi yang mereka butuhkan tanpa adanya penundaan. Banyak platform terutama yang berbasis online atau cloud yang memerlukan pengiriman data secara real-time. Misalnya e-commers, transaksi dan sebagainya yang harus disampaikan secara real-time agar informasi yang ditampilkan kepada pengguna selalu data yang terbaru

### Mana Yang Lebih Baik JSON atau XML? Kenapa JSON Lebih Popular ??

Menurut saya JSON lebih baik digunakan dalam beberapa kasus terutama dalam pengembangan web dan aplikasi dibandingkan dengan xml. JSON bersifat lebih ringkas dan mudah dibaca dibandingkan dengan XML, JSON menggunakan lebih sedikit karakter untuk merepresentasikan data yang sama yang membuat lebih efisien dalam ukuran data dan bandwidth. Struktur JSON mirip dengan objek dalam bahasa pemrograman seperti JavaScript. 

mengapa jason lebih populer???
- Dari segi simplicity dan readibility, JSON lebih sederhana dan lebih mudah dibaca
- JSON lebih efisien dalam hal ukuran data dan parsing sehingga cocok untuk aplikasi yang memerlukan respons cepat dan penggunaan bandwidth yang minimal
- Banyak API modern termasuk API dari perusahaan menggunakan JSON sebagai format default untuk penukaran data yang mendorong adopsi JSON lebih luas

### Apa Itu Fungsi is_Valid() ???
- is_Valid memeriksa apakah data yang dikirimkan melalui form sesuai dengan aturan validasi yang telah ditentukan dalam form
- jika data valid, is_valid akan mengisi atribut cleaned_data dari form dengan data yang telah dibersihkan dan divalidasi
- jika data tidak valid, is_valid akan mengisi atribut error dari form dengan pesan kesalahan yang sesuai

### Apakah csrf_token Penting???
csrf_token adalah token keamanan yang digunakan dalam form Django untuk melindungi aplikasi dari serangan CSRF. CSRF adalah jenis serangan di mana penyerang memaksa pengguna yang telah diautentikasi untuk mengirim permintaan yang tidak diinginkan ke server. Hal tersebut dapat mengakibatkan tindakan yang tidak diinginkan seperti perubahan data pengguna, melakukan transaksi ilegal, atau mengirim data sensitif. csrf_token memastikan bahwa permintaan yang diterima oleh server berasal dari sumber yang sah. Token ini bersifat unik untuk setiap sesi pengguna dan setiap form sehingga sulit bagi penyerang untuk menebak. Dengan adanya csrf_token ke form, Django dapat memverifikasi bahwa permintaan tentang data benar-benar berasal dari pengguna yang sah bukan dari sumber eksternal yang berbahaya. Jika pengembang tidak menambahkan csrf_token pada Django maka aplikasi menjadi rentan terhadap serangan CSRF serta penyerang dapat memanfaatkan serangan untuk mengubah peraturan akun pengguna, mengirimkan pesan, atau melakukan tindakan lain yang memerlukan otorisasi pengguna.

### Mengimplementasikan CheckList
#### Membuat input form untuk menambahkan objek model pada app sebelumnya
1. pada direktori utama membuat file forms.py 
	- Mengimport ModelForm dari Django Form.
	- Membuat class AdditionalEntryForm  yang mewarisi ModelForm 
 	- Dalam inner class Meta, saya menentukan model yang akan digunakan dan field-field yang akan ditampilkan dalam form
![image](https://github.com/user-attachments/assets/899e0ca6-6f30-404c-8549-7039fbaa251e)

2. membuat view untuk menangani form
	- Fungsi ini akan menangani POST request maupun GET request.
	- Jika form valid dan method adalah POST, data akan disimpan dan user akan diredirect ke halaman utama. Jika tidak, form akan ditampilkan baik form kosong atau form dengan error
![image](https://github.com/user-attachments/assets/3ba43fc6-ff71-4c16-99ca-6a7d1cbdd6ef)

3. membuat template HTML untuk form di folder template dengan nama create_additional_entry.html
	- Meng-extand base template 
	- Form yang ditampilkan akan merender form sebagai tabel 
	- Saya menambahkan styling CSS inline untuk warna pada tombol submit
![image](https://github.com/user-attachments/assets/ec39f07c-b128-492b-abae-afcbf110c84b)

4. menambahkan URL pattern di main/urls.py
	- Menambahkan path baru yang akan memanggil fungsi create_additional_entry ketika URL create-additional-entry diakses

#### Menambahkan 4 fungsi views baru
1. Menambahkan import yang dibutuhkan pada main/views.py
2. Membuat fungsi-fungsi views baru 
	- fungsi ini menggunakan serializers.serialize() untuk mengubah objek model Django menjadi format yang diinginkan (XML atau JSON)
![image](https://github.com/user-attachments/assets/eed6dea5-dd87-4d45-a51a-c50125f5aa68)

	- Fungsi-fungsi tersebut tidak menggunakan template HTML, melainkan langsung mengembalikan data dalam format XML atau JSON
![image](https://github.com/user-attachments/assets/a343748e-a416-42d9-be00-bddd01f385fa)

#### Membuat routing URL untuk masing masing views
1. Menambahkan import fungsi-fungsi baru di view pada main/urls.py
2. Menambahkan URL patterns baru di main/urls.py

### Mengakses keempat URL 
![Screenshot (366)](https://github.com/user-attachments/assets/cfbe01ba-5a56-4ada-b761-62b50eec3af1)
![Screenshot (367)](https://github.com/user-attachments/assets/65e8d62c-5ad4-433d-bedd-f476d331cd12)
![Screenshot (368)](https://github.com/user-attachments/assets/30919e89-af12-4b9b-94d8-4fd52055da87)
![Screenshot (369)](https://github.com/user-attachments/assets/74f7ca67-a009-44e4-9925-44c7b372faaa)















