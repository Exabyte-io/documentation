## Security Overview

We know your data is extremely important to you and your business, and we make it our priority to protect it.

## Need to report a security vulnerability?

Please contact us for information about our responsible disclosure process and to submit a vulnerability report.

## Security Layers

### Physical Security

We partner with trusted cloud providers and rely on their measures in facilitating physical security [^1],[^2].

### System Security

- System installation using up-to-date OS
- Dedicated firewall and VPN services to help block unauthorized access
<!-- TODO: enable when ready -->
<!-- - Distributed Denial of Service (DDoS) mitigation services powered by industry-leading solutions -->

### Operational Security

<!-- TODO: enable when ready -->
<!-- - Our primary data center operations are regularly audited by independent firms against an ISAE 3000/AT 101 Type 2 Examination standard -->
- Systems access logged and tracked for auditing purposes
- Secure document-destruction policies for all sensitive information
- Fully documented change-management procedures

#### Employee access

No Exabyte.io employees ever access private data unless required so for support reasons. Staff working directly in the file store may access the encrypted data, however it is never accessing plaintext files like it would be in your local system. 

Support staff may sign into your account to access settings related to your support issue. In rare cases staff may need to copy your data, this will only be done with your consent. Support staff does not have direct access to copy your data, they will need to temporarily elevate their permissions to access your account. We keep track of all such events. When working on a support issue we do our best to respect your privacy as much as possible, we only access the files and settings needed to resolve your issue. All copied data is deleted as soon as the support issue has been resolved.

### Software Security

Specific security policies employed within our platform are summarized in [security policies page](security-policies.md). Cloud-computing related threats and our means of mitigation are discussed [here](threats-analysis.md).

#### Data Backups

All data we store is saved on a minimum of three different servers, including an block storage backup. We retroactively remove data from backups when deleted by the user after a grace period, as we may need to restore the repository for the user if it was removed accidentally. We **encrypt** all data on disk and in transfer.

## On-premises deployment

We are aware that some companies are still not comfortable hosting data on any third-party-owned hardware. We can suggest [private deployment](../site-policy/sharing-policy.md) options in this case.

## Links

[^1]: AWS Security Policies: [link](https://aws.amazon.com/whitepapers/overview-of-security-processes/)
[^2]: Microsoft Azure Security Policies: [link](https://azure.microsoft.com/en-us/support/legal/security-overview/)
