---
layout: page
title: Service - Site
hide:
 #- navigation
 - toc
---

  
| | | Local Methods  
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  



Java Class
    com.vmware.vdi.vlsi.binding.vdi.federation.Site
See also
     [MapEntry](vdi.util.MapEntry.md), [SiteBase](vdi.federation.Site.SiteBase.md), [SiteId](vdi.entity.SiteId.md), [SiteInfo](vdi.federation.Site.SiteInfo.md)
Since 
    Horizon View 6.0

  


## Service Description

The interface representing a site in a PodFederation. A site is basically a grouping of pods that utilize shared resources: networking, storage, etc. Usually a site comprises of pods in the same datacenter. 

Methods

Methods defined in this Service   
---  
Site_Create, Site_Delete, Site_Get, Site_List, Site_Update  
  



Create a new Site. After creation, this site will have no Pod in it. To move a pod to a site, use Pod.upate() 

Privileges 

Privilege |  Description   
---|---  
FEDERATED_LDAP_MANAGE|  Global LDAP management is required to create a site.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Site](vdi.federation.Site.md) used to make the method call.   
**base**| [SiteBase](vdi.federation.Site.SiteBase.md)|  SiteBase data containing site name and description   
  
  


Return Value 

Type |  Description   
---|---  
[SiteId](vdi.entity.SiteId.md)| Unique identifier for the created site.  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidState](vdi.fault.InvalidState.md)| Thrown if the PodFederation is not initialized.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  


Events 

Event |  Description   
---|---  
VLSI_SITE_CREATE_SUCCESS|  If the site was successfully created.   
VLSI_SITE_CREATE_FAILURE|  If the site could not be created.   
  
Show WSDL type definition

  
  
  



Delete a site. This can only be done when the site has no pods in it. 

Privileges 

Privilege |  Description   
---|---  
FEDERATED_LDAP_MANAGE|  Global LDAP management is required to delete a site.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Site](vdi.federation.Site.md) used to make the method call.   
**id**| [SiteId](vdi.entity.SiteId.md)|  Id of the site to be deleted.   
  
  


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
[InvalidState](vdi.fault.InvalidState.md)| Thrown if PodFederation has not been initialized or if the site has pods in it.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  


Events 

Event |  Description   
---|---  
VLSI_SITE_DELETE_SUCCESS|  If the site was successfully deleted.   
VLSI_SITE_DELETE_FAILURE|  If the site could not be deleted.   
  
Show WSDL type definition

  
  
  



Retrieve the information about a Site. 

Privileges 

Privilege |  Description   
---|---  
FEDERATED_LDAP_VIEW|  Global LDAP read is required to read a site.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Site](vdi.federation.Site.md) used to make the method call.   
**id**| [SiteId](vdi.entity.SiteId.md)|  Id of a site   
  
  


Return Value 

Type |  Description   
---|---  
[SiteInfo](vdi.federation.Site.SiteInfo.md)| SiteInfo  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidState](vdi.fault.InvalidState.md)| Thrown if PodFederation has not been initialized.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



List all the sites in the PodFederation. 

Privileges 

Privilege |  Description   
---|---  
FEDERATED_LDAP_VIEW|  Global LDAP read is required to list sites.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Site](vdi.federation.Site.md) used to make the method call.   
  


Return Value 

Type |  Description   
---|---  
[SiteInfo[]](vdi.federation.Site.SiteInfo.md)| SiteInfo  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidState](vdi.fault.InvalidState.md)| Thrown if the PodFederation has not been initialized.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



Update displayName or description of a site.  
To change site for a pod, use MapEntry[]). 

Privileges 

Privilege |  Description   
---|---  
FEDERATED_LDAP_MANAGE|  Global LDAP management is required to update a site.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Site](vdi.federation.Site.md) used to make the method call.   
**id**| [SiteId](vdi.entity.SiteId.md)|  Id of a site   
  
**updates**| [MapEntry[]](vdi.util.MapEntry.md)|  name value pairs for update.   


  * This parameter is an update map based on [SiteInfo](vdi.federation.Site.SiteInfo.md "SiteInfo"). 

  
  


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
[InvalidRequest](vdi.fault.InvalidRequest.md)| Thrown if map contains invalid fields.  
[InvalidState](vdi.fault.InvalidState.md)| Thrown if PodFederation has not been initialized.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  


Events 

Event |  Description   
---|---  
VLSI_SITE_UPDATE_SUCCESS|  If the site was successfully updated.   
VLSI_SITE_UPDATE_FAILURE|  If the site could not be updated.   
  
Show WSDL type definition

  
  
  
  
Top of page| | | Local Methods  
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

