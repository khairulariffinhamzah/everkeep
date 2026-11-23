# everkeep-skills (Claude Code sahaja, pilihan)

Pembalut nipis yang membolehkan Claude Code mencetus kemahiran Everkeep secara automatik. Setiap pembalut hanya menunjuk ke `skills/<nama>.md`, jadi logiknya kekal di satu tempat dan dikongsi bersama semua agent.

Agent lain tidak memerlukan plugin ini. Mereka terus mengikut jadual "Kata kunci" dalam `EVERKEEP.md`.

## Pasang
```bash
claude plugin marketplace add <laluan akar memori>
claude plugin install everkeep-skills@everkeep --scope user
```
