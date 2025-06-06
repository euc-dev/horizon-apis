---
layout: page
title: Data Object - DatastoreSpec
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.utils.virtualcenter.Datastore.DatastoreSpec`

Parameter to
> [Datastore_ListDatastoresByDesktopOrFarm](vdi.utils.virtualcenter.Datastore.md#listDatastoresByDesktopOrFarm)

See also
> [DesktopId](vdi.entity.DesktopId.md), [FarmId](vdi.entity.FarmId.md), [HostOrClusterId](vdi.entity.HostOrClusterId.md)

Since
> Horizon 7.6


## Data Object Description

Datastore spec to query the datastores for updating or editing the Desktop or Farm

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**hostOrClusterId**| [HostOrClusterId](vdi.entity.HostOrClusterId.md)|  HostOrClusterId to lookup the datastores.<br>This parameter is optional and is taken from [desktopId](vdi.utils.virtualcenter.Datastore.DatastoreSpec.md#desktopId) or [farmId](vdi.utils.virtualcenter.Datastore.DatastoreSpec.md#farmId) if not provided. [^1]
**desktopId**| [DesktopId](vdi.entity.DesktopId.md)|  Desktop ID. Either DesktopId or [farmId](vdi.utils.virtualcenter.Datastore.DatastoreSpec.md#farmId) needs to be provided. [^1]
**farmId**| [FarmId](vdi.entity.FarmId.md)|  Farm ID. Either farmId or [desktopId](vdi.utils.virtualcenter.Datastore.DatastoreSpec.md#desktopId) needs to be provided. [^1]
 


 


[^1]: This property need not be set.