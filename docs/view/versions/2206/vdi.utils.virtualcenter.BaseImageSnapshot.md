---
layout: page
title: Service - BaseImageSnapshot
hide:
 #- navigation
 - toc
---

  
  
  



Java Class
    com.vmware.vdi.vlsi.binding.vdi.utils.virtualcenter.BaseImageSnapshot  
See also
     [BaseImageSnapshotInfo](vdi.utils.virtualcenter.BaseImageSnapshot.BaseImageSnapshotInfo.md), [BaseImageVmId](vdi.entity.BaseImageVmId.md)  
Since 
    Horizon View 6.0

  


## Service Description

The object for fetching VMs and snapshots from VirtualCenter. 

Methods

Methods defined in this Service   
---  
BaseImageSnapshot_List  
  



Gets a list of VM snapshots from VC, for a given VM. Requires at least one of the listed privileges. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_VIEW|  privilege is required to get the list of BaseImageSnapshotInfo.   
VC_CONFIG_VIEW|  privilege is required to get the list of BaseImageSnapshotInfo.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [BaseImageSnapshot](vdi.utils.virtualcenter.BaseImageSnapshot.md) used to make the method call.   
**baseImageVm**| [BaseImageVmId](vdi.entity.BaseImageVmId.md)|  unique identifier for VM entry.   
  
  


Return Value 

Type |  Description   
---|---  
[BaseImageSnapshotInfo[]](vdi.utils.virtualcenter.BaseImageSnapshot.BaseImageSnapshotInfo.md)| Array of BaseImageSnapshotInfo  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  
  
  
  
  

