---
layout: page
title: Service - ResourceSettings
hide:
#  - navigation
  - toc
---







Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.utils.ResourceSettings`

See also
> [ResourceSettingsInfo](vdi.utils.ResourceSettings.ResourceSettingsInfo.md)

Since
> Horizon 7.6





## Service Description

**Methods**

Methods defined in this Service:
ResourceSettings_Get




Gets the global settings that can be used with resources like Desktops, Farms.

**Privileges**

Privilege | Description
:---|:---
POOL_VIEW|  privilege is required to get any Desktop and/or Farm related settings.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ResourceSettings](vdi.utils.ResourceSettings.md) used to make the method call.



**Return Value**

Type | Description
:---|:---
[ResourceSettingsInfo](vdi.utils.ResourceSettings.ResourceSettingsInfo.md)| The ResourceSettingsInfo object.



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition












 
