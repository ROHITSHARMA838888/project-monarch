"""Cheap static port audit. A successful audit is NOT a successful ROM build."""
import argparse
import json
from pathlib import Path
import subprocess
import xml.etree.ElementTree as ET

parser = argparse.ArgumentParser()
parser.add_argument('--device', type=Path, required=True)
parser.add_argument('--output', type=Path, default=Path('port-audit.json'))
parser.add_argument('--require-ready', action='store_true')
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
manifest = ET.parse(root / 'local_manifests/roomservice.xml').getroot()
device_project = next(p for p in manifest.findall('project') if p.get('path') == 'device/xiaomi/onyx')
products = (args.device / 'AndroidProducts.mk').read_text()
board = (args.device / 'BoardConfig.mk').read_text()
device = (args.device / 'device.mk').read_text()
blockers = []
if 'aosp_onyx.mk' not in products:
    blockers.append('Device does not register aosp_onyx in AndroidProducts.mk')
for label, token, content in [
    ('Lineage product inheritance', 'vendor/lineage/config/common_full_phone.mk', (args.device / 'lineage_onyx.mk').read_text() if (args.device / 'lineage_onyx.mk').exists() else ''),
    ('Lineage SELinux policy', 'device/lineage/sepolicy', board),
    ('Qualcomm CAF build infrastructure', 'hardware/qcom-caf/common/common.mk', device),
    ('Lineage power HAL', 'android.hardware.power-service.lineage-libperfmgr', device),
    ('Lineage health HAL', 'vendor.lineage.health-service.default', device),
    ('Lineage interface namespace', 'hardware/lineage/interfaces', device),
]:
    if token in content:
        blockers.append(f'{label} requires explicit AOSP port/dependency integration: {token}')
if 'TARGET_KERNEL_SOURCE' in board:
    blockers.append('AOSP kernel/vendor-module build integration not qualified; Lineage TARGET_KERNEL_* variables alone do not implement it')
workflow = (root / '.github/workflows/build.yml').read_text()
for command in ['lunch ', 'mka ']:
    if any(command in line and '|| true' in line for line in workflow.splitlines()):
        blockers.append(f'Workflow masks {command.strip()} errors')
if not (root / 'products/monarch.mk').exists():
    blockers.append('Monarch product package/overlay integration is absent')
sha = subprocess.check_output(['git', '-C', str(args.device), 'rev-parse', 'HEAD'], text=True).strip()
report = dict(kind='static-port-audit-not-rom-build', ready=not blockers,
              device_commit=sha, device_revision=device_project.get('revision'),
              blockers=blockers, storage=dict(
                  shallow_checkout=True, recommended_free_gib=400,
                  swap_is_disk_usage=True, ccache_is_disk_usage=True,
                  estimated_actual_peak_gib=None))
args.output.parent.mkdir(parents=True, exist_ok=True)
args.output.write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))
if args.require_ready and blockers:
    raise SystemExit('ROM prerequisites are incomplete; refusing full source sync/build')
