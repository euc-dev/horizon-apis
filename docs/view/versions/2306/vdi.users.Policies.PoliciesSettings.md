---
layout: page
title: Data Object - PoliciesSettings
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.users.Policies.PoliciesSettings`

Property of
> [PoliciesInfo](vdi.users.Policies.PoliciesInfo.md#field_detail)

Parameter to
> [Policies_Set](vdi.users.Policies.md#set)

Since
> Horizon View 6.0


## Data Object Description

Object for specifying a single set of policy overrides. Policies settings objects by themselves may not have meaning outside of the context provided by the complete info objects, as the INHERIT value implies that the actual setting comes from a different settings object. If allowPCoIPHardware acceleration is set to ALLOW, the pcoipHardwareAccelerationPriority must be set.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**allowMultimediaRedirection**|  xsd:string|  Determines whether MMR (Multimedia Redirection, a Microsoft DirectShow filter) is enabled for client systems. MMR is allowed by default. <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>Allow</td><td>This policy option is set to allow.</td></tr><tr><td>Deny</td><td>This policy option is set to deny.</td></tr><tr><td>Inherit</td><td>This policy option will be inherited from the parent.</td></tr></table>
**allowUSBAccess**|  xsd:string|  Determines whether machines can use USB devices connected to the client system. USB access is allowed by default. <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>Allow</td><td>This policy option is set to allow.</td></tr><tr><td>Deny</td><td>This policy option is set to deny.</td></tr><tr><td>Inherit</td><td>This policy option will be inherited from the parent.</td></tr></table>
**allowRemoteMode**|  xsd:string|  Determines whether users can connect to and use machines running on vCenter Server instances. If set to deny, machines must be used in local mode. <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>Allow</td><td>This policy option is set to allow.</td></tr><tr><td>Deny</td><td>This policy option is set to deny.</td></tr><tr><td>Inherit</td><td>This policy option will be inherited from the parent.</td></tr></table>
**allowPCoIPHardwareAcceleration**|  xsd:string|  Determines whether to enable hardware acceleration of the PCoIP display protocol. Default is to allow acceleration. If this is set, hardware acceleration priority must be set, as well. This setting has an effect only if a PCoIP hardware acceleration device is present on the physical computer that hosts the machine. <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>Allow</td><td>This policy option is set to allow.</td></tr><tr><td>Deny</td><td>This policy option is set to deny.</td></tr><tr><td>Inherit</td><td>This policy option will be inherited from the parent.</td></tr></table>
**pcoipHardwareAccelerationPriority**|  xsd:string|  Determines priority for hardware acceleration. Ignored if PCoIP hardware acceleration is not allowed. The default value is medium priority. [^1] [^201] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>Lowest</td><td>PCOIP Hardware acceleration priority is lowest possible.</td></tr><tr><td>Lower</td><td>PCOIP Hardware acceleration priority is lower.</td></tr><tr><td>Medium</td><td>PCOIP Hardware acceleration priority is medium. Default.</td></tr><tr><td>Higher</td><td>PCOIP Hardware acceleration priority is higher.</td></tr><tr><td>Highest</td><td>PCOIP Hardware acceleration priority is highest.</td></tr></table>
 


 
