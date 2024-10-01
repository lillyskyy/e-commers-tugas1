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


## TUGAS 4

### Apa perbedaan antara HttpResponseRedirect() dan redirect()
HttpResponseRedirect adalah kelas yang mengembalikan respons HTTP dengan status kode 302 (Found) dan header location yang diatur ke URL tujuan. HttpResponseRedirect memerlukan URL absolut atau relatif sebagai argumen dan hanya menerima URL sebagai argumen. HttoRespinseRedirert cocok digunakan jika pengguna memerlukan kontrol lebih langsung atas respons HTTP atau jika pengguna bekerja dalam konteks di mana redirect tidak tersedia. Sedangkan redirect adalah fungsi utilitas yang lebih mudah digunakan dan fleksibel. Fungsi ini dapat menerima berbagai jenis argumen, seperti URL absolut, URL relatif, bana URL, atau bahkan objek model, dan secara otomatis mengonversinya menjadi HttpResponseRedirect

### Cara Kerja Penghubungan Model Product dengan User
Bertujuan sehingga pengguna yang sedang terotorisasi hanya dapat melihat data additional entries yang telah dibuat sendiri. Penghubungan model Product dengan model User di django dilakukan melalui akses penggunaan ForeignKey pada model Product. Dalam model Product, terdapat field user yang merupakan ForeignKey ke model User, dengan parameter on_delete=models.CASCADE dan related_name=’product’ . Parameter on_delete=models.CASCADE memastikan bahwa jika pengguna dihapus, semua produk yang terkait dengan pengguna tersebut juga akan dihapus. Parameter related_name=’products’ memungkinkan akses terbalik dari objek User ke semua produk yang dimiliki oleh pengguna tersebut melalui user.products.all(). Ketika pengguna membuat atau mengedit produk, field user diisi dengan pengguna yang sedang login (request.user). Dengan demikian, setiap produk yang dibuat atau diedit  akan terkait dengan pengguna yang membuat. Hal ini memungkinkan aplikasi untuk mengelola dan menampilkan produk berdasarkan pengguna yang terkait, serta memastikan integritas data dengan menghapus produk yang terkait ketika pengguna dihapus

### Perbdeaan authentication dan authorization
Authentication adalah proses verifikasi identitas pengguna di mana memastikan bahwa pengguna adalah siapa yang mereka klaim. Saat pengguna login, sistem memeriksa kredensial (username dan password) yang diberikan terhadap data yang tersimpan di database. Jika kredensial valid, maka pengguna dianggap terautentikasi. Sedangkan Authorization adalah proses menentukan hak akses pengguna yang telah terautentikasi. Ini menentukan apa yang dapat dilakukan atau diakses oleh pengguna. Setelah pengguna terautentikasi, sistem akan memeriksa hak akses pengguna untuk menentukan apa yang dapat mereka lakukan atau akses dalam aplikasi.

Django mengimplementasikan authentication melalui model User, form autentikasi seperti AuthenticationForm, dan view bawaan untuk login dan logout. Middleware AuthenticationMiddleware mengaitkan pengguna yang terautentikasi dengan objek request.user. Untuk authorization, Django menggunakan sistem izin (permissions) dan grup pengguna (groups) yang memungkinkan pengelolaan hak akses pengguna. Decorator seperti login_required memastikan bahwa hanya pengguna yang terautentikasi yang dapat mengakses view tertentu. Dengan demikian, Django memastikan bahwa hanya pengguna yang terautentikasi yang dapat mengakses bagian tertentu dari aplikasi dan bahwa mereka hanya dapat melakukan tindakan yang diizinkan berdasarkan hak akses mereka.

### Cookies
Django mengingat pengguna yang telah login menggunakan mekanisme sesi (sessions) dan cookies. Ketika pengguna berhasil login, Django membuat entri sesi di backend sesi (seperti database, cache, atau file) yang menyimpan informasi tentang pengguna tersebut. Django kemudian mengirimkan cookie sesi ke browser pengguna, yang berisi ID sesi unik. Cookie ini biasanya disebut sessionid. Middleware SessionMiddleware memeriksa cookie sesi pada setiap permintaan dan memuat data sesi yang sesuai dari backend sesi. Jika cookie sesi valid, Django mengaitkan data sesi dengan objek request.session, dan middleware AuthenticationMiddleware mengaitkan pengguna yang terautentikasi dengan objek request.user. Selain mengelola sesi, cookies juga digunakan untuk menyimpan preferensi pengguna, melacak aktivitas pengguna untuk analitik, dan personalisasi konten. Namun, tidak semua cookies aman digunakan. Cookies yang aman harus menggunakan atribut Secure untuk memastikan bahwa mereka hanya dikirim melalui koneksi HTTPS, HttpOnly untuk mencegah akses melalui JavaScript dan melindungi dari serangan cross-site scripting (XSS), serta SameSite untuk mencegah serangan cross-site request forgery (CSRF). Data sensitif tidak boleh disimpan dalam cookies tanpa enkripsi untuk melindungi informasi dari akses yang tidak sah. Dengan mempertimbangkan aspek keamanan ini, cookies dapat digunakan secara efektif dan aman dalam aplikasi web.

