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


[^1]

  
**snapshotPath**|  xsd:string|  Base image snapshot path for View Composer RDS Servers. The name is the last element of the path.   


[^1]

  
**imageManagementStreamName**|  xsd:string|  Name of image management stream used in instant clone farm when created from image catalog.  **_Since_** Horizon 7.10  


[^1]
[^2]

  
**imageManagementTagName**|  xsd:string|  Name of image management tag used in instant clone farm when created from image catalog.  **_Since_** Horizon 7.10  


[^1]
[^2]

  
**datacenterPath**|  xsd:string|  Datacenter path within which this Automated Farm is configured. The name is the last element of the path.   


[^1]

  
**vmFolderPath**|  xsd:string|  VM folder path to deploy the RDS Servers to. The name is the last element of the path.   


[^1]

  
**hostOrClusterPath**|  xsd:string|  Host or cluster path to deploy the RDS Servers in. The name is the last element of the path.   


[^1]

  
**resourcePoolPath**|  xsd:string|  Resource pool path to deploy the RDS Servers. The name is the last element of the path.   


[^1]

  
**datastorePaths**|  xsd:string[]|  Paths of the datastores. The names are the last element of the paths.   


[^1]

  
**replicaDiskDatastorePath**|  xsd:string|  Path of the replica disk datastore. The name is the last element of the path.   


[^1]

  
**nicNames**|  xsd:string[]|  Names of the network interface cards.   


[^1]

  
**networkLabelNames**|  xsd:string[]|  Names of the network labels.   


[^1]

  
**customizationSpecName**|  xsd:string|  The customization spec name.   


[^1]

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

