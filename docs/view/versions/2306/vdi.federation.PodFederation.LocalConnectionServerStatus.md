---
layout: page
title: Data Object - PodFederationLocalConnectionServerStatus
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.federation.PodFederation.LocalConnectionServerStatus  
Property of
     [PodFederationLocalPodStatus](vdi.federation.PodFederation.LocalPodStatus.md#field_detail)  
See also
     [ConnectionServerId](vdi.entity.ConnectionServerId.md), [MapEntry](vdi.util.MapEntry.md)  
Since 
    Horizon View 6.0

## Data Object Description 

Multi-DataCenter View status for a Connection Server. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [ConnectionServerId](vdi.entity.ConnectionServerId.md)|  Entity id of the connection server to which this status pertains.   
  
**name**|  xsd:string|  Name of the connection server  **_Since_** Horizon 7.8  
  
**status**|  xsd:string|  The Multi-DataCenter View status for this Connection Server. Individual connection server statuses should converge to the containing Pod's status over time.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"ENABLED"| Multi-DataCenter View is enabled.  
"DISABLED"| Multi-DataCenter View is disabled.  
"PENDING"| Multi-DataCenter View is undergoing an operation related to initialization, uninitialization, joining, or unjoining.  
"ENABLE_ERROR"| This status indicates the current Connection Server has failed to reach the ENABLED status in a timely manner. Other Connection Servers in the same Pod were successfully ENABLED. This status may also indicate the current Connection Server was recently installed.  
"DISABLE_ERROR"| This status indicates the current Connection Server has failed to reach the DISABLED status in a timely manner. Other Connection Servers in the same Pod were successfully DISABLED.  

  
**pendingPercentage**|  xsd:int|  Value between 0 and 100 representing completion percentage when Connection Server status is pending. Null in other status states.   


* This property need not be set.

  
**errorMessage**|  xsd:string|  The Multi-DataCenter View error message for this Connection Server, if any is populated, or a success message.   


* This property need not be set.

  
**errorMessageId**|  xsd:string|  Message ID of the error message.   


* This property need not be set.

  
**errorMessageValues**| [MapEntry[]](vdi.util.MapEntry.md)|  The error message values.   


* This property need not be set.
  * This property is a set of entries with unique "key" members.

  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