### Implementasi Checklist
#### Membuat Fungsi Register
- mengaktifkan terlebih dahulu environment
- kemudian pada file view.py yang berada di directori main, ditambahkan import UserCreationForm dan import messages.
- kemudian pada bagian bawahnya ditambahkan  fungsi register yang berfungsi untuk menghasilkan formulir registrasi secara otomatis dan menghasilkan akun pengguna ketika data di submit
- pada template perlu ditambahkan file baru yaitu register.html 
- pada file urls.py yang berada di main perlu ditambahkan import register dan pada bagian urlpatterns ditambahkan path register    
![image](https://github.com/user-attachments/assets/382db29b-9cc0-4f9d-8026-9812d918292e)
![image](https://github.com/user-attachments/assets/6488e80b-9e46-4eda-8a0a-b0d88e93a3a7)


#### Membuat Fungsi Login
- buka views.py yang berada di main kemudian tambahan import authenticate. login, dan AuthenticatuonForm untuk melakukan autentikasi dan login jika autentikasi berhasil
- masih di views.py tambahkan fungsi login_user
- pada directori main buat file baru bernama login.html
- tambahkan import login_user dan path login pada urls.py    
![image](https://github.com/user-attachments/assets/ea9b23a4-bb29-4003-816c-eed0b883c65a)
![image](https://github.com/user-attachments/assets/79d47eee-4561-4a09-ae6a-0d9afca080f5)


#### Membuat Fungsi Logout
- buka veiws.py tambahkan import logout dan  tambahkan fungsi logout_user untuk melakukan mekanisme logout
- pada main.html dan tambahkan button logout
- pada urls.py tambahkan import logout_user dan tambahkan path logout   
![image](https://github.com/user-attachments/assets/603c582b-fe09-493b-bf35-2077436ccf3b)
![image](https://github.com/user-attachments/assets/a4f18197-f3ba-4a55-b1ac-87b02a468a49)



#### Menghubungkan Product dengan User
- pada models.py perlu menambahkan import user dan pada class AdditionalEntry menambahkan fungsi untuk menghubungkan satu additional entry dengan satu user di mana sebuah additional entry terasosikan dengan seorang user
- mengupdate views.py dengan menambahkan parameter commit = false untuk mencegah django tidak langsung menyimpan object
- migrasi dengan python manage.py makemigrations
- python manage.py migrate

#### Menerapkan Cookies last_login
- pada bagian file views.py perlu menambahkan import HttpResponeRedirect, reverse, dan datetime
- dan pada fungsi login_user yang telah dibuat sebelumnya bagian if form.is_valid() diupdate

#### Membuat Dua Akun Pengguna dengan Tiga Data Dummy
- aktifkan environment terlebih dahulu 
- kemudian runserver dengan python manage.py runserver
- klik register now kemudian buatlah dua akun, satu persatu 
- kemudian akan balik ke halaman login, login satu persatu akun, setiap login masukan tiga data ke additional entry kemudian lakukan seterusnya 
- sehingga akan menampilkan seperti ini
![image](https://github.com/user-attachments/assets/352a83ac-7214-4f9d-ad26-08689c5a659a)
![image](https://github.com/user-attachments/assets/0c96e976-b905-427b-aa88-d9954b621831)


## TUGAS 4

### urutan prioritas pengambilan CSS selector
Ketika beberapa CSS selector diterapkan pada suatu elemen HTML, browser menggunakan sistem prioritas yang disebut "specificity" untuk menentukan aturan mana yang akan diterapkan. Urutan prioritas ini dimulai dari yang paling spesifik hingga yang paling umum. Selector dengan ID memiliki prioritas tertinggi, diikuti oleh selector kelas dan atribut. Selector elemen dan pseudo-elemen memiliki prioritas terendah. Jika dua selector memiliki specificity yang sama, aturan yang ditulis terakhir dalam stylesheet akan diterapkan. Selector inline (yang ditulis langsung pada atribut style elemen HTML) memiliki prioritas tertinggi, mengalahkan semua selector eksternal. Penggunaan !important pada deklarasi properti CSS akan memberikan prioritas tertinggi, namun penggunaannya tidak dianjurkan karena dapat membuat kode sulit dipelihara. Pemahaman tentang urutan prioritas ini sangat penting bagi pengembang web untuk menghindari konflik style dan memastikan tampilan yang konsisten pada halaman web mereka.

### Responsive Design
Responsive design telah menjadi konsep yang sangat penting dalam pengembangan aplikasi web karena beberapa alasan, yaitu:
1. Pengguna mengakses web melalui berbagai perangkat dengan ukuran layar yang berbeda-beda, mulai dari smartphone, tablet, laptop, hingga desktop. Responsive design memungkinkan satu situs web untuk beradaptasi dan tampil dengan baik di semua perangkat ini.
2. Pengalaman Pengguna: Dengan responsive design, pengguna mendapatkan pengalaman yang konsisten dan optimal terlepas dari perangkat yang mereka gunakan. Ini meningkatkan kepuasan pengguna dan mengurangi tingkat bounce rate.
3. Google dan mesin pencari lainnya memberikan preferensi pada situs web yang mobile-friendly dalam hasil pencarian mereka. Responsive design membantu meningkatkan peringkat SEO situs web.

Contoh aplikasi yang sudah menerapkan responsive design:
1. Amazon: Situs e-commerce ini menyesuaikan tata letak dan ukuran elemennya dengan baik untuk berbagai ukuran layar.
2. The New York Times: Situs berita ini memiliki desain yang responsif, menyajikan konten dengan cara yang optimal untuk setiap perangkat.

### Margin, Border, dan Padding
1. Margin
- Margin adalah ruang di luar batas elemen, yang memisahkan elemen tersebut dari elemen-elemen lain di sekitarnya.
- Margin bersifat transparan dan tidak memiliki warna atau latar belakang.
- Digunakan untuk mengatur jarak antar elemen.
```
  .element {
     margin: 10px;                /* Semua sisi */
     margin: 10px 20px;           /* Atas-bawah | Kiri-kanan */
     margin: 10px 20px 15px 25px; /* Atas | Kanan | Bawah | Kiri */
     margin-top: 10px;            /* Sisi spesifik */
   }
```

2. Border
- Border adalah garis yang mengelilingi elemen, terletak di antara margin dan padding.
- Border dapat memiliki warna, gaya (solid, dashed, dll.), dan ketebalan.
- Digunakan untuk memberi batas visual pada elemen.
```
 .element {
     border: 1px solid black;     /* Lebar | Gaya | Warna */
     border-width: 2px;           /* Lebar */
     border-style: dashed;        /* Gaya */
     border-color: red;           /* Warna */
     border-top: 1px solid blue;  /* Sisi spesifik */
   }
```
3. Padding
- Padding adalah ruang di dalam elemen, antara batas elemen (border) dan kontennya.
- Padding mempengaruhi ukuran elemen dan dapat memiliki warna latar belakang.
- Digunakan untuk memberi ruang di sekitar konten dalam elemen.
```
   .element {
     padding: 10px;               /* Semua sisi */
     padding: 10px 20px;          /* Atas-bawah | Kiri-kanan */
     padding: 10px 20px 15px 25px; /* Atas | Kanan | Bawah | Kiri */
     padding-left: 15px;          /* Sisi spesifik */
   }

```

### Flex Box dan Grid Layout
Flexbox dan Grid Layout adalah dua sistem tata letak modern dalam CSS yang menawarkan cara yang lebih efisien dan fleksibel untuk mengatur elemen-elemen dalam sebuah halaman web. Berikut penjelasan tentang kedua konsep tersebut beserta kegunaannya:
1.Flexbox
Flexbox adalah model tata letak satu dimensi yang dirancang untuk mengatur elemen-elemen dalam sebuah container secara fleksibel, baik dalam arah horizontal maupun vertikal.
- Container flex (parent) dan item flex (children)
- Main axis (sumbu utama) dan cross axis (sumbu silang)
- Properti untuk container (display: flex, flex-direction, justify-content, align-items) dan item (flex-grow, flex-shrink, flex-basis)
kegunaan:
a. Membuat layout yang responsif dan fleksibel
b. Mengatur distribusi ruang antar item secara dinamis
c. Menyelaraskan item-item dalam satu baris atau kolom
d. Mengubah urutan tampilan item tanpa mengubah HTML
```
.container {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.item {
  flex: 1;
}
```

2. Grid Layout
Grid Layout adalah sistem tata letak dua dimensi yang memungkinkan pengaturan elemen-elemen dalam baris dan kolom secara bersamaan.
- Grid container dan grid items
- Grid lines, tracks, cells, dan areas
- Properti untuk container (display: grid, grid-template-columns, grid-template-rows) dan item (grid-column, grid-row)
kegunaan:
a. Membuat layout kompleks dengan mudah
b. Mengatur elemen dalam grid yang terstruktur
c. Menciptakan desain responsif yang konsisten
```
.container {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
}

.item {
  grid-column: span 2;
}
```



























