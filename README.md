# 🔒 Everkeep

**Memori jangka panjang untuk AI teman anda, di mana-mana coding agent.**

> *Ever* + *keep*: disimpan selamanya. **One memory, every coding agent.**
> Pengalaman harian (`session`) direkod dalam `diary`, dan yang penting disimpan kekal dalam `core`.

AI coding agent lupa segalanya bila sesi tamat. Setiap agent juga ada memori sendiri yang tidak dikongsi. Everkeep memberi anda **satu otak** dalam bentuk folder fail markdown biasa. Mana-mana agent boleh memanggil otak itu dengan satu perkataan, iaitu nama AI teman anda.

```
Claude Code ─┐
OpenCode    ─┤
Antigravity ─┼──►  📁 Everkeep  (identity · user · session · projects · diary)
Cline / Roo ─┤
Aider / ... ─┘
```

## Kenapa Everkeep

- **Satu otak, banyak agent.** Mula kerja di Claude Code, sambung di OpenCode, dan AI anda tetap ingat.
- **Tanpa server, tanpa database.** Hanya fail `.md` yang boleh anda baca dan edit sendiri.
- **Tidak bergantung pada model.** Ia berfungsi dengan Claude, Gemini, GPT atau mana-mana model melalui kunci API anda sendiri.
- **Nama anda pilih sendiri.** Everkeep ialah enjinnya, manakala identiti teman AI anda tentukan sendiri.
- **Setup tanpa coding.** Agent anda sendiri yang memandu setup melalui soal jawab.

## Mula dalam 3 langkah

1. Clone atau salin folder ini ke tempat tetap, contohnya `C:\Everkeep` atau `~/everkeep`. **Gunakan satu salinan sahaja.**
2. Buka folder itu dalam coding agent anda dan taip: **`setup`**
3. Jawab beberapa soalan. Selepas itu, buka sesi baru di mana-mana agent dan taip nama AI anda.

> ⚠️ **Memori anda peribadi.** Kalau anda `git clone` templat ini, jangan push memori ke repo awam. Setup akan membantu anda tukar ke repo **private** sendiri.

## Arahan harian

| Taip | Hasil |
|---|---|
| `<nama AI>` / `hi <nama AI>` | AI muat memori dan sambung dari tempat anda berhenti |
| `save` | Simpan progres sesi dan projek |
| `save diary` | Tulis entri diari hari ini |
| `remember ...` | Simpan satu fakta kekal |
| `do you remember ...` | Cari dalam diari dan projek lama |
| `log decision` | Log keputusan dan sebabnya dalam fail projek |
| `compact memory` | Padatkan memori yang terlalu panjang |
| `new skill` | Cipta kemahiran sendiri |
| `commit memory` / `push memory` | Simpan sejarah memori dalam git |
| `init project` | Sediakan `AGENTS.md` + `CLAUDE.md` dalam projek, supaya semua agent baca peraturan yang sama |

Arahan dalam bahasa lain pun difahami (cth. `simpan`, `tolong ingat`), tapi frasa English di atas ialah standard.

## Struktur

```
EVERKEEP.md             pintu masuk: bangun, kata kunci, peraturan otak berkongsi
AGENTS.md / CLAUDE.md   arahan bila agent dibuka dalam folder memori ini
SETUP.md                wizard persediaan (dijalankan oleh agent)
LICENSE                 MIT
core/
  identity.md           siapa AI ini
  user.md               siapa anda dan cara anda bekerja
  session.md            memori kerja: di mana kita berhenti
projects/               satu fail untuk setiap projek (dipadankan dengan nama folder)
diary/                  diari harian, hanya boleh ditambah (archive/ untuk bulan lepas)
skills/                 kemahiran dalam markdown biasa, boleh diikut oleh semua agent
plugins/everkeep-skills/ pembalut auto-cetus untuk Claude Code (pilihan)
connectors/             blok sambungan + lokasi fail arahan untuk setiap agent
extras/statusline/      status line Claude Code: nama AI, bila save, saiz sesi (pilihan)
```

## Lesen

MIT. Lihat `LICENSE`.
