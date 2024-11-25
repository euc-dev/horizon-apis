---
layout: page
title: Data Object - DesktopOrFarmDatastoreUsageInfo
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.utils.virtualcenter.Datastore.DesktopOrFarmDatastoreUsageInfo`

Returned by
> [Datastore_GetUsage](vdi.utils.virtualcenter.Datastore.md#getUsage)

Since
> Horizon 7.9


## Data Object Description

Desktop or Farm datastore usage information.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**name**|  xsd:string|  Name of the Desktop or Farm. [^2]
**isFarm**|  xsd:boolean|  Represents if this is a Farm. [^5] [^2]
**source**|  xsd:string|  The Source or the Provisioning Type of machines in this Desktop or Farm.<br>**Note:** The value FULL_CLONE is not applicable in case of farms. [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"VIEW_COMPOSER"</td><td>View composer linked clones managed as view machines.</td></tr><tr><td>"INSTANT_CLONE_ENGINE"</td><td>Instant clone engine created 'instant clones' managed as view machines.</td></tr><tr><td>"FULL_CLONE"</td><td>Full Virtual Machines that are created from a vCenter Server template.</td></tr></table>
**isPersistent**|  xsd:boolean|  User assignment of the Destop: Dedicated (Persistent) / Floating.<br>Can be ignored in case of Farm. [^1] [^2]
**usedSpaceMB**|  xsd:long|  Used capacity of the datastore (in MB) for this Desktop or Farm. [^2]
**otherDatastoreNames**|  xsd:string[]|  Other datastore(s) in-use for this Desktop or Farm. [^1] [^2]
 


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^5]: This property has a default value of false.