# Microservice-login
Microservice login adalah sebuah proyek microservice dengan REST API untuk login, CRUD tabel users, dan manajemen akses pengguna (role: admin, member) yang dibangun di atas Python dan Flask. Proyek ini dibuat oleh kelompok 10 untuk menyelesaikan proyek Ujian Akhir Semester Pemrograman PL SQL.

Proyek ini memanfaatkan AES 256 untuk mengenkripsi data pengguna seperti email dan password. Jadi, email dan password akan dienkripsi terlebih dahulu sebelum disimpan pada database. Mengenai proses fungsi enkripsi dan dekripsi dapat dilihat pada file [microservice-login/encryption.py](https://github.com/josikie/UTS-Microservice-CRUD-API-PL-SQL-UNSIA/blob/main/encryption.py).

Kelompok 10:
- Josi Kie Nababan ( 220401010122 )
- Ismal Zikri ( 220401010009 )
- Jefrianto (220401010114)

# Methodology Software Development Life Cycle (SDLC): Pendekatan Agile  

Kami melakukan Pendekatan Agile karena menurut kami itulah yang terbaik bagi kami karena setiap orang dapat melakukan beberapa hal yang fleksibel, dan melakukan berbagai hal, seperti siapa yang pertama kali inisiasi, fitur yang terakhir diperbarui, dan seterusnya.

kami mencoba memisahkan dan menerapkan praktik menggunakan SCRUM, mari kami jelaskan hal ini:

Prinsip Agile
Diskusikan prinsip-prinsip utama Agile sebagaimana diuraikan dalam Agile Manifesto. Prinsip-prinsip ini meliputi:

- Individu dan interaksi atas proses dan alat.
- Solusi kerja melalui dokumentasi yang komprehensif.
- Kolaborasi pelanggan melalui negosiasi kontrak.
- Menanggapi perubahan dengan mengikuti rencana.

Praktek Tangkas
Jelaskan praktik Agile yang diikuti tim Anda. Praktik Agile yang umum meliputi:

- Scrum: Kerangka kerja berulang dan bertahap untuk mengelola pekerjaan pengetahuan yang kompleks.
- Kanban: Metode manajemen visual untuk menyeimbangkan permintaan dengan kapasitas yang tersedia.
- Kisah Pengguna: Deskripsi singkat dan sederhana tentang fitur yang diceritakan dari sudut pandang orang yang menginginkan kemampuan baru.
- Standup Harian: Pertemuan harian singkat untuk membahas kemajuan.

Postman Export: [Microservice.postman_collection.json](https://github.com/josikie/UTS-Microservice-CRUD-API-PL-SQL-UNSIA/blob/main/Microservice.postman_collection.json)

## Menyiapkan Proyek di Komputer/Laptop
### Clone Proyek
1. Clone proyek dengan perintah berikut:
   ```
   git clone https://github.com/josikie/UTS-Microservice-CRUD-API-PL-SQL-UNSIA.git
   ```
3. Buka proyek di vscode. Jika belum ada vscode, bisa di download terlebih dahulu. 
### Buat lingkungan virtual:
1. Buka terminal dari vscode. Jika kamu menggunakan Windows, download [GitBash](https://git-scm.com/downloads). Install GitBash. Kemudian buka terminal dari vscode.
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
   KEY="secretkey"
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
## Endpoint REST API
Endpoint yang dapat diakses pengguna tanpa memerlukan login:
```
1. GET /microservices
2. POST /microservices/login
```
Endpoint yang dapat diakses pengguna dengan role Member (memerlukan login):
```
1. GET /microservices
2. POST /microservices/login
3. GET /microservices/user
4. GET /microservices/user/<int:id>
5. GET /microservices/logout
```
Endpoint yang hanya dapat diakses pengguna dengan role Admin (memerlukan login):
```
1. GET /microservices
2. POST /microservices/login
3. GET /microservices/user
4. GET /microservices/user/<int:id>
5. GET /microservices/logout
6. POST /microservices/user/create_user
7. PATCH /microservices/user/<int:id>
8. DELETE /microservices/user/<int:id>
```

## REST API
GET `http://127.0.0.1:5000/microservice`
- digunakan untuk mendapatkan pesan selamat datang.
- mengembalikan objek JSON yang berisi pesan selamat datang dan success.
  
contoh return:

```
{
  "message": "Hello! Welcome to Microservice. To access another features, please log in.",
  "success": true
}
```

POST `http://127.0.0.1:5000/microservice/login`
- digunakan untuk login pengguna.
- mengembalikan objek JSON yang berisi message, success, dan status_code.
- membutuhkan objek JSON pada body yang berisi email dan kata sandi pengguna.

contoh return:

```
{
    "message": "Password and email correct. Succesfully Log in.",
    "status_code": 200,
    "success": true
}
```

GET `http://127.0.0.1:5000/microservice/user`
- digunakan untuk mengambil semua email pengguna.
- mengembalikan objek JSON yang berisi status code, success, dan semua email pengguna.
- memerlukan otorisasi untuk mengakses (peran Admin atau Anggota).
  
contoh return:

```
{
    "status_code": 200,
    "success": true,
    "users": [
        {
            "email": "admin@gmail.com"
        },
        {
            "email": "member@gmail.com"
        },
        {
            "email": "admin5@gmail.com"
        }
    ]
}
```

GET `http://127.0.0.1:5000/microservice/user/<int:id>`
- digunakan untuk mengambil email pengguna tertentu.
- mengembalikan objek JSON yang berisi status code, success, dan email dari pengguna tertentu.
- memerlukan otorisasi untuk mengakses (peran Admin atau Anggota)
- perlu mendefinisikan id pengguna pada tautan.
  
contoh return:

```
{
    "email": "admin@gmail.com",
    "isActive": false,
    "role_id": 1,
    "role_name": "Admin",
    "status_code": 200,
    "success": true
}
```

GET `http://127.0.0.1:5000/microservice/logout`
- digunakan untuk logout pengguna.
- mengembalikan objek JSON yang berisi message, status code, dan success.
- membutuhkan otorisasi (Admin atau anggota peran).
  
contoh return:

```
{
    "message": "Successfully Log out",
    "status_code": 200,
    "success": true
}
```

POST `http://127.0.0.1:5000/microservice/user/create_user`
- digunakan untuk membuat pengguna baru.
- mengembalikan objek JSON yang berisi status code dan message.
- membutuhkan otorisasi (peran Admin).
- membutuhkan objek JSON pada body untuk mengirimkan data pengguna yang ingin dibuat: email, kata sandi, dan role.
  
contoh return:

```
{
    "status_code": 200,
    "success": true
}
```

PATCH `http://127.0.0.1:5000/microservice/user/7`
- digunakan untuk memperbarui data pengguna.
- mengembalikan objek JSON yang berisi status code, success, dan peran baru.
- membutuhkan otorisasi (peran Admin)
- membutuhkan id pengguna pada tautan tersebut.
- membutuhkan objek JSON pada body untuk mengirimkan data pengguna yang ingin diperbarui.
  
contohnya return:

```
{
    "new_role": "Admin",
    "status_code": 200,
    "success": true
}
```

DELETE `http://127.0.0.1:5000/microservice/user/7`
- digunakan untuk menghapus pengguna tertentu.
- mengembalikan objek JSON yang berisi status code dan success.
- membutuhkan otorisasi (peran Admin).
- membutuhkan id pengguna pada tautan.
  
contoh return:

```
{
    "status_code": 200,
    "success": true
}
```

### Error Handling
Ada dua penangan untuk error/kesalahan. Kesalahan mengembalikan objek JSON dalam format berikut:
```
'success': False,
'status_code': 401,
'message': 'unauthorized access'
```
Berikut adalah dua jenis kesalahan ketika permintaan gagal:
- 400: Bad Request
- 401: Unauthorized Access.

### Trigger Log
Trigger Log tidak dikonfigurasi melalui aplikasi, melainkan dari database dengan query berikut
1. Buat tabel audit_log
```
CREATE TABLE audit_log(
   log_id serial PRIMARY KEY,
   users_id VARCHAR(255),
   changed_field VARCHAR(255),
   old_value VARCHAR(255),
   new_value VARCHAR(255),
   log_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
  );
```
2. Buat fungsi log_user_changes
```
CREATE OR REPLACE FUNCTION log_users_changes()
RETURNS TRIGGER AS $$
BEGIN
   IF NEW.email IS DISTINCT FROM OLD.email THEN
   INSERT INTO audit_log(users_id, changed_field, old_value, new_value)
   VALUES (current_user::text, 'email', OLD.email, NEW.email);
END IF;

   IF NEW.password IS DISTINCT FROM OLD.password THEN
   INSERT INTO audit_log(users_id, changed_field, old_value, new_value)
   VALUES(current_user::text, 'password', OLD.password, NEW.password);
END IF;

RETURN NEW;
END;
$$ LANGUAGE plpgsql;
```
3. Buat trigger users_changes_trigger dan eksekusi fungsi log_users_changes
```
CREATE TRIGGER users_changes_trigger
AFTER UPDATE ON users
FOR EACH ROW
EXECUTE FUNCTION log_users_changes();
```

## Testing
1. REST API
REST API ini bisa kamu test dengan [Postman](https://www.postman.com/). Kamu dapat download Postman terlebih dahulu dan install di komputer/laptopmu sebelum melakukan test

2. Trigger Log
Berikut adalah email dan password yang tersimpan di database
![image](https://github.com/josikie/UAS-Microservice-CRUD-API-PL-SQL-UNSIA/assets/63739078/565b4c31-8ab8-4009-b91d-8cc8cbf4e5fc)

Ketika user mengubah data, perubahan tersimpan pada tabel audit_log table dengan format aes256 yang terenkripsi
![image](https://github.com/josikie/UAS-Microservice-CRUD-API-PL-SQL-UNSIA/assets/63739078/2912bc33-57bc-4f21-9623-e56ccdd0f432)
