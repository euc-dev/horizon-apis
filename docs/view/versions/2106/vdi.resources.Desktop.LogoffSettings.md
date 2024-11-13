---
layout: page
title: Data Object - DesktopLogoffSettings
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.resources.Desktop.LogoffSettings`

Property of
> [DesktopSettings](vdi.resources.Desktop.DesktopSettings.md#field_detail)

Since
> Horizon View 6.0


## Data Object Description

Settings determine how a virtual machine behaves when the user logs off of the associated machine or when a desktop is no longer keeping a machine as a spare.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**powerPolicy**|  xsd:string|  Power policy for the machines in the desktop after logoff. This setting is only relevant for managed machines. Note(s) :- [^33] [^34] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>TAKE_NO_POWER_ACTION</td><td>Take no power action. The power state will not be changed when a user logs off or when a desktop is no longer keeping a machine as a spare.</td></tr><tr><td>ALWAYS_POWERED_ON</td><td>Ensure machines are always powered on. The connection server will monitor and power on machines as necessary.</td></tr><tr><td>SUSPEND</td><td>Suspend when a user logs off or when a desktop is no longer keeping a machine as a spare. This does not affect spare and newly provisioned machines.</td></tr><tr><td>POWER_OFF</td><td>Power off when a user logs off or when a desktop is no longer keeping a machine as a spare. This does not affect spare and newly provisioned machines.</td></tr></table>
**automaticLogoffPolicy**|  xsd:string|  Automatically log-off policy after disconnect. [^121] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>IMMEDIATELY</td><td>Logoff immediately after disconnect.</td></tr><tr><td>NEVER</td><td>Do not logoff after disconnect.</td></tr><tr><td>AFTER</td><td>Logoff 'x' minutes after disconnect.</td></tr></table>
**automaticLogoffMinutes**|  xsd:int|  The timeout in minutes for automatic log-off after disconnect. [^36] [^1] [^8] [^37]
**allowUsersToResetMachines**|  xsd:boolean|  Whether users are allowed to reset/restart their machines. [^5]
**allowMultipleSessionsPerUser**|  xsd:boolean|  Whether multiple sessions are allowed per user in case of Floating User Assignment. [^5]
**deleteOrRefreshMachineAfterLogoff**|  xsd:string|  Whether machines are to be deleted or refreshed after logoff in case of Floating User Assignment. Note(s) :- [^38] [^39] [^121] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>NEVER</td><td>Never delete or refresh the machine.</td></tr><tr><td>DELETE</td><td>Delete the machine.</td></tr><tr><td>REFRESH</td><td>Refresh the machine. Only applicable when the machine source for the automated desktop is VIEW_COMPOSER or when it is an instant clone pool.</td></tr></table>
**refreshOsDiskAfterLogoff**|  xsd:string|  Whether and when to refresh the OS disks for dedicated-assignment, linked-clone and instant-clone machines. [^121] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>NEVER</td><td>The OS disk is never refreshed.</td></tr><tr><td>ALWAYS</td><td>The OS disk is refreshed every time the user logs off.</td></tr><tr><td>EVERY</td><td>THE OS disk is refreshed at regular intervals of a specified number of days. The number of days is counted from the last refresh, or from the initial provisioning if no refresh has occurred yet. For example, if the specified value is 3 days, and three days have passed since the last refresh, the machine is refreshed after the user logs off.</td></tr><tr><td>AT_SIZE</td><td>The OS disk is refreshed when its current size reaches a specified percentage of its maximum allowable size. The maximum size of a linked clone's OS disk is the size of the replica's OS disk. With this option, the size of the linked clone's OS disk in the datastore is compared to maximum allowable size. This disk-utilization percentage does not reflect disk usage that you might see inside the machine's guest operating system.</td></tr></table>
**refreshPeriodDaysForReplicaOsDisk**|  xsd:int|  Regular interval at which to refresh the OS disk. [^1] [^8] [^40]
**refreshThresholdPercentageForReplicaOsDisk**|  xsd:int|  With the 'AT_SIZE' option for refreshOsDiskAfterLogoff, the size of the linked clone's OS disk in the datastore is compared to its maximum allowable size. This disk-utilization percentage does not reflect disk usage that you might see inside the machine's guest operating system. [^1] [^8] [^115] [^42]
**emptySessionTimeoutPolicy**|  xsd:string|  Application empty session timeout policy.  **_Since_** Horizon 7.9 [^184] [^1] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>IMMEDIATE</td><td>Empty session is disconnected immediately.</td></tr><tr><td>NEVER</td><td>Empty session is never disconnected.</td></tr><tr><td>AFTER</td><td>Empty session is disconnected after specified number of minutes.</td></tr></table>
**emptySessionTimeoutMinutes**|  xsd:int|  Application empty session timeout (in minutes). An empty session (that has no remote-able window) is disconnected after the timeout.  **_Since_** Horizon 7.9 [^10] [^1] [^8] [^44]
**logoffAfterTimeout**|  xsd:boolean|  Indicates whether the empty application sessions are logged off (true) or disconnected (false) after timeout.  **_Since_** Horizon 7.9 [^5] [^1]
**preLaunchSessionTimeoutPolicy**|  xsd:string|  Application pre-launch session timeout policy.  **_Since_** Horizon 7.12 [^184] [^1] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>NEVER</td><td>Pre-launched session is never disconnected.</td></tr><tr><td>AFTER</td><td>Pre-launched session is disconnected after specified number of minutes.</td></tr></table>
**preLaunchSessionTimeoutMinutes**|  xsd:int|  Application pre-launch session timeout (in minutes). A pre-launch session is disconnected after the timeout.  **_Since_** Horizon 7.12 [^45] [^1] [^123] [^47]
**sessionTimeoutPolicy**|  xsd:string|  Specifies the session timeout policy for the applications published from the Desktop. This policy indicates whether the launched application session is a forever application session or not.  **_Since_** Horizon 8.3 [^48] [^1] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>DEFAULT</td><td>Indicates application sessions will be disconnected either on reaching the global idle timeout or on reaching the max session timeout.</td></tr><tr><td>NEVER</td><td>Indicates application sessions will not be disconnected either on reaching the global idle timeout or on reaching the max session timeout.</td></tr></table>


 


[^1]: This property need not be set.
[^5]: This property has a default value of false.
[^8]: This property has a minimum value of 1.
[^10]: This property has a default value of 1.
[^33]: For Instant clone desktops this setting can only be set to ALWAYS_POWERED_ON.
[^34]: This property has a default value of 'TAKE_NO_POWER_ACTION'.
[^36]: This property has a default value of 120.
[^37]: This property is required if automaticLogoffPolicy is set to 'AFTER'.
[^38]: This is applicable for automated desktops with virtual machines names based on pattern naming. This is not applicable for desktops that are using specified naming since dynamic creation and deletion of VMs is not supported.
[^39]: For Instant clone desktops this setting can only be set to DELETE.
[^40]: This property is required if refreshOsDiskAfterLogoff is set to 'EVERY'.
[^42]: This property is required if refreshOsDiskAfterLogoff is set to 'AT_SIZE'.
[^44]: This property is required if emptySessionTimeoutPolicy is set to 'AFTER'.
[^45]: This property has a default value of 10.
[^47]: This property is required if preLaunchSessionTimeoutPolicy is set to 'AFTER'.
[^48]: This property has a default value of 'DEFAULT'.
[^115]: This property has a maximum value of 100.
[^121]: This property has a default value of 'NEVER'.
[^123]: This property has a minimum value of 10.
[^184]: This property has a default value of "AFTER".