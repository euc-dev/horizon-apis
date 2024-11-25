---
layout: page
title: Data Object - FarmVirtualCenterDatastoreSettings
hide:
#  - navigation
  - toc
---





Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.resources.Farm.VirtualCenterDatastoreSettings`

Property of
> [FarmVirtualCenterStorageSettings](vdi.resources.Farm.VirtualCenterStorageSettings.md#field_detail)

See also
> [DatastoreId](vdi.entity.DatastoreId.md)

Since
> Horizon View 6.2


## Data Object Description

Settings for a Virtual Center datastore.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**datastore**| [DatastoreId](vdi.entity.DatastoreId.md)|  Id of the datastore.
**storageOvercommit**|  xsd:string|  Storage overcommit determines how view places new RDS Servers on the selected datastores. With an aggressive overcommit level, view reserves less space for sparse disk growth, but fits more RDS Servers on the datastore. [^96] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"NONE"</td><td>No overcommit.</td></tr><tr><td>"CONSERVATIVE"</td><td>Conservative.</td></tr><tr><td>"MODERATE"</td><td>Moderate.</td></tr><tr><td>"AGGRESSIVE"</td><td>Aggressive.</td></tr><tr><td>"UNBOUNDED"</td><td>Unbounded.</td></tr></table>


 


[^96]: This property has a default value of 'CONSERVATIVE'.