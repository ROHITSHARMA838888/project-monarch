# 👑 Project Monarch

### The World's First AI-Native Custom ROM
**Device:** Poco F7 (onyx) | **Chipset:** Snapdragon 8s Gen 4 | **Base:** Pure AOSP (Android 17)

---

## 🧠 AI Engine
- **Model:** Google Gemma 4 E2B (INT4 Quantized)
- **Runtime:** On-Device NPU (Hexagon) — 100% Offline
- **Languages:** Hindi 🇮🇳 + English 🇬🇧
- **Speed:** ~30-35 tokens/sec | TTFT ~60ms

## 🎯 Key Features
- 🗣️ **Jarvis-Level Voice Assistant** — Continuous dialogue, full system voice control (Locks, settings, apps)
- 🔌 **Voice Power Actions with Security** — Shutdown/Restart via voice (even on lock screen) with verbal passcode verification
- ⚡ **Post-Boot Autonomous Jarvis Hook** — Auto-greets upon restart ("Sir, phone is ready, any task today?") and listens for commands
- 🔍 **Zero-Internet Knowledge Search** — Instant answers to queries completely offline using local LLM
- 🚫 **No Google Assistant Bloat** — Pure Minimal GApps (Play Store & Core Services only)
- 🔌 **Advanced Reboot Menu** — Direct reboot to Recovery (OrangeFox), Bootloader, Fastbootd & SystemUI
- 📱 **Always On Display (AOD) & Edge Lighting** — Custom AOD clocks, notification glow styles
- 🎨 **Monet Theme Engine** — Pitch Black AMOLED mode, granular chroma/luminance controls
- 🔐 **Voice Passkey Lock** — Unlock with your secret voice phrase & AI challenge question
- 🛡️ **Monarch Spoofing Hub** — TrickyStore, Keybox importer, 1-click online props fetcher, 90/120 FPS games unlock
- ⚡ **AI Performance Brain** — Auto game boost, smart battery management, aggressive night doze
- 📸 **MIUI Stock Camera** — Native Xiaomi camera quality with Leica filters

## 📦 Build Variants
| Variant | AI | Root Engine | Banking Compatibility |
|:---|:---|:---|:---|
| Standard | ✅ Gemma 4 E2B | ❌ Non-Rooted | 100% Out of the box |
| Power (KSU-Next) | ✅ Gemma 4 E2B | ⚡ KernelSU-Next + SuSFS | ✅ Stealth Mode (Bypasses Play Integrity & Root Check) |
| Power (Magisk) | ✅ Gemma 4 E2B | 🛠️ Magisk Zygisk | ✅ With DenyList / Shamiko |

## 🔒 Privacy Policy
- All AI processing happens ON-DEVICE
- ZERO data sent to any server
- NO telemetry, NO tracking

## 🏗️ Source Structure
```
project-monarch/
├── .github/workflows/    # GitHub Actions build scripts
├── local_manifests/      # AOSP device/vendor/kernel manifest
├── patches/              # Custom AOSP patches
├── packages/             # Custom apps (AI Assistant, Privacy Guard)
├── overlays/             # System UI customizations
└── scripts/              # Build helper scripts
```

---

> **Built with ❤️ by Rohit Sharma**
> 
> *"The first ROM where AI isn't just an app — it's the soul of the OS."*
