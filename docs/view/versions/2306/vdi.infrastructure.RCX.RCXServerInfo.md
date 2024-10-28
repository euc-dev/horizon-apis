---
layout: page
title: Data Object - RCXServerInfo
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.infrastructure.RCX.RCXServerInfo`

See also
> [CertificateThumbprint](vdi.utils.Certificate.CertificateThumbprint.md), [RCXServerId](vdi.entity.RCXServerId.md)

Since
> Horizon 7.11


## Data Object Description

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**id**| [RCXServerId](vdi.entity.RCXServerId.md)|  ID of the RCX server.
**host**|  xsd:string|  FQDN/IP address of the RCX server.
**thumbprints**| [CertificateThumbprint[]](vdi.utils.Certificate.CertificateThumbprint.md)|  Thumbprints of the RCX server certificates. [^1]
**port**|  xsd:int|  RCX server's port.
**status**|  xsd:string|  This indicates the current status of RCX server.<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"UP"</td><td>RCX server is running.</td></tr><tr><td>"DOWN"</td><td>RCX server is down.</td></tr><tr><td>"UNKNOWN"</td><td>RCX server status is unknown.</td></tr></table>
**version**|  xsd:string|  Version information of RCX server.
 


 


[^1]: This property need not be set.