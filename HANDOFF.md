# Project Monarch: Codex Handoff & Architecture Blueprint

**Target Device:** POCO F7 (`onyx`)  
**Chipset:** Qualcomm Snapdragon 8s Gen 4 (`SM8735` / `sun` architecture)  
**Target OS:** Pure Google AOSP (Android 15 / 17 platform baseline)  
**Author / Maintainer:** Rohit Sharma (`ROHITSHARMA838888`)  
**Repository:** `https://github.com/ROHITSHARMA838888/project-monarch`

---

## 1. Absolute Constraints & User Directives
1. **Strictly 100% Pure AOSP:**
   - The user has **explicitly rejected** LineageOS as a base.
   - The final OS must be a pure Google AOSP build with no `vendor/lineage` branding, bloat, or Lineage proprietary SDK dependencies.
   - The product lunch combo must be `aosp_onyx-userdebug` (or `aosp_onyx-user`).
2. **Strictly ₹0 Cost Policy:**
   - The user cannot spend any money on paid cloud compute.
   - Avoid services requiring post-pay billing or credit-card consumption.
   - Must build using **free GitHub Actions runners** (or free Oracle Cloud Ampere A1 if user sets it up).
   - Standard GitHub runner limits: 2-core / 4-core, 7 GB RAM, ~75 GB disk.
   - All builds must respect disk limits by using:
     - Aggressive runner bloatware cleaning (`/usr/share/dotnet`, `/usr/local/lib/android`, `/opt/ghc`, docker images).
     - 10–12 GB swap file to prevent OOM linking errors.
     - `repo init --depth=1 --no-clone-bundle --no-tags --current-branch`.
     - Modular / incremental builds with compressed `ccache` (capped under 9 GB to fit within GitHub Actions 10 GB cache quota).
3. **Repository Privacy:**
   - The repository must remain **PRIVATE** by default. Any temporary visibility toggle for CI must be reverted immediately.

---

## 2. Completed & Verified Artifacts

### ✅ Standalone Kernel with KernelSU-Next (Fully Built & Verified)
- **Status:** **SUCCESS** in GitHub Actions [Run #42334462578](https://github.com/ROHITSHARMA838888/project-monarch/actions/runs/42334462578) (branch `codex/fix-kernel-certificate-build`).
- **Artifact:** `Monarch-kernel-onyx-ksu-next.zip`
- **Contents:**
  - `Image` (compiled with LLVM/Clang for `aarch64`, GKI 2.0 compliant).
  - Pinned KernelSU-Next (`KSU_SHA: 4c706b5938665866ebe16944a481a7b91e3396af`).
  - SuSFS stealth hooks enabled.
  - AnyKernel3 flashable installer (`installer/anykernel.sh`).
  - `kernel.config` and `vmlinux.symvers` provenance generated and verified.
- **Critical Fix Applied:**
  - `scripts/fix_extract_cert.py` patched OpenSSL 3.0 `key_pass` compiler error on Ubuntu 24.04 runners.

---

## 3. Current ROM Status & Audit Findings

### Codex Audit Summary (PR #2 / `scripts/audit_rom.py`):
1. **Device Tree Legacy Dependencies:**
   - The device tree in `xiaomi-onyx-dev/android_device_xiaomi_onyx` inherits `vendor/lineage/config/common_full_phone.mk`.
   - In pure AOSP, this inheritance causes lunch / build breakage because `vendor/lineage` is absent.
2. **Missing AOSP Product Definition:**
   - Device requires a clean `aosp_onyx.mk` inheriting from:
     ```makefile
     $(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit.mk)
     $(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)
     ```
   - Must define:
     ```makefile
     PRODUCT_NAME := aosp_onyx
     PRODUCT_DEVICE := onyx
     PRODUCT_BRAND := Xiaomi
     PRODUCT_MODEL := POCO F7
     PRODUCT_MANUFACTURER := Xiaomi
     ```
3. **Hardware HAL & Vendor Integration:**
   - Qualcomm Display, Audio, USB, Telephony, and Camera HALs must map to pure AOSP HIDL/AIDL interfaces.
   - Proprietary vendor blobs must be linked from `xiaomi-onyx-dev/proprietary_vendor_xiaomi_onyx` into `vendor/xiaomi/onyx`.

---

## 4. Project Monarch Custom Components

### A. Monarch Game Turbo / Game Space
- **Spec:** [packages/MonarchGameSpace.md](file:///c:/Users/HC-CLUBB/Desktop/project%20rohit's%20toolkit/project-monarch/packages/MonarchGameSpace.md)
- **Features:**
  - Cyberpunk floating sidebar HUD overlay in games (FPS, CPU/GPU clock, temperature, battery drain).
  - **Dual Performance Engine:**
    - `Ultimate Beast Mode`: Max CPU/GPU governor clocks, touch booster 480Hz, thermal throttle delay, 90/120 FPS unlock.
    - `Balanced Mode`: Standard Qualcomm energy-aware scheduling (EAS).
  - Background call banner, notification mute, network priority packet tagging.
  - Target Path: `/system_ext/priv-app/MonarchGameSpace`

### B. Monarch AI Assistant (Offline Voice Core)
- **Spec & Source:** `packages/apps/MonarchAssistant/`
- **Architecture:**
  - Engine: On-device **Gemma 2 (2B)** quantized to 4-bit (~1.5 GB).
  - Inference: MediaPipe LLM Inference API / ExecuTorch utilizing Snapdragon 8s Gen 4 NPU / Hexagon DSP.
  - Languages: Hindi + English (Natural speech & Indian accent support).
  - Capabilities: 100% offline device control via voice:
    - "Switch to Beast Mode" -> Triggers Game Turbo performance profile.
    - "Flashlight on", "Turn off Wi-Fi", battery health analysis.
    - Protected system commands gated by biometric/passcode confirmation.
  - Target Path: `/system_ext/priv-app/MonarchAssistant`

---

## 5. Immediate Action Plan for Codex

1. **AOSP Port Foundation (PR #2):**
   - Review and merge PR #2 (`codex/aosp-port-foundation`).
   - Create `aosp_onyx.mk` and decouple device tree from `vendor/lineage`.
2. **Minimal Manifest Setup:**
   - Update `local_manifests/roomservice.xml` to include pure Qualcomm / QSSI HAL repos and Xiaomi onyx trees.
3. **Modular GitHub Actions Build (`.github/workflows/build.yml`):**
   - Implement shallow tree sync (`--depth=1`).
   - Enable 12GB swap (`/swapfile`) and strict memory quotas (`_JAVA_OPTIONS=-Xmx4g`, `NINJA_ARGS=-j4`).
   - Package prebuilt kernel from Run #42334462578 directly into `device/xiaomi/onyx/prebuilt/Image` to save compile time.
   - Run compilation to produce `Project-Monarch-onyx-OFFICIAL.zip`.
