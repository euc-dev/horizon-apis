---
layout: page
title: Data Object - ViewComposerHealthData
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.health.ViewComposerHealth.ViewComposerHealthData`

Property of
> [ViewComposerHealthInfo](vdi.health.ViewComposerHealth.ViewComposerHealthInfo.md#field_detail)

See also
> [VirtualCenterId](vdi.entity.VirtualCenterId.md)

Since
> Horizon View 6.0


## Data Object Description

Basic data about the View Composer server.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**virtualCenters**| [VirtualCenterId[]](vdi.entity.VirtualCenterId.md)|  The VirtualCenter Ids this View Composer server is pointing to. [^14]
**version**|  xsd:string|  The version of the View Composer server. [^1]
**build**|  xsd:string|  The build of the View Composer server. [^1]
**apiVersion**|  xsd:string|  The version of the View Composer API used to communicate with the View Composer server. [^1]
**minVCVersion**|  xsd:string|  The minimum Virtual Center version required for compatibility with this View Composer server. [^1]
**minESXVersion**|  xsd:string|  The minimum ESX version required for compatibility with this View Composer server. [^1]
 


 
