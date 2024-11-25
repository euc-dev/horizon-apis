---
layout: page
title: Data Object - FarmDisplayProtocolSettings
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.resources.Farm.DisplayProtocolSettings`

Property of
> [FarmData](vdi.resources.Farm.FarmData.md#field_detail)

Since
> Horizon View 6.0


## Data Object Description

Farm Display Protocol settings

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**defaultDisplayProtocol**|  xsd:string|  Default Server Display Protocol, when override display protocol is disallowed. Farms support PCOIP, RDP and BLAST. [^111] [^1] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>RDP</td><td>Microsoft Remote Desktop Protocol.</td></tr><tr><td>PCOIP</td><td>PC over IP.</td></tr><tr><td>BLAST</td><td>BLAST.</td></tr><tr><td>ULTRA</td><td>Pcoip ULTRA, supported only when it is enabled for the desktop pool/global entitlement.</td></tr></table>
**allowDisplayProtocolOverride**|  xsd:boolean|  Indicates whether the Display Protocol settings could be overridden. If set to false, then defaultDisplayProtocol is used. [^6] [^1]
**enableHTMLAccess**|  xsd:boolean| **Deprecated.**_This property is no longer in use for Horizon Components. It is always set to true._ HTML Access, enabled by VMware Blast technology, allows users to connect to View machines from Web browsers. View Client software does not have to be installed on the client devices. To enable HTML Access, you must install the HTML Machine Access feature pack. <br>**_Since_** Horizon View 6.1 [^6] [^1]
**enableCollaboration**|  xsd:boolean|  Enable session collaboration feature. Session collaboration allows a user to share their remote session with other users. Blast must be configured as a supported protocol in #supportedDisplayProtocols.  **_Since_** Horizon 7.4 [^5] [^1]
**enableGRIDvGPUs**|  xsd:boolean|  If this is true, the host or cluster associated with the farm must support NVIDIA GRID and vGPU types required by the RDSH desktop virtualMachines, VmTemplate, or BaseImageSnapshot. If this is false, RDSH instant clone farm must not support NVIDIA GRID vGPUs.  **_Since_** Horizon 7.4 [^5] [^1] [^2]
**vGPUGridProfile**|  xsd:string|  NVIDIA GRID vGPUs have multiple profiles and any one of the available profiles can be applied to newly created instant clone RDSH desktop. The profile specified in this field will be used in the newly created instant clone RDSH server.  **_Since_** Horizon 7.4 [^1] [^2] [^112]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^5]: This property has a default value of false.
[^6]: This property has a default value of true.
[^111]: This property has a default value of 'PCOIP'.
[^112]: This property is required if enableGRIDvGPUs is set to true.