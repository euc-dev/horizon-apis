---
layout: page
title: Service - BaseImageVm
hide:
 #- navigation
 - toc
---

  
   
  



Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.utils.virtualcenter.BaseImageVm`

See also  
> [BaseImageVmId](vdi.entity.BaseImageVmId.md), [BaseImageVmInfo](vdi.utils.virtualcenter.BaseImageVm.BaseImageVmInfo.md), [DatacenterId](vdi.entity.DatacenterId.md), [VirtualCenterId](vdi.entity.VirtualCenterId.md)

Since  
> Horizon View 6.0


  


## Service Description

The object for fetching VMs and snapshots from VirtualCenter. 

Methods

Methods defined in this Service   
---  
BaseImageVm_Get, BaseImageVm_List, BaseImageVm_ListByDatacenter  
  



Gets Base Image VM Information 

Privileges 

Privilege |  Description   
---|---  
VC_CONFIG_VIEW|  privilege is required to get BaseImageVmInfo.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [BaseImageVm](vdi.utils.virtualcenter.BaseImageVm.md) used to make the method call.   
**id**| [BaseImageVmId](vdi.entity.BaseImageVmId.md)|  BaseImageVmId   
  
  


Return Value 

Type |  Description   
---|---  
[BaseImageVmInfo](vdi.utils.virtualcenter.BaseImageVm.BaseImageVmInfo.md)| BaseImageVmInfo  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



Gets a list of all BaseImage VMs from VC which may be suitable as snapshots for linked clone desktop or farm creation. Requires at least one of the listed privileges. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_VIEW|  privilege is required to get the list of BaseImageVmInfo.   
VC_CONFIG_VIEW|  privilege is required to get the list of BaseImageVmInfo.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [BaseImageVm](vdi.utils.virtualcenter.BaseImageVm.md) used to make the method call.   
**virtualCenter**| [VirtualCenterId](vdi.entity.VirtualCenterId.md)|  unique identifier for vc entry   
  
**filterIncompatibleVms**|  xsd:boolean|  do not return incompatible VMs which cannot be used for pool or farm creations. Default is false.  **_Since_** Horizon 7.13  


  * This parameter need not be set.

  
  


Return Value 

Type |  Description   
---|---  
[BaseImageVmInfo[]](vdi.utils.virtualcenter.BaseImageVm.BaseImageVmInfo.md)| Array of BaseImageVmInfo  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



Gets a list of all BaseImage VMs from the given datacenter which may be suitable as snapshots for linked clone desktop or farm creation. Requires at least one of the listed privileges. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_VIEW|  privilege is required to get the list of BaseImageVmInfo.   
VC_CONFIG_VIEW|  privilege is required to get the list of BaseImageVmInfo.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [BaseImageVm](vdi.utils.virtualcenter.BaseImageVm.md) used to make the method call.   
**datacenter**| [DatacenterId](vdi.entity.DatacenterId.md)|  unique identifier for datacenter entry   
  
**filterIncompatibleVms**|  xsd:boolean|  do not return incompatible VMs which cannot be used for pool or farm creations. Default is false.  **_Since_** Horizon 7.13  


  * This parameter need not be set.

  
  


Return Value 

Type |  Description   
---|---  
[BaseImageVmInfo[]](vdi.utils.virtualcenter.BaseImageVm.BaseImageVmInfo.md)| Array of BaseImageVmInfo  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  
  
  
  
  
