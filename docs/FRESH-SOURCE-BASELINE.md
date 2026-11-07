# Fresh Android 17 source investigation — 2026-11-07

## User direction

Android 17 platform from Google AOSP, not a LineageOS distribution. Preserve the built Monarch kernel as evidence, not as proof of ROM compatibility. Independently validate hardware sources. No automatic reuse of the previous manifest. Requirements include fully offline Hindi/Hinglish assistant, volume-long-press or dedicated button activation, battery/usage intelligence, chosen Monarch gaming and visual features. Exact approved animations remain to be supplied. No new cloud resources are provisioned by this change.

## Verified source locations and pinned candidates

| Component | Source | Revision checked | Status |
|---|---|---|---|
| Android platform manifest | https://android.googlesource.com/platform/manifest | android17-release / 29ace668ae756c7b8917c57abb440f6518844b0c | Platform branch exists; individual platform project revisions are not all locked by pinning this manifest commit |
| onyx device reference | https://github.com/xiaomi-onyx-dev/android_device_xiaomi_onyx | 37ac86fe1cb218ed2198ad5c7f501106b17fb773 | Contains device layouts, extraction lists, HAL/policy references; NOT yet a pure AOSP port |
| Actual Adarsh Grewal vendor | https://gitlab.com/AdarshGrewal/proprietary_vendor_xiaomi_onyx | lineage-24.0 / 0b315cd69d0d0495b9d260e0a29724408bec0ca9 | onyx-vendor.mk, BoardConfigVendor.mk and Android.bp retrieved; candidate only, binary ABI/VINTF not validated |
| Monarch kernel source | https://github.com/xiaomi-onyx-dev/android_kernel_xiaomi_sm8735 | d0881fd7905872a11cd70bc46b37849135aa9a71 | Linux 6.6.142; built with Monarch certificate patch and pinned KernelSU |
| External kernel modules | https://github.com/xiaomi-onyx-dev/android_kernel_xiaomi_sm8735-modules | e46506b8f6e302d1e4b520dd814c9910d55b6ba7 | Ref verified; not yet compiled/ABI-matched to Monarch kernel |
| Kernel device trees | https://github.com/xiaomi-onyx-dev/android_kernel_xiaomi_sm8735-devicetrees | f4fbbed3359e85ffee608a0ff4359fa462735614 | Ref verified; DTB/DTBO build/integration pending |
| Xiaomi HAL reference | https://github.com/LineageOS/android_hardware_xiaomi | 6c12251713d74a01636482c9ffbdd9943addbfbf | Reference implementation only; not approved as a drop-in AOSP dependency |

## Important independent findings

1. The previous GitHub vendor URL at xiaomi-onyx-dev/proprietary_vendor_xiaomi_onyx, lineage-23.2 commit 2509897bd190281261ca3aa2bd8320125438a803, contains only README.md. That README points to Adarsh Grewal's GitLab. Repository size/history does not prove current blobs exist.
2. The previous Onyx-Hubs/android_hardware_xiaomi reference to lineage-23.2 does not exist in the inspected repository; only lineage-23.0 was listed. Do not silently substitute a different branch and call it compatible.
3. Device proprietary-files.txt and proprietary-firmware.txt identify onyx OS3.0.7.0.WOLMIXM as the default extraction source. This is a device-tree provenance statement, not independent verification that every selected vendor binary came from that firmware. Pinned blobs may have other origins.
4. Vendor BoardConfigVendor.mk adds bootloader/modem/firmware partitions to AB_OTA_PARTITIONS. Shipping this OTA requires firmware/region/rollback review; no firmware flash is authorized or performed by this investigation.
5. The device reference builds gki_defconfig + vendor/sun_perf.config + vendor/onyx_perf.config. The successful standalone Monarch build used gki_defconfig + vendor/onyx_perf.config, without sun_perf.config. That is a material difference to resolve before selecting the kernel for a phone ROM.
6. Actual downloaded Monarch config has CONFIG_MODVERSIONS=y, CONFIG_MODULE_SIG=y, CONFIG_MODULE_SIG_PROTECT=y, CONFIG_MODULE_SIG_ALL=y, CONFIG_LTO_NONE=y and CONFIG_KSU=y. Vendor modules must match symbol CRCs, signing requirements, architecture, release and relevant config; reusing Image alone does not establish that.
7. Downloaded candidate ZIP SHA256: 8bb164639f9a6c0a2ef1f228d488ed902885896f0740183da3582aa1daa47f71. Provenance records project 7c40c212c2ca89b88aef7deda80438e28770315e, KernelSU 4c706b5938665866ebe16944a481a7b91e3396af. No SuSFS integration is claimed.

## Hardware/source dependency worklist

- Qualcomm sm8750-family audio AGM, AudioReach graphservices, PAL, primary HAL; display core/HAL/interfaces; data IPA; common compatibility matrices/build definitions.
- Xiaomi fingerprint, sensors and device interfaces; NXP NFC/keymint/weaver; Qualcomm USB, vibrator, boot, thermal and telephony integration.
- Device SELinux, VINTF device/framework matrices, filesystem fstab/init/ueventd, permissions/feature XMLs and variant overlays.
- AOSP-compatible power/health/IR services and Settings resources. Existing device tree uses Lineage interfaces/services; importing the complete Lineage platform is not the solution.
- Kernel/module build rules, module load lists, first-stage/vendor/system DLKM placement and DTB/DTBO generation.
- Register the real AOSP product/release configuration; use AOSP image/target-files/OTA build targets, not `mka bacon`.

## Server preflight before a paid full build

Inspect CPU architecture, Linux version, RAM, free disk, existing files and current billing. Download only the necessary pinned device metadata initially. Check vendor contents/VINTF/ELF dependencies and kernel-module ABI before claiming a coherent source set. Record repo manifest -r after platform sync. No full checkout or paid resize has occurred here. Resource availability and account credit must be checked separately.

The adjacent research manifest pins verified candidates only. It is intentionally outside local_manifests so it is NOT automatically synced or represented as a finished build manifest. A complete AOSP device port and its transitive hardware dependencies remain unfinished.
