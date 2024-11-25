---
layout: page
title: Data Object - SessionProtocolStatistics
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.statistics.SessionStatistics.SessionProtocolStatistics`

Property of
> [LocalSessionStatistics](vdi.statistics.SessionStatistics.LocalSessionStatistics.md#field_detail)

Since
> Horizon 7.7


## Data Object Description

Statistics for Session protocol.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**numBlastSessions**|  xsd:int|  The number of sessions using blast. [^2]
**numPcoipSessions**|  xsd:int|  The number of sessions using pcoip. [^2]
**numRdpSessions**|  xsd:int|  The number of sessions using RDP. [^2]
**numOtherProtocols**|  xsd:int|  The number of sessions using protocol not belonging to blast, pcoip, RDP. [^2]


 


[^2]: This property cannot be updated.