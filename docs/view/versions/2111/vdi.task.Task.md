---
layout: page
title: Service - Task
hide:
#- navigation
- toc
---







Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.task.Task`

See also
> [TaskId](vdi.entity.TaskId.md), [TaskInfo](vdi.task.Task.TaskInfo.md)

Since
> Horizon View 6.0





## Service Description

The task management service.

Methods

Methods defined in this Service
---
Task_Cancel, Task_Get




Cancels the specified task.

Privileges

Privilege |  Description
---|---
FEDERATED_LDAP_MANAGE|  Global LDAP management is required to cancel a task.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Task](vdi.task.Task.md) used to make the method call.
**id**| [TaskId](vdi.entity.TaskId.md)|  The ID of the task to cancel.




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
[InvalidRequest](vdi.fault.InvalidRequest.md)| Thrown if the task is not cancellable.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Gets info on the requested task.

Privileges

Privilege |  Description
---|---
FEDERATED_LDAP_VIEW|  Global LDAP read is required to retrieve information about a task.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Task](vdi.task.Task.md) used to make the method call.
**id**| [TaskId](vdi.entity.TaskId.md)|  The ID of the task.




Return Value

Type |  Description
---|---
[TaskInfo](vdi.task.Task.TaskInfo.md)| A TaskInfo object containing the current state of the task.



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition












 
