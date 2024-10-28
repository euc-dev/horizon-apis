---
layout: page
title: Data Object - DatastoreRequirementSpec
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.utils.virtualcenter.Datastore.DatastoreRequirementSpec`

Parameter to
> [Datastore_GetDatastoreRequirements](vdi.utils.virtualcenter.Datastore.md#getDatastoreRequirements)

See also
> [BaseImageSnapshotId](vdi.entity.BaseImageSnapshotId.md), [BaseImageVmId](vdi.entity.BaseImageVmId.md), [DesktopId](vdi.entity.DesktopId.md), [FarmId](vdi.entity.FarmId.md), [VmTemplateId](vdi.entity.VmTemplateId.md)

Since
> Horizon 7.6


## Data Object Description

Datastore requirements specification.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**desktopId**| [DesktopId](vdi.entity.DesktopId.md)|  Desktop Id to be supplied when editing a Desktop Pool. [^1]
**farmId**| [FarmId](vdi.entity.FarmId.md)|  Farm Id to be supplied when editing a Farm. [^1]
**isFarm**|  xsd:boolean|  Set to true when creating/editing a Farm. [^5]
**source**|  xsd:string|  The Source or the Provisioning Type of machines.<br>**Note:** The value FULL_CLONE is not allowed in case of farms. <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"VIEW_COMPOSER"</td><td>View composer linked clones managed as view machines.</td></tr><tr><td>"INSTANT_CLONE_ENGINE"</td><td>Instant clone engine created 'instant clones' managed as view machines.</td></tr><tr><td>"FULL_CLONE"</td><td>Full Virtual Machines that are created from a vCenter Server template.</td></tr></table>
**vmId**| [BaseImageVmId](vdi.entity.BaseImageVmId.md)|  Parent VM Id.<br>Applicable in case of Linked Clones and Instant Clones. [^1] [^168]
**snapshotId**| [BaseImageSnapshotId](vdi.entity.BaseImageSnapshotId.md)|  VM Snapshot Id.<br>Applicable in case of Linked Clones and Instant Clones. [^1] [^168]
**vmTemplateId**| [VmTemplateId](vdi.entity.VmTemplateId.md)|  VM Template Id.<br>Applicable in case of Full Clones. [^1] [^169]
**poolSize**|  xsd:int|  The desired size of the Pool/Farm.
**isPersistent**|  xsd:boolean|  User assignment of the pool: Dedicated (Persistent) / Floating.<br>Ignored in case of Farm. [^5]
**userDiskSize**|  xsd:double|  Size of Persistent Disk (in MB). [^170] [^171] [^1] [^172]
**useVsan**|  xsd:boolean|  When Vmware Virtual SAN is used.<br>Set to true when Virtual SAN is configured and in use for the pool. [^5]
**useSeparateReplicaAndOSDisk**|  xsd:boolean|  Set to true when separate datastores for replica and OS disks are used. [^173] [^5]
**useSeparatePersistentAndOSDisk**|  xsd:boolean|  When the Separate datastores for persistent and OS disks are used. [^174] [^175] [^5]
**useSeparateReplicaAndOSDisk**|  xsd:boolean|  Set to true when separate datastores for replica and OS disks are used. [^173] [^5]
**useSeparatePersistentAndOSDisk**|  xsd:boolean|  When the Separate datastores for persistent and OS disks are used. [^174] [^175] [^5]


 


[^1]: This property need not be set.
[^5]: This property has a default value of false.
[^168]: This property is required if source is set to "VIEW_COMPOSER" or "INSTANT_CLONE_ENGINE".
[^169]: This property is required if source is set to "FULL_CLONE".
[^170]: This value will be considered only in case of Dedicated Linked Pool.
[^171]: It will be ignored for other Pools and Farms.
[^172]: This property is required if isPersistent is set to true.
[^173]: Applicable only in case of Linked Clones and Instant Clones.
[^174]: Set to true only in case of DEDICATED LINKED_CLONE Pool.
[^175]: It will be ignored in case of Farms and other Pools.