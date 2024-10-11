---
layout: page
title: Data Object - DesktopAdobeFlashSettings
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.resources.Desktop.AdobeFlashSettings`

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
**quality**|  xsd:string|  This setting determines the image quality that the flash movie will render. Lower quality results in less bandwidth usage.   


  * This property has a default value of "NO_CONTROL".
  * This property will be one of:  
|  Value |  Description   
---|---  
"NO_CONTROL"| Do not control.  
"LOW"| Low.  
"MEDIUM"| Medium.  
"HIGH"| High.  

  
**throttling**|  xsd:string|  This setting affects the frame rate of the flash movie. If enabled, the frames per second will be reduced based on the aggressiveness level. More aggressive throttling results in less bandwidth usage.   


  * This property has a default value of "DISABLED".
  * This property will be one of:  
|  Value |  Description   
---|---  
"DISABLED"| Disabled.  
"CONSERVATIVE"| Conservative.  
"MODERATE"| Moderate.  
"AGGRESSIVE"| Aggressive.  

  
  
  
  
  
  
