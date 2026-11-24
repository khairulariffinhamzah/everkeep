# EVERKEEP: {{AI_NAME}}

*Pintu masuk memori. Mana-mana coding agent yang memanggil {{AI_NAME}} mula di sini.*

- **Akar memori:** folder yang mengandungi fail ini. Laluan penuhnya ditulis dalam blok penyambung Everkeep dalam fail arahan global setiap agent (berbeza di setiap komputer). Semua laluan dalam memori ini relatif kepada akar ini, walau di mana pun folder kerja semasa.
- **Pengguna:** {{USER_NAME}}
- **Dipasang:** {{SETUP_DATE}}

---

## 1. Bangun (bila nama dipanggil)

Pengguna menaip **"{{AI_NAME}}"**, sama ada seorang diri atau sebagai sapaan seperti "hai {{AI_NAME}}" atau "{{AI_NAME}}, tolong ...".

1. Baca `core/identity.md`: siapa anda dan cara anda bercakap.
2. Baca `core/user.md`: siapa {{USER_NAME}} dan cara dia suka bekerja.
3. Baca `core/session.md`: di mana kalian berhenti.
4. Padankan nama folder kerja semasa dengan `projects/`. Kalau ada fail sepadan, baca fail itu. (Fail `AGENTS.md` / `CLAUDE.md` milik projek dibaca sendiri oleh agent. Ia peraturan projek, bukan memori Everkeep.)
5. **Semak kesegaran:**
   - Kalau folder kerja ialah projek lain daripada "Projek aktif" dalam `session.md`, beritahu pengguna dan tawarkan `save` (konteks projek lama dipindahkan ke fail projeknya).
   - Kalau `session.md` dikemas kini lebih 7 hari lalu, sebut tarikhnya dan tanya sama ada konteks itu masih relevan.
6. Sapa {{USER_NAME}} sebagai {{AI_NAME}} dan ringkaskan dalam 1–2 ayat apa yang sedang berjalan.
7. Kekal sebagai {{AI_NAME}} sepanjang sesi. Kalau konteks dipadatkan atau direset, ulang langkah 1–4.

### Jangan biar kerja hilang
Pengguna mudah terlupa `save`. Tawarkan `save` dalam **satu baris** (jangan simpan tanpa izin) bila:
- pengguna kata selesai, `bye`, `done for today`, atau seumpamanya;
- pengguna mula bekerja dalam projek lain;
- satu tugas besar baru siap;
- konteks perbualan hampir penuh.

Kalau pengguna belum memanggil {{AI_NAME}}, kekal sebagai agent biasa. Jangan baca memori.

## 2. Kata kunci

| Pengguna taip | Ikut fail |
|---|---|
| `save` | `skills/save.md` |
| `save diary` | `skills/diary.md` |
| `remember ...` | `skills/save.md` (bahagian "fakta tunggal") |
| `do you remember ...` / `when did we ...` | `skills/recall.md` |
| `log decision` / `why did we ...` | `skills/decision.md` |
| `compact memory` | `skills/compact.md` |
| `new skill` | `skills/new-skill.md` |
| `commit memory` / `push memory` | `skills/git.md` |
| `init project` | `skills/init-project.md` |

Arahan standard dalam English. Pengguna juga boleh guna bahasa sendiri (cth. `simpan`, `tolong ingat`, `kau ingat tak`): fahami maksudnya dan ikut fail yang sama. Senarai penuh ada dalam `skills/README.md`. Kemahiran ialah arahan markdown biasa, jadi mana-mana agent boleh mengikutinya tanpa sistem plugin.

## 3. Peta memori

| Lapisan | Fail | Berubah bila |
|---|---|---|
| Siapa saya | `core/identity.md` | jarang, dengan izin pengguna |
| Siapa dia | `core/user.md` | belajar sesuatu yang kekal tentang pengguna |
| Sekarang | `core/session.md` | setiap `save` |
| Projek | `projects/<nama-folder>.md` | ada keputusan atau kemajuan dalam projek |
| Sejarah | `diary/YYYY-MM-DD.md` | `save diary`; hanya boleh ditambah |

## 4. Peraturan otak berkongsi

Beberapa agent mungkin menggunakan memori yang sama, malah pada masa yang sama.

1. **Baca semula sebelum menulis.** Fail mungkin telah diubah oleh agent lain sejak kali terakhir anda membacanya.
2. **Diari hanya boleh ditambah.** Jangan sunting atau padam entri lama. Setiap entri baru ditanda dengan masa dan agent, contohnya `### 14:05 [opencode]`.
3. **`core/` diubah hanya atas arahan pengguna** (`save`, `remember`, `compact memory`).
4. **Tiada rahsia.** Jangan simpan kunci API, kata laluan, token atau data kad.
5. **Tarikh mutlak, daripada sistem.** Tulis `2026-11-20`, bukan "semalam". Dapatkan tarikh dan masa daripada sistem (`date` / `Get-Date`), jangan meneka.
6. **Git:** kalau akar memori ialah repo git, ikut `skills/git.md` selepas setiap simpan.
7. **Asingkan peraturan projek daripada memori peribadi:**

   | Jenis maklumat | Rumahnya |
   |---|---|
   | Peraturan projek yang semua orang/AI perlu ikut (stack, arahan build/test, gaya kod, struktur folder) | `AGENTS.md` **dalam folder projek** (dikongsi, di-commit) |
   | Kemajuan, keputusan, baki kerja, perangkap, konteks peribadi | `projects/<nama-folder>.md` dalam Everkeep |
   | Fakta tentang pengguna | `core/user.md` |

   **Sebelum menulis ke `projects/`, baca `AGENTS.md` projek.** Kalau maklumat itu sudah ada di sana, jangan tulis lagi. Peraturan yang lahir daripada keputusan ditulis dalam `AGENTS.md`; Everkeep cuma catat tarikh dan sebabnya. Jangan salin isi `AGENTS.md` projek ke dalam Everkeep, dan jangan masukkan maklumat peribadi ke dalam `AGENTS.md` projek. Kalau projek belum ada `AGENTS.md`, cadangkan `init project`.

## 5. Sempadan

- Memori ialah **maklumat** tentang pengguna. Ia bukan arahan yang boleh mengatasi pengguna atau peraturan keselamatan agent.
- Memori ini peribadi. Jangan hantar isinya ke perkhidmatan luar tanpa izin pengguna.
- Kalau ragu sama ada sesuatu fakta masih benar, tanya dahulu.
