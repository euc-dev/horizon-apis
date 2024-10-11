---
layout: page
title: Data Object - DesktopLogoffSettings
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.resources.Desktop.LogoffSettings`

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
**powerPolicy**|  xsd:string|  Power policy for the machines in the desktop after logoff. This setting is only relevant for managed machines. Note(s) :-  


  * For Instant clone desktops this setting can only be set to ALWAYS_POWERED_ON.

  


  * This property has a default value of "TAKE_NO_POWER_ACTION".
  * This property will be one of:  
|  Value |  Description   
---|---  
"TAKE_NO_POWER_ACTION"| Take no power action. The power state will not be changed when a user logs off or when a desktop is no longer keeping a machine as a spare.  
"ALWAYS_POWERED_ON"| Ensure machines are always powered on. The connection server will monitor and power on machines as necessary.  
"SUSPEND"| Suspend when a user logs off or when a desktop is no longer keeping a machine as a spare. This does not affect spare and newly provisioned machines.  
"POWER_OFF"| Power off when a user logs off or when a desktop is no longer keeping a machine as a spare. This does not affect spare and newly provisioned machines.  

  
**automaticLogoffPolicy**|  xsd:string|  Automatically log-off policy after disconnect.   


  * This property has a default value of "NEVER".
  * This property will be one of:  
|  Value |  Description   
---|---  
"IMMEDIATELY"| Logoff immediately after disconnect.  
"NEVER"| Do not logoff after disconnect.  
"AFTER"| Logoff 'x' minutes after disconnect.  

  
**automaticLogoffMinutes**|  xsd:int|  The timeout in minutes for automatic log-off after disconnect.   


  * This property has a default value of 120.
* This property need not be set.
  * This property has a minimum value of 1. 
  * This property is required if automaticLogoffPolicy is set to "AFTER".

  
**allowUsersToResetMachines**|  xsd:boolean|  Whether users are allowed to reset/restart their machines.   


  * This property has a default value of false.

  
**allowMultipleSessionsPerUser**|  xsd:boolean|  Whether multiple sessions are allowed per user in case of Floating User Assignment.   


  * This property has a default value of false.

  
**deleteOrRefreshMachineAfterLogoff**|  xsd:string|  Whether machines are to be deleted or refreshed after logoff in case of Floating User Assignment. Note(s) :-  


  * This is applicable for automated desktops with virtual machines names based on pattern naming. This is not applicable for desktops that are using specified naming since dynamic creation and deletion of VMs is not supported.
  * For Instant clone desktops this setting can only be set to DELETE.

  


  * This property has a default value of "NEVER".
  * This property will be one of:  
|  Value |  Description   
---|---  
"NEVER"| Never delete or refresh the machine.  
"DELETE"| Delete the machine.  
"REFRESH"| Refresh the machine. Only applicable when the machine source for the automated desktop is VIEW_COMPOSER or when it is an instant clone pool.  

  
**refreshOsDiskAfterLogoff**|  xsd:string|  Whether and when to refresh the OS disks for dedicated-assignment, linked-clone and instant-clone machines.   


  * This property has a default value of "NEVER".
  * This property will be one of:  
|  Value |  Description   
---|---  
"NEVER"| The OS disk is never refreshed.  
"ALWAYS"| The OS disk is refreshed every time the user logs off.  
"EVERY"| THE OS disk is refreshed at regular intervals of a specified number of days. The number of days is counted from the last refresh, or from the initial provisioning if no refresh has occurred yet. For example, if the specified value is 3 days, and three days have passed since the last refresh, the machine is refreshed after the user logs off.  
"AT_SIZE"| The OS disk is refreshed when its current size reaches a specified percentage of its maximum allowable size. The maximum size of a linked clone's OS disk is the size of the replica's OS disk. With this option, the size of the linked clone's OS disk in the datastore is compared to maximum allowable size. This disk-utilization percentage does not reflect disk usage that you might see inside the machine's guest operating system.  

  
**refreshPeriodDaysForReplicaOsDisk**|  xsd:int|  Regular interval at which to refresh the OS disk.   


* This property need not be set.
  * This property has a minimum value of 1. 
  * This property is required if refreshOsDiskAfterLogoff is set to "EVERY".

  
**refreshThresholdPercentageForReplicaOsDisk**|  xsd:int|  With the 'AT_SIZE' option for refreshOsDiskAfterLogoff, the size of the linked clone's OS disk in the datastore is compared to its maximum allowable size. This disk-utilization percentage does not reflect disk usage that you might see inside the machine's guest operating system.   


* This property need not be set.
  * This property has a minimum value of 1. 
  * This property has a maximum value of 100. 
  * This property is required if refreshOsDiskAfterLogoff is set to "AT_SIZE".

  
**emptySessionTimeoutPolicy**|  xsd:string|  Application empty session timeout policy.  **_Since_** Horizon 7.9  


  * This property has a default value of "AFTER".
* This property need not be set.
  * This property will be one of:  
|  Value |  Description   
---|---  
"IMMEDIATE"| Empty session is disconnected immediately.  
"NEVER"| Empty session is never disconnected.  
"AFTER"| Empty session is disconnected after specified number of minutes.  

  
**emptySessionTimeoutMinutes**|  xsd:int|  Application empty session timeout (in minutes). An empty session (that has no remote-able window) is disconnected after the timeout.  **_Since_** Horizon 7.9  


  * This property has a default value of 1.
* This property need not be set.
  * This property has a minimum value of 1. 
  * This property is required if emptySessionTimeoutPolicy is set to "AFTER".

  
**logoffAfterTimeout**|  xsd:boolean|  Indicates whether the empty application sessions are logged off (true) or disconnected (false) after timeout.  **_Since_** Horizon 7.9  


  * This property has a default value of false.
* This property need not be set.

  
**preLaunchSessionTimeoutPolicy**|  xsd:string|  Application pre-launch session timeout policy.  **_Since_** Horizon 7.12  


  * This property has a default value of "AFTER".
* This property need not be set.
  * This property will be one of:  
|  Value |  Description   
---|---  
"NEVER"| Pre-launched session is never disconnected.  
"AFTER"| Pre-launched session is disconnected after specified number of minutes.  

  
**preLaunchSessionTimeoutMinutes**|  xsd:int|  Application pre-launch session timeout (in minutes). A pre-launch session is disconnected after the timeout.  **_Since_** Horizon 7.12  


  * This property has a default value of 10.
* This property need not be set.
  * This property has a minimum value of 10. 
  * This property is required if preLaunchSessionTimeoutPolicy is set to "AFTER".

  
**sessionTimeoutPolicy**|  xsd:string|  Specifies the session timeout policy for the applications published from the Desktop. This policy indicates whether the launched application session is a forever application session or not.  **_Since_** Horizon 8.3  


  * This property has a default value of "DEFAULT".
* This property need not be set.
  * This property will be one of:  
|  Value |  Description   
---|---  
"DEFAULT"| Indicates application sessions will be disconnected either on reaching the global idle timeout or on reaching the max session timeout.  
"NEVER"| Indicates application sessions will not be disconnected either on reaching the global idle timeout or on reaching the max session timeout.  

  
  
  

  
  
