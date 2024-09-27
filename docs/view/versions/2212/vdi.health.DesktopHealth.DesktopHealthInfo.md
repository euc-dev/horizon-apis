---
layout: page
title: Data Object - DesktopHealthInfo
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.health.DesktopHealth.DesktopHealthInfo  
Returned by
     [DesktopHealth_Get](vdi.health.DesktopHealth.md#get)  
See also
     [AccessGroupId](vdi.entity.AccessGroupId.md), [ApplicationStatusInfo](vdi.health.DesktopHealth.ApplicationStatusInfo.md), [DesktopId](vdi.entity.DesktopId.md)  

## Data Object Description 

Desktop health Information. This data will be populated only for the desktops which support application remoting. 

##  Queryable Data Object 

This data object is queryable using [QueryService](vdi.query.QueryService.md "QueryService"). 

Query Privileges 

Privilege |  Description   
---|---  
POOL_VIEW|  privilege is required to query information   
  


## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [DesktopId](vdi.entity.DesktopId.md)|  Desktop entity ID   


* This property cannot be updated.

  
**name**|  xsd:string|  Desktop name   


* This property cannot be updated.

  
**type**|  xsd:string|  Desktop type   


* This property cannot be updated.
  * This property will be one of:  
|  Value |  Description   
---|---  
"AUTOMATED"| An automated desktop creates virtual machines cloned from a base template or snapshot.  
"MANUAL"| A manual machine desktop allows selection of existing virtual machines and addition to the desktop of available machines to connect to.  
"RDS"| An RDS Desktop Desktop.  

  
**health**|  xsd:string|  Desktop health   


* This property cannot be updated.
  * This property will be one of:  
|  Value |  Description   
---|---  
"OK"| Desktop is enabled and no machines are in WARNING or ERROR state. One or more machine(s) may be DISABLED (including the case where all of them are DISABLED).  
"WARNING"| Desktop is enabled. One or more machine(s) is either in WARNING or ERROR (not exceeding the predefined threshold) state.  
"ERROR"| Desktop is enabled. One or more machine(s) (exceeding the predefined threshold) is in ERROR state, or, for Automated Desktops, there could be a provisioning error.  
"DISABLED"| Desktop is disabled.  

  
**source**|  xsd:string|  Source of machines.   


* This property need not be set.
* This property cannot be updated.
  * This property is required if type is set to "AUTOMATED".
  * This property will be one of:  
|  Value |  Description   
---|---  
"VIRTUAL_CENTER"| Virtual center virtual machines managed as view machines. This option is valid for Automated and Manual Desktop. In case of Automated Desktop, these refer to Full Virtual Machines that are created from a vCenter Server template.  
"VIEW_COMPOSER"| View composer linked clones managed as view machines. They share the same base image and use less storage space than full virtual machines. The user profile for linked clones can be redirected to persistent disks that will be unaffected by OS updates and refreshes. This option is only valid for Automated Desktop.  
"INSTANT_CLONE_ENGINE"| Instant clone engine created 'instant clones' managed as view machines. Instant clone engine uses vmfork technology to create the instant clones, these clones take very less time for provisioning. Instant clones have many similarities to linked clones like :-  

    * Both instant and linked clones share the same base image and use less storage space than full virtual machines.
    * The user profile for both types clones can be redirected to persistent disks that will be unaffected by OS updates and refreshes.
This option is only valid for Automated Desktop.  
"UNMANAGED"| Non-vCenter Server virtual machines managed as view machines. These can include physical computers, non-vCenter Server virtual machines, and blade PCs. This option is only valid for Manual Desktops.  
"RDS"| This option is only valid for RDS Desktops.  

  
**accessGroup**| [AccessGroupId](vdi.entity.AccessGroupId.md)|  Access group associated with this Desktop.   


* This property cannot be updated.

  
**enableAppRemoting**|  xsd:boolean|  True, if this desktop can be used for application pool creation.   


  * This property has a default value of false.
* This property need not be set.

  
**applicationStatus**| [ApplicationStatusInfo[]](vdi.health.DesktopHealth.ApplicationStatusInfo.md)|  Application status   


* This property need not be set.
* This property cannot be updated.

  
  
  
  
  
  

