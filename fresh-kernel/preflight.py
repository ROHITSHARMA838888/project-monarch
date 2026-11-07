"""Reject known source-generation/entry-point mismatches before compilation."""
import json
from pathlib import Path
import re
import subprocess
import sys

work=Path(sys.argv[1]).resolve()
kernel=work/'sources/sm8735'; external=work/'sources/sm8735-modules'
pins={kernel:'d0881fd7905872a11cd70bc46b37849135aa9a71',
      external:'e46506b8f6e302d1e4b520dd814c9910d55b6ba7',
      work/'sources/sm8735-devicetrees':'f4fbbed3359e85ffee608a0ff4359fa462735614'}
for path,expected in pins.items():
    actual=subprocess.check_output(['git','-C',str(path),'rev-parse','HEAD'],text=True).strip()
    if actual!=expected:raise SystemExit(f'Wrong upstream revision: {path.name}')
script=(work/'fresh-kernel/build_onyx_external_modules.sh').read_text()
groups=re.findall(r'^ (qcom/\S+|nxp/\S+)$',script,re.M)
if len(groups)!=30 or len(set(groups))!=30:raise SystemExit('Unexpected external group set')
for group in groups:
    makefile=external/group/'Makefile'
    if not makefile.is_file():raise SystemExit(f'Missing wrapper: {group}')
    if not re.search(r'^all\s*:',makefile.read_text(),re.M):
        raise SystemExit(f'Wrapper does not expose expected all target: {group}')
required=set((work/'fresh-kernel/required-runtime-modules.txt').read_text().splitlines())
if len(required)!=465:raise SystemExit('Runtime list changed: review source generation first')
qcom_make=(kernel/'drivers/soc/qcom/Makefile').read_text()
pdr=(kernel/'drivers/soc/qcom/pdr_interface.c').read_text()
if 'qcom_pdr_msg.ko' in required and 'qcom_pdr_msg' not in qcom_make:
    raise SystemExit('Split PDR runtime list does not match embedded-PDR kernel')
if 'pdr_interface.ko' not in required or '#include "pdr_internal.h"' not in pdr:
    raise SystemExit('Unexpected PDR implementation; re-audit source set')
for fragment in ['gki_defconfig','vendor/sun_perf.config','vendor/onyx_perf.config']:
    if not (kernel/'arch/arm64/configs'/fragment).is_file():raise SystemExit(f'Missing {fragment}')
if not (kernel/'arch/arm64/boot/dts/vendor/qcom').is_dir():raise SystemExit('Broken vendor DTS link')
compiler=work/'compiler/clang-r510928/bin/clang'
if not compiler.is_file():raise SystemExit('Declared compiler is absent')
print(json.dumps({'kind':'static-precompile-source-gate','groups_checked':30,'runtime_names':465,
                  'source_revisions_match':True,'entry_targets_match':True,
                  'phone_compatibility_verified':False},indent=2))
