---
layout: page
title: Service - UsageStatistics
hide:
 #- navigation
 - toc
---

  
  
  



Java Class
    com.vmware.vdi.vlsi.binding.vdi.statistics.UsageStatistics  
See also
     [UsageStatisticsLicensingCountersInfo](vdi.statistics.UsageStatistics.LicensingCountersInfo.md)  
Since 
    Horizon 7.9

  


## Service Description

Usage Statistics. 

Methods

Methods defined in this Service   
---  
UsageStatistics_GetLicensingCounters, UsageStatistics_ResetHighestUsageCount, UsageStatistics_ResetNamedUsersCount  
  



The current and highest historical usage numbers. These numbers can be used to keep track of the product license usage. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_VIEW|  Global configuration view is required to read the licensing counters.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [UsageStatistics](vdi.statistics.UsageStatistics.md) used to make the method call.   
  


Return Value 

Type |  Description   
---|---  
[UsageStatisticsLicensingCountersInfo](vdi.statistics.UsageStatistics.LicensingCountersInfo.md)| product license usage statistics.  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



The highest historical number of concurrent connections will be reset to the current number. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_MANAGEMENT|  Global configuration management is required to reset highest usage count.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [UsageStatistics](vdi.statistics.UsageStatistics.md) used to make the method call.   
  


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
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  


Events 

Event |  Description   
---|---  
VLSI_CCU_RESET|  If the highest count is reset.   
  
Show WSDL type definition

  
  
  



The highest historical number of named users will be reset to zero. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_MANAGEMENT|  Global configuration management is required to reset named users count.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [UsageStatistics](vdi.statistics.UsageStatistics.md) used to make the method call.   
  


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
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  


Events 

Event |  Description   
---|---  
VLSI_NU_RESET|  Global If the named users count is reset.   
  
Show WSDL type definition

  
  
  
  
  
  
  

