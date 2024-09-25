---
layout: page
title: Data Object - ApplicationStatusInfo
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.health.DesktopHealth.ApplicationStatusInfo
Property of
     [DesktopHealthInfo](vdi.health.DesktopHealth.DesktopHealthInfo.md#field_detail)
See also
     [ApplicationId](vdi.entity.ApplicationId.md)

## Data Object Description 

Status of applications created from desktop. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [ApplicationId](vdi.entity.ApplicationId.md)|  Application Entity Id   


[^2]

  
**status**|  xsd:string|  Application Status   


[^2]
  * This property will be one of:  
|  Value |  Description   
---|---  
"AVAILABLE"| The application is available in all machines of the desktop.  
"MISSING"| The application is missing in one or more machines in the desktop.  
"UNAVAILABLE"| Could happen in any of following cases:  

    * The application is missing in all the machines of the desktop.
    * Desktop do not have any provisioned machines.  
"DISABLED"| The desktop is disabled and the application is disabled.  

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
