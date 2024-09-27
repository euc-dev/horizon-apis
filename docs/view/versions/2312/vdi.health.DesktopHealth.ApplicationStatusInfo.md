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
Since 
    Horizon View 6.0

## Data Object Description 

Status of applications created from desktop. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [ApplicationId](vdi.entity.ApplicationId.md)|  Application Entity Id   


 * This property cannot be updated.

  
**status**|  xsd:string|  Application Status   


 * This property cannot be updated.
  * This property will be one of:  
|  Value |  Description   
---|---  
"AVAILABLE"| The application is available in all machines of the desktop.  
"MISSING"| The application is missing in one or more machines in the desktop.  
"UNAVAILABLE"| Could happen in any of following cases:  

    * The application is missing in all the machines of the desktop.
    * Desktop do not have any provisioned machines.  
"DISABLED"| The desktop is disabled and the application is disabled.  

  
  
  
   
  
  

