---
layout: page
title: Service - ApplicationIcon
hide:
 #- navigation
 - toc
---

  
  
  



Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.resources.ApplicationIcon`

See also  
> [ApplicationIconId](vdi.entity.ApplicationIconId.md), [ApplicationIconInfo](vdi.resources.ApplicationIcon.ApplicationIconInfo.md), [ApplicationIconSpec](vdi.resources.ApplicationIcon.ApplicationIconSpec.md), [ApplicationIconSummaryView](vdi.resources.ApplicationIcon.ApplicationIconSummaryView.md), [ApplicationId](vdi.entity.ApplicationId.md)

Since  
> Horizon View 6.0


  


## Service Description

Service that represents ApplicationIcon. These are not explicitly managed by View administrator. However, the interface is required for performance reasons: while fetching Applications, icon image data is not included, and client must separately request icons. 

Methods

Methods defined in this Service   
---  
ApplicationIcon_CreateAndAssociate, ApplicationIcon_Get, ApplicationIcon_GetByApplications, ApplicationIcon_GetInfos, ApplicationIcon_GetSummaryViewByApplications, ApplicationIcon_RemoveAssociations, ApplicationIcon_UpdateAssociations  
  



Creates a new ApplicationIcon and associates it with application(s) mentioned in the spec. Any existing ApplicatonIcon association will be replaced with the newly supplied association information for application(s) specified in the spec. This API throws an exception if executionData contains an empty applications field. 

Privileges 

Privilege |  Description   
---|---  
POOL_MANAGEMENT|  privilege is required to create ApplicationIcon.   
FEDERATED_LDAP_MANAGE|  privilege is required if Application has Global Application Entitlement.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ApplicationIcon](vdi.resources.ApplicationIcon.md) used to make the method call.   
**spec**| [ApplicationIconSpec](vdi.resources.ApplicationIcon.ApplicationIconSpec.md)|  The information required to create the new ApplicationIcon and its association with given application(s).   
  
  


Return Value 

Type |  Description   
---|---  
[ApplicationIconId](vdi.entity.ApplicationIconId.md)| The id of the new ApplicationIcon.  
  


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
VLSI_APPLICATION_ICON_CREATED_ASSOCIATED|  if ApplicationIcon is created and associated with all the applications specified in spec.   
VLSI_APPLICATION_ICON_CREATE_ASSOCIATE_FAILED|  if operation failed.   
  
Show WSDL type definition

  
  
  



Get an ApplicationIcon by Id. 

Privileges 

Privilege |  Description   
---|---  
POOL_VIEW|  privilege is required on at-least one Application (that the ApplicationIconId represents) to get ApplicationIconInfo.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ApplicationIcon](vdi.resources.ApplicationIcon.md) used to make the method call.   
**id**| [ApplicationIconId](vdi.entity.ApplicationIconId.md)|  entityId of ApplicationIcon to get.   
  
  


Return Value 

Type |  Description   
---|---  
[ApplicationIconInfo](vdi.resources.ApplicationIcon.ApplicationIconInfo.md)| requested ApplicationIcon entity.  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



List all ApplicationIcons used by the given Application entityIDs. If an Application has multiple icons, the icon with the closest size matching height and width is chosen. If there is a customized icon association for the given application, it will always return customized icon only. 

Privileges 

Privilege |  Description   
---|---  
POOL_VIEW|  privilege is required for each of the Applications in ApplicationId array to get the ApplicationIconInfo array.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ApplicationIcon](vdi.resources.ApplicationIcon.md) used to make the method call.   
**height**|  xsd:int|  Icon height.   
  
**width**|  xsd:int|  Icon width.   
  
**ids**| [ApplicationId[]](vdi.entity.ApplicationId.md)|  Array of entityId of the Applications whose ApplicationIcons are being requested.   
  
  


Return Value 

Type |  Description   
---|---  
[ApplicationIconInfo[]](vdi.resources.ApplicationIcon.ApplicationIconInfo.md)| The array of ApplicationIcons associated with the specified Applications. The array index order matches with entityIds array.  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[PartialFailureFault](vdi.fault.PartialFailureFault.md)| Thrown if one or more Applications do not have any associated icons to select from. The PartialFailureFault contains an array of Objects. Each Object is either (a) ApplicationIconInfo for applications that have at least one icon, and thus return a matching icon or (b) EntityNotFound for applications that have no icons associated.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



Get all ApplicationIcons for the given ApplicationIcon entityIds 

Privileges 

Privilege |  Description   
---|---  
POOL_VIEW|  privilege is required on at-least one Application (that each ApplicationIconId represents) to get ApplicationIconInfo.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ApplicationIcon](vdi.resources.ApplicationIcon.md) used to make the method call.   
**ids**| [ApplicationIconId[]](vdi.entity.ApplicationIconId.md)|  Array of entityId of the ApplicationIcon   
  
  


Return Value 

Type |  Description   
---|---  
[ApplicationIconInfo[]](vdi.resources.ApplicationIcon.ApplicationIconInfo.md)| The list of ApplicationIcons associated with the specified ApplicationIcon entityIDs  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



List summaries of all ApplicationIcons used by the given Application entityIDs without the image data. If an Application has multiple icons, the summary of the icon with the closest size matching height and width is chosen. If there is a customized icon association for the given application, it will always return customized icon summary only. 

Privileges 

Privilege |  Description   
---|---  
POOL_VIEW|  privilege is required for each of the Applications in ApplicationId array to get the ApplicationIconInfo array.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ApplicationIcon](vdi.resources.ApplicationIcon.md) used to make the method call.   
**height**|  xsd:int|  Icon height.   
  
**width**|  xsd:int|  Icon width.   
  
**ids**| [ApplicationId[]](vdi.entity.ApplicationId.md)|  Array of entityId of the Applications whose ApplicationIconSummaryViews are being requested.   
  
  


Return Value 

Type |  Description   
---|---  
[ApplicationIconSummaryView[]](vdi.resources.ApplicationIcon.ApplicationIconSummaryView.md)| The array of ApplicationIconSummaryViews associated with the specified Applications. The array index order matches with entityIds array.  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[PartialFailureFault](vdi.fault.PartialFailureFault.md)| Thrown if one or more Applications do not have any associated icons to select from. The PartialFailureFault contains an array of Objects. Each Object is either (a) ApplicationIconSummaryViews for applications that have at least one icon, and thus return a matching icon summary or (b) EntityNotFound for applications that have no icons associated.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



Removes association between ApplicationIcon and Application(s). It deletes the ApplicationIcon if not used by any other Applications. This operation is only allowed on customized icons i.e. ApplicationIcons having iconSource as unset cannot be removed. 

Privileges 

Privilege |  Description   
---|---  
POOL_MANAGEMENT|  privilege is required to delete the icon associations.   
FEDERATED_LDAP_MANAGE|  privilege is required if Application has Global Application Entitlement.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ApplicationIcon](vdi.resources.ApplicationIcon.md) used to make the method call.   
**id**| [ApplicationIconId](vdi.entity.ApplicationIconId.md)|  The entityId of the ApplicationIcon.   
  
**applications**| [ApplicationId[]](vdi.entity.ApplicationId.md)|  Array of entityId of the Applications to which association needs to be removed.   
  
  


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
VLSI_APPLICATION_ICON_ASSOCIATION_REMOVED|  if association is removed between ApplicationIcon and all the Application(s).   
VLSI_APPLICATION_ICON_ASSOCIATION_REMOVE_FAILED|  if failed in removing association between any Application and ApplicationIcon.   
  
Show WSDL type definition

  
  
  



Updates an association between this ApplicationIcon and Application(s). This operation is only allowed on customized icons i.e. ApplicationIcons having iconSource as unset cannot be removed. 

Privileges 

Privilege |  Description   
---|---  
POOL_MANAGEMENT|  privilege is required to update any attributes.   
FEDERATED_LDAP_MANAGE|  privilege is required if Application has Global Application Entitlement.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ApplicationIcon](vdi.resources.ApplicationIcon.md) used to make the method call.   
**id**| [ApplicationIconId](vdi.entity.ApplicationIconId.md)|  The entityId of the ApplicationIcon to be updated.   
  
**applications**| [ApplicationId[]](vdi.entity.ApplicationId.md)|  Array of entityId of the Applications to which association needs to be updated.   
  
  


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
VLSI_APPLICATION_ICON_ASSOCIATION_UPDATED|  if ApplicationIcon is associated with all the applications specified.   
VLSI_APPLICATION_ICON_ASSOCIATION_UPDATE_FAILED|  if the ApplicationIcon update failed.   
  
Show WSDL type definition

  
  
  
  
  
  
  
