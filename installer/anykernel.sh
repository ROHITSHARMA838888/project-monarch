### Monarch onyx kernel candidate; runtime/ABI compatibility is not qualified.
properties() { '
kernel.string=Monarch onyx kernel candidate
do.devicecheck=1
do.modules=0
do.systemless=0
do.cleanup=1
do.cleanuponabort=0
device.name1=onyx
supported.versions=17
'; }
BLOCK=/dev/block/by-name/boot;
IS_SLOT_DEVICE=1;
SLOT_SELECT=active;
RAMDISK_COMPRESSION=auto;
PATCH_VBMETA_FLAG=0;
NO_VBMETA_PARTITION_PATCH=1;
. tools/ak3-core.sh;
[ "$BOOTMODE" = false ] || abort "Recovery installation only.";
[ "$(getprop ro.product.device)" = onyx ] || abort "Only onyx is supported.";
case "$SLOT" in _a|_b) ;; *) abort "Invalid active slot.";; esac;
[ "$BLOCK" = "/dev/block/by-name/boot$SLOT" ] || abort "Unexpected target partition.";
# Require explicit local opt-in after ROM/module ABI and backup review.
[ -f /sdcard/Monarch-kernel-compatibility-reviewed ] || abort "Unqualified candidate: review ROM/module compatibility and backup before opting in.";
split_boot;
[ "$(od -An -tu4 -j40 -N4 "$BOOTIMG" | tr -d ' \n')" = 4 ] || abort "Only boot header v4 supported.";
[ "$(od -An -tu4 -j12 -N4 "$BOOTIMG" | tr -d ' \n')" = 0 ] || abort "Unexpected boot ramdisk.";
[ "$(od -An -tu4 -j1580 -N4 "$BOOTIMG" | tr -d ' \n')" = 0 ] || abort "Signed boot image requires separate review.";
flash_boot;
