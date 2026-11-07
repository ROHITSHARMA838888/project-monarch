#!/usr/bin/env bash
# External build order follows the pinned onyx device reference.
set -euo pipefail
work=${1:?workspace required}
kernel="$work/sources/sm8735"
ext="$work/sources/sm8735-modules"
out="$kernel/out"
evidence="$work/build-evidence"
test -s "$out/Module.symvers"
test -s "$out/arch/arm64/boot/Image"
make -C "$kernel" O="$out" ARCH=arm64 LLVM=1 headers_install INSTALL_HDR_PATH="$out/usr"
modules=(
 qcom/opensource/mmrm-driver
 qcom/opensource/mm-drivers/hw_fence
 qcom/opensource/mm-drivers/msm_ext_display
 qcom/opensource/mm-drivers/sync_fence
 qcom/opensource/audio-kernel
 qcom/opensource/securemsm-kernel
 qcom/opensource/synx-kernel
 qcom/opensource/camera-kernel
 qcom/opensource/data-kernel/drivers/smem-mailbox
 qcom/opensource/datarmnet-ext/mem
 qcom/opensource/dataipa/drivers/platform/msm
 qcom/opensource/datarmnet/core
 qcom/opensource/datarmnet-ext/aps
 qcom/opensource/datarmnet-ext/offload
 qcom/opensource/datarmnet-ext/perf
 qcom/opensource/datarmnet-ext/perf_tether
 qcom/opensource/datarmnet-ext/sch
 qcom/opensource/datarmnet-ext/shs
 qcom/opensource/datarmnet-ext/wlan
 qcom/opensource/display-drivers/msm
 qcom/opensource/dsp-kernel
 qcom/opensource/eva-kernel
 qcom/opensource/graphics-kernel
 qcom/opensource/spu-kernel
 qcom/opensource/touch-drivers
 qcom/opensource/video-driver
 qcom/opensource/wlan/platform
 qcom/opensource/wlan/qcacld-3.0/.wcn7750
 qcom/opensource/bt-kernel
 nxp/opensource/driver
)
for module in "${modules[@]}"; do
  test -f "$ext/$module/Makefile"
  printf '\n=== Building %s ===\n' "$module"
  make -j2 -C "$ext/$module" M="../sm8735-modules/$module" \
    KERNEL_SRC="$kernel" OUT_DIR="$out" O="$out" ARCH=arm64 LLVM=1 LLVM_IAS=1 \
    TARGET_PRODUCT=onyx TARGET_BOARD_PLATFORM=sun KERNEL_UAPI_HEADERS_DIR="$out" \
    modules
  printf '%s\n' "$module" >> "$evidence/external-groups-completed.txt"
done
find "$work/sources" -type f -name '*.ko' -print > "$evidence/all-built-modules.txt"
release=$(cat "$evidence/kernelrelease.txt")
while IFS= read -r module; do
  actual=$(modinfo -F vermagic "$module")
  test "${actual%% *}" = "$release"
  printf '%s\t%s\n' "$module" "$actual" >> "$evidence/module-vermagic.tsv"
done < "$evidence/all-built-modules.txt"
printf '%s\n' 'External compile/vermagic checks complete; signing, firmware, full ABI and phone boot qualification still required.' > "$evidence/EXTERNAL-STATUS.txt"
