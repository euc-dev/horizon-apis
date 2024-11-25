---
layout: page
title: Service - AdvancedSettings
hide:
#  - navigation
  - toc
---







Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.utils.AdvancedSettings`

See also
> [EntityId](vdi.EntityId.md), [MapEntry](vdi.util.MapEntry.md)

Since
> Horizon View 6.0





## Service Description

Provides the ability to set advanced settings for View.

**Methods**

Methods defined in this Service:
AdvancedSettings_Get, AdvancedSettings_Perform, AdvancedSettings_Set




Gets advanced settings for an entity.

**Privileges**

Privilege | Description
:---|:---
ADMINISTRATOR_VIEW|  Administrator (read-only) is required to get advanced settings.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [AdvancedSettings](vdi.utils.AdvancedSettings.md) used to make the method call.
**id**| [EntityId](vdi.EntityId.md)|  The (optional) ID of the entity to manage. [^135]
**keys**|  xsd:string[]|  The keys of the settings to retrieve.




**Return Value**

Type | Description
:---|:---
[MapEntry[]](vdi.util.MapEntry.md)| A map from key to value of the requested advanced settings.



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Performs an advanced operation.

**Privileges**

Privilege | Description
:---|:---
ADMINISTRATOR|  Administrator is required to perform advanced operations.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [AdvancedSettings](vdi.utils.AdvancedSettings.md) used to make the method call.
**id**| [EntityId](vdi.EntityId.md)|  The entity to set advanced settings on. [^135]
**operationName**|  xsd:string|  The name of the operation to perform.
**parameters**| [MapEntry[]](vdi.util.MapEntry.md)|  A map from key to value of the parameters of the operation. [^135]





**Return Value**

Type | Description
:---|:---
xsd:anyType| The result of the operation. The type of this return will vary.



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Sets advanced settings on an entity.

**Privileges**

Privilege | Description
:---|:---
ADMINISTRATOR|  Administrator is required to set advanced settings.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [AdvancedSettings](vdi.utils.AdvancedSettings.md) used to make the method call.
**id**| [EntityId](vdi.EntityId.md)|  The entity to set advanced settings on. [^135]
**values**| [MapEntry[]](vdi.util.MapEntry.md)|  The settings to set.




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

Show WSDL type definition












 


[^135]: This parameter need not be set.