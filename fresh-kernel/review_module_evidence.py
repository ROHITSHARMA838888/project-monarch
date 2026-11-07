"""Review existing outputs against the correct pinned runtime-list generation.

This does not rerun compilation or qualify module signatures/full ABI/phone boot.
"""
import hashlib,json
from pathlib import Path
import sys

evidence=Path(sys.argv[1]); required_file=Path(sys.argv[2]); output=Path(sys.argv[3])
required=set(required_file.read_text().splitlines())
paths=(evidence/'all-built-modules.txt').read_text().splitlines()
built={Path(p).name for p in paths}
groups=(evidence/'external-groups-completed.txt').read_text().splitlines()
release=(evidence/'kernelrelease.txt').read_text().strip()
rows=[line.split('\t',1) for line in (evidence/'module-vermagic.tsv').read_text().splitlines()]
bad_release=[p for p,v in rows if v.split()[0]!=release]
expected_hash=(evidence/'Image.sha256').read_text().split()[0].lower()
actual_hash=hashlib.sha256((evidence/'Image').read_bytes()).hexdigest()
assert expected_hash==actual_hash, 'Image checksum mismatch'
assert len(groups)==30 and len(set(groups))==30, 'Incomplete external compilation'
assert len(rows)==len(paths), 'Incomplete recorded release checks'
assert not bad_release, 'Module release mismatch'
missing=sorted(required-built)
report={'kind':'existing-build-evidence-review-not-new-compilation','source_run':42393004392,
        'device_reference':'b0c670b5497338eed8b3e4bb56a524bb50638193',
        'kernel_source':'d0881fd7905872a11cd70bc46b37849135aa9a71',
        'completed_external_groups':len(groups),'built_module_names':len(built),
        'required_module_names':len(required),'missing':missing,'release':release,
        'image_sha256':actual_hash,'vermagic_checks':len(rows),
        'full_symbol_crc_verified':False,'signatures_verified':False,'phone_boot_verified':False}
output.parent.mkdir(parents=True,exist_ok=True)
output.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
if missing:raise SystemExit('Required modules missing')
