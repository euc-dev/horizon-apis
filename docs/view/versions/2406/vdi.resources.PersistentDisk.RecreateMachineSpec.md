---
layout: page
title: Data Object - PersistentDiskRecreateMachineSpec
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.resources.PersistentDisk.RecreateMachineSpec`

Parameter to
> [PersistentDisk_PreviewRecreateMachines](vdi.resources.PersistentDisk.md#previewRecreateMachines), [PersistentDisk_RecreateMachine](vdi.resources.PersistentDisk.md#recreateMachine), [PersistentDisk_RecreateMachines](vdi.resources.PersistentDisk.md#recreateMachines)

See also
> [PersistentDiskId](vdi.entity.PersistentDiskId.md)

Since
> Horizon View 6.0


## Data Object Description

**Deprecated.**_This is being deprecated since View Composer will no longer be supported from Horizon version 2012 onwards._

The specification for recreating a machine from a persistent disk.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**id**| [PersistentDiskId](vdi.entity.PersistentDiskId.md)|  The ID of the persistent disk. This is required when the spec is used in bulk operation apis like recreateMachines etc.  **_Since_** Horizon 7.8 [^1]
**machineName**|  xsd:string|  This is only valid if the desktop uses specified naming. [^1] [^196]


 


[^1]: This property need not be set.
[^196]: This property must contain only alphanumerics, underscores, and dashes. It must contain at least one alpha character. The maximum length is 15 characters.