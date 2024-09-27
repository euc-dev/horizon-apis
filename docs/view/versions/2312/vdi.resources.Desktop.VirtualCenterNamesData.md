---
layout: page
title: Data Object - DesktopVirtualCenterNamesData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.Desktop.VirtualCenterNamesData  
Property of
     [DesktopAutomatedDesktopData](vdi.resources.Desktop.AutomatedDesktopData.md#field_detail)  
Since 
    Horizon View 6.0

## Data Object Description 

Naming data for Virtual Center entities associated with this Desktop. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**templatePath**|  xsd:string|  Template path to deploy full clone VMs. The name is the last element of the path.   


 * This property need not be set.

  
**parentVmPath**|  xsd:string|  Base image path for View Composer VMs and current image parent VM path for instant clone desktops. The name is the last element of the path.   


 * This property need not be set.

  
**snapshotPath**|  xsd:string|  Base image snapshot path for View Composer desktops and current image snapshot path for instant clone desktops. The name is the last element of the path.   


 * This property need not be set.

  
**imageManagementStreamName**|  xsd:string|  Name of image management stream used in full clone and instant clone desktop when created from image catalog.  **_Since_** Horizon 7.10  


 * This property need not be set.
 * This property cannot be updated.

  
**imageManagementTagName**|  xsd:string|  Name of image management tag used in full clone and instant clone desktop when created from image catalog.  **_Since_** Horizon 7.10  


 * This property need not be set.
 * This property cannot be updated.

  
**datacenterPath**|  xsd:string|  Datacenter path within which this desktop is configured. The name is the last element of the path.   


 * This property need not be set.

  
**vmFolderPath**|  xsd:string|  VM folder path to deploy the VMs to. The name is the last element of the path.   


 * This property need not be set.

  
**hostOrClusterPath**|  xsd:string|  Host or cluster path to deploy the VMs in. The name is the last element of the path.   


 * This property need not be set.

  
**resourcePoolPath**|  xsd:string|  Resource pool path to deploy the VMs. The name is the last element of the path.   


 * This property need not be set.

  
**datastorePaths**|  xsd:string[]|  Paths of the datastores. The names are the last element of the paths.   


 * This property need not be set.

  
**sdrsClusterPath**|  xsd:string|  Path of the Storage DRS cluster. The name is the last element of the path. Only applicable for full clone desktops.  **_Since_** Horizon 7.2  


 * This property need not be set.

  
**persistentDiskDatastorePaths**|  xsd:string[]|  Paths of the persistent disk datastores. The names are the last element of the paths.   


 * This property need not be set.

  
**replicaDiskDatastorePath**|  xsd:string|  Path of the replica disk datastore. The name is the last element of the path.   


 * This property need not be set.

  
**nicNames**|  xsd:string[]|  Names of the network interface cards.   


 * This property need not be set.

  
**networkLabelNames**|  xsd:string[]|  Names of the network labels.   


 * This property need not be set.

  
**customizationSpecName**|  xsd:string|  The customization spec name.   


 * This property need not be set.

  
  
  
   
  
  

