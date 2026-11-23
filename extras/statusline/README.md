# Status line Everkeep (Claude Code sahaja, pilihan)

Satu baris di bawah kotak input Claude Code:

```
🔒 Mira · 💾 12m ago · session 34/150 · diary ✓ · ⬆ 2  |  Sonnet 5.5 · 📁 kedai-kek · ctx 41% · ⎇ main*3 · $0.42
```

| Bahagian | Maksud |
|---|---|
| `🔒 Mira` | AI teman sudah bangun dalam sesi ini (hanya muncul selepas anda panggil namanya) |
| `💾 12m ago` | Kali terakhir `core/session.md` disimpan. Hijau < 1 jam, kuning < 6 jam, merah selepas itu: masa untuk `save` |
| `session 34/150` | Saiz `core/session.md`. Kuning > 80 baris, merah > 150: masa untuk `compact memory` |
| `diary ✓` / `diary –` | Ada / tiada entri diari hari ini |
| `⬆ 2` | Fail memori yang belum di-commit (kalau folder memori ialah repo git): masa untuk `commit memory` |
| `ctx 41%` | Penggunaan konteks. Hijau < 50%, kuning < 80%, merah selepas itu |
| `⎇ main*3` | Branch git projek semasa dan bilangan fail yang berubah |

Sebelum AI dipanggil, hanya bahagian kanan (model, folder, konteks, branch, kos) dipaparkan.

## Pasang

Perlukan Python 3.

```bash
python extras/statusline/install.py
```

- Skrip menambah `statusLine` ke `~/.claude/settings.json` dan simpan sandaran `settings.json.bak-everkeep`.
- Kalau anda sudah ada status line lain, skrip **tidak** menggantinya. Guna `--force` kalau memang mahu ganti.
- Buang: `python extras/statusline/install.py --remove`

Selepas memindahkan folder Everkeep, jalankan `install.py` sekali lagi supaya laluan dikemas kini.
