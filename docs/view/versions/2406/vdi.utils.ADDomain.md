---
layout: page
title: Service - ADDomain
hide:
#- navigation
- toc
---







Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.utils.ADDomain`

See also
> [ADDomainAuxiliaryAccountSpec](vdi.utils.ADDomain.ADDomainAuxiliaryAccountSpec.md), [ADDomainAuxiliaryAccountUpdateSpec](vdi.utils.ADDomain.ADDomainAuxiliaryAccountUpdateSpec.md), [ADDomainId](vdi.entity.ADDomainId.md), [ADDomainInfo](vdi.utils.ADDomain.ADDomainInfo.md), [ADDomainSpec](vdi.utils.ADDomain.ADDomainSpec.md), [MapEntry](vdi.util.MapEntry.md), [ServiceAccountCredentialsId](vdi.entity.ServiceAccountCredentialsId.md)

Since
> Horizon View 6.0





## Service Description

Provides the ability to retrieve domain information for the View Cluster.

**Methods**

Methods defined in this Service:
ADDomain_AddAuxiliaryAccounts, ADDomain_Bind, ADDomain_DeleteAuxiliaryAccounts, ADDomain_List, ADDomain_Unbind, ADDomain_Update, ADDomain_UpdateAuxiliaryAccounts




Add auxiliary service accounts to the no-trust domain.

**Privileges**

Privilege | Description
:---|:---
GLOBAL_CONFIG_MANAGEMENT|  Global configuration management is required to add auxiliary service accounts to the no-trust domain.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ADDomain](vdi.utils.ADDomain.md) used to make the method call.
**spec**| [ADDomainAuxiliaryAccountSpec](vdi.utils.ADDomain.ADDomainAuxiliaryAccountSpec.md)|  Specification of auxiliary service accounts.




**Return Value**

Type | Description
:---|:---
None



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[PartialFailureFault](vdi.fault.PartialFailureFault.md)| Thrown if one or more service accounts can not be added.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



**Events**

Event | Description
:---|:---
AUXILIARY_ACCOUNT_ADD_SUCCESS|  If the auxiliary service account added successfully.

Show WSDL type definition







Bind no-trust domain to connection server.

**Privileges**

Privilege | Description
:---|:---
GLOBAL_CONFIG_MANAGEMENT|  Global configuration management is required to bind no-trust domain.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ADDomain](vdi.utils.ADDomain.md) used to make the method call.
**spec**| [ADDomainSpec](vdi.utils.ADDomain.ADDomainSpec.md)|  Specification of domain to bind.




**Return Value**

Type | Description
:---|:---
[ADDomainId](vdi.entity.ADDomainId.md)| [ADDomainId](vdi.entity.ADDomainId.md) Domain Id of no-trust domain bound to connection server



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



**Events**

Event | Description
:---|:---
NOTRUST_DOMAIN_BOUND|  If the no-trust domain successfully created.

Show WSDL type definition







Delete auxiliary service accounts from the no-trust domain.

**Privileges**

Privilege | Description
:---|:---
GLOBAL_CONFIG_MANAGEMENT|  Global configuration management is required to delete auxiliary service accounts from the no-trust domain.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ADDomain](vdi.utils.ADDomain.md) used to make the method call.
**id**| [ADDomainId](vdi.entity.ADDomainId.md)|  Entity id for the no-trust domain.
**ids**| [ServiceAccountCredentialsId[]](vdi.entity.ServiceAccountCredentialsId.md)|  Entity Id's for the auxiliary service accounts




**Return Value**

Type | Description
:---|:---
None



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[PartialFailureFault](vdi.fault.PartialFailureFault.md)| Thrown if one or more service accounts can not be deleted.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



**Events**

Event | Description
:---|:---
AUXILIARY_ACCOUNT_DELETE_SUCCESS|  If the auxiliary service account deleted successfully.

Show WSDL type definition







Lists the Active Directory domains.

**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ADDomain](vdi.utils.ADDomain.md) used to make the method call.



**Return Value**

Type | Description
:---|:---
[ADDomainInfo[]](vdi.utils.ADDomain.ADDomainInfo.md)| A list of [ADDomainInfo](vdi.utils.ADDomain.ADDomainInfo.md) containing information about the domains.



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Unbind no-trust domain from connection server.All the service accounts of no-trust domain will be deleted. There must be no entitlements for users/groups belonging to it.

**Privileges**

Privilege | Description
:---|:---
GLOBAL_CONFIG_MANAGEMENT|  Global configuration management is required to delete no-trust domain.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ADDomain](vdi.utils.ADDomain.md) used to make the method call.
**domainId**| [ADDomainId](vdi.entity.ADDomainId.md)|




**Return Value**

Type | Description
:---|:---
None



**Faults**

Type | Description
:---|:---
[EntityInUse](vdi.fault.EntityInUse.md)| Thrown if entitlements are associated with no-trust domain.
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



**Events**

Event | Description
:---|:---
NOTRUST_DOMAIN_UNBOUND|  If the no-trust domain was successfully unbound.

Show WSDL type definition







Update no-trust domain with the set of attributes in the map.

**Privileges**

Privilege | Description
:---|:---
GLOBAL_CONFIG_MANAGEMENT|  Global configuration management is required to update no-trust domain.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ADDomain](vdi.utils.ADDomain.md) used to make the method call.
**id**| [ADDomainId](vdi.entity.ADDomainId.md)|  Entity id for the no-trust domain.
**updates**| [MapEntry[]](vdi.util.MapEntry.md)|  Key value pairs describing attributes to be updated. [^190]





**Return Value**

Type | Description
:---|:---
None



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



**Events**

Event | Description
:---|:---
NOTRUST_DOMAIN_UPDATED|  If the no-trust domain was successfully updated.

Show WSDL type definition







Update Auxiliary service accounts of no-trust domain.

**Privileges**

Privilege | Description
:---|:---
GLOBAL_CONFIG_MANAGEMENT|  Global configuration management is required to update auxiliary service accounts to the no-trust domain.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ADDomain](vdi.utils.ADDomain.md) used to make the method call.
**updateSpec**| [ADDomainAuxiliaryAccountUpdateSpec](vdi.utils.ADDomain.ADDomainAuxiliaryAccountUpdateSpec.md)|  Specification to update auxiliary accounts




**Return Value**

Type | Description
:---|:---
None



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[PartialFailureFault](vdi.fault.PartialFailureFault.md)| Thrown if one or more service accounts can not be updated.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



**Events**

Event | Description
:---|:---
AUXILIARY_ACCOUNT_UPDATE_SUCCESS|  If the auxiliary service account updated successfully.

Show WSDL type definition












 


[^190]: This parameter is an update map based on [ADDomainInfo](vdi.utils.ADDomain.ADDomainInfo.md "ADDomainInfo").