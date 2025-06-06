---
layout: page
title: Data Object - DesktopSpaceReclamationSettings
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.resources.Desktop.SpaceReclamationSettings`

Property of
> [DesktopViewComposerStorageSettings](vdi.resources.Desktop.ViewComposerStorageSettings.md#field_detail)

Since
> Horizon View 6.0


## Data Object Description

Settings related to the Space Reclamation feature.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**reclaimVmDiskSpace**|  xsd:boolean|  With vSphere 5.x, virtual machines can be configured to use a space efficient disk format that supports reclamation of unused disk space (such as deleted files). This option reclaims unused disk space on each virtual machine. The operation is initiated when an estimate of used disk space exceeds the specified threshold. vSphere 5.1 Patch1 or later is required for this option. Note(s) :- [^5]
**reclamationThresholdGB**|  xsd:long|  Initiate reclamation when unused space on VM exceeds the threshold. [^10] [^1] [^72] [^79]


 


[^1]: This property need not be set.
[^5]: This property has a default value of false.
[^10]: This property has a default value of 1.
[^72]: This property has a minimum value of 0.
[^79]: This property is required if reclaimVmDiskSpace is set to true.