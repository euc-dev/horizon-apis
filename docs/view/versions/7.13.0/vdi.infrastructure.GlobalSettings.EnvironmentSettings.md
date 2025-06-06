---
layout: page
title: Data Object - EnvironmentSettings
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.infrastructure.GlobalSettings.EnvironmentSettings`

Returned by
> [GlobalSettings_GetEnvironmentSettings](vdi.infrastructure.GlobalSettings.md#getEnvironmentSettings)

Since
> Horizon 7.6


## Data Object Description

Environment settings information.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**ipMode**|  xsd:string|  Indicates the IP mode of the environment. [^1]<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"IPv4"</td><td>This Connection Server is running in IPv4 environment.</td></tr><tr><td>"IPv6"</td><td>This Connection Server is running in IPv6 environment.</td></tr></table>
**fipsModeEnabled**|  xsd:boolean|  Indicates if FIPS mode is enabled. [^5] [^1]
**clusterName**|  xsd:string|  The name of a group of connection servers sharing the same configuration.  **_Since_** Horizon 7.7 [^1]
**clusterGuid**|  xsd:string|  The GUID of a group of connection servers sharing the same configuration.  **_Since_** Horizon 7.7 [^1]
**localPodName**|  xsd:string|  The name of the current pod in the Multi-DataCenter View Pod, the value will be null when PodFederation is not initialized.  **_Since_** Horizon 7.7 [^1]
**timezoneOffset**|  xsd:int|  Represents this Connection Server's time zone offset from UTC in seconds.  **_Since_** Horizon 7.7 [^1]


 


[^1]: This property need not be set.
[^5]: This property has a default value of false.