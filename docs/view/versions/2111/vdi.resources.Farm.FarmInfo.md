---
layout: page
title: Data Object - FarmInfo
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.Farm.FarmInfo  
Returned by
     [Farm_Get](vdi.resources.Farm.md#get), [Farm_GetByNamingPattern](vdi.resources.Farm.md#getByNamingPattern)  
See also
     [FarmAutomatedFarmData](vdi.resources.Farm.AutomatedFarmData.md), [FarmData](vdi.resources.Farm.FarmData.md), [FarmId](vdi.entity.FarmId.md)  
Since 
    Horizon View 6.0

## Data Object Description 

Farm info 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [FarmId](vdi.entity.FarmId.md)|  Farm entity ID   


* This property cannot be updated.

  
**type**|  xsd:string|  Type of farm.  **_Since_** Horizon View 6.2  


* This property cannot be updated.
  * This property will be one of:  
|  Value |  Description   
---|---  
"AUTOMATED"| An automated farm creates RDS Servers cloned from a snapshot.  
"MANUAL"| A manual farm allows selection and addition of existing RDS Servers to the farm.  

  
**source**|  xsd:string|  Source of farm machines.  **_Since_** Horizon 7.1  


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

  
**imageSource**|  xsd:string|  Source of image used in the farm. Applicable for automated farm.  **_Since_** Horizon 7.10  


* This property need not be set.
* This property cannot be updated.
  * This property will be one of:  
|  Value |  Description   
---|---  
"VIRTUAL_CENTER"| Image was created in virtual center.  
"IMAGE_CATALOG"| Image was created in image catalog.  

  
**data**| [FarmData](vdi.resources.Farm.FarmData.md)|  Farm data   
  
**automatedFarmData**| [FarmAutomatedFarmData](vdi.resources.Farm.AutomatedFarmData.md)|  Automated farm data.  **_Since_** Horizon View 6.2  


* This property need not be set.
  * This property is required if type is set to "AUTOMATED".

  
**refId**|  xsd:string|  Reference ID used for this farm.  **_Since_** Horizon 8.2  


* This property need not be set.
* This property cannot be updated.

  
  
  
   
  
  

