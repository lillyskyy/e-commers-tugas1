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
1. Dropbox
Halaman web Dropbox sangat adaptif terhadap ukuran layar yang berbeda, dengan tata letak yang menyesuaikan tanpa mengorbankan fungsionalitas atau estetika.
![image](https://github.com/user-attachments/assets/7d963b44-5aa1-4b28-ab68-aa74f8412f05)
![image](https://github.com/user-attachments/assets/2d04d0bf-0764-4f67-82c1-cdc0df414734)

2. Smashing Magazine
Situs web ini dikenal dengan desain responsif yang dioptimalkan untuk pembaca dari berbagai perangkat, baik desktop maupun perangkat seluler.
![image](https://github.com/user-attachments/assets/87b07555-6f6a-481c-8991-2da82f326426)
![image](https://github.com/user-attachments/assets/1e3a5fad-3522-4649-9ce8-18b49282767a)


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


## IMPLEMENTASI CHECK LIST
### COSTUM LOGIN REGISTER

Pembuatan style login pada kode ini mengikuti alur yang terstruktur dan estetis, memanfaatkan kerangka kerja Tailwind CSS untuk styling yang efisien. Proses dimulai dengan membuat kontainer utama yang mengisi seluruh tinggi layar, menggunakan latar belakang berwarna merah muda. Di dalam kontainer ini, ditambahkan sebuah kotak putih dengan bayangan dan sudut melengkung ditempatkan di tengah.

Kotak login dibagi menjadi dua bagian yang seimbang. Bagian pertama untuk form login atau register, dimulai dengan judul yang menegaskan identitas brand. Form login atau register menggunakan spacing yang konsisten dan label yang jelas untuk meningkatkan kegunaan. Input field diberi styling yang membuatnya mudah dibaca dan diinteraksi, dengan efek fokus.

Tombol login atau register menggunakan warna biru yang kontras dengan latar belakang putih dan efek hover untuk feedback visual. Di bawah form, sebuah link untuk registrasi ditempatkan dengan subtle, memberikan opsi bagi pengguna baru. Bagian lainnya kotak diisi dengan gambar, memberikan keseimbangan visual.

### COSTUM CARD
Layout kartu dibagi menjadi beberapa bagian yang terorganisir. Bagian atas menampilkan nama produk dan stok dengan warna kontras, diikuti oleh deskripsi produk di bagian tengah, dan informasi harga di bagian bawah. Tombol Edit dan Delete ditempatkan di sudut kanan atas untuk akses cepat, dengan warna yang berbeda (kuning untuk Edit, merah untuk Delete) untuk membedakan fungsinya dengan jelas.

Responsivitas dalam desain ini diimplementasikan melalui penggunaan kelas-kelas Tailwind yang fleksibel. Meskipun tidak ada breakpoint eksplisit yang ditentukan untuk perangkat berbeda, beberapa aspek desain secara inheren responsif:
1. Penggunaan `w-full` pada elemen-elemen memastikan mereka mengisi lebar penuh dari container induknya, yang akan menyesuaikan pada berbagai ukuran layar.
2. Padding dan margin yang konsisten (`p-6`, `mb-2`, dll.) membantu mempertahankan tata letak yang rapi pada berbagai ukuran layar.
3. Penggunaan `text-sm`, `text-lg`, dan `text-2xl` untuk ukuran font memungkinkan skalabilitas teks yang baik.
4. Kelas `break-inside-avoid` membantu dalam penempatan kartu dalam layout masonry atau grid, mencegah pemisahan konten kartu.
5. Transisi dan efek hover (`group-hover:scale-105`) memberikan interaktivitas yang halus, yang berfungsi baik di desktop maupun perangkat sentuh.

IMPLEMENTASI EDIT DELETE
- Button ditempatkan dalam sebuah div dengan kelas `absolute top-3 right-3`, yang memposisikan mereka di pojok kanan atas kartu.
- Menggunakan `flex` dan `space-x-2` untuk menyusun button secara horizontal dengan jarak antar button.
- `z-10` memastikan button tetap di atas elemen lain dalam kartu.
- Kedua button menggunakan kelas `rounded-md` untuk sudut melengkung.
- `px-3 py-1` memberikan padding horizontal dan vertikal. 
- Button edit menggunakan `bg-yellow-400` untuk warna latar kuning.  hover: bg-yellow-500 memberikan efek hover dengan warna kuning yang lebih gelap
- Button Delete menggunakan `bg-red-400` untuk warna latar merah.  `additional_entry.pk` digunakan untuk mengidentifikasi item spesifik yang akan diedit atau dihapus.

### RESPONSIVE NAVBAR
- `hidden md:flex` pada div menu utama: Menyembunyikan menu pada layar kecil, menampilkannya sebagai flex container pada layar medium ke atas.
- `md:hidden` pada div tombol menu mobile: Menampilkan tombol hamburger hanya pada layar kecil, menyembunyikannya pada layar medium ke atas.
- Penggunaan `flex` dan `justify-between` untuk mengatur tata letak elemen navbar secara horizontal dan memberikan ruang di antara logo dan menu.
- Penggunaan `px-4 sm:px-6 lg:px-8` untuk menyesuaikan padding horizontal pada berbagai ukuran layar.
- Penggunaan kelas yang konsisten untuk tombol (seperti `rounded`, `transition duration-300`) memastikan tampilan yang seragam di semua ukuran layar.
- Penggunaan `fixed top-0 left-0 z-40 w-screen` memastikan navbar tetap terlihat di atas konten lain saat di-scroll, konsisten di semua ukuran layar.


##TUGAS 6

###Manfaat dari penggunaan JavaScripts dalam pengembangan web
JavaScript memiliki peran yang sangat penting dalam pengembangan aplikasi web modern. Manfaat utamanya terletak pada kemampuannya untuk meningkatkan interaktivitas dan responsivitas halaman web. Dengan JavaScript, pengembang dapat menciptakan antarmuka pengguna yang dinamis dan responsif, memungkinkan interaksi real-time tanpa perlu me-refresh halaman. Ini tidak hanya meningkatkan pengalaman pengguna, tetapi juga memungkinkan validasi form di sisi klien, yang dapat mengurangi beban server dan mempercepat respons aplikasi.


Dari segi performa, JavaScript memungkinkan pemrosesan data di sisi klien dan pembaruan konten secara asinkron melalui AJAX. Hal ini secara signifikan meningkatkan kecepatan dan efisiensi aplikasi web. Selain itu, JavaScript juga mendukung pengembangan aplikasi single-page (SPA) yang memberikan pengalaman navigasi yang mulus seperti aplikasi native. Kompatibilitas lintas platform JavaScript juga memungkinkan aplikasi web berjalan di berbagai browser dan perangkat, termasuk pengembangan aplikasi hybrid untuk mobile dan desktop.


Ekosistem JavaScript yang kaya, dengan berbagai library dan framework seperti React, Vue, dan Angular, mempercepat dan mempermudah proses pengembangan. Dengan Node.js, JavaScript juga dapat digunakan di sisi server, memungkinkan pengembangan full-stack dengan satu bahasa pemrograman. Kemampuan manipulasi DOM JavaScript memungkinkan perubahan dinamis pada struktur dan gaya halaman web, sementara fitur-fitur seperti animasi dan efek visual dapat meningkatkan daya tarik visual aplikasi. 

###Fungsi await ketika menggunakan fetch()
Penggunaan `await` ketika bekerja dengan `fetch()` memiliki peran krusial dalam penanganan operasi asynchronous di JavaScript. Fungsi utamanya adalah untuk menyinkronkan kode asynchronous, membuatnya lebih mudah dibaca dan dipahami. Ketika `await` digunakan, eksekusi fungsi async akan berhenti sampai Promise yang dikembalikan oleh `fetch()` selesai atau gagal. Ini memungkinkan pengembang untuk menulis kode yang menangani operasi jaringan seolah-olah itu adalah operasi synchronous, meskipun sebenarnya berjalan secara asynchronous di latar belakang.

Tanpa menggunakan `await`, kode akan berjalan secara non-blocking, yang berarti eksekusi akan berlanjut tanpa menunggu `fetch()` selesai. Ini bisa menyebabkan masalah jika ada kode selanjutnya yang bergantung pada hasil dari operasi fetch. Dalam skenario tanpa `await`, pengembang harus mengandalkan metode `.then()` untuk menangani hasil Promise, yang dapat mengakibatkan kode yang lebih sulit dibaca, terutama jika ada banyak operasi asynchronous yang berurutan. Selain itu, penanganan error menjadi lebih rumit karena harus menggunakan `.catch()` alih-alih blok try-catch yang lebih intuitif.


Keuntungan lain dari penggunaan `await` adalah kemampuannya untuk secara otomatis mengekstrak nilai yang di-resolve oleh Promise. Ini berarti hasil dari operasi fetch dapat langsung digunakan tanpa perlu callback tambahan. Sebaliknya, tanpa `await`, nilai Promise tidak langsung tersedia dan harus ditangani di dalam callback `.then()`. Dalam konteks penanganan error, `await` memungkinkan penggunaan blok try-catch yang familiar untuk menangani kesalahan dalam operasi asynchronous, membuat penanganan error lebih straightforward dan konsisten dengan kode synchronous.

###Mengapa perlu decorator csrf_exempt
Decorator `csrf_exempt` digunakan dalam Django untuk menonaktifkan perlindungan CSRF (Cross-Site Request Forgery) pada view tertentu. Dalam konteks AJAX POST, ada beberapa alasan mengapa Anda mungkin perlu menggunakan `csrf_exempt`:


1. Kemudahan Pengembangan: Selama tahap pengembangan, Anda mungkin ingin menonaktifkan perlindungan CSRF untuk mempermudah pengujian dan debugging. Ini memungkinkan Anda untuk mengirim permintaan POST tanpa harus mengatur token CSRF yang valid.

2. **Permintaan dari Sumber Eksternal**: Jika aplikasi Anda menerima permintaan POST dari sumber eksternal yang tidak dapat menyertakan token CSRF, Anda mungkin perlu menonaktifkan perlindungan CSRF untuk view tersebut. Namun, ini harus dilakukan dengan hati-hati karena dapat membuka celah keamanan.

3. **Kesalahan Konfigurasi**: Terkadang, pengembang menggunakan `csrf_exempt` untuk mengatasi kesalahan konfigurasi sementara, seperti ketika token CSRF tidak dikirim atau diterima dengan benar dalam permintaan AJAX. Ini bisa menjadi solusi sementara sambil mencari cara yang lebih aman untuk mengelola token CSRF.

Namun, penting untuk dicatat bahwa menonaktifkan perlindungan CSRF dapat meningkatkan risiko keamanan aplikasi Anda. CSRF adalah serangan di mana penyerang dapat membuat pengguna yang diautentikasi melakukan tindakan yang tidak diinginkan di aplikasi web. Oleh karena itu, penggunaan `csrf_exempt` harus dibatasi dan dipertimbangkan dengan hati-hati. Sebagai alternatif, Anda dapat memastikan bahwa token CSRF disertakan dalam permintaan AJAX dengan benar, misalnya dengan menyertakannya dalam header atau sebagai bagian dari data yang dikirim. Ini akan menjaga keamanan aplikasi Anda sambil tetap memungkinkan operasi AJAX POST.

###Pembersihan data input
Pembersihan data input pengguna di backend adalah praktik penting dalam pengembangan aplikasi web yang aman dan andal. Meskipun validasi dan pembersihan data di frontend dapat meningkatkan pengalaman pengguna dengan memberikan umpan balik langsung, ada beberapa alasan mengapa pembersihan data juga harus dilakukan di backend:

1. **Keamanan**: Frontend dapat dimanipulasi oleh pengguna yang berniat jahat. Mereka dapat mem-bypass validasi frontend dengan menggunakan alat pengembang browser atau mengirimkan permintaan langsung ke server. Oleh karena itu, backend harus memverifikasi dan membersihkan data untuk mencegah serangan seperti SQL injection, XSS (Cross-Site Scripting), dan lainnya.

2. **Integritas Data**: Backend bertanggung jawab untuk memastikan bahwa data yang masuk ke sistem adalah valid dan sesuai dengan aturan bisnis. Ini memastikan bahwa data yang disimpan dalam database adalah konsisten dan dapat diandalkan.

3. **Pengendalian Pusat**: Backend memberikan satu titik kontrol untuk semua validasi dan pembersihan data, yang memudahkan pemeliharaan dan pembaruan aturan validasi. Jika ada perubahan dalam aturan validasi, Anda hanya perlu memperbarui backend, bukan setiap klien yang mungkin mengirimkan data.

###Step
1. Menambahkan Pesan Error untuk Validasi Kesalahan pada Form Login
view login mengirim pesan error menggunakan messages jika ada kesalahan.
```
  def login_user(request):
      if request.method == 'POST':
          form = AuthenticationForm(data=request.POST)
          if form.is_valid():
              user = form.get_user()
              login(request, user)
              response = HttpResponseRedirect(reverse("main:show_main"))
              response.set_cookie('last_login', str(datetime.datetime.now()))
              return response
          else:
              messages.error(request, "Invalid username or password. Please try again.")
      else:
          form = AuthenticationForm(request)
      context = {'form': form}
      return render(request, 'login.html', context)
```
Tampilkan pesan error di template login.html
```
  {% if messages %}
    <ul>
      {% for message in messages %}
        <li class="text-red-600 font-bold">{{ message }}</li>
      {% endfor %}
    </ul>
  {% endif %}
```

2. Membuat View Baru add_additional_entry_ajax
add_additional_entry_ajax yang menangani permintaan POST menggunakan AJAX.
```
  @csrf_exempt
  @require_POST
  def add_additional_entry_ajax(request):
      product = strip_tags(request.POST.get("product"))
      description = strip_tags(request.POST.get("description"))
      stock = request.POST.get("stock")
      price = request.POST.get("price")
      user = request.user

      new_additional = AdditionalEntry(
          product=product, 
          description=description,
          stock=stock,
          price=price,
          user=user
      )
      new_additional.save()

      return HttpResponse(b"CREATED", status=201)
```

3. Menambahkan Path Baru untuk View add_additional_entry_ajax
```
  from django.urls import path
  from . import views

  urlpatterns = [
      # ... path lainnya ...
      path('add-additional-entry-ajax/', views.add_additional_entry_ajax, name='add_additional_entry_ajax'),
  ]
```
4.  Membuat Fungsi refreshAdditionalEntry untuk Mengambil dan Menampilkan Data Produk
```
async function refreshAdditionalEntries() {
    document.getElementById("additional_entry_cards").innerHTML = "";
    document.getElementById("additional_entry_cards").className = "";
    const additionalEntries = await getAdditionalEntries();
    let htmlString = "";
    let classNameString = "";

    if (additionalEntries.length === 0) {
        classNameString = "flex flex-col items-center justify-center min-h-[24rem] p-6";
        htmlString = `
            <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
                <img src="{% static 'images/cat2.png' %}" alt="Sad face" class="w-32 h-32 mb-4"/>
                <p class="text-center text-gray-600 mt-4">Belum ada data additional pada MyVintageChoice.</p>
            </div>
        `;
    } else {
        classNameString = "columns-1 sm:columns-2 lg:columns-3 gap-6 space-y-6 w-full"
        additionalEntries.forEach((item) => {
          const product = DOMPurify.sanitize(item.fields.product);
          const description = DOMPurify.sanitize(item.fields.description);
            htmlString += `
            <div class="relative break-inside-avoid group">
                <div class="relative bg-white shadow-lg rounded-xl overflow-hidden transition-all duration-300 transform group-hover:scale-105">
                    <div class="absolute top-3 right-3 flex space-x-2 z-10">
                        <a href="/edit-additional/${item.pk}" class="bg-yellow-400 hover:bg-yellow-500 text-white rounded-md px-3 py-1 text-sm font-medium transition duration-300 shadow-md">
                            Edit
                        </a>
                        <a href="/delete-additional/${item.pk}" class="bg-red-400 hover:bg-red-500 text-white rounded-md px-3 py-1 text-sm font-medium transition duration-300 shadow-md">
                            Delete
                        </a>
                    </div>
                    <div class="bg-[#C1CFA1] text-white p-6 rounded-t-xl">
                        <h3 class="font-bold text-2xl mb-2">${item.fields.product}</h3>
                        <p class="text-white opacity-80">Stock: ${item.fields.stock}</p>
                    </div>
                    <div class="p-6">
                        <p class="font-semibold text-lg mb-3 text-gray-700">Description</p> 
                        <p class="text-gray-600 mb-4 leading-relaxed">
                            ${item.fields.description}
                        </p>
                        <div class="mt-6">
                            <p class="text-gray-700 font-semibold mb-2">Price</p>
                            <div class="bg-[#C1CFA1] rounded-full py-2 px-4 inline-block">
                                <span class="text-lg font-bold text-gray-700">
                                    Rp ${item.fields.price}
                                </span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            `;
        });
    }
    document.getElementById("additional_entry_cards").className = classNameString;
    document.getElementById("additional_entry_cards").innerHTML = htmlString;
}
```

5. Menambahkan Modal Form untuk Menambahkan Produk Baru
```
  <div id="crudModal" tabindex="-1" aria-hidden="true" class="hidden fixed inset-0 z-50 w-full flex items-center justify-center bg-gray-800 bg-opacity-50 overflow-x-hidden overflow-y-auto transition-opacity duration-300 ease-out">
      <div id="crudModalContent" class="relative bg-white rounded-lg shadow-lg w-5/6 sm:w-3/4 md:w-1/2 lg:w-1/3 mx-4 sm:mx-0 transform scale-95 opacity-0 transition-transform transition-opacity duration-300 ease-out">
          <!-- Modal content -->
      </div>
  </div>
```

6. Menambahkan Fungsi untuk Menangani Pengiriman Form Menggunakan AJAX POST
7. Menggunakan DOMPurify untuk Membersihkan Data
```
 const product = DOMPurify.sanitize(item.fields.product);
          const description = DOMPurify.sanitize(item.fields.description);
```






















