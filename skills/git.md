# Kemahiran: git

**Dicetus oleh:** selesai `save`, `save diary`, `compact memory`, `log decision`; atau pengguna taip `commit memory` / `push memory`
**Skop:** **repo akar memori sahaja** (folder yang mengandungi `EVERKEEP.md`), tidak pernah repo projek lain

## Langkah
1. Pastikan akar memori ialah repo git. Kalau bukan, berhenti tanpa sebarang mesej.
2. Jalankan semua arahan dengan `git -C <akar memori> ...`, walau di mana pun folder kerja semasa.
3. Semak `status`. Kalau ada konflik atau keadaan pelik, beritahu pengguna dan jangan commit.
4. `add` fail yang ditukar mengikut nama. Jangan guna `add -A` membuta tuli.
5. Commit dengan mesej `memori: <ringkasan pendek> [nama-agent]`.
6. **Push hanya kalau pengguna minta** (`push memory`) atau sudah memberi izin tetap.
7. **Kalau push gagal** (cth. "Repository not found", 403, salah akaun): jangan cuba berulang kali. Laporkan ralat, semak akaun dalam `core/user.md` → "Akaun & alat", dan cadangkan tetapkan akaun pada remote (cth. `https://<akaun>@github.com/<akaun>/<repo>.git`). Commit tempatan kekal selamat.

## Banyak peranti
- **Pilihan A, satu memori merentas peranti:** satu repo private. Sebelum bangun, `git pull --rebase`; selepas simpan, commit + push. Jangan guna dua peranti serentak tanpa pull dahulu.
- **Pilihan B, memori berasingan setiap peranti:** setiap peranti ada repo sendiri. **Jangan pull/merge dari repo peranti lain**, kerana memori akan bercampur. Kongsi `skills/` sahaja, satu fail pada satu masa.
- Tanya pengguna pilihan mana semasa setup git, dan catat dalam `core/user.md` → "Akaun & alat".

## Jangan
- Jangan commit fail `.env` atau fail yang mengandungi rahsia.
- Jangan guna `--force`, `reset --hard` atau tulis semula sejarah tanpa izin jelas pengguna.
- Jangan push ke repo awam. Memori ini peribadi.
