---
layout: page
title: Data Object - DesktopAdobeFlashSettings
hide:
#- navigation
- toc
---





Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.resources.Desktop.AdobeFlashSettings`

Property of
> [DesktopSettings](vdi.resources.Desktop.DesktopSettings.md#field_detail)

Since
> Horizon View 6.0


## Data Object Description

**Deprecated.**_This property is no longer in use for Horizon Components._

Settings for Adobe Flash.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**quality**|  xsd:string|  This setting determines the image quality that the flash movie will render. Lower quality results in less bandwidth usage. [^183] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"NO_CONTROL"</td><td>Do not control.</td></tr><tr><td>"LOW"</td><td>Low.</td></tr><tr><td>"MEDIUM"</td><td>Medium.</td></tr><tr><td>"HIGH"</td><td>High.</td></tr></table>
**throttling**|  xsd:string|  This setting affects the frame rate of the flash movie. If enabled, the frames per second will be reduced based on the aggressiveness level. More aggressive throttling results in less bandwidth usage. [^17] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"DISABLED"</td><td>Disabled.</td></tr><tr><td>"CONSERVATIVE"</td><td>Conservative.</td></tr><tr><td>"MODERATE"</td><td>Moderate.</td></tr><tr><td>"AGGRESSIVE"</td><td>Aggressive.</td></tr></table>


 


[^17]: This property has a default value of 'DISABLED'.
[^183]: This property has a default value of "NO_CONTROL".