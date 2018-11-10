# Security

All objects in object storage by default are private. This means that only the owner has permission to access them. The owner can optionally share objects with others by creating a pre-signed URL, using their own security credentials, to grant time-limited permission to download the objects. See AWS S3 and Azure Blob pre-signed URLs in [links](#Links) section for more information.

Our web application creates pre-signed URLs for the objects owned by user when they are accessed. We automatically provide security credentials and expiration date and time. Please note that the pre-signed URLs are valid only for the specified duration (15 min by default).


Please consult [security](/security/current-state/) section for more information about security polices in place.

- [AWS S3 pre-signed URLs](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-signed-urls.html)
- [Azure Blob pre-signed URLs](https://docs.microsoft.com/en-us/azure/storage/common/storage-dotnet-shared-access-signature-part-1)
