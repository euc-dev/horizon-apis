---
layout: page
title: Service - GlobalApplicationEntitlement
hide:
 #- navigation
 - toc
---

  
 
  



Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.federation.GlobalApplicationEntitlement`

See also  
> [ApplicationId](vdi.entity.ApplicationId.md), [GlobalApplicationEntitlementBase](vdi.federation.GlobalApplicationEntitlement.GlobalApplicationEntitlementBase.md), [GlobalApplicationEntitlementId](vdi.entity.GlobalApplicationEntitlementId.md), [GlobalApplicationEntitlementInfo](vdi.federation.GlobalApplicationEntitlement.GlobalApplicationEntitlementInfo.md), [MapEntry](vdi.util.MapEntry.md)

Since  
> Horizon View 6.2


  


## Service Description

The Global Application Entitlement service interface. 

Methods

Methods defined in this Service   
---  
GlobalApplicationEntitlement_AddApplicationsToGAE, GlobalApplicationEntitlement_Create, GlobalApplicationEntitlement_Delete, GlobalApplicationEntitlement_Get, GlobalApplicationEntitlement_Update, GlobalEntitlement_ListCompatibleBackupGAEs  
  



Add list of applications to the Global Application Entitlement. 

Privileges 

Privilege |  Description   
---|---  
FEDERATED_LDAP_MANAGE|  Global LDAP management is required to update the ApplicationInfo#data.globalApplicationEntitlement members of an application.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [GlobalApplicationEntitlement](vdi.federation.GlobalApplicationEntitlement.md) used to make the method call.   
**id**| [GlobalApplicationEntitlementId](vdi.entity.GlobalApplicationEntitlementId.md)|  unique identifier for Global Application Entitlement   
  
**applications**| [ApplicationId[]](vdi.entity.ApplicationId.md)|  Applications to be added to the Global Application Entitlement   
  
  


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
[PartialFailureFault](vdi.fault.PartialFailureFault.md)| Thrown if all operations were not successful, a PartialFailureFault will be thrown indicating which applications were successfully added and which ones failed. The index of results in the PartialFailureFault corresponds to the application's index in request. The result entry will contain either the original return type (on success) or an exception (on failure).  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  


Events 

Event |  Description   
---|---  
VLSI_APPLICATION_UPDATED|  for each Application attribute that was updated   
VLSI_APPLICATION_UPDATE_FAILED|  if the Application update failed.   
  
Show WSDL type definition

  
  
  



Creates a Global Application Entitlement. Global application entitlements are used to route users to their resources across multiple pods. These are persisted in a global ldap instance that is replicated across all pods in a linked mode view set.  


Privileges 

Privilege |  Description   
---|---  
FEDERATED_LDAP_MANAGE|  Global LDAP management is required to create a global application entitlement.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [GlobalApplicationEntitlement](vdi.federation.GlobalApplicationEntitlement.md) used to make the method call.   
**base**| [GlobalApplicationEntitlementBase](vdi.federation.GlobalApplicationEntitlement.GlobalApplicationEntitlementBase.md)|  attributes required to create a Global Application Entitlement   
  
  


Return Value 

Type |  Description   
---|---  
[GlobalApplicationEntitlementId](vdi.entity.GlobalApplicationEntitlementId.md)| unique identifier for Global Application Entitlement  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidState](vdi.fault.InvalidState.md)| Thrown if this pod is not part of a Pod Federation  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  


Events 

Event |  Description   
---|---  
VLSI_GAE_ADDED|  If the global application entitlement was successfully created.   
VLSI_GAE_ADD_FAILED|  If the global application entitlement could not be created.   
  
Show WSDL type definition

  
  
  



Deletes a Global Application Entitlement. 

Privileges 

Privilege |  Description   
---|---  
FEDERATED_LDAP_MANAGE|  Global LDAP management is required to delete a Global Application Entitlement.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [GlobalApplicationEntitlement](vdi.federation.GlobalApplicationEntitlement.md) used to make the method call.   
**id**| [GlobalApplicationEntitlementId](vdi.entity.GlobalApplicationEntitlementId.md)|  unique identifier for Global Application Entitlement to be deleted   
  
  


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
[InvalidRequest](vdi.fault.InvalidRequest.md)| Thrown if Global Application Entitlement is active and has resources associated with it in any pod.  
[InvalidState](vdi.fault.InvalidState.md)| Thrown if the Pod Federation has not been initialized.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  


Events 

Event |  Description   
---|---  
VLSI_GAE_DELETED|  If the Global Application Entitlement was successfully deleted.   
VLSI_GAE_DELETE_FAILED|  If the Global Application Entitlement could not be deleted.   
  
Show WSDL type definition

  
  
  



Returns Global Application Entitlement information corresponding to a specific Global Application Entitlement id. 

Privileges 

Privilege |  Description   
---|---  
FEDERATED_LDAP_VIEW|  Global LDAP read is required to read a Global Application Entitlement.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [GlobalApplicationEntitlement](vdi.federation.GlobalApplicationEntitlement.md) used to make the method call.   
**id**| [GlobalApplicationEntitlementId](vdi.entity.GlobalApplicationEntitlementId.md)|  unique identifier for Global Application Entitlement   
  
  


Return Value 

Type |  Description   
---|---  
[GlobalApplicationEntitlementInfo](vdi.federation.GlobalApplicationEntitlement.GlobalApplicationEntitlementInfo.md)| Global Application Entitlement information  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidState](vdi.fault.InvalidState.md)| Thrown if this pod is not part of a Pod Federation  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



Updates Global Application Entitlement with the set of attributes in the map.  


Privileges 

Privilege |  Description   
---|---  
FEDERATED_LDAP_MANAGE|  Global LDAP management is required to update a Global Application Entitlement.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [GlobalApplicationEntitlement](vdi.federation.GlobalApplicationEntitlement.md) used to make the method call.   
**id**| [GlobalApplicationEntitlementId](vdi.entity.GlobalApplicationEntitlementId.md)|  unique identifier for Global Application Entitlement to be updated   
  
**updates**| [MapEntry[]](vdi.util.MapEntry.md)|  key value pairs describing attributes to be updated   


  * This parameter is an update map based on [GlobalApplicationEntitlementInfo](vdi.federation.GlobalApplicationEntitlement.GlobalApplicationEntitlementInfo.md "GlobalApplicationEntitlementInfo"). 

  
  


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
[InvalidRequest](vdi.fault.InvalidRequest.md)| Thrown if the update map contains invalid or non-permitted fields  
[InvalidState](vdi.fault.InvalidState.md)| Thrown if the Pod Federation has not been initialized.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  


Events 

Event |  Description   
---|---  
VLSI_GAE_CHANGED|  If the Global Application Entitlement was successfully updated.   
VLSI_GAE_CHANGE_FAILED|  If the Global Application Entitlement could not be updated.   
  
Show WSDL type definition

  
  
  



Lists the Global Application Entitlements that can be associated as backup Global Application Entitlement. 

Privileges 

Privilege |  Description   
---|---  
FEDERATED_LDAP_VIEW|  Global LDAP read is required to read a global application entitlement.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [GlobalApplicationEntitlement](vdi.federation.GlobalApplicationEntitlement.md) used to make the method call.   
**id**| [GlobalApplicationEntitlementId](vdi.entity.GlobalApplicationEntitlementId.md)|  unique identifier for Global Application Entitlement   
  
  


Return Value 

Type |  Description   
---|---  
[GlobalApplicationEntitlementInfo[]](vdi.federation.GlobalApplicationEntitlement.GlobalApplicationEntitlementInfo.md)|   
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  
  
  
  
  
