---
layout: page
title: Data Object - DesktopVirtualCenterDatastoreSettings
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.resources.Desktop.VirtualCenterDatastoreSettings`

Property of
> [DesktopPersistentDiskSettings](vdi.resources.Desktop.PersistentDiskSettings.md#field_detail), [DesktopVirtualCenterStorageSettings](vdi.resources.Desktop.VirtualCenterStorageSettings.md#field_detail)

See also
> [DatastoreId](vdi.entity.DatastoreId.md)

Since
> Horizon View 6.0


## Data Object Description

Settings for a Virtual Center datastore.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**datastore**| [DatastoreId](vdi.entity.DatastoreId.md)|  Id of the datastore.
**sdrsCluster**|  xsd:boolean|  Set to true if [datastore](vdi.resources.Desktop.VirtualCenterDatastoreSettings.md#datastore) represents a Storage DRS clsuter. Only applicable for full clone desktops.  **_Since_** Horizon 7.2 [^5] [^1]
**storageOvercommit**|  xsd:string|  Storage overcommit determines how view places new VMs on the selected datastores. With an aggressive overcommit level, view reserves less space for sparse disk growth, but fits more VMs on the datastore. Note(s) :- [^95] [^96] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>NONE</td><td>No overcommit.</td></tr><tr><td>CONSERVATIVE</td><td>Conservative.</td></tr><tr><td>MODERATE</td><td>Moderate.</td></tr><tr><td>AGGRESSIVE</td><td>Aggressive.</td></tr><tr><td>UNBOUNDED</td><td>Unbounded.</td></tr></table>




 


[^1]: This property need not be set.
[^5]: This property has a default value of false.
[^95]: For Instant clone desktops, this setting can only be set to UNBOUNDED.
[^96]: This property has a default value of 'CONSERVATIVE'.