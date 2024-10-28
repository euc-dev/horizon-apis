---
layout: page
title: Data Object - SessionClientStatistics
hide:
#- navigation
- toc
---





Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.statistics.SessionStatistics.SessionClientStatistics`

Property of
> [LocalSessionStatistics](vdi.statistics.SessionStatistics.LocalSessionStatistics.md#field_detail)

Since
> Horizon 7.7


## Data Object Description

Statistics for Client type of sessions.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**numWindowsClients**|  xsd:int|  The number of sessions whose client type is Windows. [^2]
**numMacClients**|  xsd:int|  The number of sessions whose client type is Mac. [^2]
**numBrowserClients**|  xsd:int|  The number of sessions whose client type is htmlaccess. [^2]
**numLinuxClients**|  xsd:int|  The number of sessions whose client type is Linux. [^2]
**numAndroidClients**|  xsd:int|  The number of sessions whose client type is Android. [^2]
**numIosClients**|  xsd:int|  The number of sessions whose client type is iOS. [^2]
**numOtherClients**|  xsd:int|  The number of sessions whose client type is other. [^2]


 


[^2]: This property cannot be updated.