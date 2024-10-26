---
layout: page
title: Service - Pod
hide:
#- navigation
- toc
---







Java Class
> `com.vmware.vdi.vlsi.binding.vdi.federation.Pod`

See also
> [MapEntry](vdi.util.MapEntry.md), [PodId](vdi.entity.PodId.md), [PodInfo](vdi.federation.Pod.PodInfo.md)

Since
> Horizon View 6.0





## Service Description

Interface representing a Pod object in a Multi-DataCenter View Pod Federation.

Methods

Methods defined in this Service
---
Pod_Get, Pod_List, Pod_Update




Get information about a specific pod in the Multi-DataCenter View Pod Federation that the local pod is a member of.


Privileges

Privilege |  Description
---|---
FEDERATED_LDAP_VIEW|  Global LDAP read is required to read a pod.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Pod](vdi.federation.Pod.md) used to make the method call.
**id**| [PodId](vdi.entity.PodId.md)|  the id of the pod to get




Return Value

Type |  Description
---|---
[PodInfo](vdi.federation.Pod.PodInfo.md)| PodInfo for the pod



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidState](vdi.fault.InvalidState.md)| Thrown if this pod is not part of a Pod Federation
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







List all pods in the Multi-DataCenter View Pod Federation that the local pod is a member of.

Privileges

Privilege |  Description
---|---
FEDERATED_LDAP_VIEW|  Global LDAP read is required to list pods.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Pod](vdi.federation.Pod.md) used to make the method call.



Return Value

Type |  Description
---|---
[PodInfo[]](vdi.federation.Pod.PodInfo.md)| All podInfo for the Pod Federation



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidState](vdi.fault.InvalidState.md)| Thrown if this pod is not part of a Pod Federation
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Update display name, description, or Site for the pod with the given podId. Note endpoints and activeGlobalEntitlements are maintained by the system and can not be updated using this method.

Privileges

Privilege |  Description
---|---
FEDERATED_LDAP_MANAGE|  Global LDAP management is required to update a pod.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Pod](vdi.federation.Pod.md) used to make the method call.
**id**| [PodId](vdi.entity.PodId.md)|  the id of the pod to be updated.
**updates**| [MapEntry[]](vdi.util.MapEntry.md)|  key value pairs describing attributes to be updated. Only displayName and description are permitted for update. [^230]





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
[InvalidRequest](vdi.fault.InvalidRequest.md)| Thrown if the update map contains invalid or non-permitted fields
[InvalidState](vdi.fault.InvalidState.md)| Thrown if the Pod Federation has not been initialized.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



Events

Event |  Description
---|---
VLSI_POD_UPDATE_SUCCESS|  If the pod was successfully updated.
VLSI_POD_UPDATE_FAILURE|  If the pod could not be updated.

Show WSDL type definition












 


[^230]: This parameter is an update map based on [PodInfo](vdi.federation.Pod.PodInfo.md "PodInfo").