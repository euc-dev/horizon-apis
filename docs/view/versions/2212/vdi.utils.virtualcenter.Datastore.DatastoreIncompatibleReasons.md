---
layout: page
title: Data Object - DatastoreIncompatibleReasons
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.utils.virtualcenter.Datastore.DatastoreIncompatibleReasons`

Property of
> [DatastoreData](vdi.utils.virtualcenter.Datastore.DatastoreData.md#field_detail)

Since
> Horizon View 6.0


## Data Object Description

Reasons that may preclude this Datastore from being used in desktop creation.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**inaccessibleToSomeHosts**|  xsd:boolean|  This Datastore is inaccessible to at least one host if in a cluster. If true, it is not recommended to be used in desktop creation - the vm must be local to this datastore. [^2]
**vmfs5AndMoreThan32Hosts**|  xsd:boolean|  This Datastore is VMFS version 5 or greater, but belongs to a cluster with more than 32 hosts. If true, this cannot be used as a replica disk in linked clone desktop creation. [^2]
**vmfs6AndMoreThan64Hosts**|  xsd:boolean|  This Datastore is VMFS version 6 or greater, but belongs to a cluster with more than 64 hosts. If true, this cannot be used as a replica disk in linked clone desktop creation.  **_Since_** Horizon 8.1 [^2]
**notVmfs5AndMoreThan8Hosts**|  xsd:boolean|  This Datastore is not VMFS version 5 and belongs to a cluster with more than 8 hosts. If true, this cannot be used as a replica disk in linked clone desktop creation. [^2]
**esx51AndMoreThan32Hosts**|  xsd:boolean|  This Datastore is ESX version 5.1 or greater, but belongs to a cluster with more than 32 hosts. If true, this cannot be used as a replica disk in linked clone desktop creation. [^2]
**esx65AndMoreThan64Hosts**|  xsd:boolean|  This Datastore is ESX version 6.5 or greater, but belongs to a cluster with more than 64 hosts. If true, this cannot be used as a replica disk in linked clone desktop creation.  **_Since_** Horizon 8.1 [^2]
**notEsx51AndMoreThan8Hosts**|  xsd:boolean|  This Datastore is not ESX version 5.1 and belongs to a cluster with more than 8 hosts. If true, this cannot be used as a replica disk in linked clone desktop creation. [^2]
**incompatibleNativeSnapshots**|  xsd:boolean|  Whether or not the datastore is incompatible with the native snapshot feature. If true, this datastore cannot be used as a replica or OS disk for linked clone desktop creation with native snapshots enabled. [^2]


 


[^2]: This property cannot be updated.