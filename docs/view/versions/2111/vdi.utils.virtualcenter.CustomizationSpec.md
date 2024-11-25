---
layout: page
title: Service - CustomizationSpec
hide:
#  - navigation
  - toc
---







Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.utils.virtualcenter.CustomizationSpec`

See also
> [CustomizationSpecInfo](vdi.utils.virtualcenter.CustomizationSpec.CustomizationSpecInfo.md), [VirtualCenterId](vdi.entity.VirtualCenterId.md)

Since
> Horizon View 6.0





## Service Description

The service for fetching Customization Spec from VirtualCenter.

**Methods**

Methods defined in this Service:
CustomizationSpec_List




Gets a list of customization specs from VC which may be suitable for desktop creation. Requires at least one of the listed privileges.

**Privileges**

Privilege | Description
:---|:---
GLOBAL_CONFIG_VIEW|  privilege is required to get the list of CustomizationSpecInfo.
VC_CONFIG_VIEW|  privilege is required to get the list of CustomizationSpecInfo.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [CustomizationSpec](vdi.utils.virtualcenter.CustomizationSpec.md) used to make the method call.
**virtualCenter**| [VirtualCenterId](vdi.entity.VirtualCenterId.md)|  unique identifier for VirtualCenter




**Return Value**

Type | Description
:---|:---
[CustomizationSpecInfo[]](vdi.utils.virtualcenter.CustomizationSpec.CustomizationSpecInfo.md)| Array of CustomizationSpecInfo



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition












 
