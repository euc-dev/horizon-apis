---
layout: page
title: Data Object - ViewComposerHealthInfo
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.health.ViewComposerHealth.ViewComposerHealthInfo
Returned by
     [ViewComposerHealth_Get](vdi.health.ViewComposerHealth.md#get), [ViewComposerHealth_List](vdi.health.ViewComposerHealth.md#list)
See also
     [ViewComposerHealthConnectionServerConnectionData](vdi.health.ViewComposerHealth.ConnectionServerConnectionData.md), [ViewComposerHealthData](vdi.health.ViewComposerHealth.ViewComposerHealthData.md)
Since 
    Horizon View 6.0

## Data Object Description 

Information about the health of a View Composer server. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**serverName**|  xsd:string|  The host name or ip address for the View Composer server.   
  
**port**|  xsd:int|  the port number configured for the View Composer server   


[^1]

  
**data**| [ViewComposerHealthData](vdi.health.ViewComposerHealth.ViewComposerHealthData.md)|  Basic information about the View Composer server.   
  
**connectionServerData**| [ViewComposerHealthConnectionServerConnectionData[]](vdi.health.ViewComposerHealth.ConnectionServerConnectionData.md)|  Information about the View Composer connections from each connection server.   


[^1]

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

