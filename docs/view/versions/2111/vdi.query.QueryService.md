---
layout: page
title: Service - QueryService
hide:
 #- navigation
 - toc
---

  
   
  



Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.query.QueryService`

See also  
> [QueryDefinition](vdi.query.QueryDefinition.md), [QueryId](vdi.entity.QueryId.md), [QueryResults](vdi.query.QueryResults.md)

Since  
> Horizon View 6.0


  


## Service Description

The Query Service provides a uniform simple query interface to allow bulk enumeration of entities, using either a paging or "virtual list" model. 

  * To use the paging model, create a query with the [QueryService_Create](vdi.query.QueryService.md#create) method, get successive results with the [QueryService_GetNext](vdi.query.QueryService.md#getNext) method, then release server-side resources with the [QueryService_Delete](vdi.query.QueryService.md#delete) method.
  * To use the "virtual list" model, use the [QueryService_Query](vdi.query.QueryService.md#query) method to get one page of results at the offset of your choice. There is no need to free server-side resources using this model, but successive queries may be significantly less performant as a result.
  * The privileges on an individual query will be based on the [queried entity type](vdi.query.QueryDefinition.md#queryEntityType).



Methods

Methods defined in this Service   
---  
QueryService_Create, QueryService_Delete, QueryService_DeleteAll, QueryService_DeleteByIds, QueryService_GetCount, QueryService_GetNext, QueryService_Query  
  



Create a cursor for iterating though query results efficiently, and return the first set of results. Creates server-side state which should be explicitly deleted via [QueryService_Delete](vdi.query.QueryService.md#delete). Server side state will also time out eventually. 

Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [QueryService](vdi.query.QueryService.md) used to make the method call.   
**definition**| [QueryDefinition](vdi.query.QueryDefinition.md)|  query definition.   
  
  


Return Value 

Type |  Description   
---|---  
[QueryResults](vdi.query.QueryResults.md)| first page of results.  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidState](vdi.fault.InvalidState.md)| Thrown if the per session query limit has been reached.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



Delete the server-side state associated with this cursor. To be used after [QueryService_Create](vdi.query.QueryService.md#create). 

Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [QueryService](vdi.query.QueryService.md) used to make the method call.   
**id**| [QueryId](vdi.entity.QueryId.md)|  from a result set.   
  
  


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
  
Show WSDL type definition

  
  
  



Delete the server-side state associated with any outstanding cursors. To be used after [QueryService_Create](vdi.query.QueryService.md#create). 

Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [QueryService](vdi.query.QueryService.md) used to make the method call.   
  


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
  
Show WSDL type definition

  
  
  



Deletes the server-side states associated with given cursors. To be used after multiple [QueryService_Create](vdi.query.QueryService.md#create) invocations. 

Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [QueryService](vdi.query.QueryService.md) used to make the method call.   
**ids**| [QueryId[]](vdi.entity.QueryId.md)|  Array of Query Ids to delete.   
  
  


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
  
Show WSDL type definition

  
  
  



Get only a count of results. Resources are released automatically. This should not be used if any results are needed to be read. 

Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [QueryService](vdi.query.QueryService.md) used to make the method call.   
**definition**| [QueryDefinition](vdi.query.QueryDefinition.md)|  query definition.   
  
  


Return Value 

Type |  Description   
---|---  
xsd:int| count of objects which match this query.  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



Get the next set of results. To be used after [QueryService_Create](vdi.query.QueryService.md#create). 

Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [QueryService](vdi.query.QueryService.md) used to make the method call.   
**id**| [QueryId](vdi.entity.QueryId.md)|  from the previous result set.   
  
  


Return Value 

Type |  Description   
---|---  
[QueryResults](vdi.query.QueryResults.md)| next page of results.  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



Perform a "virtual list"-style query for a set of results. Inefficient for iterating through many items. Resources are released automatically. 

Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [QueryService](vdi.query.QueryService.md) used to make the method call.   
**definition**| [QueryDefinition](vdi.query.QueryDefinition.md)|  query definition.   
  
  


Return Value 

Type |  Description   
---|---  
[QueryResults](vdi.query.QueryResults.md)| one page of results.  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  
  
  
  
  
