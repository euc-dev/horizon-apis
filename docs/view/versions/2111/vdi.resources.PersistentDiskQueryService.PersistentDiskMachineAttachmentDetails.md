---
layout: page
title: Data Object - PersistentDiskMachineAttachmentDetails
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.resources.PersistentDiskQueryService.PersistentDiskMachineAttachmentDetails`

See also  
> [MachineId](vdi.entity.MachineId.md)

Since  
> Horizon 7.8


## Data Object Description 

**Deprecated.**_This is being deprecated since View Composer will no longer be supported from Horizon version 2012 onwards._

deprecated This is being deprecated since View Composer will no longer be supported from Horizon version 2012 onwards. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**machineId**| [MachineId](vdi.entity.MachineId.md)|  The id of the Machine.   


* This property cannot be updated.

  
**machineName**|  xsd:string|  The name of the machine   


* This property cannot be updated.

  
**desktopName**|  xsd:string|  The name of the desktop that the machine belongs to.   


* This property cannot be updated.

  
**userName**|  xsd:string|  Name of the user assigned to the machine   


* This property cannot be updated.

  
**machineBasicState**|  xsd:string|  The basic state of the Machine. For a Virtual Machine based Machine, the complete state is determined by basicState, isMissingInVCenter, operationState and isInHoldCustomization. In the Admin UI, the last three states are shown in brackets in the Machine State.   


* This property cannot be updated.
  * This property will be one of:  
|  Value |  Description   
---|---  
"PROVISIONING"| The virtual machine is being provisioned  
"PROVISIONING_ERROR"| An error occurred during provisioning.  
"WAIT_FOR_AGENT"| View Connection Server is waiting to establish communication with View Agent for one of these cases - a virtual machine in a manual desktop, unmanaged machine or terminal server.  
"CUSTOMIZING"| The virtual machine in automated/provisioned desktop is being customized  
"DELETING"| The virtual machine is marked for deletion. View Manager will delete the virtual machine soon.  
"MAINTENANCE"| The virtual machine is in maintenance mode. Users cannot log in or use the virtual machine  
"ERROR"| An unknown error occurred in the virtual machine.  
"PROVISIONED"| The virtual machine is powered off or suspended.  
"AGENT_UNREACHABLE"| View Connection Server cannot establish communication with View Agent on a virtual machine  
"UNASSIGNED_USER_CONNECTED"| A user other than the assigned user is logged in to a virtual machine in a dedicated desktop  
"CONNECTED"| The virtual machine is in an active session and has an active remote connection to a View client  
"UNASSIGNED_USER_DISCONNECTED"| A user other than the assigned user is logged in and disconnected from a virtual machine in a dedicated desktop.  
"DISCONNECTED"| The virtual machine is in an active session, but it is disconnected from the View client  
"AGENT_ERR_STARTUP_IN_PROGRESS"| View Agent has started on the virtual machine, but other required services such as the display protocol are still starting  
"AGENT_ERR_DISABLED"| View Agent is disabled  
"AGENT_ERR_INVALID_IP"| View Agent has invalid IP  
"AGENT_ERR_NEED_REBOOT"| View Agent needs reboot.  
"AGENT_ERR_PROTOCOL_FAILURE"| Protocol such as RDP or PCoIP is not enabled.  
"AGENT_ERR_DOMAIN_FAILURE"| View Agent has invalid domain.  
"AGENT_CONFIG_ERROR"| The Remote Desktop Services role is not enabled.  
"AGENT_DRAIN_MODE"| RDS host is configured for drain mode  
"AGENT_DRAIN_UNTIL_RESTART"| RDS host is configured for drain until restart mode  
"ALREADY_USED"| The virtual machine is configured to have only one session which is currently in progress and cannot accept new sessions  
"AVAILABLE"| The virtual machine is powered on and ready for an active connection.  
"IN_PROGRESS"| There is a virtual machine operation in-progress.  
"DISABLED"| The machine is disabled  
"DISABLE_IN_PROGRESS"| Disabled server still has some view brokered sessions. It can still accept re-connections  
"VALIDATING"| The connection server is synchronizing state information with the agent.  
"UNKNOWN"| Could not determine the state of the virtual machine.  

  
**compatible**|  xsd:boolean|  True if the machine can be attached to PersistentDisk. If the value is false, incompatible reasons are available at [incompatibleReasons](vdi.resources.PersistentDiskQueryService.PersistentDiskMachineAttachmentDetails.md#incompatibleReasons)   


* This property cannot be updated.

  
**incompatibleReasons**|  xsd:string[]|  Incompatible reasons for attach machine to the persistent disk.   


* This property need not be set.
* This property cannot be updated.
  * This property will be one of:  
|  Value |  Description   
---|---  
"NON_VSPHERE_DESKTOP"| vSphere mode of Disk is not compatible with Desktop.  
"MACHINE_WITH_VSAN_ENABLED"| Machine with vSAN enabled can not be attached to disk without vSAN enabled.  
"MACHINE_WITH_VSAN_DISABLED"| Machine without vSAN enabled can not be attached to disk with vSAN enabled.  
"MACHINE_NOT_MANAGED_BY_DISK_VC"| Machine and disk are not in same vCenter.  
"DISK_DATASTORE_NOT_ACCESSIBLE_TO_THE_MACHINE"| Datastore of the disk should be accessible by machine.  
"INSUFFICIENT_PERMISSION_TO_MANAGE_DESKTOP"| Insufficient permission to manage the desktop.  

  
  
  
   
  
  
