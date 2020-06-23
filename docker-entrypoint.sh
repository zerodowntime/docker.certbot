#!/bin/sh

set -eu

[ -f /root/.ssh/id_rsa ] || ssh-keygen -t rsa -N "" -f /root/.ssh/id_rsa

exec "$@"
