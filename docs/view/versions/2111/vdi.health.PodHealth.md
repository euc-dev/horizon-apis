---
layout: page
title: Service - PodHealth
hide:
#- navigation
- toc
---







Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.health.PodHealth`

See also
> [PodHealthInfo](vdi.health.PodHealth.PodHealthInfo.md), [PodId](vdi.entity.PodId.md)

Since
> Horizon View 6.0





## Service Description

Representing status and health information for PodFederation.

**Methods**

Methods defined in this Service:
PodHealth_Get, PodHealth_List




Get health status on a specified pod.
This operation can only be performed if the current pod is a member pod of a Pod Federation.


**Privileges**

Privilege | Description
:---|:---
FEDERATED_LDAP_VIEW|  Global LDAP read is required to read the health of a pod.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [PodHealth](vdi.health.PodHealth.md) used to make the method call.
**id**| [PodId](vdi.entity.PodId.md)|  pod to get health status for. Cannot be local pod.




**Return Value**

Type | Description
:---|:---
[PodHealthInfo](vdi.health.PodHealth.PodHealthInfo.md)| PodHealthInfo containing health/status information the specified pod



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidState](vdi.fault.InvalidState.md)| Thrown if the Pod Federation has not been initialized
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Get health status on all remote pods in the Multi-DataCenter View Pod Federation.
This operation can only be performed if the current pod is a member pod of a Pod Federation.


**Privileges**

Privilege | Description
:---|:---
FEDERATED_LDAP_VIEW|  Global LDAP read is required to list pod health.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [PodHealth](vdi.health.PodHealth.md) used to make the method call.



**Return Value**

Type | Description
:---|:---
[PodHealthInfo[]](vdi.health.PodHealth.PodHealthInfo.md)| list of PodHealthInfo containing health/status information for all pods except for the local pod.



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidState](vdi.fault.InvalidState.md)| Thrown if this pod is not in the valid state to perform getStatus operation.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition












 
