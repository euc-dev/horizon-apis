---
layout: page
title: Data Object - RoleData
hide:
#- navigation
- toc
---





Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.users.Role.RoleData`

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
**permissions**| [PermissionId[]](vdi.entity.PermissionId.md)|  Administrative permissions (user/group and access group) for this role. [^1]
**appliesToAccessGroup**|  xsd:boolean|  Specifies whether access group is applicable for this role. This will be true when the role contains atleast one object specific privilege.  **_Since_** Horizon 7.8 [^5] [^2]
**type**|  xsd:string|  The role type. It will be null for custom roles.  **_Since_** Horizon 7.8 [^1] [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>ADMINISTRATOR</td><td>Role with full administrative rights</td></tr><tr><td>ADMINISTRATOR_READ_ONLY</td><td>Role with full read-only administrative rights</td></tr><tr><td>AGENT_REGISTRATION_ADMIN</td><td>Role with rights to register Agents</td></tr><tr><td>GLOBAL_CONFIG_AND_POLICY_ADMIN</td><td>Role with rights for View Configuration settings and policies</td></tr><tr><td>GLOBAL_CONFIG_AND_POLICY_ADMIN_READ_ONLY</td><td>Role with read-only rights for View Configuration settings and policies</td></tr><tr><td>HELP_DESK_ADMIN</td><td>Role with rights for Help Desk portal management</td></tr><tr><td>HELP_DESK_ADMIN_READ_ONLY</td><td>Role with read-only rights for Help Desk portal management</td></tr><tr><td>INVENTORY_ADMIN</td><td>Role with rights for inventory management</td></tr><tr><td>INVENTORY_ADMIN_READ_ONLY</td><td>Role with read-only rights for inventory management</td></tr><tr><td>LOCAL_ADMIN</td><td>Local Pod Administration role with full administrative rights</td></tr><tr><td>LOCAL_ADMIN_READ_ONLY</td><td>Local Pod Administration role with full read-only administrative rights</td></tr></table>
**appliesToGlobalAccessGroup**|  xsd:boolean|  Specifies whether global access group is applicable for this role. This will be true when the role contains atleast one of FEDEREATED_LDAP_MANAGE, FEDEREATED_LDAP_VIEW, FEDERATED_SESSIONS_MANAGE or FEDERATED_SESSIONS_VIEW privileges  **_Since_** Horizon 8.2 [^5] [^2]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^5]: This property has a default value of false.