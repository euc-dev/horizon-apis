---
layout: page
title: Data Object - FarmDisplayProtocolSettings
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.Farm.DisplayProtocolSettings  
Property of
     [FarmData](vdi.resources.Farm.FarmData.md#field_detail)  
Since 
    Horizon View 6.0

## Data Object Description 

Farm Display Protocol settings 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**defaultDisplayProtocol**|  xsd:string|  Default Server Display Protocol, when override display protocol is disallowed. Farms support PCOIP, RDP and BLAST.   


  * This property has a default value of "PCOIP".
* This property need not be set.
  * This property will be one of:  
|  Value |  Description   
---|---  
"RDP"| Microsoft Remote Desktop Protocol.  
"PCOIP"| PC over IP.  
"BLAST"| BLAST.  

  
**allowDisplayProtocolOverride**|  xsd:boolean|  Indicates whether the Display Protocol settings could be overridden. If set to false, then defaultDisplayProtocol is used.   


  * This property has a default value of true.
* This property need not be set.

  
**enableHTMLAccess**|  xsd:boolean| **Deprecated.**_This property is no longer in use for Horizon Components. It is always set to true._ HTML Access, enabled by VMware Blast technology, allows users to connect to View machines from Web browsers. View Client software does not have to be installed on the client devices. To enable HTML Access, you must install the HTML Machine Access feature pack.  
**_Since_** Horizon View 6.1  


  * This property has a default value of true.
* This property need not be set.

  
**enableCollaboration**|  xsd:boolean|  Enable session collaboration feature. Session collaboration allows a user to share their remote session with other users. Blast must be configured as a supported protocol in #supportedDisplayProtocols.  **_Since_** Horizon 7.4  


  * This property has a default value of false.
* This property need not be set.

  
**enableGRIDvGPUs**|  xsd:boolean|  If this is true, the host or cluster associated with the farm must support NVIDIA GRID and vGPU types required by the RDSH desktop virtualMachines, VmTemplate, or BaseImageSnapshot. If this is false, RDSH instant clone farm must not support NVIDIA GRID vGPUs.  **_Since_** Horizon 7.4  


  * This property has a default value of false.
* This property need not be set.
* This property cannot be updated.

  
**vGPUGridProfile**|  xsd:string|  NVIDIA GRID vGPUs have multiple profiles and any one of the available profiles can be applied to newly created instant clone RDSH desktop. The profile specified in this field will be used in the newly created instant clone RDSH server.  **_Since_** Horizon 7.4  


* This property need not be set.
* This property cannot be updated.
  * This property is required if enableGRIDvGPUs is set to true.

  
  
  
  
  
  

