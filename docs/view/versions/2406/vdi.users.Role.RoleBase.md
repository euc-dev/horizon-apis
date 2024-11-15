---
layout: page
title: Data Object - RoleBase
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.users.Role.RoleBase`

Property of
> [RoleInfo](vdi.users.Role.RoleInfo.md#field_detail)

Parameter to
> [Role_Create](vdi.users.Role.md#create)

Since
> Horizon View 6.0


## Data Object Description

Base data used for role creation.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**name**|  xsd:string|  The role name. [^2] [^3]
**description**|  xsd:string|  The role description. [^1] [^4]
**privileges**|  xsd:string[]|  Privileges for this role. When being created or updated, input non-selectable privileges are ignored. [^1] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>ADMINISTRATOR</td><td>Full administrator privilege, including Multi-Datacenter View configuration.</td></tr><tr><td>ADMINISTRATOR_VIEW</td><td>Full read-only administrator privilege, including Multi-Datacenter View configuration.</td></tr><tr><td>VC_CONFIG_VIEW</td><td>Read-only access to vCenter Configuration.</td></tr><tr><td>LOG_COLLECTION</td><td>Collect Operation Logs.</td></tr><tr><td>FORENSICS</td><td>Manage Forensics Operations.</td></tr><tr><td>LOCAL_ADMINISTRATOR</td><td>Full local administrator privilege, except for Multi-Datacenter View configuration and managing roles/privileges.</td></tr><tr><td>LOCAL_ADMINISTRATOR_VIEW</td><td>Full local read-only administrator privilege, except for Multi-Datacenter View configuration.</td></tr><tr><td>INVENTORY_ADMINISTRATOR</td><td>Access to all inventory objects.</td></tr><tr><td>INVENTORY_ADMINISTRATOR_VIEW</td><td>Read-only access to all inventory objects.</td></tr><tr><td>HELPDESK_ADMINISTRATOR</td><td>Access to Help Desk portal.</td></tr><tr><td>HELPDESK_ADMINISTRATOR_VIEW</td><td>Read-only access to Help Desk portal.</td></tr><tr><td>FEDERATED_LDAP_MANAGE</td><td>Manage Pod (Multi-Datacenter View) Federation.</td></tr><tr><td>FEDERATED_LDAP_VIEW</td><td>Read-only access to global (Multi-Datacenter View) LDAP.</td></tr><tr><td>FEDERATED_SESSIONS_MANAGE</td><td>Manage federated (local and non-local) sessions.</td></tr><tr><td>FEDERATED_SESSIONS_VIEW</td><td>Read-only access to federated (local and non-local) sessions.</td></tr><tr><td>GLOBAL_ADMINISTRATOR</td><td>Manage global (non-inventory) configuration settings, including global (Multi-Datacenter View) LDAP.</td></tr><tr><td>GLOBAL_ADMINISTRATOR_VIEW</td><td>Read-only access to global (non-inventory) configuration settings, including global (Multi-Datacenter View) LDAP.</td></tr><tr><td>GLOBAL_ADMIN_UI_INTERACTIVE</td><td>Can log into View Administrator.</td></tr><tr><td>GLOBAL_ADMIN_SDK_INTERACTIVE</td><td>Can run all command line utilities and PowerShell commands.</td></tr><tr><td>GLOBAL_MACHINE_REGISTER</td><td>Register non-vCenter machine sources such as Windows Terminal Servers and physical PCs.</td></tr><tr><td>GLOBAL_ROLE_PERMISSION_MANAGEMENT</td><td>Add, modify, and delete administrator roles and permissions.</td></tr><tr><td>GLOBAL_ROLE_MANAGEMENT</td><td>Add, modify, and delete administrator roles.</td></tr><tr><td>GLOBAL_ROLE_VIEW</td><td>Read-only access to administrator roles.</td></tr><tr><td>GLOBAL_PERMISSION_VIEW</td><td>Read-only access to administrator permissions.</td></tr><tr><td>GLOBAL_PERMISSION_MANAGEMENT</td><td>Add, modify, and delete administrator permissions.</td></tr><tr><td>GLOBAL_CONFIG_VIEW</td><td>Read-only access to global (non-inventory) policy, configuration, and RDS server settings.</td></tr><tr><td>GLOBAL_CONFIG_MANAGEMENT</td><td>View and change global (non-inventory) policy, configuration, and RDS server settings.</td></tr><tr><td>FOLDER_MANAGEMENT</td><td>Add, modify, and delete access groups.</td></tr><tr><td>FOLDER_VIEW</td><td>Read-only access to access groups.</td></tr><tr><td>POOL_VIEW</td><td>Read-only access to desktops, farms, applications, their local sessions, and their machines.</td></tr><tr><td>POOL_MANAGEMENT</td><td>Add, modify, and delete desktops, applications, and farms. Add and remove machines from desktops.</td></tr><tr><td>POOL_ENABLE</td><td>Enable and disable desktops, farms, and applications.</td></tr><tr><td>POOL_ENTITLE</td><td>Add and remove desktop and application entitlements.</td></tr><tr><td>POOL_SVI_IMAGE_MANAGEMENT</td><td>Schedule push image, maintenance, and change default image for desktops and farms.</td></tr><tr><td>MACHINE_VIEW</td><td>Read-only access to machines and their local sessions.</td></tr><tr><td>MACHINE_MANAGEMENT</td><td>Perform all machine and session-related commands.</td></tr><tr><td>MACHINE_REBOOT</td><td>Reset local machines.</td></tr><tr><td>MACHINE_SHUTDOWN</td><td>Shutdown local machines.</td></tr><tr><td>MACHINE_MANAGE_VDI_SESSION</td><td>Disconnect, logoff, and send messages to local sessions.</td></tr><tr><td>MACHINE_MANAGE_OFFLINE_SESSION</td><td>Roll back offline sessions and initiate replications.</td></tr><tr><td>MACHINE_USER_MANAGEMENT</td><td>Assign and unassign users for machines, update machine aliases for machines.</td></tr><tr><td>MACHINE_MAINTENANCE</td><td>Put machine in and out of maintenance mode.</td></tr><tr><td>MANAGE_REMOTE_PROCESS</td><td>Manage Remote Processes and Applications.</td></tr><tr><td>REMOTE_ASSISTANCE</td><td>Remote Assistance to Remote desktop.</td></tr><tr><td>API_SMART_CARD_BYPASS</td><td>Allows API's credential-based login when smart card authentication mode is REQUIRED.</td></tr><tr><td>MANAGE_CERTIFICATES</td><td>Allows user to import certificates or generate CSR.</td></tr><tr><td>UDD_VIEW</td><td>Read-only access to persistent disks.</td></tr><tr><td>UDD_MANAGEMENT</td><td>Manage persistent disks.</td></tr><tr><td>HORIZON_CLOUD_SERVICE</td><td>Allows Horizon cloud service to activate subscription license and monitoring from the cloud.</td></tr><tr><td>SUBSCRIPTION_LICENSE_ADD</td><td>Allows activation of subscription license.</td></tr><tr><td>CLOUD_ADMIN</td><td>Allows Cloud Admin login.</td></tr><tr><td>CLOUD_ON_BOARDING_MANAGEMENT</td><td>Enables cloud onboarding operations.</td></tr><tr><td>CLOUD_OPS_MANAGEMENT</td><td>Enables post-onboarding operations from the cloud.</td></tr><tr><td>CAPACITY_PROVIDER_CONFIG_VIEW</td><td>Manage Capacity Provider Configuration (Read Only).</td></tr><tr><td>CAPACITY_PROVIDER_CONFIG_MANAGEMENT</td><td>Manage Capacity Provider Configuration.</td></tr></table>




 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^3]: This property must contain only alphanumerics, spaces, underscores, and dashes. The maximum length is 32 characters.
[^4]: This property has a maximum length of 400 characters.