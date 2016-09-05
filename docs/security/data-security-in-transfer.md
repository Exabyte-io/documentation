<!-- TODO by MM: revise -->

This page contains information about how data "in transfer" is protected at exabyte.io.

## Data in transfer

Protecting data "in flight" or "in transfer" involves encrypting the data stream at one point and decrypting it at another point. For example, if you download the result of a calculation from our data centers to your local computer and want to ensure confidentiality of this exchange, encryption is used to protect data stream as it leaves our data centers. Decryption is then used to at the other end of the channel on your local computer.

## How data in transfer is protected

Since the data exchange is very brief, the keys used to encrypt the frames or packets are no longer needed after the data is decrypted at the other end so they are discarded. Most common protocols used for in flight data encryption are IPsec, VPN and TLS/SSL. We use strong TLS/SSL encryption for exchanging data between all components of our application stack to make sure no one has access to your data while it leaves or enters our servers.

<!-- TODO: explain more about how the encryption works, why we chose this particular type and how users can be assured that this type of encryption provides good protection -->
