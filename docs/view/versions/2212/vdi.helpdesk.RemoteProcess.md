---
layout: page
title: Service - RemoteProcess
hide:
#- navigation
- toc
---







Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.helpdesk.RemoteProcess`

See also
> [RemoteProcessBase](vdi.helpdesk.RemoteProcess.RemoteProcessBase.md), [SessionId](vdi.entity.SessionId.md)

Since
> Horizon 7.3





## Service Description

The service for operating remote virtual desktop process.

**Methods**

Methods defined in this Service:
RemoteProcess_EndProcess




Terminate a process running on virtual machine by session Id and the basic process information.

**Privileges**

Privilege | Description
:---|:---
MANAGE_REMOTE_PROCESS|  Remote process management with the corresponding access group permission is required to terminate a remote process.
MACHINE_MANAGEMENT|  Desktop management with the corresponding access group permission is sufficient to terminate a remote process.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [RemoteProcess](vdi.helpdesk.RemoteProcess.md) used to make the method call.
**id**| [SessionId](vdi.entity.SessionId.md)|  ID of the session which contains the process to be terminated.
**process**| [RemoteProcessBase](vdi.helpdesk.RemoteProcess.RemoteProcessBase.md)|  An instance of RemoteProcessBase class. It contains remote process basic information which used to identify a remote process.




**Return Value**

Type | Description
:---|:---
xsd:boolean| True if end process action executes successfully, otherwise return false.



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition












 
