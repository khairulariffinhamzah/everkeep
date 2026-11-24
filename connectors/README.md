# Penyambung: tempat letak teks `CONNECTOR.md` untuk setiap agent

Setiap agent ada fail arahan global sendiri. Tambah blok dalam `CONNECTOR.md` di hujung fail itu. Jangan tulis ganti kandungan sedia ada.

> ⚠️ **Status: belum disahkan.** Laluan di bawah ditulis berdasarkan ingatan dan mesti diuji pada versi terkini setiap agent sebelum dikeluarkan. Agent selalu menukar laluan ini.

| Agent | Fail arahan global (anggaran) | Status |
|---|---|---|
| Claude Code (CLI, VS Code, JetBrains) | `~/.claude/CLAUDE.md` | ✅ terbukti |
| Claude Desktop: tab **Code** | `~/.claude/CLAUDE.md`, fail sama dengan Claude Code | ⏳ sepatutnya jalan, perlu diuji |
| Claude Desktop: tab **Cowork** | memori Cowork sendiri (lihat bahagian Claude di bawah) | ⏳ perlu diuji |
| Claude Desktop / claude.ai: tab **Chat** | arahan Project atau tetapan peribadi + connector sistem fail | ⚠️ terhad, lihat di bawah |
| OpenCode | `~/.config/opencode/AGENTS.md` | ✅ terbukti (setup + panggilan, Nov 2026) |
| Antigravity | `~/.gemini/GEMINI.md` (Global Rules) | ✅ terbukti (panggilan, Nov 2026) |
| Gemini CLI | `~/.gemini/GEMINI.md`, fail sama dengan Antigravity | ⚠️ akaun individu percuma ditolak Google ("IneligibleTierError", Nov 2026): guna Antigravity |
| Codex CLI | `~/.codex/AGENTS.md` | ⏳ perlu diuji |
| Cline | folder Global Rules (dalam tetapan Cline) | ⏳ perlu diuji |
| Roo Code / Kilo Code | `~/.roo/rules/` / `~/.kilocode/rules/` | ⏳ perlu diuji |
| Aider | `~/.aider.conf.yml` → `read: [<akar memori>/connectors/CONNECTOR.md]` (salinan yang sudah diisi) | ⏳ perlu diuji |
| Agent lain | kotak "Custom Instructions" / "System Prompt" dalam tetapan | tampal manual |

**WSL:** guna folder Windows yang sama melalui `/mnt/c/...` (cth. `/mnt/c/Everkeep`). Jangan buat salinan kedua dalam Linux. Dalam blok penyambung, tulis kedua-dua laluan kalau pengguna guna Windows dan WSL.

`~` = folder pengguna (Windows: `C:\Users\<nama>`). Di Windows, kebanyakan agent guna `C:\Users\<nama>\.claude`, `C:\Users\<nama>\.gemini` dan seterusnya.

## Claude: fail mana yang dibaca

### Claude Code (CLI, IDE, tab Code dalam Claude Desktop)
Untuk peraturan **projek**, Claude Code membaca:
1. `CLAUDE.md` (fail utama; juga dicari ke atas dalam folder induk)
2. `AGENTS.md`, **hanya sebagai sandaran** bila tiada `CLAUDE.md` (sejak v2.1.277, boleh ditukar dalam `/config` → "Project instructions")

Sebab itu `init project` sentiasa cipta `CLAUDE.md` berisi `@AGENTS.md`:
- Versi lama, sesi pertama selepas install/upgrade, dan sesetengah pemasangan (Bedrock, Vertex, gateway) hanya membaca `CLAUDE.md`.
- **Kalau `CLAUDE.md` wujud tetapi tidak merujuk `@AGENTS.md`, `AGENTS.md` diabaikan.**
- Import tidak menyebabkan `AGENTS.md` dibaca dua kali.

Untuk **Everkeep**, blok penyambung diletak dalam `~/.claude/CLAUDE.md` (global), jadi AI teman boleh dipanggil dari mana-mana folder. Tab Code dalam Claude Desktop berkongsi tetapan yang sama dengan CLI.

### Claude Desktop: tab Cowork
Cowork ada folder memori sendiri dengan `CLAUDE.md` berasingan, bukan `~/.claude/CLAUDE.md`. Cadangan (belum diuji): tampal blok `CONNECTOR.md` dalam memori/arahan Cowork, dan beri Cowork akses ke folder Everkeep.

### Claude Desktop / claude.ai: tab Chat
Chat tidak membaca fail dalam komputer secara automatik. Everkeep hanya boleh berfungsi kalau:
1. Connector sistem fail (MCP) dipasang dan diberi akses ke folder Everkeep, **dan**
2. Blok `CONNECTOR.md` ditampal dalam arahan Project atau tetapan peribadi.

Kalau tidak, gunakan tab Code atau Claude Code untuk kerja yang memerlukan memori Everkeep.

## Nota

- **Agent dengan kunci API sendiri** (Cline, Roo, Kilo, Aider, OpenCode dan lain-lain): Everkeep tidak bergantung pada model. Selagi model boleh baca dan tulis fail melalui agent, memori berfungsi.
- **Model kecil atau murah** mungkin terlepas langkah dalam protokol. Kalau itu berlaku, sebut terus: "{{AI_NAME}}, baca EVERKEEP.md".
- Penanda `<!-- everkeep:start -->` / `<!-- everkeep:end -->` membolehkan setup dan skrip kemas kini mencari blok ini tanpa menyentuh kandungan lain.
