# Security

We know your data is extremely important to you and your business, and we're very protective of it.

# Need to report a security vulnerability?

Please contact us about our security bug bounty policies, for information about our responsible disclosure process and to submit a vulnerability report.

# Physical Security

We partner with trusted cloud providers [[1,2](#links)] whose policies include among the rest:

- Limited data center access to data center technicians and approved staff
- Biometric scanning for controlled data center access
- Security cameras monitoring at all data center locations
- 24x7 onsite staff provides additional protection against unauthorized entry
- Unmarked facilities to help maintain low profile
- Audited by independent firms

# System Security

- System installation using up-to-date OS
- Dedicated firewall and VPN services to help block unauthorized access
<!-- TODO: enable when ready -->
<!-- - Distributed Denial of Service (DDoS) mitigation services powered by industry-leading solutions -->

# Operational Security

<!-- TODO: enable when ready -->
<!-- - Our primary data center operations are regularly audited by independent firms against an ISAE 3000/AT 101 Type 2 Examination standard -->
- Systems access logged and tracked for auditing purposes
- Secure document-destruction policies for all sensitive information
- Fully documented change-management procedures

# Software Security

We employ a team of 24/7/365 server specialists at Exabyte.io to keep our software and its dependencies up to date eliminating potential security vulnerabilities. We employ a wide range of monitoring solutions for preventing and eliminating attacks to the site. 

Data encryption policies are explained in:

- [data security at rest](data-security-at-rest.md)
- [data security in transfer](data-security-in-transfer.md)

# Communications

All private data exchanged with Exabyte.io is always transmitted over SSL (which is why your profile is served over HTTPS, for instance). All pushing and pulling of private data is done over SSH authenticated with keys, or over HTTPS using your username and password.

# File system and backups

Every piece of hardware we use has an identical copy ready and waiting for an immediate hot-swap in case of hardware or software failure. Every bit of data we store is saved on a minimum of three different servers, including an block storage backup. We retroactively remove data from backups when deleted by the user after a grace period, as we may need to restore the repository for the user if it was removed accidentally.

We **encrypt** all data on disk and in transfer. No user with shell access to the file system has access to the decryption routine. We focus on making our machines and network as secure as possible.

# Employee access

No Exabyte.io employees ever access private data unless required so for support reasons. Staff working directly in the file store may access the encrypted data, however it is never accessing plaintext files like it would be in your local system. 

Support staff may sign into your account to access settings related to your support issue. In rare cases staff may need to copy your data, this will only be done with your consent. Support staff does not have direct access to copy your data, they will need to temporarily elevate their permissions to access your account. We keep track of all such events. When working on a support issue we do our best to respect your privacy as much as possible, we only access the files and settings needed to resolve your issue. All copied data is deleted as soon as the support issue has been resolved.

# Maintaining security

We protect your login from brute force attacks with rate limiting. All passwords are filtered from all our logs and are one-way encrypted in the database using bcrypt. Login information is always sent over SSL.

We also support two-factor authentication, or 2FA, as an additional security measure when accessing your Exabyte.io account. Enabling 2FA adds security to your account by requiring both your password as well as access to a security code on your phone to access your account.

We have security staff to help identify and prevent new attack vectors. We always test new features in order to rule out potential attacks.

<!-- TODO: enable when ready -->
<!-- We also maintain relationships with reputable security firms to perform regular penetration tests and ongoing audits of Exabyte.io and its code. -->

We're extremely concerned and active about security. We are aware that many companies are not comfortable hosting sensitive data outside their firewall. For these companies we can offer "Exabyte.io On-premises", a version of Exabyte.io that can be installed to a server within the company's network.

# Credit card safety

When you sign up for a paid account on Exabyte.io, we do not store any of your card information on our servers. It's handed off to Stripe, a company dedicated to storing your sensitive data on PCI-Compliant servers.

# Contact Us

Have a question, concern, or comment about Exabyte.io security? Please contact Exabyte.io Support.

# Links

1. AWS Security Policies: [link](https://aws.amazon.com/whitepapers/overview-of-security-processes/)
1. Microsoft Azure Security Policies: [link](https://azure.microsoft.com/en-us/support/legal/security-overview/)
