# certbot

Compatible with AWS by dns-route53 plugin and Azure by python's scripts which use Azure API.

## How to use with Azure

Before you start you have to:

1. create an azure active directory application
2. assign DNS Zone Contributor role
3. create a new application secret

You can do this by azure portal or az cli.

## azure portal

https://docs.microsoft.com/en-us/azure/active-directory/develop/howto-create-service-principal-portal#create-an-azure-active-directory-application

## az cli
https://docs.microsoft.com/en-us/cli/azure/ad/sp?view=azure-cli-latest#az-ad-sp-create-for-rbac
https://docs.microsoft.com/en-us/azure/media-services/previous/media-services-cli-create-and-configure-aad-app

get DNS zone resource ID (scope)
```shell
az network dns zone show --name <DNS zone name> --resource-group <resource group>
```

create app with DNS Zone Contributor role assignment
```shell
az ad sp create-for-rbac --name <app name> --years <number of years for which the credentials will be valid> --role "DNS Zone Contributor" --scopes <DNS zone resource ID>
```
