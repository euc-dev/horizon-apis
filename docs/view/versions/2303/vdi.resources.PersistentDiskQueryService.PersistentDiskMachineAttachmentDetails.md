---
layout: page
title: Data Object - PersistentDiskMachineAttachmentDetails
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.resources.PersistentDiskQueryService.PersistentDiskMachineAttachmentDetails`

See also
> [MachineId](vdi.entity.MachineId.md)

Since
> Horizon 7.8


## Data Object Description

**Deprecated.**_This is being deprecated since View Composer will no longer be supported from Horizon version 2012 onwards._

deprecated This is being deprecated since View Composer will no longer be supported from Horizon version 2012 onwards.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**machineId**| [MachineId](vdi.entity.MachineId.md)|  The id of the Machine. [^2]
**machineName**|  xsd:string|  The name of the machine [^2]
**desktopName**|  xsd:string|  The name of the desktop that the machine belongs to. [^2]
**userName**|  xsd:string|  Name of the user assigned to the machine [^2]
**machineBasicState**|  xsd:string|  The basic state of the Machine. For a Virtual Machine based Machine, the complete state is determined by basicState, isMissingInVCenter, operationState and isInHoldCustomization. In the Admin UI, the last three states are shown in brackets in the Machine State. [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"PROVISIONING"</td><td>The virtual machine is being provisioned</td></tr><tr><td>"PROVISIONING_ERROR"</td><td>An error occurred during provisioning.</td></tr><tr><td>"WAIT_FOR_AGENT"</td><td>View Connection Server is waiting to establish communication with View Agent for one of these cases - a virtual machine in a manual desktop, unmanaged machine or terminal server.</td></tr><tr><td>"CUSTOMIZING"</td><td>The virtual machine in automated/provisioned desktop is being customized</td></tr><tr><td>"DELETING"</td><td>The virtual machine is marked for deletion. View Manager will delete the virtual machine soon.</td></tr><tr><td>"MAINTENANCE"</td><td>The virtual machine is in maintenance mode. Users cannot log in or use the virtual machine</td></tr><tr><td>"ERROR"</td><td>An unknown error occurred in the virtual machine.</td></tr><tr><td>"PROVISIONED"</td><td>The virtual machine is powered off or suspended.</td></tr><tr><td>"AGENT_UNREACHABLE"</td><td>View Connection Server cannot establish communication with View Agent on a virtual machine</td></tr><tr><td>"UNASSIGNED_USER_CONNECTED"</td><td>A user other than the assigned user is logged in to a virtual machine in a dedicated desktop</td></tr><tr><td>"CONNECTED"</td><td>The virtual machine is in an active session and has an active remote connection to a View client</td></tr><tr><td>"UNASSIGNED_USER_DISCONNECTED"</td><td>A user other than the assigned user is logged in and disconnected from a virtual machine in a dedicated desktop.</td></tr><tr><td>"DISCONNECTED"</td><td>The virtual machine is in an active session, but it is disconnected from the View client</td></tr><tr><td>"AGENT_ERR_STARTUP_IN_PROGRESS"</td><td>View Agent has started on the virtual machine, but other required services such as the display protocol are still starting</td></tr><tr><td>"AGENT_ERR_DISABLED"</td><td>View Agent is disabled</td></tr><tr><td>"AGENT_ERR_INVALID_IP"</td><td>View Agent has invalid IP</td></tr><tr><td>"AGENT_ERR_NEED_REBOOT"</td><td>View Agent needs reboot.</td></tr><tr><td>"AGENT_ERR_PROTOCOL_FAILURE"</td><td>Protocol such as RDP or PCoIP is not enabled.</td></tr><tr><td>"AGENT_ERR_DOMAIN_FAILURE"</td><td>View Agent has invalid domain.</td></tr><tr><td>"AGENT_CONFIG_ERROR"</td><td>The Remote Desktop Services role is not enabled.</td></tr><tr><td>"AGENT_DRAIN_MODE"</td><td>RDS host is configured for drain mode</td></tr><tr><td>"AGENT_DRAIN_UNTIL_RESTART"</td><td>RDS host is configured for drain until restart mode</td></tr><tr><td>"ALREADY_USED"</td><td>The virtual machine is configured to have only one session which is currently in progress and cannot accept new sessions</td></tr><tr><td>"AVAILABLE"</td><td>The virtual machine is powered on and ready for an active connection.</td></tr><tr><td>"IN_PROGRESS"</td><td>There is a virtual machine operation in-progress.</td></tr><tr><td>"DISABLED"</td><td>The machine is disabled</td></tr><tr><td>"DISABLE_IN_PROGRESS"</td><td>Disabled server still has some view brokered sessions. It can still accept re-connections</td></tr><tr><td>"VALIDATING"</td><td>The connection server is synchronizing state information with the agent.</td></tr><tr><td>"UNKNOWN"</td><td>Could not determine the state of the virtual machine.</td></tr></table>
**compatible**|  xsd:boolean|  True if the machine can be attached to PersistentDisk. If the value is false, incompatible reasons are available at [incompatibleReasons](vdi.resources.PersistentDiskQueryService.PersistentDiskMachineAttachmentDetails.md#incompatibleReasons) [^2]
**incompatibleReasons**|  xsd:string[]|  Incompatible reasons for attach machine to the persistent disk. [^1] [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>NON_VSPHERE_DESKTOP</td><td>vSphere mode of Disk is not compatible with Desktop.</td></tr><tr><td>MACHINE_WITH_VSAN_ENABLED</td><td>Machine with vSAN enabled can not be attached to disk without vSAN enabled.</td></tr><tr><td>MACHINE_WITH_VSAN_DISABLED</td><td>Machine without vSAN enabled can not be attached to disk with vSAN enabled.</td></tr><tr><td>MACHINE_NOT_MANAGED_BY_DISK_VC</td><td>Machine and disk are not in same vCenter.</td></tr><tr><td>DISK_DATASTORE_NOT_ACCESSIBLE_TO_THE_MACHINE</td><td>Datastore of the disk should be accessible by machine.</td></tr><tr><td>INSUFFICIENT_PERMISSION_TO_MANAGE_DESKTOP</td><td>Insufficient permission to manage the desktop.</td></tr></table>
 


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.