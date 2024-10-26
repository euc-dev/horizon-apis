---
layout: page
title: Data Object - RDSServerSummaryData
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.resources.RDSServer.RDSServerSummaryData`

Property of
> [RDSServerSummaryView](vdi.resources.RDSServer.RDSServerSummaryView.md#field_detail)

Since
> Horizon View 6.0


## Data Object Description

RDSServerSummaryData

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**farmName**|  xsd:string|  Farm name that the RDS server (optionally) belongs to [^1] [^2]
**desktopName**|  xsd:string|  Desktop name that the RDS server (optionally) is associated with [^1] [^2]
**farmType**|  xsd:string|  Represents the Farm type that RDS Server is part of.  **_Since_** Horizon 7.6 <br>* This property has a default value of "NONE". [^1] [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>AUTOMATED</td><td>This RDS Server is part of Automated Farm.</td></tr><tr><td>MANUAL</td><td>This RDS Server is part of Manual Farm.</td></tr><tr><td>NONE</td><td>This RDS Server is not part of any Farm.</td></tr></table>




 


[^1]: This property need not be set.
[^2]: This property cannot be updated.