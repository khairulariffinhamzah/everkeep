# Kemahiran: diari

**Dicetus oleh:** `save diary`, `write diary`; atau di hujung sesi yang panjang dan penting (tawarkan dahulu)
**Membaca:** `diary/YYYY-MM-DD.md` hari ini   **Menulis:** fail yang sama (tambah sahaja)

## Langkah
1. Dapatkan tarikh dan masa sebenar daripada sistem, dalam zon masa pengguna (`core/user.md`). Jangan meneka.
2. Buka `diary/YYYY-MM-DD.md`. Kalau belum wujud, cipta fail itu dengan tajuk `# Diari YYYY-MM-DD`.
3. **Tambah** entri di hujung fail:

   ```markdown
   ### HH:MM [nama-agent] <projek atau topik>
   **Apa berlaku:** <2–5 baris>
   **Keputusan:** <kalau ada>
   **Belajar tentang {{USER_NAME}}:** <kalau ada>
   **Seterusnya:** <1–3 perkara>
   ```

4. Kalau hari ini hari pertama bulan baru, pindahkan fail diari bulan lepas ke `diary/archive/YYYY-MM/`.
5. Kalau ada git, jalankan `git.md`.

## Jangan
- Jangan sunting entri lama, termasuk entri yang ditulis oleh agent lain.
- Jangan tulis perkara sensitif yang pengguna tidak mahu direkodkan.
