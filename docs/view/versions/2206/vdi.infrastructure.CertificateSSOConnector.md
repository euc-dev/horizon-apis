---
layout: page
title: Service - CertificateSSOConnector
hide:
#- navigation
- toc
---







Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.infrastructure.CertificateSSOConnector`

See also
> [CertificateSSOConnectorId](vdi.entity.CertificateSSOConnectorId.md), [CertificateSSOConnectorInfo](vdi.infrastructure.CertificateSSOConnector.CertificateSSOConnectorInfo.md), [CertificateSSOConnectorSpec](vdi.infrastructure.CertificateSSOConnector.CertificateSSOConnectorSpec.md), [MapEntry](vdi.util.MapEntry.md)

Since
> Horizon 7.0





## Service Description

The Certificate SSO Connector service interface.

Methods

Methods defined in this Service
---
CertificateSSOConnector_Create, CertificateSSOConnector_Delete, CertificateSSOConnector_Get, CertificateSSOConnector_List, CertificateSSOConnector_Update




Creates a Certificate SSO Connector.

Privileges

Privilege |  Description
---|---
ADMINISTRATOR|  Administrator is required to create a connector.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [CertificateSSOConnector](vdi.infrastructure.CertificateSSOConnector.md) used to make the method call.
**spec**| [CertificateSSOConnectorSpec](vdi.infrastructure.CertificateSSOConnector.CertificateSSOConnectorSpec.md)|  The specification of the connector.




Return Value

Type |  Description
---|---
[CertificateSSOConnectorId](vdi.entity.CertificateSSOConnectorId.md)| The ID of the newly created connector.



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



Events

Event |  Description
---|---
VLSI_CERT_SSO_CONNECTOR_CREATED|  If the connector was successfully created.
VLSI_CERT_SSO_CONNECTOR_CREATE_FAILED|  If the connector could not be created.

Show WSDL type definition







Deletes the specified Certificate SSO Connector.

Privileges

Privilege |  Description
---|---
ADMINISTRATOR|  Administrator is required to delete a connector.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [CertificateSSOConnector](vdi.infrastructure.CertificateSSOConnector.md) used to make the method call.
**id**| [CertificateSSOConnectorId](vdi.entity.CertificateSSOConnectorId.md)|  The ID of the connector to delete.




Return Value

Type |  Description
---|---
None



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



Events

Event |  Description
---|---
VLSI_CERT_SSO_CONNECTOR_DELETED|  If the connector was successfully deleted.
VLSI_CERT_SSO_CONNECTOR_DELETE_FAILED|  If the connector could not be deleted.

Show WSDL type definition







Retrieves information about a Certificate SSO Connector.

Privileges

Privilege |  Description
---|---
ADMINISTRATOR_VIEW|  Administrator (read-only) is required to retrieve information about a connector.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [CertificateSSOConnector](vdi.infrastructure.CertificateSSOConnector.md) used to make the method call.
**id**| [CertificateSSOConnectorId](vdi.entity.CertificateSSOConnectorId.md)|  The ID of the connector.




Return Value

Type |  Description
---|---
[CertificateSSOConnectorInfo](vdi.infrastructure.CertificateSSOConnector.CertificateSSOConnectorInfo.md)| Information about the specified connector.



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Lists the configured Certificate SSO Connectors.

Privileges

Privilege |  Description
---|---
ADMINISTRATOR_VIEW|  Administrator (read-only) is required to list connectors.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [CertificateSSOConnector](vdi.infrastructure.CertificateSSOConnector.md) used to make the method call.



Return Value

Type |  Description
---|---
[CertificateSSOConnectorInfo[]](vdi.infrastructure.CertificateSSOConnector.CertificateSSOConnectorInfo.md)| Information about the configured connectors.



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Updates a Certificate SSO Connector.

Privileges

Privilege |  Description
---|---
ADMINISTRATOR|  Administrator is required to update a connector.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [CertificateSSOConnector](vdi.infrastructure.CertificateSSOConnector.md) used to make the method call.
**id**| [CertificateSSOConnectorId](vdi.entity.CertificateSSOConnectorId.md)|  The ID of the connector to update.
**updates**| [MapEntry[]](vdi.util.MapEntry.md)|  Key value pairs describing attributes to be updated. [^246]





Return Value

Type |  Description
---|---
None



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



Events

Event |  Description
---|---
VLSI_CERT_SSO_CONNECTOR_UPDATED|  If the connector was successfully updated.
VLSI_CERT_SSO_CONNECTOR_UPDATE_FAILED|  If the connector could not be updated.

Show WSDL type definition












 


[^246]: This parameter is an update map based on [CertificateSSOConnectorInfo](vdi.infrastructure.CertificateSSOConnector.CertificateSSOConnectorInfo.md "CertificateSSOConnectorInfo").