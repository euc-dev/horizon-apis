---
layout: page
title: Service - CertificateSSOEnrollmentServer
hide:
#- navigation
- toc
---







Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.infrastructure.CertificateSSOEnrollmentServer`

See also
> [CertificateSSOEnrollmentServerId](vdi.entity.CertificateSSOEnrollmentServerId.md), [CertificateSSOEnrollmentServerInfo](vdi.infrastructure.CertificateSSOEnrollmentServer.CertificateSSOEnrollmentServerInfo.md)

Since
> Horizon 7.0





## Service Description

The Certificate SSO Enrollment Server service interface.

Methods

Methods defined in this Service
---
CertificateSSOEnrollmentServer_Get, CertificateSSOEnrollmentServer_List




Retrieves information about a paired Certificate SSO Enrollment Server.

Privileges

Privilege |  Description
---|---
ADMINISTRATOR_VIEW|  Administrator (read-only) is required to retrieve information about a server.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [CertificateSSOEnrollmentServer](vdi.infrastructure.CertificateSSOEnrollmentServer.md) used to make the method call.
**id**| [CertificateSSOEnrollmentServerId](vdi.entity.CertificateSSOEnrollmentServerId.md)|  The ID of the server.




Return Value

Type |  Description
---|---
[CertificateSSOEnrollmentServerInfo](vdi.infrastructure.CertificateSSOEnrollmentServer.CertificateSSOEnrollmentServerInfo.md)| Information about the specified server.



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Lists the paired Certificate SSO Enrollment Servers.

Privileges

Privilege |  Description
---|---
ADMINISTRATOR_VIEW|  Administrator (read-only) is required to list servers.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [CertificateSSOEnrollmentServer](vdi.infrastructure.CertificateSSOEnrollmentServer.md) used to make the method call.



Return Value

Type |  Description
---|---
[CertificateSSOEnrollmentServerInfo[]](vdi.infrastructure.CertificateSSOEnrollmentServer.CertificateSSOEnrollmentServerInfo.md)| Information about the paired servers.



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition












 
