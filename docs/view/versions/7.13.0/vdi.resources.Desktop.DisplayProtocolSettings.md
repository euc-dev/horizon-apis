---
layout: page
title: Data Object - DesktopDisplayProtocolSettings
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.resources.Desktop.DisplayProtocolSettings`

Property of
> [DesktopSettings](vdi.resources.Desktop.DesktopSettings.md#field_detail)

See also
> [DesktopPCoIPDisplaySettings](vdi.resources.Desktop.PCoIPDisplaySettings.md)

Since
> Horizon View 6.0


## Data Object Description

Settings for the networking protocol to display the remote machine.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**supportedDisplayProtocols**|  xsd:string[]|  The list of supported display protocols for the desktop. [^30] [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>RDP</td><td>Microsoft Remote Desktop Protocol.</td></tr><tr><td>PCOIP</td><td>PC over IP.</td></tr><tr><td>BLAST</td><td>BLAST.</td></tr></table>
**defaultDisplayProtocol**|  xsd:string|  The default display protocol for the desktop. For a managed desktop, this will default to "PCOIP". For an unmanaged desktop, this will default to "RDP".<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>RDP</td><td>Microsoft Remote Desktop Protocol.</td></tr><tr><td>PCOIP</td><td>PC over IP.</td></tr><tr><td>BLAST</td><td>BLAST.</td></tr></table>
**allowUsersToChooseProtocol**|  xsd:boolean|  Whether the users can choose the protocol. [^6]
**pcoipDisplaySettings**| [DesktopPCoIPDisplaySettings](vdi.resources.Desktop.PCoIPDisplaySettings.md)|  Settings specific to 3D rendering when allowed protocol is PCOIP or BLAST.
**enableHTMLAccess**|  xsd:boolean| **Deprecated.**_This property is no longer in use for Horizon Components. It is always set to true._ HTML Access, enabled by VMware Blast technology, allows users to connect to View machines from Web browsers. View Client software does not have to be installed on the client devices. To enable HTML Access, you must install the HTML Machine Access feature pack. Also, Blast must be configured as a supported protocol in [supportedDisplayProtocols](vdi.resources.Desktop.DisplayProtocolSettings.md#supportedDisplayProtocols). [^6] [^1]
**enableCollaboration**|  xsd:boolean|  Enable session collaboration feature. Session collaboration allows a user to share their remote session with other users. Blast must be configured as a supported protocol in [supportedDisplayProtocols](vdi.resources.Desktop.DisplayProtocolSettings.md#supportedDisplayProtocols).  **_Since_** Horizon 7.4 [^5] [^1]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^5]: This property has a default value of false.
[^6]: This property has a default value of true.
[^30]: This property has a default value of ['PCOIP', 'RDP', 'BLAST'].