# Setup Everkeep (wizard dijalankan oleh agent anda)

*Pengguna: buka folder ini dalam coding agent anda dan taip **`setup`**. Agent akan menjalankan langkah di bawah.*

---

## Arahan untuk agent

Jalankan langkah ini satu demi satu. Tanya pengguna satu soalan pada satu masa.

### Langkah 1: Soal jawab

1. Apa nama AI teman anda? (contoh: Mira, Jarvis, Luna). Nama ini juga menjadi **kata panggilan**.
2. Nama anda, atau nama yang anda mahu dipanggil?
3. Gaya hubungan? (contoh: coding partner and friendly assistant / mentor / pembantu profesional / kawan santai)
4. Bahasa perbualan? (BM / English / campur)
5. Zon masa? (cth. Asia/Kuala_Lumpur). Kesan daripada sistem dan minta pengguna sahkan sahaja.

### Langkah 2: Isi placeholder

Gantikan placeholder dalam **semua** fail `.md` dan `.json`, kecuali folder `_dev/`. **Kecuali `{{MEMORY_ROOT}}`:** biarkan ia dalam `connectors/CONNECTOR.md` dan isi hanya dalam salinan yang ditambah ke fail arahan global agent (Langkah 4). Dengan cara ini folder memori boleh dibawa ke komputer lain tanpa laluan yang putus.

| Placeholder | Nilai |
|---|---|
| `{{AI_NAME}}` | jawapan 1 |
| `{{USER_NAME}}` | jawapan 2 |
| `{{RELATIONSHIP_STYLE}}` | jawapan 3 |
| `{{SETUP_DATE}}` | tarikh hari ini, `YYYY-MM-DD`, **daripada sistem** (lihat nota di bawah) |
| `{{MEMORY_ROOT}}` | laluan penuh folder ini **di komputer ini**, dengan `/` (cth. `C:/Everkeep` atau `/home/ali/everkeep`). Hanya dalam blok penyambung |

**Tarikh dan masa:** dapatkan daripada sistem (cth. `date` atau PowerShell `Get-Date`) dalam zon masa pengguna. Jangan meneka daripada ingatan model, kerana model selalu tersilap hari.

Selepas itu, semak dengan carian `{{` untuk memastikan tiada placeholder yang tertinggal (kecuali `{{MEMORY_ROOT}}` dalam `connectors/CONNECTOR.md`, serta `SETUP.md` dan `_dev/`).

Isi juga bahagian `<...>` dalam `core/identity.md` (bahasa, suara) dan `core/user.md` (bahasa, zon masa, bidang) berdasarkan jawapan. Kalau pengguna tidak menjawab sesuatu, biarkan `<...>` kosong. Jangan reka.

### Langkah 3: Rekod setup

Cipta `diary/YYYY-MM-DD.md` dengan entri pertama. Tarikh dan masa daripada sistem; `[nama-agent]` ialah nama agent yang menjalankan setup (cth. `[claude-code]`, `[opencode]`), bukan nama AI teman:

```markdown
# Diari YYYY-MM-DD

### HH:MM [nama-agent] Setup
**Apa berlaku:** <nama AI> dilahirkan. Pengguna: <nama>. Gaya: <gaya>. Akar memori: <laluan>.
**Seterusnya:** sambungkan agent dan uji panggilan.
```

### Langkah 4: Sambungkan ke agent

1. Tunjukkan jadual dalam `connectors/README.md` dan tanya agent mana yang pengguna guna.
2. Untuk setiap agent yang dipilih:
   - Kalau fail arahan global itu wujud, **buat salinan sandaran** (`<fail>.bak-everkeep`).
   - Tunjukkan teks yang akan ditambah, dan tunggu pengguna setuju.
   - **Tambah** blok dari `connectors/CONNECTOR.md` di hujung fail, dengan `{{MEMORY_ROOT}}` diganti laluan folder ini di komputer ini. Jangan tulis ganti kandungan sedia ada.
   - Kalau blok `<!-- everkeep:start -->` sudah ada, kemas kini blok itu sahaja.
3. Untuk agent yang hanya ada kotak "Custom Instructions", beri teks itu kepada pengguna untuk ditampal sendiri.
4. **Claude Code (pilihan):** tawarkan pemasangan plugin `everkeep-skills`, iaitu pembalut auto-cetus untuk kemahiran (lihat `plugins/everkeep-skills/README.md`).
5. **Claude Code (pilihan):** tawarkan status line yang menunjukkan bila kali terakhir `save`, saiz sesi dan diari hari ini (lihat `extras/statusline/README.md`). Pasang dengan `python extras/statusline/install.py`. Kalau pengguna sudah ada status line lain, tanya dahulu sebelum guna `--force`.

### Langkah 5: Git (pilihan, disyorkan)

Tanya: "Mahu simpan sejarah memori dengan git? Ia boleh undur kalau ada fail yang rosak."
Kalau setuju, jalankan `git init` dan buat commit pertama. **Kalau folder ini di-clone daripada repo templat Everkeep yang awam**, buang atau tukar `origin` (`git remote remove origin`) sebelum apa-apa push, supaya memori peribadi tidak dihantar ke repo awam. Repo GitHub **mesti private** kalau pengguna mahu backup ke awan. Kalau pengguna guna lebih dari satu komputer, terangkan pilihan dalam `skills/git.md` → "Banyak peranti" dan catat pilihannya.

### Langkah 6: Uji

Minta pengguna buka sesi baru dalam agent yang sudah disambung, dari folder lain, dan taip nama AI.
Ujian berjaya kalau AI menyapa pengguna dengan namanya.

Akhir sekali, tambah baris `SETUP SELESAI: YYYY-MM-DD` di bahagian atas fail ini supaya setup tidak dijalankan dua kali.

---

## Komputer tambahan (memori sedia ada)

Pengguna sudah ada memori Everkeep dan mahu gunanya di komputer lain:

1. Dapatkan folder memori di komputer baru: `git clone <repo private pengguna>` (disyorkan), atau salin folder. **Satu salinan sahaja di setiap komputer.**
2. Buka folder itu dalam agent dan taip `setup`. Agent nampak `SETUP SELESAI` di atas fail ini, jadi:
   - **Jangan** tanya soalan Langkah 1 atau tulis semula `core/`.
   - Jalankan **Langkah 4 sahaja** (sambungkan agent), dengan `{{MEMORY_ROOT}}` = laluan folder di komputer ini.
   - Pilihan: status line dan plugin Claude Code.
3. Ikut `skills/git.md` → "Banyak peranti": `git pull --rebase` sebelum mula kerja, commit + push selepas `save`.
4. Uji: buka sesi baru dari folder lain dan panggil nama AI.

## Selepas setup

Senarai kemahiran ada dalam `skills/README.md`. Untuk menambah kemahiran sendiri, taip `new skill`.
