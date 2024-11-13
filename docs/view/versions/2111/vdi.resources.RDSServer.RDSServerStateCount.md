---
layout: page
title: Data Object - RDSServerStateCount
hide:
#- navigation
- toc
---





Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.resources.RDSServer.RDSServerStateCount`

Returned by
> [RDSServer_GetStateCounts](vdi.resources.RDSServer.md#getRDSServerStateCounts)

See also
> [PreparedCount](vdi.resources.RDSServer.PreparedCount.md), [ProblemCount](vdi.resources.RDSServer.ProblemCount.md), [UnderConstructionCount](vdi.resources.RDSServer.UnderConstructionCount.md)

Since
> Horizon 8.4


## Data Object Description

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**problemCount**| [ProblemCount](vdi.resources.RDSServer.ProblemCount.md)|  Counts of the RDS server machines which are in problem state. [^2]
**underConstructionCount**| [UnderConstructionCount](vdi.resources.RDSServer.UnderConstructionCount.md)|  Counts of the RDS server machines which are in under construction state. [^2]
**preparedCount**| [PreparedCount](vdi.resources.RDSServer.PreparedCount.md)|  Counts of the RDS server machines which are in prepared state. [^2]


 


[^2]: This property cannot be updated.