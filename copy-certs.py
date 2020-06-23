#!/usr/local/bin/python3

"""
This script concatenates fullchain
with private key and copying it to haproxy server(s)
"""

import os
import subprocess

USER = "certbot"
SERVER = "haproxy.service.consul"
PATH = "/home/certbot/"
DOMAIN_NAME = os.path.basename(os.environ.get('RENEWED_LINEAGE'))
FULLCHAIN = "/etc/letsencrypt/live/" + DOMAIN_NAME + "/fullchain.pem"
PRIVKEY = "/etc/letsencrypt/live/" + DOMAIN_NAME + "/privkey.pem"
PEM_FILE = "/etc/letsencrypt/archive/" + DOMAIN_NAME + "/" + DOMAIN_NAME

with open(FULLCHAIN) as f:
    f = f.read()

with open(PRIVKEY) as p:
    p = p.read()

full_pem = f + "\n" + p 

with open(PEM_FILE, 'w') as pem:
  pem.write(full_pem)

subprocess.run(["/usr/bin/scp", "-o StrictHostKeyChecking=no", "-o UserKnownHostsFile=/dev/null", PEM_FILE, USER + '@' + SERVER + ':' + PATH])
os.chmod(PEM_FILE, 0o600)
