# Kemahiran

Setiap kemahiran ialah **satu fail markdown berisi langkah**. Mana-mana agent boleh membaca dan mengikutinya tanpa sistem plugin. Claude Code boleh juga memasang pembalut auto-cetus dalam `plugins/everkeep-skills/`.

| Fail | Dicetus oleh | Hasil |
|---|---|---|
| `save.md` | `save`, `remember ...` | Kemas kini `core/session.md`, projek dan pengguna |
| `diary.md` | `save diary` | Entri diari hari ini |
| `recall.md` | `do you remember ...`, `when did we ...` | Cari dalam diary/projek, cerita semula |
| `decision.md` | `log decision`, `why did we choose ...` | Log keputusan dalam fail projek |
| `compact.md` | `compact memory`, atau `session.md` melebihi 150 baris | Ringkaskan dan pindahkan butiran lama |
| `git.md` | selepas setiap save (kalau ada git), `commit memory`, `push memory` | Commit memori |
| `new-skill.md` | `new skill` | Cipta fail kemahiran baru |
| `init-project.md` | `init project` | Cipta `AGENTS.md` + `CLAUDE.md` (`@AGENTS.md`) dalam projek, dan fail projek Everkeep |

## Format fail kemahiran

```markdown
# Kemahiran: <nama>
**Dicetus oleh:** <frasa English standard> (frasa bahasa lain yang sama maksud juga diterima)
**Membaca:** <fail>   **Menulis:** <fail>

## Langkah
1. ...

## Jangan
- ...
```
