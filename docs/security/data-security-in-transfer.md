# Introduction

Protecting data "in flight" or "in transfer" involves encrypting the data stream at one point and decrypting it at another point. For example, when you download the result of a calculation from our data center to your local computer we ensure confidentiality of this exchange through encryption.
 
 Encryption is used to protect data stream as it leaves our data centers. Decryption is then used to at the other end of the channel on your local computer. Since the data exchange is very brief, the keys used to encrypt the frames or packets are no longer needed after the data is decrypted at the other end so they are discarded. 

# How data is protected

Most common protocols used for "in-flight" data encryption are IPsec, VPN and TLS/SSL. We use strong 256-bit AES encryption for TLS/SSL for exchanging data between all components of our application stack to make sure no one has access to your data while it leaves or enters our servers.

## What Is TLS/SSL?

TLS/SSL (Transport Layer Security/Secure Sockets Layer) is a standard security technology for establishing an encrypted link between a server and a client — typically a web server (website) and a browser; or a mail server and a mail client (e.g., Outlook). 

TLS allows sensitive information such as credit card numbers, social security numbers, and login credentials to be transmitted securely. Normally, data sent between browsers and web servers is sent in plain text—leaving users vulnerable to eavesdropping. If an attacker is able to intercept all data being sent between a browser and a web server they can see and use that information. More specifically, TLS/SSL is a security protocol and describes how algorithms should be used when determining variables of the encryption for both the link and the data being transmitted.

## Why TLS/SSL

SSL secures millions of peoples' data on the Internet every day, especially during online transactions or when transmitting confidential information. Internet users have come to associate their online security with the lock icon that comes with an SSL-secured website or green address bar that comes with an extended validation SSL-secured website. SSL-secured websites begin with https rather than http.

# Links

1. TLS - Transport Layer Security: [wikipedia](https://en.wikipedia.org/wiki/Transport_Layer_Security)
