---
layout: page
title: Data Object - FarmHealthInfo
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.health.FarmHealth.FarmHealthInfo`

Returned by
> [FarmHealth_Get](vdi.health.FarmHealth.md#get)

See also
> [AccessGroupId](vdi.entity.AccessGroupId.md), [FarmHealthRDSServerHealthInfo](vdi.health.FarmHealth.RDSServerHealthInfo.md), [FarmId](vdi.entity.FarmId.md)

Since
> Horizon View 6.0


## Data Object Description

Farm health data

##  Queryable Data Object

This data object is queryable using [QueryService](vdi.query.QueryService.md "QueryService").

Cannot filter on any of FarmHealthInfo attributes.

Query **Privileges**

Privilege | Description
:---|:---
POOL_VIEW|  privilege is required to query information



## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**id**| [FarmId](vdi.entity.FarmId.md)|  Farm entity ID [^2]
**name**|  xsd:string|  Farm name [^2]
**type**|  xsd:string|  Farm type  **_Since_** Horizon View 6.2 [^2]<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"AUTOMATED"</td><td>An automated farm creates RDS Servers cloned from a snapshot.</td></tr><tr><td>"MANUAL"</td><td>A manual farm allows selection and addition of existing RDS Servers to the farm.</td></tr></table>
**health**|  xsd:string|  Farm health [^2]<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"OK"</td><td>Farm is enabled and no servers are in WARNING or ERROR state. One or more server(s) may be DISABLED (including the case where all of them are DISABLED).</td></tr><tr><td>"WARNING"</td><td>Farm is enabled. One or more of the following is true: [^237] [^238]</td></tr><tr><td>"ERROR"</td><td>Farm is enabled. One or more server(s) (exceeding the predefined threshold) is in ERROR state, or, for Automated Farms, there could be a provisioning error.</td></tr><tr><td>"DISABLED"</td><td>Farm is disabled.</td></tr></table>
**source**|  xsd:string|  Source of farm machines.  **_Since_** Horizon 7.6 [^1] [^2] [^29]<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"VIEW_COMPOSER"</td><td>View composer linked clones managed as view RDS Servers. They share the same base image and use less storage space than full RDS Servers.</td></tr><tr><td>"INSTANT_CLONE_ENGINE"</td><td>Instant clone engine created 'instant clones' managed as view RDS Servers. Instant clone engine uses vmfork technology to create the instant clones, these clones take much less time for provisioning. Instant clones have many similarities to linked clones like :- [^109] [^110] This option is only valid for Automated Farm.</td></tr></table>
**accessGroup**| [AccessGroupId](vdi.entity.AccessGroupId.md)|  Access group associated with this Farm.  **_Since_** Horizon 7.6 [^2]
**rdsServerHealth**| [FarmHealthRDSServerHealthInfo[]](vdi.health.FarmHealth.RDSServerHealthInfo.md)|  RDS server health information of the servers that belong to the Farm [^1] [^2]
**numApplications**|  xsd:int|  Number of applications published from this Farm.  **_Since_** Horizon 7.9 [^1] [^2]
**refId**|  xsd:string|  Reference ID of the Farm.  **_Since_** Horizon 7.10 [^1]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^29]: This property is required if type is set to 'AUTOMATED'.
[^109]: Both instant and linked clones share the same base image and use less storage space than full virtual machines.
[^110]: The user profile for both types clones can be redirected to persistent disks that will be unaffected by OS updates and refreshes.
[^237]: One or more server(s) is either in WARNING or ERROR (not exceeding the predefined threshold) state.
[^238]: The RDSServers in this Farm present a mix of both known and unknown load preferences.