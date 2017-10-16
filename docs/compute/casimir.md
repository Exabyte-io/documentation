Casimir is a private cluster dedicated to Shell organization.

# Security

- LUKS is used to encrypt the data at rest. Please visit [Data at rest](../security/data-security-at-rest/#data-at-rest) for more information.

- TLS/SSL is used to secure data in transfer. Please visit [Data in transfer](../security/data-security-in-transfer/#data-in-transfer) for more information.

- The Casimir cluster is only accessible to Shell IP addresses. Only port 22 (SSH) is open at current.

# How to connect

To be able to SSH to Casimir cluster you need to configure one of the following `ZScaler` proxies:

- zproxy-houcy1.americas.shell.com port 80

- zproxy-amsdc1.europe.shell.com port 80
 
If you are using Putty you can configure proxy via `Connection -> Proxy`.

On Linux, you need to configure your ~/.ssh/config with (for example) the following content:
 
## RHEL6
```bash 
host casimir.exabyte.io
   IdentityFile PATH_TO_YOUR_PRIVATE_KEY_FILE
   ServerAliveInterval 10
   ProxyCommand nc -X connect -x zproxy-amsdc1.europe.shell.com:80 %h %p
```

## RHEL7
```bash
host casimir.exabyte.io
   IdentityFile PATH_TO_YOUR_PRIVATE_KEY_FILE
   ServerAliveInterval 10
   ProxyCommand ncat --proxy-type http --proxy zproxy-amsdc1.europe.shell.com:80 %h %p
```
