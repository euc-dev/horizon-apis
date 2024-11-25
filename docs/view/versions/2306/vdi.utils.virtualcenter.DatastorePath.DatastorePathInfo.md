---
layout: page
title: Data Object - DatastorePathInfo
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.utils.virtualcenter.DatastorePath.DatastorePathInfo`

Returned by
> [DatastorePath_List](vdi.utils.virtualcenter.DatastorePath.md#list)

See also
> [DatastorePathId](vdi.entity.DatastorePathId.md)

Since
> Horizon View 6.0


## Data Object Description

DatastorePath info
 [^167]



## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**id**| [DatastorePathId](vdi.entity.DatastorePathId.md)|  DatastorePath entityId [^2]
**path**|  xsd:string|  Full path of Datastore [^2]
**refId**|  xsd:string|  Reference ID used for this datastore path.  **_Since_** Horizon 8.1 [^1] [^2]
 


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^167]: This data object must be updated as a whole.