# Kemahiran: init project

**Dicetus oleh:** `init project`, `setup project`; atau tawarkan bila folder kerja ialah projek tanpa `AGENTS.md`
**Menulis:** `AGENTS.md` + `CLAUDE.md` dalam **folder projek**, `projects/<nama-folder>.md` dalam Everkeep

Tujuan: setiap projek ada **satu** fail peraturan (`AGENTS.md`) yang dibaca oleh semua agent. `CLAUDE.md` hanya mengandungi `@AGENTS.md` supaya Claude Code membaca fail yang sama.

> Kenapa `CLAUDE.md` masih perlu: Claude Code membaca `CLAUDE.md` dahulu dan hanya guna `AGENTS.md` sebagai sandaran bila tiada `CLAUDE.md`. Kalau `CLAUDE.md` wujud tanpa `@AGENTS.md`, `AGENTS.md` **diabaikan**. Butiran: `connectors/README.md` → "Claude: fail mana yang dibaca".

## Langkah
1. **Pastikan ini folder projek.** Jangan jalankan dalam folder home, akar Everkeep, atau folder sistem. Kalau ragu, tanya pengguna.
2. **Semak fail sedia ada** dalam folder projek: `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.cursorrules`, `.clinerules`.
3. **Ikut keadaan:**

   | Keadaan | Tindakan |
   |---|---|
   | Tiada `AGENTS.md`, tiada `CLAUDE.md` | Draf `AGENTS.md` (langkah 4), kemudian cipta `CLAUDE.md` berisi `@AGENTS.md` |
   | Ada `CLAUDE.md`, tiada `AGENTS.md` | Tawarkan: pindah isi `CLAUDE.md` ke `AGENTS.md`, kemudian `CLAUDE.md` jadi `@AGENTS.md`. Kalau pengguna tak setuju, biarkan |
   | Ada `AGENTS.md`, tiada `CLAUDE.md` | Cipta `CLAUDE.md` berisi `@AGENTS.md` |
   | Ada kedua-duanya | Semak `CLAUDE.md` merujuk `@AGENTS.md`. Kalau tidak, tunjuk perbezaan dan tanya pengguna. Jangan gabung tanpa izin |
   | Ada `.cursorrules` / `.clinerules` / `GEMINI.md` | Guna isinya sebagai bahan draf. Jangan padam fail itu |

4. **Draf `AGENTS.md`** dengan membaca projek (README, `package.json` / `composer.json` / `pyproject.toml`, struktur folder). Pendek, fakta sahaja:

   ```markdown
   # <Nama projek>

   <Satu ayat: apa projek ini>

   ## Stack
   - <bahasa, framework, hosting>

   ## Arahan
   - Install: `<...>`
   - Dev: `<...>`
   - Build / test: `<...>`

   ## Struktur
   - `<folder>/`: <fungsi>

   ## Peraturan
   - <gaya kod, perkara yang dilarang, akaun/deploy yang betul>
   ```

   Hanya tulis perkara yang disahkan daripada fail projek atau pengguna. Kalau tak pasti, tinggalkan `<...>` dan tanya.
5. **Tunjuk draf kepada pengguna** dan tunggu persetujuan sebelum menulis. Fail ini akan dikongsi dengan sesiapa yang membuka projek.
6. **Pilihan:** kalau pengguna guna Gemini CLI, tawarkan `GEMINI.md` berisi `@AGENTS.md`.
7. **Memori Everkeep:** kalau `projects/<nama-folder>.md` belum wujud, cipta daripada `projects/_template.md`. Isi **Folder, Peraturan projek (laluan `AGENTS.md`) dan Status sahaja**. Jangan salin apa-apa dari `AGENTS.md` (apa projek, stack, arahan, peraturan) dan jangan catat "AGENTS.md dicipta" sebagai keputusan.
8. Laporkan fail yang dicipta. **Jangan commit repo projek** melainkan pengguna minta. Repo Everkeep boleh di-commit melalui `git.md`.

## Jangan
- Jangan masukkan maklumat peribadi, memori Everkeep, rahsia atau kunci API ke dalam `AGENTS.md` projek.
- Jangan tulis ganti `AGENTS.md` atau `CLAUDE.md` sedia ada tanpa izin.
