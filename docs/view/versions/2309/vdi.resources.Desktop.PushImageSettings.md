---
layout: page
title: Data Object - DesktopPushImageSettings
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.Desktop.PushImageSettings  
Property of
     [DesktopImageManagementPushImageSpec](vdi.resources.Desktop.ImageManagementPushImageSpec.md#field_detail), [DesktopInstantCloneDesktopProvisioningStatusData](vdi.resources.Desktop.InstantCloneProvisioningStatusData.md#field_detail), [DesktopPushImageSpec](vdi.resources.Desktop.PushImageSpec.md#field_detail)  
Since 
    Horizon 7.0

## Data Object Description 

Settings for the push image operation. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**startTime**|  xsd:dateTime|  When to start the operation. If unset or the time is in the past, the operation will begin immediately.   


 * This property need not be set.

  
**logoffSetting**|  xsd:string|  Determines when to perform the operation on machines which have an active session.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"FORCE_LOGOFF"| Users will be forced to log off when the system is ready to operate on their virtual machines. Before being forcibly logged off, users may have a grace period in which to save their work (Global Settings).  
"WAIT_FOR_LOGOFF"| Wait for connected users to disconnect before the task starts. The operation starts immediately on machines without active sessions.  

  
**stopOnFirstError**|  xsd:boolean|  Indicates that the operation should stop on first error.   


  * This property has a default value of true.

  
**addVirtualTPM**|  xsd:boolean|  Whether to add Virtual TPM device.  **_Since_** Horizon 7.7  


  * This property has a default value of false.
 * This property need not be set.

  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

