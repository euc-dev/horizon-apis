---
layout: page
title: Data Object - FarmHealthInfo
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.health.FarmHealth.FarmHealthInfo  
Returned by
     [FarmHealth_Get](vdi.health.FarmHealth.md#get)  
See also
     [AccessGroupId](vdi.entity.AccessGroupId.md), [FarmHealthRDSServerHealthInfo](vdi.health.FarmHealth.RDSServerHealthInfo.md), [FarmId](vdi.entity.FarmId.md)  
Since 
    Horizon View 6.0

## Data Object Description 

Farm health data 

##  Queryable Data Object 

This data object is queryable using [QueryService](vdi.query.QueryService.md "QueryService"). 

Cannot filter on any of FarmHealthInfo attributes. 

Query Privileges 

Privilege |  Description   
---|---  
POOL_VIEW|  privilege is required to query information   
  


## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [FarmId](vdi.entity.FarmId.md)|  Farm entity ID   


* This property cannot be updated.

  
**name**|  xsd:string|  Farm name   


* This property cannot be updated.

  
**type**|  xsd:string|  Farm type  **_Since_** Horizon View 6.2  


* This property cannot be updated.
  * This property will be one of:  
|  Value |  Description   
---|---  
"AUTOMATED"| An automated farm creates RDS Servers cloned from a snapshot.  
"MANUAL"| A manual farm allows selection and addition of existing RDS Servers to the farm.  

  
**health**|  xsd:string|  Farm health   


* This property cannot be updated.
  * This property will be one of:  
|  Value |  Description   
---|---  
"OK"| Farm is enabled and no servers are in WARNING or ERROR state. One or more server(s) may be DISABLED (including the case where all of them are DISABLED).  
"WARNING"| Farm is enabled. One or more of the following is true:  

    * One or more server(s) is either in WARNING or ERROR (not exceeding the predefined threshold) state.
    * The RDSServers in this Farm present a mix of both known and unknown load preferences.  
"ERROR"| Farm is enabled. One or more server(s) (exceeding the predefined threshold) is in ERROR state, or, for Automated Farms, there could be a provisioning error.  
"DISABLED"| Farm is disabled.  

  
**source**|  xsd:string|  Source of farm machines.  **_Since_** Horizon 7.6  


* This property need not be set.
* This property cannot be updated.
  * This property is required if type is set to "AUTOMATED".
  * This property will be one of:  
|  Value |  Description   
---|---  
"VIEW_COMPOSER"| View composer linked clones managed as view RDS Servers. They share the same base image and use less storage space than full RDS Servers.  
"INSTANT_CLONE_ENGINE"| Instant clone engine created 'instant clones' managed as view RDS Servers. Instant clone engine uses vmfork technology to create the instant clones, these clones take much less time for provisioning. Instant clones have many similarities to linked clones like :-  

    * Both instant and linked clones share the same base image and use less storage space than full virtual machines.
    * The user profile for both types clones can be redirected to persistent disks that will be unaffected by OS updates and refreshes.
This option is only valid for Automated Farm.  

  
**accessGroup**| [AccessGroupId](vdi.entity.AccessGroupId.md)|  Access group associated with this Farm.  **_Since_** Horizon 7.6  


* This property cannot be updated.

  
**rdsServerHealth**| [FarmHealthRDSServerHealthInfo[]](vdi.health.FarmHealth.RDSServerHealthInfo.md)|  RDS server health information of the servers that belong to the Farm   


* This property need not be set.
* This property cannot be updated.

  
**numApplications**|  xsd:int|  Number of applications published from this Farm.  **_Since_** Horizon 7.9  


* This property need not be set.
* This property cannot be updated.

  
**refId**|  xsd:string|  Reference ID of the Farm.  **_Since_** Horizon 7.10  


* This property need not be set.

  
  
  

  
  

