<!-- by MM -->

This page contains information about how data "at rest" is protected at exabyte.io.

## Data at rest

Data "at rest" refers to the encryption of data that is not moving. This data is usually stored on hardware such as local disk, SAN, NAS, or other portable storage devices. Regardless of how the data gets there, as long as it remains on that device and is not transferred or transmitted over a network, it is considered at rest data.

## How data at rest is secured

There are different methodologies to encrypt at rest data. The most common one is disk encryption. Disk encryption is a method where all data on a particular physical disk is encrypted. We use Linux Unified Key Setup-on-disk-format (or LUKS) along with AES-256 to encrypt partitions on our servers. 

### LUKS

LUKS is the standard for Linux hard disk encryption. By providing a standard on-disk-format, it does not only facilitate compatibility among distributions, but also provides secure management of multiple user passwords. In contrast to existing solution, LUKS stores all setup necessary setup information in the partition header, enabling the user to transport or migrate his data seamlessly.

Why LUKS?

* compatiblity via standardization,
* secure against low entropy attacks,
* support for multiple keys,
* effective passphrase revocation
