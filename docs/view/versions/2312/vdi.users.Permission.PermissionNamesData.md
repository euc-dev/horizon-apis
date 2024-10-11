---
layout: page
title: Data Object - PermissionNamesData
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.users.Permission.PermissionNamesData`

Property of  
> [PermissionInfo](vdi.users.Permission.PermissionInfo.md#field_detail)

Since  
> Horizon 7.8


## Data Object Description 

Names data of User, Role and AccessGroup involved in the permission. 

  * This data object must be updated as a whole.



## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**userOrGroupName**|  xsd:string|  Name of the user or group for this permission.   


 * This property cannot be updated.

  
**roleName**|  xsd:string|  Name of the role for this permission.   


 * This property cannot be updated.

  
**accessGroupName**|  xsd:string|  Name of the access group for this permission.   


 * This property need not be set.
 * This property cannot be updated.

  
**globalAccessGroupName**|  xsd:string|  Name of the global access group for this permission.  **_Since_** Horizon 8.2  


 * This property need not be set.
 * This property cannot be updated.

  
  
  
   
  
  
