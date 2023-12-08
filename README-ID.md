# Microservice-login
Proyek UTS untuk Pemrograman PL SQL. Kelompok 10. 
## Menyiapkan Proyek di Komputer/Laptop
### Clone Proyek
1. Clone proyek dengan perintah berikut:
   ```
   git clone https://github.com/josikie/microservice-login.git
   ```
3. Buka proyek di vscode. Jika belum ada vscode, bisa di download terlebih dahulu. 
### Buat lingkungan virtual:
1. Bukan terminal dari vscode. Jika kamu menggunakan Windows, download [GitBash](https://git-scm.com/downloads). Install GitBash. Kemudian buka terminal dari vscode.
2. Install virualenv dengan perintah berikut:
   ```
   pip install virtualenv
   ```
3. Buat lingkungan virtual dengan perintah berikut:
   ```
   python -m virtualenv env
   ```
4. Jalankan proyek di dalam lingkungan virtual dengan perintah berikut:
   ```
   source env/Scripts/activate
   ```
### Install semua dependency yang dibutuhkan
Untuk menginstall semua dependency yang dibutuhkan, jalankan perintah berikut di terminal GitBash:
```
pip install -r requirements.txt
```
### Menyiapkan Database
1. Buat .env file, dan isi variabel database host, database user, and database password di .env file.
   Contohnya:
   ```
    DB_HOST="localhost:5432"
    DB_USER="yourdb"
    DB_PASSWORD="yourpassword"
   ```
2. Buat terminal baru di vscode.
3. Jalankan Postgres dengan default database. Setelah perintah di bawah dijalankan, Postgres akan menanyakan password yang kamu atur untuk user Postgres.
   Below is the command:
   ```
   psql postgres postgres
   ```
4. Kita akan berada di psql postgres setelah menjalankan perintah di atas.
   Perintah untuk membuat database sudah didefinisikan di file setup.sql, jadi kita hanya perlu menjalankan perintah berikut di psql Postgres untuk membuat database yang dibutuhkan:
   ```
   \i setup.sql
   ```
5. Untuk memastikan database sudah dibuat, mari berpindah database ke database microservice dengan menjalankan perintah berikut:
   ```
   \c microservice
   ```
### Menjalankan Proyek
Kembali ke terminal Git Bash yang kita buka lewat vscode tadi, jalankan perintah ini satu satu:
   ```
   export FLASK_APP=flaskr
   ```
   ```
   export FLASK_DEBUG=TRUE
   ```
   ```
   flask run
   ```
### Testing
REST API ini bisa kamu test dengan [Postman](https://www.postman.com/). Kamu dapat download Postman terlebih dahulu dan install di komputer/laptopmu sebelum melakukan test

### Kontributor
Josi Kie Nababan
