---
layout: page
title: Data Object - LocalSessionStatistics
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.statistics.SessionStatistics.LocalSessionStatistics`

Returned by
> [SessionStatistics_GetLocalSessionStatistics](vdi.statistics.SessionStatistics.md#getLocalSessionStatistics)

See also
> [SessionClientStatistics](vdi.statistics.SessionStatistics.SessionClientStatistics.md), [SessionGatewayStatistics](vdi.statistics.SessionStatistics.SessionGatewayStatistics.md), [SessionProtocolStatistics](vdi.statistics.SessionStatistics.SessionProtocolStatistics.md), [SessionsStateStatistics](vdi.statistics.SessionStatistics.SessionStateStatistics.md)

Since
> Horizon 7.7


## Data Object Description

summary for session Statistics

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**numSessions**|  xsd:int|  The total number of sessions. [^2]
**numUsers**|  xsd:int|  The total number of users. [^2]
**desktopSessionStatistics**| [SessionsStateStatistics](vdi.statistics.SessionStatistics.SessionStateStatistics.md)|  The session state Statistics for VDI sessions. [^2]
**rdsSessionStatistics**| [SessionsStateStatistics](vdi.statistics.SessionStatistics.SessionStateStatistics.md)|  The session state Statistics for RDS sessions. [^2]
**applicationSessionStatistics**| [SessionsStateStatistics](vdi.statistics.SessionStatistics.SessionStateStatistics.md)|  The session state Statistics for application sessions. [^2]
**protocolStatistics**| [SessionProtocolStatistics](vdi.statistics.SessionStatistics.SessionProtocolStatistics.md)|  The protocol Statistics for sessions. [^2]
**clientStatistics**| [SessionClientStatistics](vdi.statistics.SessionStatistics.SessionClientStatistics.md)|  The client Statistics for sessions. [^2]
**gatewayStatistics**| [SessionGatewayStatistics](vdi.statistics.SessionStatistics.SessionGatewayStatistics.md)|  The gateway Statistics for sessions. [^2]
 


 
