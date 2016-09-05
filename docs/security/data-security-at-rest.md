<!-- by MM -->

This page contains information about how data "at rest" is protected at exabyte.io.

## Data at rest

Data "at rest" refers to the encryption of data that is not moving. This data is usually stored on hardware such as local disk, SAN, NAS, or other portable storage devices. Regardless of how the data gets there, as long as it remains on that device and is not transferred or transmitted over a network, it is considered at rest data.

## How data at rest is secured

There are different methodologies to encrypt at rest data. The most common one is disk encryption. Disk encryption is a method where all data on a particular physical disk is encrypted. We use AES 256 bits encryption algorithm to encrypt your data while is at rest.

<!-- TODO: explain more about how the encryption works, why we chose this particular type and how users can be assured that this type of encryption provides good protection -->
