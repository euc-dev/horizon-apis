---
layout: page
title: Data Object - RoleBase
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.users.Role.RoleBase`

Property of
> [RoleInfo](vdi.users.Role.RoleInfo.md#field_detail)

Parameter to
> [Role_Create](vdi.users.Role.md#create)

Since
> Horizon View 6.0


## Data Object Description

Base data used for role creation.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**name**|  xsd:string|  The role name. [^2] [^3]
**description**|  xsd:string|  The role description. [^1] [^4]
**privileges**|  xsd:string[]|  Privileges for this role. When being created or updated, input non-selectable privileges are ignored. [^1] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>ADMINISTRATOR</td><td>Name: Full<br>Type: All<br>Description: Full administrator privilege, including Multi-Datacenter View configuration.<br>Selectable: no</td></tr><tr><td>ADMINISTRATOR_VIEW</td><td>Name: Full (Read only)<br>Type: All<br>Description: Full read-only administrator privilege, including Multi-Datacenter View configuration.<br>Selectable: no</td></tr><tr><td>VC_CONFIG_VIEW</td><td>Name: Manage vCenter Configuration (Read Only)<br>Type: All<br>Description: Read-only access to vCenter Configuration.<br>Selectable: yes</td></tr><tr><td>LOG_COLLECTION</td><td>Name: Collect Operation Logs<br>Type: All<br>Description: Collect Operation Logs.<br>Selectable: yes</td></tr><tr><td>LOCAL_ADMINISTRATOR</td><td>Name: Full Local<br>Type: All<br>Description: Full administrator privilege, except to Multi-Datacenter View configuration and to manage roles and privileges.<br>Selectable: no</td></tr><tr><td>LOCAL_ADMINISTRATOR_VIEW</td><td>Name: Full Local (Read only)<br>Type: All<br>Description: Full read-only administrator privilege, except to Multi-Datacenter View configuration.<br>Selectable: no</td></tr><tr><td>INVENTORY_ADMINISTRATOR</td><td>Name: Manage Inventory<br>Type: All<br>Description: Access to all inventory objects.<br>Selectable: no</td></tr><tr><td>INVENTORY_ADMINISTRATOR_VIEW</td><td>Name: Manage Inventory (Read only)<br>Type: All<br>Description: Read-only access to all inventory objects.<br>Selectable: no</td></tr><tr><td>HELPDESK_ADMINISTRATOR</td><td>Name: Manage Help Desk<br>Type: All<br>Description: Access to Help Desk portal.<br>Selectable: no</td></tr><tr><td>HELPDESK_ADMINISTRATOR_VIEW</td><td>Name: Manage Help Desk (Read only)<br>Type: All<br>Description: Read-only access to Help Desk portal.<br>Selectable: yes</td></tr><tr><td>FEDERATED_LDAP_MANAGE</td><td>Name: Manage Pod Federation<br>Type: All<br>Description: Manage Pod (Multi-Datacenter View) Federation.<br>Selectable: yes</td></tr><tr><td>FEDERATED_LDAP_VIEW</td><td>Name: Manage Global LDAP (Read only)<br>Type: All<br>Description: Read-only access to global (Multi-Datacenter View) LDAP.<br>Selectable: no</td></tr><tr><td>FEDERATED_SESSIONS_MANAGE</td><td>Name: Manage Federated Sessions<br>Type: All<br>Description: Manage federated (local and non-local) sessions.<br>Selectable: yes</td></tr><tr><td>FEDERATED_SESSIONS_VIEW</td><td>Name: Manage Federated Sessions (Read only)<br>Type: All<br>Description: Read-only access to federated (local and non-local) sessions.<br>Selectable: no</td></tr><tr><td>GLOBAL_ADMINISTRATOR</td><td>Name: Manage Global Configuration<br>Type: All<br>Description: Manage global (non-inventory) configuration settings, including global (Multi-Datacenter View) LDAP.<br>Selectable: no</td></tr><tr><td>GLOBAL_ADMINISTRATOR_VIEW</td><td>Name: Manage Global Configuration (Read only)<br>Type: All<br>Description: Read-only access to global (non-inventory) configuration settings, including global (Multi-Datacenter View) LDAP.<br>Selectable: no</td></tr><tr><td>GLOBAL_ADMIN_UI_INTERACTIVE</td><td>Name: Console Interaction<br>Type: Global<br>Description: Can log into View Administrator.<br>Selectable: no</td></tr><tr><td>GLOBAL_ADMIN_SDK_INTERACTIVE</td><td>Name: Direct Interaction<br>Type: Global<br>Description: Can run all command line utilities and PowerShell commands.<br>Selectable: no</td></tr><tr><td>GLOBAL_MACHINE_REGISTER</td><td>Name: Register Agent<br>Type: Global<br>Description: Register non-vCenter machine sources such as Windows Terminal Servers and physical PCs.<br>Selectable: yes</td></tr><tr><td>GLOBAL_ROLE_PERMISSION_MANAGEMENT</td><td>Name: Manage Roles and Permissions<br>Type: Global<br>Description: Add, modify, and delete administrator roles and permissions.<br>Selectable: yes</td></tr><tr><td>GLOBAL_ROLE_MANAGEMENT</td><td>Name: Manage Roles<br>Type: Global<br>Description: Add, modify, and delete administrator roles.<br>Selectable: no</td></tr><tr><td>GLOBAL_ROLE_VIEW</td><td>Name: Manage Roles (Read only)<br>Type: Global<br>Description: Read-only access to administrator roles.<br>Selectable: no</td></tr><tr><td>GLOBAL_PERMISSION_VIEW</td><td>Name: Manage Permissions (Read only)<br>Type: Global<br>Description: Read-only access to administrator permissions.<br>Selectable: no</td></tr><tr><td>GLOBAL_PERMISSION_MANAGEMENT</td><td>Name: Manage Permissions<br>Type: Global<br>Description: Add, modify, and delete administrator permissions.<br>Selectable: no</td></tr><tr><td>GLOBAL_CONFIG_VIEW</td><td>Name: Manage Global Configuration and Policies (Read only)<br>Type: Global<br>Description: Read-only access to global (non-inventory) policy, configuration, and RDS server settings, except administrator roles and permissions and global (Multi-Datacenter View) LDAP.<br>Selectable: no</td></tr><tr><td>GLOBAL_CONFIG_MANAGEMENT</td><td>Name: Manage Global Configuration and Policies<br>Type: Global<br>Description: View and change global (non-inventory) policy, configuration, and RDS server settings, except for administrator roles and permissions.<br>Selectable: yes</td></tr><tr><td>FOLDER_MANAGEMENT</td><td>Name: Manage Access Groups<br>Type: Global<br>Description: Add, modify, and delete access groups.<br>Selectable: yes</td></tr><tr><td>FOLDER_VIEW</td><td>Name: Manage Access Groups (Read only)<br>Type: Access group<br>Description: Read-only access to access groups.<br>Selectable: no</td></tr><tr><td>POOL_VIEW</td><td>Name: Manage Desktops, Farms, and Applications (Read only)<br>Type: Inventory - desktop<br>Description: Read-only access to desktops, farms, applications, their local sessions, and their machines.<br>Selectable: no</td></tr><tr><td>POOL_MANAGEMENT</td><td>Name: Manage Desktops, Farms, and Applications<br>Type: Inventory - desktop<br>Description: Add, modify, and delete desktops, applications, and farms. Add and remove machines from desktops.<br>Selectable: yes<br>Includes: POOL_ENABLE, POOL_ENTITLE, POOL_SVI_IMAGE_MANAGEMENT</td></tr><tr><td>POOL_ENABLE</td><td>Name: Enable Desktops, Farms, and Applications<br>Type: Inventory - desktop<br>Description: Enable and disable desktops, farms, and applications.<br>Selectable: yes</td></tr><tr><td>POOL_ENTITLE</td><td>Name: Entitle Desktops and Applications<br>Type: Inventory - desktop<br>Description: Add and remove desktop and application entitlements.<br>Selectable: yes</td></tr><tr><td>POOL_SVI_IMAGE_MANAGEMENT</td><td>Name: Manage maintenance operations on Automated Desktops & Farms<br>Type: Inventory - desktop<br>Description: Schedule push image, schedule maintenance, and change default image for desktop and farm.<br>Selectable: yes</td></tr><tr><td>MACHINE_VIEW</td><td>Name: Manage Machines (read only)<br>Type: Inventory - machine<br>Description: Read-only access to machines and their local sessions.<br>Selectable: no</td></tr><tr><td>MACHINE_MANAGEMENT</td><td>Name: Manage Machines<br>Type: Inventory - machine<br>Description: Perform all machine and session-related commands.<br>Selectable: yes<br>Includes: MACHINE_REBOOT, MACHINE_MANAGE_VDI_SESSION, MACHINE_MANAGE_OFFLINE_SESSION</td></tr><tr><td>MACHINE_REBOOT</td><td>Name: Manage Reboot Operation<br>Type: Inventory - machine<br>Description: Reset local machines.<br>Selectable: yes</td></tr><tr><td>MACHINE_MANAGE_VDI_SESSION</td><td>Name: Manage Local Sessions<br>Type: Inventory - machine<br>Description: Disconnect, log off, and send messages to local sessions.<br>Selectable: yes</td></tr><tr><td>MACHINE_MANAGE_OFFLINE_SESSION</td><td>Name: Manage Offline Sessions<br>Type: Inventory - machine<br>Description: Roll back offline sessions and initiate replications.<br>Selectable: yes</td></tr><tr><td>MANAGE_REMOTE_PROCESS</td><td>Name: Manage Remote Processes and Applications<br>Type: Inventory - machine<br>Description: Manage Remote Processes and Applications.<br>Selectable: yes</td></tr><tr><td>REMOTE_ASSISTANCE</td><td>Name: Remote Assistance<br>Type: Inventory - machine<br>Description: Remote Assistance to Remote desktop.<br>Selectable: yes</td></tr></table>




 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^3]: This property must contain only alphanumerics, spaces, underscores, and dashes. The maximum length is 32 characters.
[^4]: This property has a maximum length of 400 characters.