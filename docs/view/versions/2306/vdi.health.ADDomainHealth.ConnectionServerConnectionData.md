---
layout: page
title: Data Object - ADDomainHealthConnectionServerConnectionData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.health.ADDomainHealth.ConnectionServerConnectionData
Property of
     [ADDomainHealthInfo](vdi.health.ADDomainHealth.ADDomainHealthInfo.md#field_detail)
See also
     [ConnectionServerId](vdi.entity.ConnectionServerId.md)
Since 
    Horizon View 6.0

## Data Object Description 

The domain connection health for a connection server. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [ConnectionServerId](vdi.entity.ConnectionServerId.md)|  The ID of the connection server.   
  
**connectionServerName**|  xsd:string|  The name of the connection server.   
  
**status**|  xsd:string|  The status of the connection to the domain.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"OK"| Domain is accepting LDAP bind operations and has full functionality.  
"WARN"| Domain is only accepting LDAP ping operations and has limited functionality. This may indicate a one-way trust relationship with this domain.  
"ERROR"| Domain can not be contacted.  
"UNKNOWN"| Domain health could not be determined.  

  
**trustRelationship**|  xsd:string|  The trust relationship for the domain.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"PRIMARYDOMAIN"| The domain is the domain that the broker is present in.  
"FROMBROKER"| The domain is trusted by the domain that the broker is in.  
"TOBROKER"| The domain trusts the brokers domain (this is for completeness and generally will not be used).  
"TWOWAY"| The domain has a two way trust relationship with the broker's domain.  
"TWOWAY_FOREST"| The domain is in the same forest as the broker domain, implies two way trust.  
"MANUAL"| The domain was manually configured (the trust has not been detected).  
"UNKNOWN"| The trust relationship could not be determined  
"NOTRUST"| The domain not having trust with broker domain.  

  
**contactable**|  xsd:string|  Whether the domain can be contacted.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"UNCONTACTABLE"| No domain controllers appear to be present on the network for this domain.  
"FULLYACCESSIBLE"| The domain controller(s) are accepting bind operations.  
"CANNOTBIND"| The domain controller(s) are only accepting LDAP ping operations.  
"UNKNOWN"| Cannot determine accessibility.  

  
**refId**|  xsd:string|  Reference ID of the connection server.  **_Since_** Horizon 7.10  


[^1]

  
**lastUpdatedTimestamp**|  xsd:long|  The timestamp in milliseconds when the last update was obtained. Measured as epoch time.  **_Since_** Horizon 7.12  


[^1]
[^2]

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

