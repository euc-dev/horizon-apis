---
layout: page
title: Data Object - RoleData
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.users.Role.RoleData`

Property of  
> [RoleInfo](vdi.users.Role.RoleInfo.md#field_detail)

See also  
> [PermissionId](vdi.entity.PermissionId.md)

Since  
> Horizon View 6.0


## Data Object Description 

Readonly data about this role. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**builtin**|  xsd:boolean|  Whether or not this is a built-in role (or custom). Built-in roles cannot be edited.   
  
**permissions**| [PermissionId[]](vdi.entity.PermissionId.md)|  Administrative permissions (user/group and access group) for this role.   


* This property need not be set.

  
**appliesToAccessGroup**|  xsd:boolean|  Specifies whether access group is applicable for this role. This will be true when the role contains atleast one object specific privilege.  **_Since_** Horizon 7.8  


  * This property has a default value of false.
* This property cannot be updated.

  
**type**|  xsd:string|  The role type. It will be null for custom roles.  **_Since_** Horizon 7.8  


* This property need not be set.
* This property cannot be updated.
  * This property will be one of:  
|  Value |  Description   
---|---  
"ADMINISTRATOR"| Role with full administrative rights  
"ADMINISTRATOR_READ_ONLY"| Role with full read-only administrative rights  
"AGENT_REGISTRATION_ADMIN"| Role with rights to register Agents  
"GLOBAL_CONFIG_AND_POLICY_ADMIN"| Role with rights for View Configuration settings and policies  
"GLOBAL_CONFIG_AND_POLICY_ADMIN_READ_ONLY"| Role with read-only rights for View Configuration settings and policies  
"HELP_DESK_ADMIN"| Role with rights for Help Desk portal management  
"HELP_DESK_ADMIN_READ_ONLY"| Role with read only rights for Help Desk portal management  
"INVENTORY_ADMIN"| Role with rights for inventory management  
"INVENTORY_ADMIN_READ_ONLY"| Role with read only rights for inventory management  
"LOCAL_ADMIN"| Local Pod Administration role with full administrative rights  
"LOCAL_ADMIN_READ_ONLY"| Local Pod Administration role with full read-only administrative rights  

  
**appliesToGlobalAccessGroup**|  xsd:boolean|  Specifies whether global access group is applicable for this role. This will be true when the role contains atleast one of FEDEREATED_LDAP_MANAGE, FEDEREATED_LDAP_VIEW, FEDERATED_SESSIONS_MANAGE or FEDERATED_SESSIONS_VIEW privileges  **_Since_** Horizon 8.2  


  * This property has a default value of false.
* This property cannot be updated.

  
  
  

  
  
