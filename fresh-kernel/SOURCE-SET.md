# Source-set correction for the PDR module list

The kernel source is pinned to d0881fd7905872a11cd70bc46b37849135aa9a71. In that source drivers/soc/qcom/Makefile builds pdr_interface.o and pdr_interface.c includes pdr_internal.h, which contains static PDR message tables. There is no qcom_pdr_msg source/build target at this revision.

Device reference 37ac86fe1cb218ed2198ad5c7f501106b17fb773 adds qcom_pdr_msg.ko to modules.list.second_stage for a newer split implementation. Its exact parent b0c670b5497338eed8b3e4bb56a524bb50638193 differs only by that single module-list entry. Use the parent as this kernel generation's runtime-list reference. Do not silently drop this driver from a newer split kernel generation.

Run 42393004392 compiled all 30 external groups and recorded 576 module-release checks. It failed its final coverage assertion because this source set used the newer runtime-list entry. The evidence-review workflow rechecks those existing outputs with the explicitly version-aligned list; it is not a new compile and does not turn the old failed run green.

Required runtime names: 465. The replay finds all 465 among 576 compiled module names. Image checksum and all recorded release strings match. Complete symbol CRC/namespace/signature validation, packaging, firmware/VINTF and phone boot remain unverified. No flash-ready claim.
