---
layout: page
title: Service - VmTemplate
hide:
#- navigation
- toc
---







Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.utils.virtualcenter.VmTemplate`

See also
> [DatacenterId](vdi.entity.DatacenterId.md), [VirtualCenterId](vdi.entity.VirtualCenterId.md), [VmTemplateInfo](vdi.utils.virtualcenter.VmTemplate.VmTemplateInfo.md)

Since
> Horizon View 6.0





## Service Description

The object for fetching VM templates from VirtualCenter.

**Methods**

Methods defined in this Service:
VmTemplate_List, VmTemplate_ListByDatacenter




Gets a list of all VM templates from VC suitable for full clone desktop creation. Requires at least one of the listed privileges.

**Privileges**

Privilege | Description
:---|:---
GLOBAL_CONFIG_VIEW|  privilege is required to get the list of VmTemplateInfo.
VC_CONFIG_VIEW|  privilege is required to get the list of VmTemplateInfo.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [VmTemplate](vdi.utils.virtualcenter.VmTemplate.md) used to make the method call.
**virtualCenter**| [VirtualCenterId](vdi.entity.VirtualCenterId.md)|  unique identifier for vc entry




**Return Value**

Type | Description
:---|:---
[VmTemplateInfo[]](vdi.utils.virtualcenter.VmTemplate.VmTemplateInfo.md)| Array of VmTemplateInfo



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Gets a list of all VM templates from the given datacenter suitable for full clone desktop creation. Requires at least one of the listed privileges.

**Privileges**

Privilege | Description
:---|:---
GLOBAL_CONFIG_VIEW|  privilege is required to get the list of VmTemplateInfo.
VC_CONFIG_VIEW|  privilege is required to get the list of VmTemplateInfo.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [VmTemplate](vdi.utils.virtualcenter.VmTemplate.md) used to make the method call.
**datacenter**| [DatacenterId](vdi.entity.DatacenterId.md)|  unique identifier for the data center




**Return Value**

Type | Description
:---|:---
[VmTemplateInfo[]](vdi.utils.virtualcenter.VmTemplate.VmTemplateInfo.md)| Array of VmTemplateInfo



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition












 
