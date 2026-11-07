#!/usr/bin/env bash
# Fresh configuration validation only. Does not produce a phone-ready kernel.
set -euo pipefail
kernel_dir=${1:?kernel source required}
evidence_dir=${2:?absolute evidence directory required}
mkdir -p "$evidence_dir"
cd "$kernel_dir"
test -f arch/arm64/configs/vendor/sun_perf.config
test -f arch/arm64/configs/vendor/onyx_perf.config
make O=out ARCH=arm64 LLVM=1 gki_defconfig vendor/sun_perf.config vendor/onyx_perf.config
make O=out ARCH=arm64 LLVM=1 olddefconfig
cp out/.config "$evidence_dir/kernel.config"
make O=out ARCH=arm64 LLVM=1 -s kernelrelease > "$evidence_dir/kernelrelease.txt"
python3 - "$evidence_dir" <<'PY'
from pathlib import Path
import json,sys
root=Path(sys.argv[1]); values={}
for line in (root/'kernel.config').read_text().splitlines():
    if line.startswith('CONFIG_') and '=' in line:
        key,value=line.split('=',1); values[key]=value
checks={key:values.get(key,'unset') for key in ['CONFIG_ARCH_SUN','CONFIG_ARCH_TUNA','CONFIG_MODVERSIONS','CONFIG_ARM64_4K_PAGES']}
failed=[key for key,value in checks.items() if value!='y']
report={'kind':'kernel-config-validation-only','flags':checks,'failed':failed,'phone_boot_verified':False,'vendor_module_abi_verified':False,'compiler_for_full_build_qualified':False}
(root/'configuration-result.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
if failed: raise SystemExit('Required device configuration did not survive Kconfig resolution')
PY
