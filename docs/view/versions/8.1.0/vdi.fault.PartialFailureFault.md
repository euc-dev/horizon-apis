---
layout: page
title: Fault - PartialFailureFault
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.fault.PartialFailureFault`

Thrown by
> [Application_DeleteApplications](vdi.resources.Application.md#deleteApplications), [ApplicationIcon_GetByApplications](vdi.resources.ApplicationIcon.md#getByApplications), [ApplicationIcon_GetSummaryViewByApplications](vdi.resources.ApplicationIcon.md#getSummaryViewByApplications), [Desktop_AddMachinesToManualDesktop](vdi.resources.Desktop.md#addMachinesToManualDesktop), [Desktop_AddMachinesToSpecifiedNamingDesktop](vdi.resources.Desktop.md#addMachinesToSpecifiedNamingDesktop), [Desktop_Rebalance](vdi.resources.Desktop.md#rebalance), [Desktop_Recompose](vdi.resources.Desktop.md#recompose), [Desktop_Refresh](vdi.resources.Desktop.md#refresh), [Desktop_RemoveMachinesFromManualDesktop](vdi.resources.Desktop.md#removeMachinesFromManualDesktop), [Farm_Recompose](vdi.resources.Farm.md#recompose), [GlobalApplicationEntitlement_AddApplicationsToGAE](vdi.federation.GlobalApplicationEntitlement.md#addApplicationsToGAE), [GlobalEntitlement_AddDesktopsToGE](vdi.federation.GlobalEntitlement.md#addDesktopsToGE), [ImageManagementAsset_CreateAssets](vdi.utils.imagemanagement.ImageManagementAsset.md#createAssets), [ImageManagementStream_CreateStreams](vdi.utils.imagemanagement.ImageManagementStream.md#createStreams), [ImageManagementTag_CreateTags](vdi.utils.imagemanagement.ImageManagementTag.md#createTags), [ImageManagementVersion_CreateVersions](vdi.utils.imagemanagement.ImageManagementVersion.md#createVersions), [LogCollector_Clean](vdi.utils.logcollector.LogCollector.md#clean), [LogCollector_Collect](vdi.utils.logcollector.LogCollector.md#collect), [LogCollector_GetDownloadURL](vdi.utils.logcollector.LogCollector.md#getDownloadURL), [LogCollector_GetTaskInfo](vdi.utils.logcollector.LogCollector.md#getTaskInfo), [LogCollector_GetTaskInfoById](vdi.utils.logcollector.LogCollector.md#getTaskInfoById), [LogCollector_Purge](vdi.utils.logcollector.LogCollector.md#purge), [Machine_assignUsers](vdi.resources.Machine.md#assignUsers), [Machine_CancelTasks](vdi.resources.Machine.md#cancelTasks), [Machine_DeleteMachines](vdi.resources.Machine.md#deleteMachines), [Machine_EnterMaintenanceModeMachines](vdi.resources.Machine.md#enterMaintenanceModeMachines), [Machine_ExitMaintenanceModeMachines](vdi.resources.Machine.md#exitMaintenanceModeMachines), [Machine_RebuildMachines](vdi.resources.Machine.md#rebuildMachines), [Machine_RecoverMachines](vdi.resources.Machine.md#recoverMachines), [Machine_ResetMachines](vdi.resources.Machine.md#resetMachines), [Machine_RestartMachines](vdi.resources.Machine.md#restartMachines), [Machine_unassignUsers](vdi.resources.Machine.md#unassignUsers), [Machine_UpdateMachineAliases](vdi.resources.Machine.md#updateMachineAliases), [Permission_CreatePermissions](vdi.users.Permission.md#createPermissions), [Permission_DeletePermissions](vdi.users.Permission.md#deletePermissions), [RDSServer_RecoverMachines](vdi.resources.RDSServer.md#recoverMachines), [Session_DisconnectSessions](vdi.users.Session.md#disconnectSessions), [Session_LogoffSessions](vdi.users.Session.md#logoffSessions), [Session_LogoffSessionsForced](vdi.users.Session.md#logoffSessionsForced), [Session_ResetSessions](vdi.users.Session.md#resetSessions), [Session_RestartSessions](vdi.users.Session.md#restartSessions), [Session_SendMessages](vdi.users.Session.md#sendMessages), [UserEntitlement_CreateUserEntitlements](vdi.users.UserEntitlement.md#createUserEntitlements), [UserEntitlement_DeleteUserEntitlements](vdi.users.UserEntitlement.md#deleteUserEntitlements)

Extends
> [ViewServerFault](vdi.fault.ViewServerFault.md)

See also
> [PartialFailureFaultResult](vdi.fault.PartialFailureFault.PartialFailureFaultResult.md)

Since
> Horizon View 6.0


## Fault Description

Indicates a partial failure with some possible successful return values. Normally used in "create multiple" and "delete multiple" methods when transactional behavior is not provided. The results array field will contain either a return value or an exception in original index order.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**resultCount**|  xsd:int|  The number of results, either successful or unsuccessful, returned in this partial failure.
**successCount**|  xsd:int|  The number of successful results returned in this partial failure.
**results**| [PartialFailureFaultResult[]](vdi.fault.PartialFailureFault.PartialFailureFaultResult.md)|  All the successful or unsuccessful results of this partial failure, in their original order. [^1]
Properties inherited from [ViewServerFault](vdi.fault.ViewServerFault.md)
[errorMessage](vdi.fault.ViewServerFault.md#errorMessage)
Properties inherited from [MethodFault](vmodl.MethodFault.md)
None


 


[^1]: This property need not be set.