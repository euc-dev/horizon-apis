---
layout: page
title: Data Object - PreparedCount
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.resources.RDSServer.PreparedCount`

Property of  
> [RDSServerStateCount](vdi.resources.RDSServer.RDSServerStateCount.md#field_detail)

Since  
> Horizon 8.4


## Data Object Description 

Number of the RDS server machines which are in prepared states. Such machine's [status](vdi.resources.RDSServer.RDSServerStateView.md#status) is one of the following : PROVISIONED,AVAILABLE,CONNECTED,DISCONNECTED. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**available**|  xsd:int|  Number of RDS server machines which are in AVAILABLE [status](vdi.resources.RDSServer.RDSServerStateView.md#status)   


* This property cannot be updated.

  
**provisioned**|  xsd:int|  Number of RDS server machines which are in PROVISIONED [status](vdi.resources.RDSServer.RDSServerStateView.md#status)   


* This property cannot be updated.

  
  
  
 
  
  
