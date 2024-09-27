---
layout: page
title: Data Object - ConnectionServerHealthLdapReplicationStatusData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.health.ConnectionServerHealth.LdapReplicationStatusData  
Property of
     [ConnectionServerHealthInfo](vdi.health.ConnectionServerHealth.ConnectionServerHealthInfo.md#field_detail)  
Since 
    Horizon 7.10

## Data Object Description 

Information about the LDAP replication status of the Connection Server. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**serverName**|  xsd:string|  Replica Server name.   
  
**status**|  xsd:string|  Status of the server.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"OK"| The connection to the connection server is working properly.  
"ERROR"| Error occurred when connecting to connection server.  

  
**message**|  xsd:string|  Status message.   


 * This property need not be set.

  
  
  
   
  
  

