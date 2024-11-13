---
layout: page
title: Data Object - ViewComposerWithVCSpec
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.utils.Certificate.ViewComposerWithVCSpec`

Parameter to
> [Certificate_ValidateViewComposerLocalToVC](vdi.utils.Certificate.md#validateViewComposerLocalToVC)

See also
> [VirtualCenterId](vdi.entity.VirtualCenterId.md)

Since
> Horizon 7.8


## Data Object Description

Specification of View Composer co-installed with Virtual Center.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**vcId**| [VirtualCenterId](vdi.entity.VirtualCenterId.md)|  The Virtual Center using a View Composer server which is co-installed.
**port**|  xsd:int|  Port of the View Composer server instance to connect to. [^8] [^189]


 


[^8]: This property has a minimum value of 1.
[^189]: This property has a maximum value of 65535.