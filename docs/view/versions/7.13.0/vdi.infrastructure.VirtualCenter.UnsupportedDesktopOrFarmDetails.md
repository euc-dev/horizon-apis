---
layout: page
title: Data Object - UnsupportedDesktopOrFarmDetails
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.infrastructure.VirtualCenter.UnsupportedDesktopOrFarmDetails`

Returned by
> [VirtualCenter_ListUnsupportedDesktopsAndFarmsForVMC](vdi.infrastructure.VirtualCenter.md#listUnsupportedDesktopsAndFarmsForVMC)

Since
> Horizon 7.8


## Data Object Description

The details of the desktops and farms which are unsupported.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**name**|  xsd:string|  The desktop name is the unique name used to identify this desktop or farm. [^2]
**displayName**|  xsd:string|  The display name is the name that users will see when they connect to view client. If the display name is left blank, the identifier will be used. [^1] [^2]
**description**|  xsd:string|  The description is a set of notes about the desktop. [^1] [^2]
**isFarm**|  xsd:boolean|  If true, it indicates a farm else it is a desktop [^5] [^2]
**numMachines**|  xsd:int|  Number of machines attached to a desktop pool or farm. [^2]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^5]: This property has a default value of false.