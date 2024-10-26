---
layout: page
title: Data Object - HealthCounter
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.health.Monitoring.HealthCounter`

Property of
> [SystemStatusCounter](vdi.health.Monitoring.SystemStatusCounter.md#field_detail)

Returned by
> [Monitoring_GetHealthCounters](vdi.health.Monitoring.md#getHealthCounters)

See also
> [MapEntry](vdi.util.MapEntry.md)


## Data Object Description

The health status information.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**category**|  xsd:string|  Component category. [^2]<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"CONNECTION_SERVER"</td><td>The Connection Server.</td></tr><tr><td>"EVENT_DATABASE"</td><td>The Event Database.</td></tr><tr><td>"CERTIFICATE_SSO"</td><td>The Certificate SSO Connector.</td></tr><tr><td>"VIRTUAL_CENTER"</td><td>The Virtual Center.</td></tr><tr><td>"ESX_HOST"</td><td>The ESX Host managed by one of the Virtual Center Configured.</td></tr><tr><td>"DATASTORE"</td><td>Datastore of the ESX Host.</td></tr><tr><td>"GATEWAY"</td><td>The Gateway configured.</td></tr><tr><td>"FARM"</td><td>The Farm.</td></tr><tr><td>"RDS_SERVER"</td><td>RDS Server.</td></tr><tr><td>"VIEW_COMPOSER"</td><td>View Composer.</td></tr><tr><td>"AD_DOMAIN"</td><td>AD Domain controller.</td></tr><tr><td>"SAML_AUTHENTICATOR"</td><td>SAML 2.0 Authenticator.</td></tr><tr><td>"REMOTE_CONNECTION_SERVER"</td><td>Connection Server from the Remote Pod.</td></tr><tr><td>"LICENSE"</td><td>License added to the connection server.</td></tr><tr><td>"ALL"</td><td>Represents all the categories.</td></tr></table>
**totalCount**|  xsd:int|  Total number of items of the category. [^2]
**healthyCount**|  xsd:int|  Number of healthy items of the category. [^2]
**errorCount**|  xsd:int|  Number of items in the system those are in error state.  **_Since_** Horizon 7.12 [^2]
**warningCount**|  xsd:int|  Number of items in the system those are in warning state.  **_Since_** Horizon 7.12 [^2]
**unknownCount**|  xsd:int|  Number of items in the system those are in unknown state.  **_Since_** Horizon 7.12 [^2]
**details**| [MapEntry[]](vdi.util.MapEntry.md)|  Additional details. [^2]


 


[^2]: This property cannot be updated.