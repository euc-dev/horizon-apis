---
layout: page
title: Data Object - VirtualCenterHealthConnectionServerConnectionData
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.health.VirtualCenterHealth.ConnectionServerConnectionData`

Property of  
> [VirtualCenterHealthInfo](vdi.health.VirtualCenterHealth.VirtualCenterHealthInfo.md#field_detail)

See also  
> [CertificateHealthData](vdi.health.CertificateHealthData.md), [ConnectionServerId](vdi.entity.ConnectionServerId.md)

Since  
> Horizon View 6.0


## Data Object Description 

Health information for a specific connection server's connection to the virtual center server. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [ConnectionServerId](vdi.entity.ConnectionServerId.md)|  The ID of the connection server.   
  
**name**|  xsd:string|  The name of the Connection Server.   
  
**status**|  xsd:string|  The status of the connection to the Virtual Center server.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"STATUS_UP"| The connection to Virtual Center server is working properly.  
"STATUS_DOWN"| The connection to Virtual Center server was down  
"STATUS_RECONNECTING"| The connection to Virtual Center server was lost and is being reconnected to.  
"STATUS_UNKNOWN"| Connection state to Virtual Center server is unknown.  
"STATUS_INVALIDCREDENTIALS"| The supplied credentials cannot be used to authenticate to the Virtual Center server.  
"STATUS_CANNOTLOGIN"| The connection server cannot login to the Virtual Center server.  
"STATUS_NOT_YET_CONNECTED"| Connection server has not yet connect to Virtual Center server.  

  
**thumbprintAccepted**|  xsd:boolean|  Whether the thumbprint of the Virtual Center server was accepted.   


* This property need not be set.

  
**certificateHealth**| [CertificateHealthData](vdi.health.CertificateHealthData.md)|  The health of the certificate.   


* This property need not be set.
  * This property is required if thumbprintAccepted is set to false.

  
**refId**|  xsd:string|  Reference ID of the connection server.  **_Since_** Horizon 7.10  


* This property need not be set.

  
**lastUpdatedTimestamp**|  xsd:long|  The timestamp in milliseconds when the last update was obtained. Measured as epoch time.  **_Since_** Horizon 7.12  


* This property need not be set.
* This property cannot be updated.

  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
