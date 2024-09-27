---
layout: page
title: Data Object - RCXServerInfo
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.infrastructure.RCX.RCXServerInfo  
See also
     [CertificateThumbprint](vdi.utils.Certificate.CertificateThumbprint.md), [RCXServerId](vdi.entity.RCXServerId.md)  
Since 
    Horizon 7.11

## Data Object Description 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [RCXServerId](vdi.entity.RCXServerId.md)|  ID of the RCX server.   
  
**host**|  xsd:string|  FQDN/IP address of the RCX server.   
  
**thumbprints**| [CertificateThumbprint[]](vdi.utils.Certificate.CertificateThumbprint.md)|  Thumbprints of the RCX server certificates.   


* This property need not be set.

  
**port**|  xsd:int|  RCX server's port.   
  
**status**|  xsd:string|  This indicates the current status of RCX server.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"UP"| RCX server is running.  
"DOWN"| RCX server is down.  
"UNKNOWN"| RCX server status is unknown.  

  
**version**|  xsd:string|  Version information of RCX server.   
  
  
  
 
  
  

