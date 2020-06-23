FROM certbot/certbot:latest

COPY *.py /opt/
COPY certbot-cronjob.sh /etc/periodic/daily/certbot
COPY docker-entrypoint.sh /

RUN \
  apk update && \
  apk add openssh openssh-keygen py-pip && \
  apk add --virtual=build gcc libffi-dev musl-dev openssl-dev python-dev make && \
  pip --no-cache-dir install -U pip && \
  pip --no-cache-dir uninstall enum34 -y && \ 
  pip --no-cache-dir install azure-cli && \
  pip --no-cache-dir install certbot-dns-route53 && \
  apk del --purge build

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["/usr/sbin/crond", "-f"]
