---
layout: page
title: Service - Syslog
hide:
#- navigation
- toc
---







Java Class
> `com.vmware.vdi.vlsi.binding.vdi.infrastructure.Syslog`

See also
> [MapEntry](vdi.util.MapEntry.md), [SyslogInfo](vdi.infrastructure.Syslog.SyslogInfo.md)

Since
> Horizon View 6.0





## Service Description

The Syslog service interface.

Methods

Methods defined in this Service
---
Syslog_Get, Syslog_Update




Gets the SyslogInfo.

Privileges

Privilege |  Description
---|---
GLOBAL_CONFIG_VIEW|  Global configuration view privilege is required to read Syslog settings.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Syslog](vdi.infrastructure.Syslog.md) used to make the method call.



Return Value

Type |  Description
---|---
[SyslogInfo](vdi.infrastructure.Syslog.SyslogInfo.md)| Root syslog configuration information object.



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Update syslog configuration with the set of attributes in the map.

Privileges

Privilege |  Description
---|---
GLOBAL_CONFIG_MANAGEMENT|  Global configuration management privilege is required to update Syslog settings.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Syslog](vdi.infrastructure.Syslog.md) used to make the method call.
**updates**| [MapEntry[]](vdi.util.MapEntry.md)|  Key value pairs describing attributes to be updated. [^303]





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
[InvalidRequest](vdi.fault.InvalidRequest.md)| Thrown if UNC username is changed without changing UNC password, or either UNC path or UNC username is missing when attempting to use a remote file server.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition












 
