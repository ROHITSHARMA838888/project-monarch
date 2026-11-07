"""Align PIN guards with the existing non-BoringSSL ENGINE implementation."""
from pathlib import Path
import sys

path = Path(sys.argv[1]) / "certs/extract-cert.c"
source = path.read_text()
for body in ('static const char *key_pass;', '\tkey_pass = getenv("KBUILD_SIGN_PIN");'):
    before = '#ifdef USE_PKCS11_ENGINE\n' + body + '\n#endif'
    if source.count(before) != 1:
        raise SystemExit(f"Unexpected extract-cert source around {body!r}; refusing patch")
    source = source.replace(before, '#ifndef OPENSSL_IS_BORINGSSL\n' + body + '\n#endif')
path.write_text(source)
print("Aligned key_pass guards with OpenSSL ENGINE code")
