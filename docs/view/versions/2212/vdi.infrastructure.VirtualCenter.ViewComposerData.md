---
layout: page
title: Data Object - VirtualCenterViewComposerData
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.infrastructure.VirtualCenter.ViewComposerData`

Property of  
> [VirtualCenterInfo](vdi.infrastructure.VirtualCenter.VirtualCenterInfo.md#field_detail), [VirtualCenterSpec](vdi.infrastructure.VirtualCenter.VirtualCenterSpec.md#field_detail)

See also  
> [CertificateThumbprint](vdi.utils.Certificate.CertificateThumbprint.md), [ServerSpec](vdi.utils.Certificate.ServerSpec.md)

Since  
> Horizon View 6.0


## Data Object Description 

**Deprecated.**_This is being deprecated since View Composer will no longer be supported from Horizon version 2012 onwards._

View composer related attributes 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**viewComposerType**|  xsd:string|  Denotes the View Composer type to use.   


  * This property has a default value of "DISABLED".
  * This property will be one of:  
|  Value |  Description   
---|---  
"DISABLED"| Denotes when View Composer is disabled for this VC.  
"LOCAL_TO_VC"| Denotes the Virtual Center is using a View Composer server which is co-installed.  
"STANDALONE"| Denotes when Virtual Center is paired with a standalone View Composer server.  

  
**serverSpec**| [ServerSpec](vdi.utils.Certificate.ServerSpec.md)|  Details needed to connect to the view composer server.   


* This property need not be set.
  * This property is required if viewComposerType is set to "LOCAL_TO_VC"or "STANDALONE".

  
**certificateOverride**| [CertificateThumbprint](vdi.utils.Certificate.CertificateThumbprint.md)|  View composer certificate thumbprint. This is specified if an invalid certificate is overridden by the client.   


* This property need not be set.

  
  
  
  
  
  
