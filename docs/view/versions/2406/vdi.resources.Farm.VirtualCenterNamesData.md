---
layout: page
title: Data Object - FarmVirtualCenterNamesData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.Farm.VirtualCenterNamesData  
Property of
     [FarmAutomatedFarmData](vdi.resources.Farm.AutomatedFarmData.md#field_detail)  
Since 
    Horizon View 6.2

## Data Object Description 

Naming data for Virtual Center entities associated with this RDS Server clone. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**parentVmPath**|  xsd:string|  Base image path for View Composer RDS Servers. The name is the last element of the path.   


 * This property need not be set.

  
**snapshotPath**|  xsd:string|  Base image snapshot path for View Composer RDS Servers. The name is the last element of the path.   


 * This property need not be set.

  
**imageManagementStreamName**|  xsd:string|  Name of image management stream used in instant clone farm when created from image catalog.  **_Since_** Horizon 7.10  


 * This property need not be set.
 * This property cannot be updated.

  
**imageManagementTagName**|  xsd:string|  Name of image management tag used in instant clone farm when created from image catalog.  **_Since_** Horizon 7.10  


 * This property need not be set.
 * This property cannot be updated.

  
**datacenterPath**|  xsd:string|  Datacenter path within which this Automated Farm is configured. The name is the last element of the path.   


 * This property need not be set.

  
**vmFolderPath**|  xsd:string|  VM folder path to deploy the RDS Servers to. The name is the last element of the path.   


 * This property need not be set.

  
**hostOrClusterPath**|  xsd:string|  Host or cluster path to deploy the RDS Servers in. The name is the last element of the path.   


 * This property need not be set.

  
**resourcePoolPath**|  xsd:string|  Resource pool path to deploy the RDS Servers. The name is the last element of the path.   


 * This property need not be set.

  
**datastorePaths**|  xsd:string[]|  Paths of the datastores. The names are the last element of the paths.   


 * This property need not be set.

  
**replicaDiskDatastorePath**|  xsd:string|  Path of the replica disk datastore. The name is the last element of the path.   


 * This property need not be set.

  
**nicNames**|  xsd:string[]|  Names of the network interface cards.   


 * This property need not be set.

  
**networkLabelNames**|  xsd:string[]|  Names of the network labels.   


 * This property need not be set.

  
**customizationSpecName**|  xsd:string|  The customization spec name.   


 * This property need not be set.

  
  

  

