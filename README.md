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
- 🗣️ **Jarvis-Level Voice Assistant** — Continuous dialogue, full system control
- 🔐 **Voice Passkey Lock** — Unlock with your secret voice phrase
- 🛡️ **AI Privacy Guard** — Real-time app monitoring, zero data leakage
- ⚡ **AI Performance Brain** — Auto game boost, smart battery management
- 📅 **Smart Scheduler** — Voice-activated task automation
- 🌐 **Offline Live Translator** — Hindi/English on-screen translation
- 📸 **AI Photo/Video Editor** — On-device background removal, noise reduction

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
