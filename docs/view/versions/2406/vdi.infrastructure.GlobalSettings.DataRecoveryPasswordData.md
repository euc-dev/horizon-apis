---
layout: page
title: Data Object - GlobalSettingsDataRecoveryPasswordData
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.infrastructure.GlobalSettings.DataRecoveryPasswordData`

Property of
> [GlobalSettingsInfo](vdi.infrastructure.GlobalSettings.GlobalSettingsInfo.md#field_detail)

Since
> Horizon View 6.0


## Data Object Description

The data recovery password protects data backups of your View Connection Server. This password will be required to recover a backup.
 [^167]



## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**recoveryPasswordSHA256**|  xsd:base64Binary|  The SHA-256 hash of the (UTF-8) recovery password.
**recoveryPasswordHint**|  xsd:string|  The recovery password hint. [^1] [^267]


 


[^1]: This property need not be set.
[^167]: This data object must be updated as a whole.
[^267]: This property has a maximum length of 128 characters.