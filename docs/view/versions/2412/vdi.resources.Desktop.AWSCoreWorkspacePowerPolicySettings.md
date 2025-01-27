---
layout: page
title: Data Object - AWSCoreWorkspacePowerPolicySettings
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.resources.Desktop.AWSCoreWorkspacePowerPolicySettings`

Property of
> [AWSCoreDesktopSettings](vdi.resources.Desktop.AWSCoreDesktopSettings.md#field_detail)

See also
> [AWSCoreWorkspaceSchedule](vdi.resources.Desktop.AWSCoreWorkspaceSchedule.md)

Since
> Horizon 8.13


## Data Object Description

Specification for an AWS Core power management settings.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**runningMode**|  xsd:string|  Running mode for the AWS core workspaces in the desktop pool.<br>* This property has a default value of "ALWAYS_ON".<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>ALWAYS_ON</td><td>Billed monthly. Instant access to an always running WorkSpace.</td></tr><tr><td>MANUAL</td><td>Billed by the hour. WorkSpace starts and stops automatically at scheduled duration.</td></tr></table>
**workspaceSchedules**| [AWSCoreWorkspaceSchedule[]](../2406/vdi.resources.Desktop.AWSCoreWorkspaceSchedule.md)|  The Schedules for workspace power policy can only be set for workspaces where the running mode is set to MANUAL. [^1]
**idleTimeoutPolicy**|  xsd:string|  Shutdown policy after idle timeout can only be set for workspaces where the running mode is set to MANUAL..<br>* This property has a default value of "NEVER".<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>NEVER</td><td>Do not shutdown after idle timeout</td></tr><tr><td>AFTER</td><td>Shutdown 'x' minutes after idle timeout.</td></tr></table>
**idleTimeoutMinutes**| xsd:int|  The timeout in minutes for automatic shutdown after idle timeout.<br>* This property is required if idleTimeoutPolicy is set to "AFTER". <br>* This property has a default value of 60. <br>* This property has a minimum value of 1.


 


[^1]: This property need not be set.