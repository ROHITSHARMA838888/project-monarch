# Monarch pure AOSP port

The onyx Lineage tree is reference material, not a completed pure AOSP port.
Run `python3 scripts/audit_rom.py --device PATH --require-ready` before a full sync.
A green **port audit** job means the report was generated, not that a ROM exists.

## Work required before a phone build

1. Register an AOSP product and release configuration without vendor/lineage product inheritance.
2. Pin and integrate the Qualcomm audio, display, USB, telephony, NXP and Xiaomi dependencies referenced by device.mk, BoardConfig.mk and Soong files.
3. Port the Lineage power/health/IR services, Settings resources and overlays, plus their SELinux/framework dependencies; do not remove hardware services just to silence errors.
4. Integrate the kernel build, device trees and vendor modules as one ABI-consistent set. The standalone kernel artifact is not the complete ROM kernel integration.
5. Build the vanilla base first, verify product configuration, build images/target-files and OTA using AOSP targets, then qualify boot and hardware on the device.
6. Add Monarch packages with explicit product inheritance. The assistant's voice/session classes, recognition, inference, permission lifecycle and privacy controls remain incomplete; do not auto-enable it at boot.

## Storage work retained

- Keep shallow `repo init --depth=1`, current-branch sync, no tags and no clone bundles.
- Cleanup of unused hosted SDKs frees existing space; it does not provision a bigger disk.
- Compressed ccache reduces cache bytes but requires disk and only helps when actually wired into the compiler. A first build can disable ccache to save its allocation.
- 12 GiB swap consumes 12 GiB disk; use only when enough space remains. It is not extra RAM performance or extra storage.
- Cirrus `disk: 300` is a request, not evidence that this allocation/free eligibility was granted. Inspect the real worker `df` output and service result.
- Do not remove arbitrary AOSP projects, compiler intermediates or Git metadata mid-build. Do not mount unverified network drives as compiler output storage.
- Track `df` and source/output/cache size at each phase; no measured peak for this complete port is available yet. The official AOSP baseline is 400 GB free; an optimized lower peak must be measured, not promised.

Current full builds must stop before source sync when the static port audit reports blockers. This prevents spending CI quota on a known incompatible product.
