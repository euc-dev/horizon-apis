---
layout: page
title: Service - SecurityServerHealth
hide:
 #- navigation
 - toc
---

  
   
  



Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.health.SecurityServerHealth`

See also  
> [SecurityServerHealthInfo](vdi.health.SecurityServerHealth.SecurityServerHealthInfo.md), [SecurityServerId](vdi.entity.SecurityServerId.md)

Since  
> Horizon View 6.0


  


## Service Description

**Deprecated.**_This service is being deprecated since Security Server will no longer be supported in future releases. Please consider using Unified Access Gateway (UAG) instead._

Service for retrieving health information on security servers. 

Methods

Methods defined in this Service   
---  
SecurityServerHealth_Get, SecurityServerHealth_List  
  



**Deprecated.**_This API is being deprecated since Security Server will no longer be supported in future releases. Please consider using Unified Access Gateway (UAG) instead._

Gets the health information for an individual security server. 

Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [SecurityServerHealth](vdi.health.SecurityServerHealth.md) used to make the method call.   
**id**| [SecurityServerId](vdi.entity.SecurityServerId.md)|  The ID of the security server.   
  
  


Return Value 

Type |  Description   
---|---  
[SecurityServerHealthInfo](vdi.health.SecurityServerHealth.SecurityServerHealthInfo.md)| The health information for an individual security server.  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



**Deprecated.**_This API is being deprecated since Security Server will no longer be supported in future releases. Please consider using Unified Access Gateway (UAG) instead._

Gets the health information for all security servers. 

Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [SecurityServerHealth](vdi.health.SecurityServerHealth.md) used to make the method call.   
  


Return Value 

Type |  Description   
---|---  
[SecurityServerHealthInfo[]](vdi.health.SecurityServerHealth.SecurityServerHealthInfo.md)| The health information for all security servers.  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  
  
  
  
  
