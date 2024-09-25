---
layout: page
title: Data Object - FarmSummaryData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.Farm.FarmSummaryData
Property of
     [FarmSummaryView](vdi.resources.Farm.FarmSummaryView.md#field_detail)
See also
     [AccessGroupId](vdi.entity.AccessGroupId.md), [DesktopId](vdi.entity.DesktopId.md)
Since 
    Horizon View 6.0

## Data Object Description 

Farm summary Data 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**type**|  xsd:string|  Type of Farm.  **_Since_** Horizon View 6.2  


[^2]
  * This property will be one of:  
|  Value |  Description   
---|---  
"AUTOMATED"| An automated farm creates RDS Servers cloned from a snapshot.  
"MANUAL"| A manual farm allows selection and addition of existing RDS Servers to the farm.  

  
**source**|  xsd:string|  Source of farm machines.  **_Since_** Horizon 7.1  


[^1]
[^2]
  * This property is required if type is set to "AUTOMATED".
  * This property will be one of:  
|  Value |  Description   
---|---  
"VIEW_COMPOSER"| View composer linked clones managed as view RDS Servers. They share the same base image and use less storage space than full RDS Servers.  
"INSTANT_CLONE_ENGINE"| Instant clone engine created 'instant clones' managed as view RDS Servers. Instant clone engine uses vmfork technology to create the instant clones, these clones take much less time for provisioning. Instant clones have many similarities to linked clones like :-  

    * Both instant and linked clones share the same base image and use less storage space than full virtual machines.
    * The user profile for both types clones can be redirected to persistent disks that will be unaffected by OS updates and refreshes.
This option is only valid for Automated Farm.  

  
**imageSource**|  xsd:string|  Source of image used in the farm. Applicable for automated farm.  **_Since_** Horizon 7.10  


[^1]
[^2]
  * This property will be one of:  
|  Value |  Description   
---|---  
"VIRTUAL_CENTER"| Image was created in virtual center.  
"IMAGE_CATALOG"| Image was created in image catalog.  

  
**name**|  xsd:string|  Farm name   


[^2]

  
**displayName**|  xsd:string|  Farm display name.   


[^2]

  
**description**|  xsd:string|  Farm description  **_Since_** Horizon View 6.2  


[^1]
[^2]

  
**accessGroup**| [AccessGroupId](vdi.entity.AccessGroupId.md)|  View access groups can organize the farms in your organization. They can also be used for delegated administration.   


[^2]

  
**accessGroupName**|  xsd:string|  View access group name   


[^2]

  
**enabled**|  xsd:boolean|  Indicates if Farm is enabled   


[^2]

  
**provisioningEnabled**|  xsd:boolean|  Indicates if provisioning is enabled for the Farm  **_Since_** Horizon 7.2  


[^2]

  
**deleting**|  xsd:boolean|  Indicates if the farm is in the process of being deleted. Only applicable for automated farms.  **_Since_** Horizon View 6.2  


[^2]

  
**desktop**| [DesktopId](vdi.entity.DesktopId.md)|  RDS Desktop EntityId   


[^1]
[^2]

  
**desktopName**|  xsd:string|  RDS Desktop display name   


[^1]
[^2]

  
**rdsServerCount**|  xsd:int|  Count of RDS servers that belong to the Farm   


[^2]

  
**applicationCount**|  xsd:int|  Count of Applications that belong to the Farm   


[^2]

  
**maxSessionsType**|  xsd:string|  Farm max sessions type   


  * This property has a default value of "LIMITED".
[^2]
  * This property will be one of:  
|  Value |  Description   
---|---  
"UNLIMITED"| Farm has unlimited number of sessions  
"LIMITED"| Farm has a limited number of sessions  

  
**maximumNumberOfSessions**|  xsd:long|  Sum of maximum number of sessions of all RDS servers that belong to the Farm.   


[^1]
[^2]
  * This property has a minimum value of 1. 
  * This property is required if maxSessionsType is set to "LIMITED".

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

