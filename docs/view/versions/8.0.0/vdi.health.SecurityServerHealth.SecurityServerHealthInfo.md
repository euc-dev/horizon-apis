---
layout: page
title: Data Object - SecurityServerHealthInfo
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.health.SecurityServerHealth.SecurityServerHealthInfo`

Returned by  
> [SecurityServerHealth_Get](vdi.health.SecurityServerHealth.md#get), [SecurityServerHealth_List](vdi.health.SecurityServerHealth.md#list)

See also  
> [CertificateHealthData](vdi.health.CertificateHealthData.md), [SecurityServerHealthConnectionData](vdi.health.SecurityServerHealth.ConnectionData.md), [SecurityServerId](vdi.entity.SecurityServerId.md)

Since  
> Horizon View 6.0


## Data Object Description 

**Deprecated.**_This is being deprecated since Security Server will no longer be supported in future releases. Please consider using Unified Access Gateway (UAG) instead._

Health information about a security server. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [SecurityServerId](vdi.entity.SecurityServerId.md)|  The ID for this security server.   
  
**name**|  xsd:string|  The name of this security server.   
  
**status**|  xsd:string|  The status of this security server.  **_Since_** Horizon 7.0  


  * This property will be one of:  
|  Value |  Description   
---|---  
"OK"| The connection to the security server is working properly.  
"NOT_RESPONDING"| The security server is not responding.  
"UNKNOWN"| The status of the security server is not known.  

  
**version**|  xsd:string|  The version of the Security Server.   
  
**build**|  xsd:string|  Build number of the security server.   
  
**connectionData**| [SecurityServerHealthConnectionData](vdi.health.SecurityServerHealth.ConnectionData.md)|  The connection data for this security server.   
  
**defaultCertificate**|  xsd:boolean|  Is this the default certificate?   
  
**certificateHealth**| [CertificateHealthData](vdi.health.CertificateHealthData.md)|  The certificate data for this security server.   
  
**ipSecStatus**|  xsd:string|  The status of the IPSec connection to the Connection Server.   
  
**pcoipControllerStatus**|  xsd:string|  The PCoIP controller status of this security server.  **_Since_** Horizon 7.0  
  
  
  

  
  
