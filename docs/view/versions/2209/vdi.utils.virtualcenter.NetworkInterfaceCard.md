---
layout: page
title: Service - NetworkInterfaceCard
hide:
 #- navigation
 - toc
---

  
| | | Local Methods  
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  



Java Class
    com.vmware.vdi.vlsi.binding.vdi.utils.virtualcenter.NetworkInterfaceCard
See also
     [BaseImageSnapshotId](vdi.entity.BaseImageSnapshotId.md), [NetworkInterfaceCardInfo](vdi.utils.virtualcenter.NetworkInterfaceCard.NetworkInterfaceCardInfo.md), [VmTemplateId](vdi.entity.VmTemplateId.md)
Since 
    Horizon View 6.0

  


## Service Description

The service for fetching network interface cards (NICs) from VirtualCenter. 

Methods

Methods defined in this Service   
---  
NetworkInterfaceCard_ListBySnapshot, NetworkInterfaceCard_ListByTemplate  
  



Returns a list of network interface cards (NICs) present on the given snapshot suitable for configuration on a linked-clone desktop based on a parent image with that snapshot. Requires at least one of the listed privileges. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_VIEW|  privilege is required to get the NICs.   
VC_CONFIG_VIEW|  privilege is required to get the NICs.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [NetworkInterfaceCard](vdi.utils.virtualcenter.NetworkInterfaceCard.md) used to make the method call.   
**baseImageSnapshot**| [BaseImageSnapshotId](vdi.entity.BaseImageSnapshotId.md)|  The BaseImageSnapshot id   
  
  


Return Value 

Type |  Description   
---|---  
[NetworkInterfaceCardInfo[]](vdi.utils.virtualcenter.NetworkInterfaceCard.NetworkInterfaceCardInfo.md)| An array of NetworkInterfaceCardInfos  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



Returns a list of network interface cards (NICs) present on the given template suitable for configuration on a full-clone desktop based on a parent image with that template. Requires at least one of the listed privileges. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_VIEW|  privilege is required to get the NICs.   
VC_CONFIG_VIEW|  privilege is required to get the NICs.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [NetworkInterfaceCard](vdi.utils.virtualcenter.NetworkInterfaceCard.md) used to make the method call.   
**template**| [VmTemplateId](vdi.entity.VmTemplateId.md)|  The template id   
  
  


Return Value 

Type |  Description   
---|---  
[NetworkInterfaceCardInfo[]](vdi.utils.virtualcenter.NetworkInterfaceCard.NetworkInterfaceCardInfo.md)| An array of NetworkInterfaceCardInfos  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  
  
Top of page| | | Local Methods  
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

