---
layout: page
title: Data Object - AWSCoreWorkspacePowerPolicySettings
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.resources.Desktop.AWSCoreWorkspacePowerPolicySettings`

Property of
> [AWSCoreDesktopSettings](vdi.resources.Desktop.AWSCoreDesktopSettings.md#field_detail)

See also
> [AWSCoreWorkspaceSchedule](vdi.resources.Desktop.AWSCoreWorkspaceSchedule.md)

Since
> Horizon 8.13


## Data Object Description

Specification for an AWS Core power management settings.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**runningMode**|  xsd:string|  Running mode for the AWS core workspaces in the desktop pool.<br>* This property has a default value of "ALWAYS_ON".<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>ALWAYS_ON</td><td>Billed monthly. Instant access to an always running WorkSpace.</td></tr><tr><td>MANUAL</td><td>Billed by the hour. WorkSpace starts and stops automatically at scheduled duration.</td></tr></table>
**workspaceSchedules**| [AWSCoreWorkspaceSchedule[]](vdi.resources.Desktop.AWSCoreWorkspaceSchedule.md)|  The Schedules for workspace power policy can only be set for workspaces where the running mode is set to MANUAL. [^1]


 


[^1]: This property need not be set.