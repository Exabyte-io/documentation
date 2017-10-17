# Introduction

Data "at rest" refers to the encryption of data that is not "moving". This data is usually stored on hardware such as local disk, SAN, NAS, or other portable storage devices. Regardless of how the data gets there, as long as it remains on that device and is not transferred or transmitted over a network, it is considered "at rest".

# How data is secured

There are different methodologies to encrypt at rest data. The most common one is disk encryption. Disk encryption is a method where all data on a particular physical disk is encrypted. 

We use Linux Unified Key Setup-on-disk-format (or LUKS) along with AES-256 to encrypt partitions on our servers, the standard for Linux hard disk encryption 

## LUKS

By providing a standard on-disk-format,  LUKS does not only facilitate compatibility among distributions, but also provides secure management of multiple user passwords. In contrast to other solutions, LUKS stores all necessary setup information in the partition header, enabling the user to transport or migrate his data seamlessly.

## Reasons for choosing LUKS

* secure against low entropy attacks,
* support for multiple keys,
* effective passphrase revocation,
* compatiblity via standardization,

# Links

1. LUKS - open-source disk encryption: [source](https://gitlab.com/cryptsetup/cryptsetup)
