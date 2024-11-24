---
layout: page
title: Fault - InsufficientPermission
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.fault.InsufficientPermission`

Extends
> [SecurityError](vmodl.fault.SecurityError.md)

See also
> [AccessGroupId](vdi.entity.AccessGroupId.md), [EntityId](vdi.EntityId.md)

Since
> Horizon View 6.0


## Fault Description

An InsufficientPermission exception is thrown if the calling user does not have a valid permission on a certain resource involved in the method. That resource may be stored within a permitted access group hierarchy.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**resource**| [EntityId](vdi.EntityId.md)|  The id, if any, of the resource that the user has insufficient permissions for. [^1]
**privileges**|  xsd:string[]|  The insufficent privileges.<br>* This property will be one of:<br><table><thead><tr><th>Value</th><th>Description</th></tr></thead><tbody><tr><td>"ADMINISTRATOR"</td><td>ADMINISTRATOR Privilege</td></tr><tr><td>"ADMINISTRATOR_VIEW"</td><td>ADMINISTRATOR_VIEW Privilege</td></tr><tr><td>"VC_CONFIG_VIEW"</td><td>VC_CONFIG_VIEW Privilege</td></tr><tr><td>"LOG_COLLECTION"</td><td>LOG_COLLECTION Privilege</td></tr><tr><td>"FORENSICS"</td><td>FORENSICS Privilege</td></tr><tr><td>"LOCAL_ADMINISTRATOR"</td><td>LOCAL_ADMINISTRATOR Privilege</td></tr><tr><td>"LOCAL_ADMINISTRATOR_VIEW"</td><td>LOCAL_ADMINISTRATOR_VIEW Privilege</td></tr><tr><td>"INVENTORY_ADMINISTRATOR"</td><td>INVENTORY_ADMINISTRATOR Privilege</td></tr><tr><td>"INVENTORY_ADMINISTRATOR_VIEW"</td><td>INVENTORY_ADMINISTRATOR_VIEW Privilege</td></tr><tr><td>"HELPDESK_ADMINISTRATOR"</td><td>HELPDESK_ADMINISTRATOR Privilege</td></tr><tr><td>"HELPDESK_ADMINISTRATOR_VIEW"</td><td>HELPDESK_ADMINISTRATOR_VIEW Privilege</td></tr><tr><td>"FEDERATED_LDAP_MANAGE"</td><td>FEDERATED_LDAP_MANAGE Privilege</td></tr><tr><td>"FEDERATED_LDAP_VIEW"</td><td>FEDERATED_LDAP_VIEW Privilege</td></tr><tr><td>"FEDERATED_SESSIONS_MANAGE"</td><td>FEDERATED_SESSIONS_MANAGE Privilege</td></tr><tr><td>"FEDERATED_SESSIONS_VIEW"</td><td>FEDERATED_SESSIONS_VIEW Privilege</td></tr><tr><td>"GLOBAL_ADMINISTRATOR"</td><td>GLOBAL_ADMINISTRATOR Privilege</td></tr><tr><td>"GLOBAL_ADMINISTRATOR_VIEW"</td><td>GLOBAL_ADMINISTRATOR_VIEW Privilege</td></tr><tr><td>"GLOBAL_ADMIN_UI_INTERACTIVE"</td><td>GLOBAL_ADMIN_UI_INTERACTIVE Privilege</td></tr><tr><td>"GLOBAL_ADMIN_SDK_INTERACTIVE"</td><td>GLOBAL_ADMIN_SDK_INTERACTIVE Privilege</td></tr><tr><td>"GLOBAL_MACHINE_REGISTER"</td><td>GLOBAL_MACHINE_REGISTER Privilege</td></tr><tr><td>"GLOBAL_ROLE_PERMISSION_MANAGEMENT"</td><td>GLOBAL_ROLE_PERMISSION_MANAGEMENT Privilege</td></tr><tr><td>"GLOBAL_ROLE_MANAGEMENT"</td><td>GLOBAL_ROLE_MANAGEMENT Privilege</td></tr><tr><td>"GLOBAL_ROLE_VIEW"</td><td>GLOBAL_ROLE_VIEW Privilege</td></tr><tr><td>"GLOBAL_PERMISSION_VIEW"</td><td>GLOBAL_PERMISSION_VIEW Privilege</td></tr><tr><td>"GLOBAL_PERMISSION_MANAGEMENT"</td><td>GLOBAL_PERMISSION_MANAGEMENT Privilege</td></tr><tr><td>"GLOBAL_CONFIG_VIEW"</td><td>GLOBAL_CONFIG_VIEW Privilege</td></tr><tr><td>"GLOBAL_CONFIG_MANAGEMENT"</td><td>GLOBAL_CONFIG_MANAGEMENT Privilege</td></tr><tr><td>"FOLDER_MANAGEMENT"</td><td>FOLDER_MANAGEMENT Privilege</td></tr><tr><td>"FOLDER_VIEW"</td><td>FOLDER_VIEW Privilege</td></tr><tr><td>"POOL_VIEW"</td><td>POOL_VIEW Privilege</td></tr><tr><td>"POOL_MANAGEMENT"</td><td>POOL_MANAGEMENT Privilege</td></tr><tr><td>"POOL_ENABLE"</td><td>POOL_ENABLE Privilege</td></tr><tr><td>"POOL_ENTITLE"</td><td>POOL_ENTITLE Privilege</td></tr><tr><td>"POOL_SVI_IMAGE_MANAGEMENT"</td><td>POOL_SVI_IMAGE_MANAGEMENT Privilege</td></tr><tr><td>"MACHINE_VIEW"</td><td>MACHINE_VIEW Privilege</td></tr><tr><td>"MACHINE_MANAGEMENT"</td><td>MACHINE_MANAGEMENT Privilege</td></tr><tr><td>"MACHINE_REBOOT"</td><td>MACHINE_REBOOT Privilege</td></tr><tr><td>"MACHINE_SHUTDOWN"</td><td>MACHINE_SHUTDOWN Privilege</td></tr><tr><td>"MACHINE_MANAGE_VDI_SESSION"</td><td>MACHINE_MANAGE_VDI_SESSION Privilege</td></tr><tr><td>"MACHINE_MANAGE_OFFLINE_SESSION"</td><td>MACHINE_MANAGE_OFFLINE_SESSION Privilege</td></tr><tr><td>"MACHINE_USER_MANAGEMENT"</td><td>MACHINE_USER_MANAGEMENT Privilege</td></tr><tr><td>"MACHINE_MAINTENANCE"</td><td>MACHINE_MAINTENANCE Privilege</td></tr><tr><td>"MANAGE_REMOTE_PROCESS"</td><td>MANAGE_REMOTE_PROCESS Privilege</td></tr><tr><td>"REMOTE_ASSISTANCE"</td><td>REMOTE_ASSISTANCE Privilege</td></tr><tr><td>"API_SMART_CARD_BYPASS"</td><td>API_SMART_CARD_BYPASS Privilege</td></tr><tr><td>"MANAGE_CERTIFICATES"</td><td>MANAGE_CERTIFICATES Privilege</td></tr><tr><td>"UDD_VIEW"</td><td>UDD_VIEW Privilege</td></tr><tr><td>"UDD_MANAGEMENT"</td><td>UDD_MANAGEMENT Privilege</td></tr><tr><td>"HORIZON_CLOUD_SERVICE"</td><td>HORIZON_CLOUD_SERVICE Privilege</td></tr><tr><td>"SUBSCRIPTION_LICENSE_ADD"</td><td>SUBSCRIPTION_LICENSE_ADD Privilege</td></tr><tr><td>"CLOUD_ADMIN"</td><td>CLOUD_ADMIN Privilege</td></tr><tr><td>"CLOUD_ON_BOARDING_MANAGEMENT"</td><td>CLOUD_ON_BOARDING_MANAGEMENT Privilege</td></tr><tr><td>"CLOUD_OPS_MANAGEMENT"</td><td>CLOUD_OPS_MANAGEMENT Privilege</td></tr><tr><td>"CAPACITY_PROVIDER_CONFIG_VIEW"</td><td>CAPACITY_PROVIDER_CONFIG_VIEW Privilege</td></tr><tr><td>"CAPACITY_PROVIDER_CONFIG_MANAGEMENT"</td><td>CAPACITY_PROVIDER_CONFIG_MANAGEMENT Privilege</td></tr></tbody></table>
**accessGroup**| [AccessGroupId](vdi.entity.AccessGroupId.md)|  If the resource is located in an access group, the id of that access group. [^1]
Properties inherited from [SecurityError](vmodl.fault.SecurityError.md)
None
Properties inherited from [RuntimeFault](vmodl.RuntimeFault.md)
None
Properties inherited from [MethodFault](vmodl.MethodFault.md)
None


 


[^1]: This property need not be set.