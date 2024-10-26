---
layout: page
title: Data Object - RDSServerSessionSettings
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.resources.RDSServer.RDSServerSessionSettings`

Property of
> [FarmHealthRDSServerHealthInfo](vdi.health.FarmHealth.RDSServerHealthInfo.md#field_detail), [RDSServerSettings](vdi.resources.RDSServer.RDSServerSettings.md#field_detail)

Since
> Horizon View 6.0


## Data Object Description

RDS Server session settings

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**maxSessionsType**|  xsd:string|  RDSServer max sessions type. If RDS Server is part of automated farm, this value is inherited from farm configuration. [^134] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>UNLIMITED</td><td>RDSServer has unlimited number of sessions</td></tr><tr><td>LIMITED</td><td>RDSServer has a limited number of sessions</td></tr><tr><td>UNCONFIGURED</td><td>The max number of sessions has not yet been defined for the RDSServer</td></tr></table>
**maxSessionsSetByAdmin**|  xsd:int|  Maximum number of sessions on an RDS server as set by the admin. [^1] [^8] [^9]
 


 


[^1]: This property need not be set.
[^8]: This property has a minimum value of 1.
[^9]: This property is required if maxSessionsType is set to 'LIMITED'.
[^134]: This property has a default value of "UNCONFIGURED".