---
layout: page
title: Data Object - DesktopDisplayProtocolSettings
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.resources.Desktop.DisplayProtocolSettings`

Property of  
> [DesktopSettings](vdi.resources.Desktop.DesktopSettings.md#field_detail)

See also  
> [DesktopPCoIPDisplaySettings](vdi.resources.Desktop.PCoIPDisplaySettings.md)

Since  
> Horizon View 6.0


## Data Object Description 

Settings for the networking protocol to display the remote machine. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**supportedDisplayProtocols**|  xsd:string[]|  The list of supported display protocols for the desktop.   


  * This property has a default value of ["PCOIP", "RDP", "BLAST"].
* This property cannot be updated.
  * This property will be one of:  
|  Value |  Description   
---|---  
"RDP"| Microsoft Remote Desktop Protocol.  
"PCOIP"| PC over IP.  
"BLAST"| BLAST.  

  
**defaultDisplayProtocol**|  xsd:string|  The default display protocol for the desktop. For a managed desktop, this will default to "PCOIP". For an unmanaged desktop, this will default to "RDP".   


  * This property will be one of:  
|  Value |  Description   
---|---  
"RDP"| Microsoft Remote Desktop Protocol.  
"PCOIP"| PC over IP.  
"BLAST"| BLAST.  

  
**allowUsersToChooseProtocol**|  xsd:boolean|  Whether the users can choose the protocol.   


  * This property has a default value of true.

  
**pcoipDisplaySettings**| [DesktopPCoIPDisplaySettings](vdi.resources.Desktop.PCoIPDisplaySettings.md)|  Settings specific to 3D rendering when allowed protocol is PCOIP or BLAST.   
  
**enableHTMLAccess**|  xsd:boolean| **Deprecated.**_This property is no longer in use for Horizon Components. It is always set to true._ HTML Access, enabled by VMware Blast technology, allows users to connect to View machines from Web browsers. View Client software does not have to be installed on the client devices. To enable HTML Access, you must install the HTML Machine Access feature pack. Also, Blast must be configured as a supported protocol in [supportedDisplayProtocols](vdi.resources.Desktop.DisplayProtocolSettings.md#supportedDisplayProtocols).  
  


  * This property has a default value of true.
* This property need not be set.

  
**enableCollaboration**|  xsd:boolean|  Enable session collaboration feature. Session collaboration allows a user to share their remote session with other users. Blast must be configured as a supported protocol in [supportedDisplayProtocols](vdi.resources.Desktop.DisplayProtocolSettings.md#supportedDisplayProtocols).  **_Since_** Horizon 7.4  


  * This property has a default value of false.
* This property need not be set.

  
  
  

  
  
