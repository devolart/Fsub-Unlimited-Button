`Repo ini merupakan modifikasi dari File-Sharing-Man dengan tambahan fitur unlimited button`

# File-Sharing-Man

Bot Telegram untuk menyimpan Posting atau File yang dapat Diakses melalui Link Khusus.
Saya Kira Ini Akan Bermanfaat Bagi Banyak Orang.

## ⚠️ Disclaimer

```
Saya tidak bertanggung jawab atas penyalahgunaan bot ini.
Bot ini dimaksudkan untuk membantu untuk menyimpan file yang diinginkan yang dapat diakses melalui Link Khusus.
Gunakan bot ini dengan risiko Anda sendiri, dan gunakan bot ini dengan bijak.
```

### Features
- Sepenuhnya dapat dicustom.
- Dapat di-deploy di heroku & vps.
- Pesan sambutan & Forcesub yang dapat dicustom.
- Lebih dari satu Posting dalam Satu Link (batch).
- Fleksibel FSUB Button bisa unlimited button menyesuaikan dengan var yang di isi.

### Setup

- Tambahkan bot ke Channel Database dengan semua izin admin
- Tambahkan bot ke Channel & Group ForceSub tambahkan bot sebagai ADMIN

## 🛡 Installation
### Deploy on Heroku
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://risman.vercel.app/file-deploy.html)</br>

**Tonton Video Tutorial Ini di YouTube untuk Bantuan memasang di Heroku**<br>
<a href="https://youtu.be/O2tieQgzYZg">
  <img src="https://img.shields.io/badge/How%20to-Deploy-red?logo=youtube" width="147">
</a><br>

<details>
<summary><h3><b>🔗 Extra Custom & List Vars</b></h3></summary>

### Variables

* `API_HASH` Dapatkan API HASH di web my.telegram.org.
* `API_ID` Dapatkan APP ID di web my.telegram.org
* `TG_BOT_TOKEN` Dapatkan dari t.me/BotFather
* `OWNER` Masukan Username Telegram untuk Owner BOT
* `CHANNEL_ID` Masukan ID Channel Untuk [Channel Database] contoh:- -100xxxxxxxx
* `ADMINS` Masukan User ID untuk mendapatkan hak Admin di BOT
* `START_MESSAGE` Opsional: Pesan /start memulai awalan ke bot, Gunakan <a href='https://github.com/mrismanaziz/File-Sharing-Man/blob/main/README.md#start_message'>format</a> parsemode HTML 
* `FORCE_SUB_MESSAGE` Opsional: Pesan Paksa Subscribe bot, Gunakan Format parsemode HTML
* `FORCE_SUB1`, `FORCE_SUB2`, `FORCE_SUB3`, `FORCE_SUB4`, `FORCE_SUB5`, dst: Masukan ID dari Channel dan Group Untuk Wajib Subscribenya
* `BUTTONS_PER_ROW` Opsional: Maksimal jumlah button per baris (untuk unlimited button). Default `3`
* `BUTTONS_JOIN_TEXT` Opsional: Isi tulisan button untuk join (untuk unlimited button). Default `ᴊᴏɪɴ`

### Extra Variables

* `CUSTOM_CAPTION` letakkan teks teks Kustom Anda jika Anda ingin Mengatur Teks Kustom, Anda dapat menggunakan HTML dan <a href='https://github.com/mrismanaziz/File-Sharing-Man/blob/main/README.md#custom_caption'>fillings</a> untuk pemformatan (hanya untuk dokumen)
* `DISABLE_CHANNEL_BUTTON` Masukan True untuk Nonaktifkan Tombol Berbagi Saluran, Default jika False

### Fillings
#### START_MESSAGE | FORCE_SUB_MESSAGE

* `{first}` - User first name
* `{last}` - User last name
* `{id}` - User ID
* `{mention}` - Mention the user
* `{username}` - Username

#### CUSTOM_CAPTION

* `{filename}` - file name of the Document
* `{previouscaption}` - Original Caption

</details>

## 🏷 Support   
- Follow Channel [@Lunatic0de](https://t.me/Lunatic0de) untuk info Update bot 
- Gabung Group [@SharingUserbot](https://t.me/SharingUserbot) untuk diskusi, pelaporan bug, dan bantuan tentang File-Sharing-Man.

## 👨🏻‍💻 Credits

-  [Dan](https://github.com/delivrance) for [Pyrogram](https://github.com/pyrogram/pyrogram)
-  [Risman](https://github.com/mrismanaziz) for [File-Sharing-Man](https://github.com/mrismanaziz/File-Sharing-Man)
-  Based on [CodeXBotz](https://github.com/CodeXBotz) Repo [File-Sharing-Bot](https://github.com/CodeXBotz/File-Sharing-Bot)
-  [katarina_ox](https://t.me/katarina_ox) for [unlimited button feature](https://github.com/devolart/Fsub-Unlimited-Button)

## 📑 License
[![GNU GPLv3 Image](https://www.gnu.org/graphics/gplv3-127x51.png)](http://www.gnu.org/licenses/gpl-3.0.en.html)  

[FILE-SHARING-BOT](https://github.com/mrismanaziz/File-Sharing-Man/) is Free Software: You can use, study share and improve it at your
will. Specifically you can redistribute and/or modify it under the terms of the
[GNU General Public License](https://www.gnu.org/licenses/gpl.html) as
published by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version. 

##

   **Berikan Bintang Repo ini jika Anda menyukainya ⭐⭐⭐⭐⭐**

