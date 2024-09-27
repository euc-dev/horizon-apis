---
layout: page
title: Service - PersistentDiskQueryService
hide:
 #- navigation
 - toc
---

  
 
  



Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.PersistentDiskQueryService  
See also
     [PersistentDiskQueryServiceQuerySpec](vdi.resources.PersistentDiskQueryService.QuerySpec.md), [QueryResults](vdi.query.QueryResults.md)  
Since 
    Horizon 7.8

  


## Service Description

Methods

Methods defined in this Service   
---  
PersistentDiskQueryService_QueryWithSpec  
  



Queries linked clone dedicated machines which has user assigned and populates compatibilities for each machines which user can manage. 

Privileges 

Privilege |  Description   
---|---  
UDD_VIEW|  is required to query by spec.   
MACHINE_MANAGEMENT|  Needed on machines for them to be included in the response.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [PersistentDiskQueryService](vdi.resources.PersistentDiskQueryService.md) used to make the method call.   
**querySpec**| [PersistentDiskQueryServiceQuerySpec](vdi.resources.PersistentDiskQueryService.QuerySpec.md)|  querySpec to filter the results   
  
  


Return Value 

Type |  Description   
---|---  
[QueryResults](vdi.query.QueryResults.md)| [QueryResults](vdi.query.QueryResults.md)  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidRequest](vdi.fault.InvalidRequest.md)| Thrown if [id](vdi.resources.PersistentDiskQueryService.QuerySpec.md#id) is set to null  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  
  
  
  
  

