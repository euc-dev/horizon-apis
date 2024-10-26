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
**viewComposerType**|  xsd:string|  Denotes the View Composer type to use. [^17] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"DISABLED"</td><td>Denotes when View Composer is disabled for this VC.</td></tr><tr><td>"LOCAL_TO_VC"</td><td>Denotes the Virtual Center is using a View Composer server which is co-installed.</td></tr><tr><td>"STANDALONE"</td><td>Denotes when Virtual Center is paired with a standalone View Composer server.</td></tr></table>
**serverSpec**| [ServerSpec](vdi.utils.Certificate.ServerSpec.md)|  Details needed to connect to the view composer server. [^1] [^179]
**certificateOverride**| [CertificateThumbprint](vdi.utils.Certificate.CertificateThumbprint.md)|  View composer certificate thumbprint. This is specified if an invalid certificate is overridden by the client. [^1]


 


[^1]: This property need not be set.
[^17]: This property has a default value of 'DISABLED'.
[^179]: This property is required if viewComposerType is set to "LOCAL_TO_VC" or "STANDALONE".