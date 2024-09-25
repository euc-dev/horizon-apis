---
layout: page
title: Data Object - PrivilegeInfo
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.users.Privilege.PrivilegeInfo
Returned by
     [Privilege_ListSelectablePrivileges](vdi.users.Privilege.md#listSelectablePrivileges)
Since 
    Horizon 7.8

## Data Object Description 

Privilege Information. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**name**|  xsd:string|  Name of the privilege.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"ADMINISTRATOR"| ADMINISTRATOR Privilege 
    * **Name:** Full
    * **Type:** All
    * **Description:** Full administrator privilege, including Multi-Datacenter View configuration.
    * **Selectable:** no  
"ADMINISTRATOR_VIEW"| ADMINISTRATOR_VIEW Privilege 
    * **Name:** Full (Read only)
    * **Type:** All
    * **Description:** Full read only administrator privilege, including Multi-Datacenter View configuration.
    * **Selectable:** no  
"VC_CONFIG_VIEW"| VC_CONFIG_VIEW Privilege 
    * **Name:** Manage vCenter Configuration (Read Only)
    * **Type:** All
    * **Description:** Read only access to vCenter Configuration.
    * **Selectable:** yes  
"LOG_COLLECTION"| LOG_COLLECTION Privilege 
    * **Name:** Collect Operation Logs
    * **Type:** All
    * **Description:** Collect Operation Logs
    * **Selectable:** yes  
"FORENSICS"| FORENSICS Privilege 
    * **Name:** Manage Forensics Operations
    * **Type:** All
    * **Description:** Privilege that governs forensics operations. 
    * **Selectable:** yes
    * **Includes:** MACHINE_VIEW   
"LOCAL_ADMINISTRATOR"| LOCAL_ADMINISTRATOR Privilege 
    * **Name:** Full Local
    * **Type:** All
    * **Description:** Full administrator privilege, except to Multi-Datacenter View configuration and to manage roles and privileges. 
    * **Selectable:** no  
"LOCAL_ADMINISTRATOR_VIEW"| LOCAL_ADMINISTRATOR_VIEW Privilege 
    * **Name:** Full Local (Read only)
    * **Type:** All
    * **Description:** Full read only administrator privilege, except to Multi-Datacenter View configuration.
    * **Selectable:** no  
"INVENTORY_ADMINISTRATOR"| INVENTORY_ADMINISTRATOR Privilege 
    * **Name:** Manage Inventory
    * **Type:** All
    * **Description:** Access to all inventory objects.
    * **Selectable:** no  
"INVENTORY_ADMINISTRATOR_VIEW"| INVENTORY_ADMINISTRATOR_VIEW Privilege 
    * **Name:** Manage Inventory (Read only)
    * **Type:** All
    * **Description:** Read only access to all inventory objects.
    * **Selectable:** no  
"HELPDESK_ADMINISTRATOR"| HELPDESK_ADMINISTRATOR Privilege 
    * **Name:** Manage Help Desk
    * **Type:** All
    * **Description:** Access to Help Desk portal.
    * **Selectable:** no  
"HELPDESK_ADMINISTRATOR_VIEW"| HELPDESK_ADMINISTRATOR_VIEW Privilege 
    * **Name:** Manage Help Desk (Read only)
    * **Type:** All
    * **Description:** Read only access to Help Desk portal.
    * **Selectable:** yes  
"FEDERATED_LDAP_MANAGE"| FEDERATED_LDAP_MANAGE Privilege 
    * **Name:** Manage Pod Federation
    * **Type:** All
    * **Description:** Manage Pod (Multi-Datacenter View) Federation.
    * **Selectable:** yes  
"FEDERATED_LDAP_VIEW"| FEDERATED_LDAP_VIEW Privilege 
    * **Name:** Manage Global LDAP (Read only)
    * **Type:** All
    * **Description:** Read only access to global (Multi-Datacenter View) LDAP.
    * **Selectable:** no  
"FEDERATED_SESSIONS_MANAGE"| FEDERATED_SESSIONS_MANAGE Privilege 
    * **Name:** Manage Federated Sessions
    * **Type:** All
    * **Description:** Manage federated (local and non-local) sessions.
    * **Selectable:** yes  
"FEDERATED_SESSIONS_VIEW"| FEDERATED_SESSIONS_VIEW Privilege 
    * **Name:** Manage Federated Sessions (Read only)
    * **Type:** All
    * **Description:** Read only access to federated (local and non-local) sessions.
    * **Selectable:** no  
"GLOBAL_ADMINISTRATOR"| GLOBAL_ADMINISTRATOR Privilege 
    * **Name:** Manage Global Configuration
    * **Type:** All
    * **Description:** Manage global (non-inventory) configuration settings, including global (Multi-Datacenter View) LDAP.
    * **Selectable:** no  
"GLOBAL_ADMINISTRATOR_VIEW"| GLOBAL_ADMINISTRATOR_VIEW Privilege 
    * **Name:** Manage Global Configuration (Read only)
    * **Type:** All
    * **Description:** Read only access to global (non-inventory) configuration settings, including global (Multi-Datacenter View) LDAP.
    * **Selectable:** no  
"GLOBAL_ADMIN_UI_INTERACTIVE"| GLOBAL_ADMIN_UI_INTERACTIVE Privilege 
    * **Name:** Console Interaction
    * **Type:** Global
    * **Description:** Can log into View Administrator.
    * **Selectable:** no  
"GLOBAL_ADMIN_SDK_INTERACTIVE"| GLOBAL_ADMIN_SDK_INTERACTIVE Privilege 
    * **Name:** Direct Interaction
    * **Type:** Global
    * **Description:** Can run all command line utilities and PowerShell commands.
    * **Selectable:** no  
"GLOBAL_MACHINE_REGISTER"| GLOBAL_MACHINE_REGISTER Privilege 
    * **Name:** Register Agent
    * **Type:** Global
    * **Description:** Register non-vCenter machine sources such as Windows Terminal Servers and physical PCs.
    * **Selectable:** yes  
"GLOBAL_ROLE_PERMISSION_MANAGEMENT"| GLOBAL_ROLE_PERMISSION_MANAGEMENT Privilege 
    * **Name:** Manage Roles and Permissions
    * **Type:** Global
    * **Description:** Add, modify, and delete administrator roles and permissions.
    * **Selectable:** yes  
"GLOBAL_ROLE_MANAGEMENT"| GLOBAL_ROLE_MANAGEMENT Privilege 
    * **Name:** Manage Roles
    * **Type:** Global
    * **Description:** Add, modify, and delete administrator roles.
    * **Selectable:** no  
"GLOBAL_ROLE_VIEW"| GLOBAL_ROLE_VIEW Privilege 
    * **Name:** Manage Roles (Read only)
    * **Type:** Global
    * **Description:** Read only access to administrator roles.
    * **Selectable:** no  
"GLOBAL_PERMISSION_VIEW"| GLOBAL_PERMISSION_VIEW Privilege 
    * **Name:** Manage Permissions (Read only)
    * **Type:** Global
    * **Description:** Read only access to administrator permissions.
    * **Selectable:** no  
"GLOBAL_PERMISSION_MANAGEMENT"| GLOBAL_PERMISSION_MANAGEMENT Privilege 
    * **Name:** Manage Permissions
    * **Type:** Global
    * **Description:** Add, modify, and delete administrator permissions.
    * **Selectable:** no  
"GLOBAL_CONFIG_VIEW"| GLOBAL_CONFIG_VIEW Privilege 
    * **Name:** Manage Global Configuration and Policies (Read only)
    * **Type:** Global
    * **Description:** Read only access to global (non-inventory) policy, configuration, and RDS server settings, except administrator roles and permissions and global (Multi-Datacenter View) LDAP.
    * **Selectable:** no  
"GLOBAL_CONFIG_MANAGEMENT"| GLOBAL_CONFIG_MANAGEMENT Privilege 
    * **Name:** Manage Global Configuration and Policies
    * **Type:** Global
    * **Description:** View and change global (non-inventory) policy, configuration, and RDS server settings, except for administrator roles and permissions.
    * **Selectable:** yes  
"FOLDER_MANAGEMENT"| FOLDER_MANAGEMENT Privilege 
    * **Name:** Manage Access Groups
    * **Type:** Global
    * **Description:** Add, modify, and delete access groups.
    * **Selectable:** yes  
"FOLDER_VIEW"| FOLDER_VIEW Privilege 
    * **Name:** Manage Access Groups (Read only)
    * **Type:** Access group
    * **Description:** Read only access to access groups.
    * **Selectable:** no  
"POOL_VIEW"| POOL_VIEW Privilege 
    * **Name:** Manage Desktops, Farms, and Applications (Read only)
    * **Type:** Inventory - desktop
    * **Description:** Read only access to desktops, farms, applications, their local sessions, and their machines.
    * **Selectable:** no  
"POOL_MANAGEMENT"| POOL_MANAGEMENT Privilege 
    * **Name:** Manage Desktops, Farms, and Applications
    * **Type:** Inventory - desktop
    * **Description:** Add, modify, and delete desktops, applications and farms. Add and remove machines from desktops.
    * **Selectable:** yes
    * **Includes:** POOL_ENABLE, POOL_ENTITLE, POOL_SVI_IMAGE_MANAGEMENT  
"POOL_ENABLE"| POOL_ENABLE Privilege 
    * **Name:** Enable Desktops, Farms, and Applications
    * **Type:** Inventory - desktop
    * **Description:** Enable and disable desktops, farms, and applications.
    * **Selectable:** yes  
"POOL_ENTITLE"| POOL_ENTITLE Privilege 
    * **Name:** Entitle Desktops and Applications
    * **Type:** Inventory - desktop
    * **Description:** Add and remove desktop and application entitlements.
    * **Selectable:** yes  
"POOL_SVI_IMAGE_MANAGEMENT"| POOL_SVI_IMAGE_MANAGEMENT Privilege 
    * **Name:** Manage maintenance operations on Automated Desktops & Farms
    * **Type:** Inventory - desktop
    * **Description:** Schedule push image, schedule maintenance and change default image for desktop and farm.
    * **Selectable:** yes  
"MACHINE_VIEW"| MACHINE_VIEW Privilege 
    * **Name:** Manage Machines (read only)
    * **Type:** Inventory - machine
    * **Description:** Read only access to machines and their local sessions.
    * **Selectable:** no  
"MACHINE_MANAGEMENT"| MACHINE_MANAGEMENT Privilege 
    * **Name:** Manage Machines
    * **Type:** Inventory - machine
    * **Description:** Perform all machine and session-related commands.
    * **Selectable:** yes
    * **Includes:** MACHINE_REBOOT, MACHINE_MANAGE_VDI_SESSION, MACHINE_MANAGE_OFFLINE_SESSION, MACHINE_USER_MANAGEMENT, MACHINE_MAINTENANCE, MANAGE_REMOTE_PROCESS, REMOTE_ASSISTANCE  
"MACHINE_REBOOT"| MACHINE_REBOOT Privilege 
    * **Name:** Manage Reboot Operation
    * **Type:** Inventory - machine
    * **Description:** Reset local machines.
    * **Selectable:** yes  
"MACHINE_MANAGE_VDI_SESSION"| MACHINE_MANAGE_VDI_SESSION Privilege 
    * **Name:** Manage Local Sessions
    * **Type:** Inventory - machine
    * **Description:** Disconnect, logoff, and send messages to local sessions.
    * **Selectable:** yes  
"MACHINE_MANAGE_OFFLINE_SESSION"| MACHINE_MANAGE_OFFLINE_SESSION Privilege 
    * **Name:** Manage Offline Sessions
    * **Type:** Inventory - machine
    * **Description:** Roll back offline sessions and initiate replications.
    * **Selectable:** yes  
"MACHINE_USER_MANAGEMENT"| MACHINE_USER_MANAGEMENT Privilege 
    * **Name:** Manage User Assignments and Machine Aliases
    * **Type:** Inventory - machine
    * **Description:** Assign and unassign users for machines, Update machine aliases for machines
    * **Selectable:** yes  
"MACHINE_MAINTENANCE"| MACHINE_MAINTENANCE Privilege 
    * **Name:** Manage Machine Maintenance Operations
    * **Type:** Inventory - machine
    * **Description:** Put machine in and out of maintenance mode. 
    * **Selectable:** yes  
"MANAGE_REMOTE_PROCESS"| MANAGE_REMOTE_PROCESS Privilege 
    * **Name:** Manage Remote Processes and Applications
    * **Type:** Inventory - machine
    * **Description:** Manage Remote Processes and Applications.
    * **Selectable:** yes  
"REMOTE_ASSISTANCE"| REMOTE_ASSISTANCE Privilege 
    * **Name:** Remote Assistance
    * **Type:** Inventory - machine
    * **Description:** Remote Assistance to Remote desktop.
    * **Selectable:** yes  
"API_SMART_CARD_BYPASS"| API_SMART_CARD_BYPASS Privilege 
    * **Name:** Bypass smart card authentication
    * **Type:** All
    * **Description:** Allows API's credential based login when smart card authentication mode is REQUIRED.
    * **Selectable:** yes  
"MANAGE_CERTIFICATES"| MANAGE_CERTIFICATES Privilege 
    * **Name:** Manage Certificates
    * **Type:** All
    * **Description:** Allows user to import the certificates or generate-csr
    * **Selectable:** yes  

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
