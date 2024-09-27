---
layout: page
title: Data Object - PoliciesSettings
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.users.Policies.PoliciesSettings  
Property of
     [PoliciesInfo](vdi.users.Policies.PoliciesInfo.md#field_detail)  
Parameter to
     [Policies_Set](vdi.users.Policies.md#set)  
Since 
    Horizon View 6.0

## Data Object Description 

Object for specifying a single set of policy overrides. Policies settings objects by themselves may not have meaning outside of the context provided by the complete info objects, as the INHERIT value implies that the actual setting comes from a different settings object. If allowPCoIPHardware acceleration is set to ALLOW, the pcoipHardwareAccelerationPriority must be set. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**allowMultimediaRedirection**|  xsd:string|  Determines whether MMR (Multimedia Redirection, a Microsoft DirectShow filter) is enabled for client systems. MMR is allowed by default.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"Allow"| This policy option is set to allow.  
"Deny"| This policy option is set to deny.  
"Inherit"| This policy option will be inherited from the parent.  

  
**allowUSBAccess**|  xsd:string|  Determines whether machines can use USB devices connected to the client system. USB access is allowed by default.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"Allow"| This policy option is set to allow.  
"Deny"| This policy option is set to deny.  
"Inherit"| This policy option will be inherited from the parent.  

  
**allowRemoteMode**|  xsd:string|  Determines whether users can connect to and use machines running on vCenter Server instances. If set to deny, machines must be used in local mode.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"Allow"| This policy option is set to allow.  
"Deny"| This policy option is set to deny.  
"Inherit"| This policy option will be inherited from the parent.  

  
**allowPCoIPHardwareAcceleration**|  xsd:string|  Determines whether to enable hardware acceleration of the PCoIP display protocol. Default is to allow acceleration. If this is set, hardware acceleration priority must be set, as well. This setting has an effect only if a PCoIP hardware acceleration device is present on the physical computer that hosts the machine.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"Allow"| This policy option is set to allow.  
"Deny"| This policy option is set to deny.  
"Inherit"| This policy option will be inherited from the parent.  

  
**pcoipHardwareAccelerationPriority**|  xsd:string|  Determines priority for hardware acceleration. Ignored if PCoIP hardware acceleration is not allowed. The default value is medium priority.   


 * This property need not be set.
  * This property is required if allowPCoIPHardwareAcceleration is set to "Allow".
  * This property will be one of:  
|  Value |  Description   
---|---  
"Lowest"| PCOIP Hardware acceleration priority is lowest possible.  
"Lower"| PCOIP Hardware acceleration priority is lower.  
"Medium"| PCOIP Hardware acceleration priority is medium. Default.  
"Higher"| PCOIP Hardware acceleration priority is higher.  
"Highest"| PCOIP Hardware acceleration priority is highest.  

  
  
  
   
  
  

