---
layout: page
title: Data Object - DesktopVirtualCenterManagedCommonSettings
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.resources.Desktop.VirtualCenterManagedCommonSettings`

Property of  
> [DesktopAutomatedDesktopData](vdi.resources.Desktop.AutomatedDesktopData.md#field_detail), [DesktopAutomatedDesktopSpec](vdi.resources.Desktop.AutomatedDesktopSpec.md#field_detail), [DesktopManualDesktopData](vdi.resources.Desktop.ManualDesktopData.md#field_detail), [DesktopManualDesktopSpec](vdi.resources.Desktop.ManualDesktopSpec.md#field_detail)

Since  
> Horizon View 6.1


## Data Object Description 

Settings common to both Manual and Automated Desktops managed by Virtual Center sources. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**transparentPageSharingScope**|  xsd:string|  The transparent page sharing scope.   


  * This property has a default value of "VM".
  * This property will be one of:  
|  Value |  Description   
---|---  
"VM"| Inter-VM page sharing is not permitted.  
"DESKTOP"| Inter-VM page sharing among VMs belonging to the same Desktop is permitted.  
"POD"| Inter-VM page sharing among VMs belonging to the same Pod is permitted.  
"GLOBAL"| Inter-VM page sharing among all VMs on the same host is permitted.  

  
  
  
 
  
  
