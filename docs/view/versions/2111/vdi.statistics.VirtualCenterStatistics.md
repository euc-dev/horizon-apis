---
layout: page
title: Service - VirtualCenterStatistics
hide:
 #- navigation
 - toc
---

  
   
  



Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.statistics.VirtualCenterStatistics`

See also  
> [VirtualCenterId](vdi.entity.VirtualCenterId.md), [VirtualCenterSummaryStatistics](vdi.statistics.VirtualCenterStatistics.VirtualCenterSummaryStatistics.md)

Since  
> Horizon 7.8


  


## Service Description

Service for retrieving statistics information on Virtual Center servers. 

Methods

Methods defined in this Service   
---  
VirtualCenterStatistics_getSummaryStatistics, VirtualCenterStatistics_listSummaryStatistics  
  



Gets the Virtual Center summary statistics for a specified Virtual Center server. 

Privileges 

Privilege |  Description   
---|---  
VC_CONFIG_VIEW|  privilege is required to list Virtual Center summary statistics.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [VirtualCenterStatistics](vdi.statistics.VirtualCenterStatistics.md) used to make the method call.   
**id**| [VirtualCenterId](vdi.entity.VirtualCenterId.md)|  The ID of the Virtual Center server.   
  
  


Return Value 

Type |  Description   
---|---  
[VirtualCenterSummaryStatistics](vdi.statistics.VirtualCenterStatistics.VirtualCenterSummaryStatistics.md)| summary statistics information on the specified server.  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



Gets the Virtual Center summary statistics for all Virtual Center servers. 

Privileges 

Privilege |  Description   
---|---  
VC_CONFIG_VIEW|  privilege is required to list Virtual Center summary statistics.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [VirtualCenterStatistics](vdi.statistics.VirtualCenterStatistics.md) used to make the method call.   
  


Return Value 

Type |  Description   
---|---  
[VirtualCenterSummaryStatistics[]](vdi.statistics.VirtualCenterStatistics.VirtualCenterSummaryStatistics.md)| A list of summary statistics information on all Virtual Center servers.  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  
  
  
  
  
