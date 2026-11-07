# 🎮 Monarch Game Turbo & Space Engine

### Deep System & Kernel-Level Gaming Optimization for Poco F7 (onyx)

---

## 🚀 Overview
Monarch Game Turbo is an integrated system-level gaming framework directly hooked into the Snapdragon 8s Gen 4 (sm8735) kernel governors, Adreno GPU drivers, and custom SystemUI overlays.

---

## ⚡ Dual Performance Modes (Direct Kernel Switching)

### 1. 🔥 Ultimate Performance (Beast Mode)
- **CPU Governor:** Switches big & prime cores to `performance` / custom `schedutil_burst`
- **GPU Clocks:** Locked to maximum boost frequency (900MHz+)
- **FPS Cap:** 90 FPS & 120 FPS unlocked across all supported titles (BGMI, COD, Genshin, PUBG)
- **Touch Sampling:** Overclocked to **480Hz** for instantaneous touch response
- **Thermal Throttling:** Raised safety threshold to prevent sudden frame drops during intense teamfights
- **Network Tunneling:** High-priority packet routing (DSCP QoS) to eliminate ping spikes

### 2. ⚖️ Balanced Mode (Smart Daily Gaming)
- **CPU Governor:** AI-optimized dynamic scaling (powers up only during heavy render passes)
- **Battery Optimization:** Up to **30% power savings** on menu screens and lobby wait times
- **Touch Sampling:** Dynamic 240Hz / 360Hz
- **Thermals:** Strict cool-to-touch profile for long endurance sessions

---

## 📱 In-Game Floating Sidebar HUD
- **Trigger:** Edge swipe from top-left or top-right bezel during any registered game.
- **Visuals:** High-tech Cyberpunk Monarch HUD with glowing neon telemetry.
- **Live Stats:**
  - Real-time FPS Counter (hardware-accurate)
  - CPU & GPU Load percentage
  - Battery temperature (°C)
  - Current Ping (ms)
- **Quick Controls:**
  - One-tap Mode Switcher: **[ Balanced ] ⟷ [ Ultimate Beast ]**
  - Do Not Disturb (Blocks heads-up calls and notifications)
  - Mistouch Prevention (Locks gesture bar / home bar)
  - Screen Recording (Internal audio 60fps lossless)
  - Voice Changer hook for in-game squad chat

---

## 🧠 AI Integration (Monarch Core)
- The on-device **Gemma 4 E2B AI Core** continuously analyzes gameplay frame pacing.
- If micro-stutters or frame drops are detected, it proactively alerts the kernel scheduler to allocate more power to the render thread before lag is felt.
