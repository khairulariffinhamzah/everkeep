# Kemahiran: save

**Dicetus oleh:** `save`, `save memory`, `remember ...`
**Membaca:** `core/*`, `projects/<nama>.md`   **Menulis:** fail yang sama

## Langkah: simpan penuh
1. Semak semula perbualan dan senaraikan apa yang **baharu dan berguna untuk sesi akan datang**: kemajuan, keputusan, baki kerja, perkara yang dipelajari tentang pengguna.
2. **Baca semula** setiap fail sasaran sebelum menulisnya, kerana agent lain mungkin telah mengubahnya.
3. **Kalau projek aktif sudah bertukar** (folder kerja berbeza daripada "Projek aktif" dalam `session.md`): pindahkan baki, keputusan dan perangkap projek lama ke `projects/<projek-lama>.md` dahulu, kemudian tulis semula `session.md` untuk projek baru. `session.md` tidak pernah menyimpan lebih daripada satu projek.
4. Tulis ke fail yang betul:
   - `core/session.md`: **tulis semula** (bukan tambah) bahagian "Di mana kita berhenti", "Baki" dan "Jangan lupa", kemudian kemas kini baris `Dikemas kini` dengan masa dalam zon masa pengguna (`core/user.md`).
   - `projects/<nama-folder>.md`: tambah keputusan dan kemas kini baki. Kalau fail belum wujud, salin daripada `projects/_template.md`.
   - `core/user.md`: fakta kekal sahaja (keutamaan, peraturan, fokus baru), diringkaskan. Kemas kini baris sedia ada kalau fakta berubah. Jangan tulis log sesi di sini.
   - `core/identity.md`: ubah hanya kalau pengguna minta, atau setelah dia setuju dengan cadangan anda.
5. Kalau `core/session.md` melebihi 150 baris, atau `core/user.md` melebihi 250 baris, jalankan `compact.md`.
6. Kalau ada git, jalankan `git.md`.
7. Laporkan kepada pengguna dalam 2–4 baris: fail mana yang ditulis dan apa intipatinya.

## Langkah: fakta tunggal ("remember ...")
1. Tentukan rumah fakta itu: tentang pengguna → `user.md`; kemajuan/keputusan projek → `projects/<nama>.md`; **peraturan projek** (stack, arahan build, gaya kod) → `AGENTS.md` dalam folder projek (tunjuk teks dan minta izin dahulu, kerana fail itu dikongsi); tentang cara AI bercakap → `identity.md` (minta izin dahulu).
2. Tambah satu baris bertarikh. Kalau fakta lama bercanggah, gantikan fakta lama itu dan jangan simpan kedua-duanya.
3. Sahkan dengan satu ayat.

## Jangan
- Jangan salin perbualan bulat-bulat. Tulis intipati sahaja.
- Jangan simpan rahsia.
- Jangan pendua peraturan yang sudah ada dalam `AGENTS.md` / `CLAUDE.md` projek ke dalam Everkeep.
- Jangan padam fakta pengguna tanpa sebab yang jelas.
