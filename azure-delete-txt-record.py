#!/usr/local/bin/python3

import os
import time

from msrestazure.azure_exceptions import CloudError
from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.dns import DnsManagementClient

DNS_ZONE = os.environ.get('DNS_ZONE')

AZ_RESOURCE_GROUP = os.environ.get('AZ_RESOURCE_GROUP')
AZ_TENANT = os.environ.get('AZ_TENANT')
AZ_CLIENT_ID = os.environ.get('AZ_CLIENT_ID')
AZ_CLIENT_SECRET = os.environ.get('AZ_CLIENT_SECRET')
AZ_SUBSCRIPTION_ID = os.environ.get('AZ_SUBSCRIPTION_ID')

CERTBOT_VALIDATION = os.environ.get('CERTBOT_VALIDATION')
record_name = os.environ.get('CERTBOT_DOMAIN')
record_name = record_name[:record_name.index(DNS_ZONE)]
record_name = record_name.rstrip('.')

if len(record_name) == 0:
  record_name = "_acme-challenge"
else:
  record_name = "_acme-challenge." + record_name

credentials = ServicePrincipalCredentials(
  tenant = AZ_TENANT,
  client_id = AZ_CLIENT_ID,
  secret = AZ_CLIENT_SECRET)

dns_client = DnsManagementClient(
  credentials,
  AZ_SUBSCRIPTION_ID
)

dns_client.record_sets.delete(
  AZ_RESOURCE_GROUP,
  DNS_ZONE,
  record_name,
  'TXT',
)
