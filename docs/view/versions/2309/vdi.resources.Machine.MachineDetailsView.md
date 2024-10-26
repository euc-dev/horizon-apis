---
layout: page
title: Data Object - MachineDetailsView
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.resources.Machine.MachineDetailsView`

See also
> [MachineAgentPairingData](vdi.resources.Machine.MachineAgentPairingData.md), [MachineData](vdi.resources.Machine.MachineData.md), [MachineDesktopData](vdi.resources.Machine.MachineDesktopData.md), [MachineId](vdi.entity.MachineId.md), [MachineSessionData](vdi.resources.Machine.MachineSessionData.md), [ManagedMachineDetailsData](vdi.resources.Machine.ManagedMachineDetailsData.md), [UserOrGroupId](vdi.entity.UserOrGroupId.md)

Since
> Horizon 7.7


## Data Object Description

Details View of Machine.

##  Queryable Data Object

This data object is queryable using [QueryService](vdi.query.QueryService.md "QueryService").

Cannot filter on the following MachineDetailsView attributes:

* [sessionData](vdi.resources.Machine.MachineDetailsView.md#sessionData).[user](vdi.resources.Machine.MachineSessionData.md#user)
* [desktopData](vdi.resources.Machine.MachineDetailsView.md#desktopData).[name](vdi.resources.Machine.MachineDesktopData.md#name)
* [managedMachineDetailsData](vdi.resources.Machine.MachineDetailsView.md#managedMachineDetailsData).[hostName](vdi.resources.Machine.ManagedMachineDetailsData.md#hostName)
* [managedMachineDetailsData](vdi.resources.Machine.MachineDetailsView.md#managedMachineDetailsData).[datastorePaths](vdi.resources.Machine.ManagedMachineDetailsData.md#datastorePaths)

The following caveats apply:
* You can only apply [QueryFilterEquals](vdi.query.QueryFilter.Equals.md) filter on [groupId](vdi.resources.Machine.MachineDetailsView.md#groupId)



Query Privileges

Privilege |  Description
---|---
MACHINE_VIEW|  is required to query MachineDetailsView.



## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**id**| [MachineId](vdi.entity.MachineId.md)|  The id of the Machine. [^2]
**groupId**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  The id of the group. Required for querying the machines assigned to the users of this group. [^1]
**data**| [MachineData](vdi.resources.Machine.MachineData.md)|  Information about the Machine.
**desktopData**| [MachineDesktopData](vdi.resources.Machine.MachineDesktopData.md)|  Information about the desktop pool of the Machine.
**sessionData**| [MachineSessionData](vdi.resources.Machine.MachineSessionData.md)|  Information about the active session on the Machine. This will be unset when there is no active session on this Machine. [^1]
**managedMachineDetailsData**| [ManagedMachineDetailsData](vdi.resources.Machine.ManagedMachineDetailsData.md)|  Information applicable only to Managed Machines. [^1]
**machineAgentPairingData**| [MachineAgentPairingData](vdi.resources.Machine.MachineAgentPairingData.md)|  Agent pairing data for this Machine. [^1]
**refId**|  xsd:string|  Reference ID used for this Machine.  **_Since_** Horizon 8.8 [^1] [^2]
 


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.