Proyek ini berisi skrip Python untuk melakukan web scraping informasi tentang pemain Manchester United dari situs resmi mereka. Skrip ini mengumpulkan data dari berbagai kategori tim, termasuk tim utama, tim wanita, u-21, u-18, dan legend.

## Fitur

- Melakukan scraping data pemain dari beberapa halaman tim di situs resmi Manchester United
- Mengambil detail seperti tim, posisi, nomor jersey, nama depan, nama belakang, nama lengkap, tautan pemain dll
- Menyimpan data yang di-scrape ke file CSV dan JSON

## Bahasa dan Library yang Digunakan

- **Python**: Bahasa pemrograman yang digunakan untuk scripting
- **Selenium**: Untuk otomatisasi web dan interaksi dengan konten dinamis
- **BeautifulSoup**: Untuk parsing konten HTML dan ekstraksi informasi
- **CSV**: Untuk menyimpan data yang di-scrape dalam format CSV
- **JSON**: Untuk menyimpan data yang di-scrape dalam format JSON

## Data yang Diambil

Skrip ini mengumpulkan data berikut untuk setiap pemain:

- Tim
- Posisi
- Nomor Jersey
- Nama Depan
- Nama Belakang
- Nama Lengkap
- Tautan Pemain
- Biografi
- Negara
- Tanggal Lahir

## Deskripsi File

- `mu_team.py`: Skrip utama yang berisi logika web scraping.
- `mu_team.csv`: File CSV tempat data pemain yang di-scrape akan disimpan.
- `mu_team.json`: File JSON tempat data pemain yang di-scrape akan disimpan.

## Screenshot Hasil

- JSON
![image](https://github.com/NCholisM/manchester_united_player/assets/57277402/31f8dba9-9126-46d6-9125-c26fc7bded9c)

- CSV
![image](https://github.com/NCholisM/manchester_united_player/assets/57277402/a6ae866a-0833-4755-8cfc-58eb643d7522)

![image](https://github.com/NCholisM/manchester_united_player/assets/57277402/bed0ecda-0971-4a2b-a6f3-2aa5dac64e82)
