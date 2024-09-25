---
layout: page
title: Data Object - DesktopProvisioningStatusData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.Desktop.ProvisioningStatusData
Property of
     [DesktopAutomatedDesktopData](vdi.resources.Desktop.AutomatedDesktopData.md#field_detail)
See also
     [DesktopInstantCloneDesktopProvisioningStatusData](vdi.resources.Desktop.InstantCloneProvisioningStatusData.md)
Since 
    Horizon View 6.0

## Data Object Description 

Provisioning status data about this desktop. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**lastProvisioningError**|  xsd:string|  String message detailing the last provisioning error on this desktop while [stopProvisioningOnError](vdi.resources.Desktop.VirtualCenterProvisioningSettings.md#stopProvisioningOnError) is enabled. This will be cleared when [enableProvisioning](vdi.resources.Desktop.VirtualCenterProvisioningSettings.md#enableProvisioning) is updated to true.   


[^1]
[^2]

  
**lastProvisioningErrorTime**|  xsd:dateTime|  Time the last provisioning error occurred on this desktop while [stopProvisioningOnError](vdi.resources.Desktop.VirtualCenterProvisioningSettings.md#stopProvisioningOnError) is enabled. This will be cleared when [enableProvisioning](vdi.resources.Desktop.VirtualCenterProvisioningSettings.md#enableProvisioning) is updated to true.   


[^1]
[^2]

  
**instantCloneProvisioningStatusData**| [DesktopInstantCloneDesktopProvisioningStatusData](vdi.resources.Desktop.InstantCloneProvisioningStatusData.md)|  ProvisioningStatusData applicable only to instant clone desktops.  **_Since_** Horizon 7.0  


[^1]
[^2]

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
