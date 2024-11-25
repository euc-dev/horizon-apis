---
layout: page
title: Service - CertificateSSOConnectorHealth
hide:
#  - navigation
  - toc
---







Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.health.CertificateSSOConnectorHealth`

See also
> [CertificateSSOConnectorHealthInfo](vdi.health.CertificateSSOConnectorHealth.CertificateSSOConnectorHealthInfo.md), [CertificateSSOConnectorId](vdi.entity.CertificateSSOConnectorId.md)

Since
> Horizon 7.0





## Service Description

Service for retrieving health information on CertSSO connectors.

**Methods**

Methods defined in this Service:
CertificateSSOConnectorHealth_Get, CertificateSSOConnectorHealth_List




Gets the health of the specified CertSSO connector.

**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [CertificateSSOConnectorHealth](vdi.health.CertificateSSOConnectorHealth.md) used to make the method call.
**id**| [CertificateSSOConnectorId](vdi.entity.CertificateSSOConnectorId.md)|  The ID of the CertSSO connector.




**Return Value**

Type | Description
:---|:---
[CertificateSSOConnectorHealthInfo](vdi.health.CertificateSSOConnectorHealth.CertificateSSOConnectorHealthInfo.md)| The health of the CertSSO connector.



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Gets the health of all CertSSO connectors associated with this View cluster.

**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [CertificateSSOConnectorHealth](vdi.health.CertificateSSOConnectorHealth.md) used to make the method call.



**Return Value**

Type | Description
:---|:---
[CertificateSSOConnectorHealthInfo[]](vdi.health.CertificateSSOConnectorHealth.CertificateSSOConnectorHealthInfo.md)| The health of all CertSSO connectors.



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition












 
