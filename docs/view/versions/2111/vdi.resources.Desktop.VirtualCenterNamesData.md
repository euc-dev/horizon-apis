---
layout: page
title: Data Object - DesktopVirtualCenterNamesData
hide:
#  - navigation
  - toc
---





Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.resources.Desktop.VirtualCenterNamesData`

Property of
> [DesktopAutomatedDesktopData](vdi.resources.Desktop.AutomatedDesktopData.md#field_detail)

Since
> Horizon View 6.0


## Data Object Description

Naming data for Virtual Center entities associated with this Desktop.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**templatePath**|  xsd:string|  Template path to deploy full clone VMs. The name is the last element of the path. [^1]
**parentVmPath**|  xsd:string|  Base image path for View Composer VMs and current image parent VM path for instant clone desktops. The name is the last element of the path. [^1]
**snapshotPath**|  xsd:string|  Base image snapshot path for View Composer desktops and current image snapshot path for instant clone desktops. The name is the last element of the path. [^1]
**imageManagementStreamName**|  xsd:string|  Name of image management stream used in full clone and instant clone desktop when created from image catalog.  **_Since_** Horizon 7.10 [^1] [^2]
**imageManagementTagName**|  xsd:string|  Name of image management tag used in full clone and instant clone desktop when created from image catalog.  **_Since_** Horizon 7.10 [^1] [^2]
**datacenterPath**|  xsd:string|  Datacenter path within which this desktop is configured. The name is the last element of the path. [^1]
**vmFolderPath**|  xsd:string|  VM folder path to deploy the VMs to. The name is the last element of the path. [^1]
**hostOrClusterPath**|  xsd:string|  Host or cluster path to deploy the VMs in. The name is the last element of the path. [^1]
**resourcePoolPath**|  xsd:string|  Resource pool path to deploy the VMs. The name is the last element of the path. [^1]
**datastorePaths**|  xsd:string[]|  Paths of the datastores. The names are the last element of the paths. [^1]
**sdrsClusterPath**|  xsd:string|  Path of the Storage DRS cluster. The name is the last element of the path. Only applicable for full clone desktops.  **_Since_** Horizon 7.2 [^1]
**persistentDiskDatastorePaths**|  xsd:string[]|  Paths of the persistent disk datastores. The names are the last element of the paths. [^1]
**replicaDiskDatastorePath**|  xsd:string|  Path of the replica disk datastore. The name is the last element of the path. [^1]
**nicNames**|  xsd:string[]|  Names of the network interface cards. [^1]
**networkLabelNames**|  xsd:string[]|  Names of the network labels. [^1]
**customizationSpecName**|  xsd:string|  The customization spec name. [^1]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.