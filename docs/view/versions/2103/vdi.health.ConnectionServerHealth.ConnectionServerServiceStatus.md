---
layout: page
title: Data Object - ConnectionServerServiceStatus
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.health.ConnectionServerHealth.ConnectionServerServiceStatus`

Property of
> [ConnectionServerHealthInfo](vdi.health.ConnectionServerHealth.ConnectionServerHealthInfo.md#field_detail)

Since
> Horizon 7.10


## Data Object Description

Information about the status of Connection Server related Services.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**serviceName**|  xsd:string|  Name of the service<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"SECURITY_GATEWAY_COMPONENT"</td><td>Security Gateway Component Service.</td></tr><tr><td>"PCOIP_SECURE_GATEWAY"</td><td>PCoIP Secure Gateway Service.</td></tr><tr><td>"BLAST_SECURE_GATEWAY"</td><td>BLAST Secure Gateway Service.</td></tr></table>
**status**|  xsd:string|  Status of the service.<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"UP"</td><td>Service is working properly.</td></tr><tr><td>"DOWN"</td><td>Service is not working properly.</td></tr></table>


 
