---
layout: page
title: Service - PodAssignment
hide:
#- navigation
- toc
---







Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.federation.PodAssignment`

See also
> [PodAssignmentId](vdi.entity.PodAssignmentId.md), [PodAssignmentInfo](vdi.federation.PodAssignment.PodAssignmentInfo.md)

Since
> Horizon View 6.0





## Service Description

This interface represents data about which pod contains resource assignments for a given user and global entitlement. This assigned pod helps brokering make good decisions when trying to launch a resource for a user, especially in cases where a pod is offline and we want to avoid assigning a new resource for an existing user and persistent global entitlement. This data is automatically calculated and created when a new user and global entitlement requests brokering. It is not automatically deleted when user or global entitlement assignments change. Deleting a pod assignment with this interface is generally fine, as it will be re-created when required.

Methods

Methods defined in this Service
---
PodAssignment_Get, PodAssignment_GetInfos




Get the Pod Assignment.

Privileges

Privilege |  Description
---|---
FEDERATED_LDAP_VIEW|  Global LDAP read is required to read a pod assignment.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [PodAssignment](vdi.federation.PodAssignment.md) used to make the method call.
**id**| [PodAssignmentId](vdi.entity.PodAssignmentId.md)|  The pod assignment id




Return Value

Type |  Description
---|---
[PodAssignmentInfo](vdi.federation.PodAssignment.PodAssignmentInfo.md)| The PodAssignmentInfo.



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidState](vdi.fault.InvalidState.md)| Thrown if the Pod Federation has not been initialized.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Get multiple Pod Assignments.

Privileges

Privilege |  Description
---|---
FEDERATED_LDAP_VIEW|  Global LDAP read is required to read multiple pod assignments.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [PodAssignment](vdi.federation.PodAssignment.md) used to make the method call.
**ids**| [PodAssignmentId[]](vdi.entity.PodAssignmentId.md)|  The pod assignment ids




Return Value

Type |  Description
---|---
[PodAssignmentInfo[]](vdi.federation.PodAssignment.PodAssignmentInfo.md)| The PodAssignmentInfos.



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidState](vdi.fault.InvalidState.md)| Thrown if the Pod Federation has not been initialized.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition












 
