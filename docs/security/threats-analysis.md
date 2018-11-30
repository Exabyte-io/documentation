# Security Threats Analysis

This page contains information about security threats and their mitigation. Our categorization is similar to that discussed in [^1].

## Data Threats

### Data Breaches

We prevent data breaches through the use of encryption as explained above, UNIX permissions for users in the shared regime and private clusters, as an option.

### Data Loss

In our platform users always have access to their data, regardless of the service level and the type of contract. Users have the ability to export the data in standard formats for use outside our platform. We use redundant storage architecture and run daily backups for the data in order to prevent any losses.


## Network Threats

### Account Hijacking

We have an intrusion detection system based on daily account activity monitoring (screen for malicious or out-of-the-ordinary behavior). We use of strong passwords and have plans to implement multi-factor authentication soon.

### Denial of Service

We verify all network requests within the production servers by using virtual private network and security groups. We also maintain a backup IP pool for urgent cases. We further implement load balancing and use multiple cloud providers, multiple datacenters within each provider, and multiple availability zones within each datacenter.

## Cloud-specific Threats

### Interface and API security

The interface-related threats are mitigated through the use of a transparent user-level permission scheme, extensive onboarding/training, and regular data access checks by the support team.

Our software architecture is based on trusted computing principles, where trusted and non-trusted code is clearly differentiated through secure authorization.

### Malicious Insiders

All sensitive information (eg. encryption keys) is only accessible to authorized Exabyte personnel (2 persons) and are stored in multiple locations on company-owned hardware. A Proprietary Information Agreement is requred for each employee. We further consider Non-disclosure agreements a normal practice for customers.

### Abuse of Cloud Service

We deploy a strict initial registration and validation processes: we verify the information about and establish contact with each new user. The policies for the protection of important assets are made part of the agreement between user and Exabyte as a service provider.

We maintain and present to the customers a clear log of all usage-related transactions so that they can control spends and prevent over-use.

### Insufficient Due Diligence

We as a service providers can disclose the applicable logs, infrastructure, such as firewall, and other measures we take for securing the operations to our customers. We further follow the requirements set by the cloud providers for implementing cloud applications, and services using industry standards.

### Shared Technology Vulnerabilities

We work with trusted cloud service providers (AWS, Azure) that monitor the vulnerabilities in the cloud environment, and release/deploy patches to fix those vulnerabilities regularly.

## Other Threats
### Regulatory

Our policy is to work with an established distribution partner in the local area (eg. ITOCHU Techno-solutions in Japan) who is able to facilitate support and allow for reducing any direct effect of regulatory changes to the customers.

### Unexpected Outage

We deploy a fault-tolerant architecture spanning multiple cloud providers with frequent storage backups, so that no single accident could affect mission-critical operations.

### Service-level-related

Mitigated through the use of service level agreements with a clearly identified response time and associated cost/responsibility for the support requests. Our accounting methods are finalized in the service agreement and persist throughout the validity period.

## More...

Please contact us and we will be glad to assist you with any further security related considerations.

## Links

[1]: Kazim et. al,  “A survey on top security threats in cloud computing”,  International Journal of Advanced Computer Science and Applications, Vol. 6, No. 3, 2015 [link](http://thesai.org/Downloads/Volume6No3/Paper_16-A_survey_on_top_security_threats_in_cloud_computing.pdf)
