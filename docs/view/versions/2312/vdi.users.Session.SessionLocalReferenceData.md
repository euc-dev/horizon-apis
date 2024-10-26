---
layout: page
title: Data Object - SessionLocalReferenceData
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.users.Session.SessionLocalReferenceData`

Property of
> [SessionGlobalReferenceData](vdi.users.Session.SessionGlobalReferenceData.md#field_detail), [SessionLocalSummaryView](vdi.users.Session.SessionLocalSummaryView.md#field_detail)

See also
> [AccessGroupId](vdi.entity.AccessGroupId.md), [DesktopId](vdi.entity.DesktopId.md), [FarmId](vdi.entity.FarmId.md), [MachineId](vdi.entity.MachineId.md), [RDSServerId](vdi.entity.RDSServerId.md), [UserOrGroupId](vdi.entity.UserOrGroupId.md)

Since
> Horizon View 6.0


## Data Object Description

References to other objects in a local session.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**user**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  User Id for the user logged into this session. May not match the broker user id for non-SSO scenarios.
**brokerUser**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  User Id for the broker user associated with the session. Will be unset for non-broker sessions. [^1]
**groups**| [UserOrGroupId[]](vdi.entity.UserOrGroupId.md)|  All group ids associated with this session's user. [^1] [^14]
**accessGroup**| [AccessGroupId](vdi.entity.AccessGroupId.md)|  Access group associated with this session. For a non-RDS Desktop session, this is the Desktop's access group. For an RDS Desktop session, this is the RDS Desktop's Farm's access group. For an Application session, this is the Application's Farm's access group.
**desktop**| [DesktopId](vdi.entity.DesktopId.md)|  Desktop Id for this Desktop session. This is unset if the session is not brokered through a Desktop, such as for Application sessions or direct console access. [^1]
**farm**| [FarmId](vdi.entity.FarmId.md)|  Farm Id for this Application or RDS Desktop session. [^1]
**machine**| [MachineId](vdi.entity.MachineId.md)|  Machine Id for this session. This is unset for Application or RDS Desktop sessions. If [desktop](vdi.users.Session.SessionLocalReferenceData.md#desktop) is unset, MachineIds of this type originate from the [RegisteredPhysicalMachine](vdi.resources.RegisteredPhysicalMachine.md) service. Otherwise, MachineIds of this type originate from the [Machine](vdi.resources.Machine.md) service. [^1]
**rdsServer**| [RDSServerId](vdi.entity.RDSServerId.md)|  RDS Server Id for this RDS Desktop or Application session. [^1]


 
