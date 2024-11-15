---
layout: page
title: Data Object - DatastoreSpaceRequirement
hide:
#- navigation
- toc
---





Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.utils.virtualcenter.Datastore.DatastoreSpaceRequirement`

Returned by
> [Datastore_GetDatastoreRequirements](vdi.utils.virtualcenter.Datastore.md#getDatastoreRequirements)

Since
> Horizon 7.6


## Data Object Description

Datastore Requirements specified in GB.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**DiskType**|  xsd:string|  Disk Type used for storage. [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"REPLICA"</td><td>Identifies disk for the placement of the replica that View Composer and Instant clone engine sourced desktops use as their base image.</td></tr><tr><td>"PERSISTENT"</td><td>Identifies disk to preserves the user information when the OS data is updated, refreshed, or rebalanced for View Composer.</td></tr><tr><td>"OS"</td><td>Identifies disk to store the Operating System related data.</td></tr></table>
**minDiskSize**|  xsd:double|  Minimum recommended Disk Space, in GB. [^2]
**midDiskSize**|  xsd:double|  Recommended Disk Space with 50% utilization, in GB. [^1] [^2]
**maxDiskSize**|  xsd:double|  Maximum recommended Disk Space, in GB. [^1] [^2]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.