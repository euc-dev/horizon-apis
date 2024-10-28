---
layout: page
title: Service - DesktopTask
hide:
#- navigation
- toc
---







Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.task.DesktopTask`

See also
> [DesktopId](vdi.entity.DesktopId.md), [DesktopTaskId](vdi.entity.DesktopTaskId.md), [DesktopTaskInfo](vdi.task.DesktopTask.DesktopTaskInfo.md), [ResumeTaskSpec](vdi.task.DesktopTask.ResumeTaskSpec.md)

Since
> Horizon 7.4





## Service Description

Interface for managing desktop related tasks

Methods

Methods defined in this Service
---
DesktopTask_Cancel, DesktopTask_Get, DesktopTask_List, DesktopTask_Pause, DesktopTask_Resume




Cancels the specified task on a desktop. Requires one or more of the listed privileges based on the task.

Privileges

Privilege |  Description
---|---
POOL_SVI_IMAGE_MANAGEMENT|  Manage maintenance operations on Automated Desktops & Farms privilege with the corresponding access group permission is required to cancel the task related to rebalance, refresh, resync, push image or checkpoint operation.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [DesktopTask](vdi.task.DesktopTask.md) used to make the method call.
**id**| [DesktopTaskId](vdi.entity.DesktopTaskId.md)|  unique id of desktopTask




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

Show WSDL type definition







Gets info on the specified task on a desktop.

Privileges

Privilege |  Description
---|---
POOL_VIEW|  Desktop read privilege with the corresponding access group permission is required to read a desktop.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [DesktopTask](vdi.task.DesktopTask.md) used to make the method call.
**id**| [DesktopTaskId](vdi.entity.DesktopTaskId.md)|  unique id of desktopTask




Return Value

Type |  Description
---|---
[DesktopTaskInfo](vdi.task.DesktopTask.DesktopTaskInfo.md)| DesktopTaskInfo object containing the current state of the task.



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Lists info for all tasks on a desktop.

Privileges

Privilege |  Description
---|---
POOL_VIEW|  Desktop read privilege with the corresponding access group permission is required to read a desktop.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [DesktopTask](vdi.task.DesktopTask.md) used to make the method call.
**id**| [DesktopId](vdi.entity.DesktopId.md)|  unique identifier for a desktop entry.




Return Value

Type |  Description
---|---
[DesktopTaskInfo[]](vdi.task.DesktopTask.DesktopTaskInfo.md)| Array of DesktopTaskInfo objects containing the current states of the tasks on a desktop.



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Pauses the specified task on a desktop. Requires one or more of the listed privileges based on the task.

Privileges

Privilege |  Description
---|---
POOL_SVI_IMAGE_MANAGEMENT|  Manage maintenance operations on Automated Desktops & Farms privilege with the corresponding access group permission is required to pause the task related to rebalance, refresh, resync, push image or checkpoint operation.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [DesktopTask](vdi.task.DesktopTask.md) used to make the method call.
**id**| [DesktopTaskId](vdi.entity.DesktopTaskId.md)|  unique id of desktopTask




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

Show WSDL type definition







Resumes the specified task on a desktop. Requires one or more of the listed privileges based on the task.

Privileges

Privilege |  Description
---|---
POOL_SVI_IMAGE_MANAGEMENT|  Manage maintenance operations on Automated Desktops & Farms privilege with the corresponding access group permission is required to resume the task related to rebalance, refresh, resync, push image or checkpoint operation.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [DesktopTask](vdi.task.DesktopTask.md) used to make the method call.
**id**| [DesktopTaskId](vdi.entity.DesktopTaskId.md)|  unique id of desktopTask
**resumeTaskSpec**| [ResumeTaskSpec](vdi.task.DesktopTask.ResumeTaskSpec.md)|  ResumeTaskSpec object for additional params [^135]





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

Show WSDL type definition












 


[^135]: This parameter need not be set.