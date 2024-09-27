---
layout: page
title: Data Object - DesktopBlackoutTime
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.Desktop.BlackoutTime  
Property of
     [DesktopViewStorageAcceleratorSettings](vdi.resources.Desktop.ViewStorageAcceleratorSettings.md#field_detail)  
Since 
    Horizon View 6.0

## Data Object Description 

Fields for specifying blackout time for View Storage Accelerator. Storage accelerator regeneration and VM disk space reclamation do not occur during blackout times. The same blackout policy applies to both operations. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**days**|  xsd:string[]|  List of days for a given range of time.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"MONDAY"| Monday  
"TUESDAY"| Tuesday  
"WEDNESDAY"| Wednesday  
"THURSDAY"| Thursday  
"FRIDAY"| Friday  
"SATURDAY"| Saturday  
"SUNDAY"| Sunday  
"ALL"| All seven days of the week  

  
**startTime**|  xsd:string|  Starting time for the blackout.   


  * This property must be in the form hh:mm in 24 hours format. 

  
**endTime**|  xsd:string|  Ending time for the blackout.   


  * This property must be in the form hh:mm in 24 hours format. 

  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

