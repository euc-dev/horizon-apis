---
layout: page
title: Service - Certificate
hide:
#- navigation
- toc
---







Java Class
> `com.vmware.vdi.vlsi.binding.vdi.utils.Certificate`

See also
> [CertificateData](vdi.utils.Certificate.CertificateData.md), [ViewComposerWithVCSpec](vdi.utils.Certificate.ViewComposerWithVCSpec.md)

Since
> Horizon View 6.0





## Service Description

The interface to fetch and validate certificates.

Methods

Methods defined in this Service
---
Certificate_Validate, Certificate_ValidateViewComposerLocalToVC




Validate the certificate of the specified server.

Privileges

Privilege |  Description
---|---
GLOBAL_CONFIG_VIEW|  Global configuration (read-only) is required to validate a certificate.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Certificate](vdi.utils.Certificate.md) used to make the method call.
**spec**|  xsd:anyType|  attributes needed to connect to the server. The valid types for this parameter are: [^225] [^226]






Return Value

Type |  Description
---|---
[CertificateData](vdi.utils.Certificate.CertificateData.md)| null iff successful else [CertificateData](vdi.utils.Certificate.CertificateData.md) describing the server certificate



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







**Deprecated.**_This API is being deprecated since View Composer will no longer be supported from Horizon version 2012 onwards._

Validate the certificate when View Composer instance is co-installed with Virtual Center.

Privileges

Privilege |  Description
---|---
GLOBAL_CONFIG_VIEW|  Global configuration (read-only) is required to validate a certificate.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Certificate](vdi.utils.Certificate.md) used to make the method call.
**spec**| [ViewComposerWithVCSpec](vdi.utils.Certificate.ViewComposerWithVCSpec.md)|  Specification of View Composer co-installed with Virtual Center.




Return Value

Type |  Description
---|---
[CertificateData](vdi.utils.Certificate.CertificateData.md)| null iff successful else [CertificateData](vdi.utils.Certificate.CertificateData.md) describing the server certificate



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition












 


[^225]: [ServerSpec](vdi.utils.Certificate.ServerSpec.md).
[^226]: [SAMLAuthenticatorServerData](vdi.infrastructure.SAMLAuthenticator.ServerData.md).