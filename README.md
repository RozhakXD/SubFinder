# SubFinder - Subdomain Finder
![SubFinder Images](https://github.com/user-attachments/assets/7442e55c-cde8-4edf-98c0-d4edd917eb3b)

**SubFinder** adalah alat sederhana yang berfungsi untuk mengumpulkan semua subdomain dari suatu domain menggunakan API yang diperoleh melalui bypass SSL pinning dari aplikasi Android.

## Fitur

- **Antarmuka Interaktif**: Memudahkan pengguna untuk memasukkan data dengan format yang benar.
- **Mode Cepat & Lengkap**: Pilih antara pencarian subdomain cepat atau pencarian lengkap.
- **Subdomain Enumeration**: Mengumpulkan semua subdomain dari domain target.
- **Penyimpanan Output**: Hasil pencarian disimpan dalam file teks yang dapat Anda tentukan.

## Persyaratan

- Python 3.x
- Library yang dibutuhkan:
  - `requests`
  - `json`
  - `re`
  - `sys`
  - `time`

Untuk menginstal dependencies, jalankan perintah ini:

```bash
pip install requests
```

## Cara Penggunaan
1. **Clone repository ini ke mesin lokal Anda**:
    ```bash
    git clone https://github.com/RozhakXD/SubFinder.git
    ```

2. **Navigasi ke direktori SubFinder**:
    ```bash
    cd SubFinder
    ```
3. **Jalankan program**:
    ```bash
    python Run.py
    ```
4. **Masukkan domain** (contoh: `facebook.com`, **tanpa** `http`, `https`, **atau** `www`):
    ```less
    Domain (Ex: facebook.com): example.com
    ```
5. **Tentukan lokasi file untuk menyimpan hasil** (**contoh**: `Temporary/Save.txt`):
    ```mathematica
    Files (Ex: Temporary/Save.txt): Output.txt
    ```
6. **Pilih tipe pencarian**:
    - **Complite**: Untuk pencarian subdomain yang lebih mendalam.
    - **Quick**: Untuk pencarian subdomain yang lebih cepat.

    ```graphql
    Type (Quick/Complite): Quick
    ```
7. **Lihat hasil**: Program akan menampilkan hasil subdomain yang ditemukan dan menyimpannya ke file yang telah Anda tentukan. Setelah selesai, Anda akan melihat pesan berikut:
    ```yaml
    Successfully Saved Subdomain!
    Domain Count: X
    Saved in: Output.txt
    ```

## Bug dan Permintaan Fitur
Jika Anda menemukan bug atau memiliki permintaan fitur baru, silakan buka [Issue](https://github.com/RozhakXD/SubFinder/issues) di GitHub. Pastikan memberikan deskripsi yang jelas dan langkah-langkah untuk mereproduksi bug tersebut (jika ada).

## Kontribusi
Kontribusi sangat disambut baik! Jika Anda ingin berkontribusi ke proyek ini:

1. Fork repository ini.
2. Buat branch fitur (`git checkout -b fitur-baru`).
3. Commit perubahan Anda (`git commit -m 'Tambah fitur X'`).
4. Push ke branch (`git push origin fitur-baru`).
5. Buat Pull Request.

Kami akan memeriksa dan meninjau kontribusi Anda secepatnya.

## Dukungan
Jika Anda menyukai proyek ini dan ingin mendukung pengembang, Anda dapat memberikan donasi melalui:

- [Trakteer](https://trakteer.id/rozhak_official/tip)
- [PayPal](https://paypal.me/rozhak9)
Setiap dukungan Anda sangat berarti dan membantu pengembangan lebih lanjut dari SubFinder!

## Tangkapan Layar
![FunPic_20240925](https://github.com/user-attachments/assets/7b3a12d9-ab2d-43a6-9e4f-cda9d9a0a559)

## Lain-lain
- **Keamanan**: Pastikan bahwa Anda memiliki izin untuk melakukan pencarian subdomain di domain tertentu. Penggunaan alat ini terhadap domain tanpa izin dapat melanggar hukum setempat.
- **Pengembangan API**: Jika API yang digunakan dari aplikasi Android diperbarui atau diblokir, Anda mungkin perlu melakukan bypass SSL pinning yang baru untuk terus menggunakannya.

## Lisensi
Proyek ini dilisensikan di bawah lisensi MIT. Lihat file [LICENSE](https://github.com/RozhakXD/SubFinder?tab=MIT-1-ov-file) untuk informasi lebih lanjut.
