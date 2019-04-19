# Security policies

This page contains a brief description of security policies we employ at Exabyte.io.

We protect the data at all steps during the simulation and analysis process with a set of layered methods:

- we always encrypt data during transfers
- we always encrypt data while it is at rest - stored on disk
- when data resides in cloud object storage we enforce strict access rules
- we limit the accessibility of the servers involved in the computation

We offer a set of extra options, such as:

- isolated single-tenant clusters
- limiting access only to trusted IP ranges, corporate VPN
- multi-factor authentication

## Encryption in transfer

Protecting data "in flight" or "in transfer" involves encrypting the data stream at one point and decrypting it at another point. For example, if you download the result of a calculation from our data center to your local system and want to ensure confidentiality of this exchange, encryption is used to protect the data stream before it leaves our server. Most common protocols used for in-flight data encryption are IPsec, VPN and TLS/SSL [^1]. We use 4096 and 2048 bit strong TLS/SSL encryption for exchanging data between all components of our application stack to make sure no one has access to your data when it leaves or enters our servers.

## Encryption at rest

Data "at rest" refers to the encryption of data that is not moving. This data is usually stored on hardware such as local disk, storage area network, network-accessible storage, or other portable storage devices. Regardless of how the data gets there, as long as it remains on that device and is not transferred or transmitted over a network, it is considered at rest. Disk encryption is a method where all data on a particular physical disk is protected and made inaccessible to parties without an encryption key. We use Linux Unified Key Setup-on-disk-format (or LUKS [^2]) along with AES-256 to encrypt partitions on our servers. By providing a standard on-disk-format, it does not only facilitate compatibility among distributions, but also provides secure management of multiple user passwords. LUKS is secure against low entropy attacks and supports effective passphrase revocation. Only authorized Exabyte personnel has access to decryption keys,  stored securely on company-owned hardware, also encrypted.

## Protection in object storage

Object storage is a computer data storage architecture that manages data as objects, as opposed to managing data as a file hierarchy. All objects in object storage by default are private. Only the owner has permission to access them. The owner can optionally share objects with others by creating a pre-signed URL, using their own security credentials, to grant time-limited permission to download the objects. Our web application creates pre-signed URLs for the objects owned by user when he/she is accessing them. We automatically provide security credentials and expiration date and time. The pre-signed URLs are valid only for the specified duration (15 min by default) [^3].

## Other

Other notable security features are:

- Kerberos-based [^4] encryption/authentication for the network file system
- 2048 bit AES database encryption
- UNIX + role-based permission schemes [^5] with SSH key-based authentication
- we protect login from brute force attacks through limiting the rate
- passwords are filtered from all our logs and are one-way encrypted


## Links

[^1]: TLS - Transport Layer Security: [wikipedia](https://en.wikipedia.org/wiki/Transport_Layer_Security)
[^2]: LUKS - open-source disk encryption: [source](https://gitlab.com/cryptsetup/cryptsetup)
[^3]: AWS S3, signed URLs: [source](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-signed-urls.html)
[^4]: Kerberos: the Network Authentication Protocol, [source](http://web.mit.edu/kerberos/)
[^5]: Linux permission scheme: [source](https://support.suso.com/supki/Linux_permissions_scheme)
