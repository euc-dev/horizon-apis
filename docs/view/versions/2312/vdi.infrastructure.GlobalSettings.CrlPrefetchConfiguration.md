---
layout: page
title: Data Object - GlobalSettingsCrlPrefetchConfiguration
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.infrastructure.GlobalSettings.CrlPrefetchConfiguration`

Property of
> [GlobalSettingsSecurityData](vdi.infrastructure.GlobalSettings.SecurityData.md#field_detail)

Since
> Horizon 8.11


## Data Object Description

configurations for crl prefetch service.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**distributionPoints**|  xsd:string[]|  List of CRL distribution points URLs, from where CRLs needs to be fetched. [^1]
**refreshPeriodMinutes**|  xsd:int|  Time Interval (in minutes) to refresh CRLs. [^269] [^1] [^8]
**fileMaxSizeKb**|  xsd:int|  Maximum allowed size for CRL file (in kb). [^176] [^1] [^72]


 


[^1]: This property need not be set.
[^8]: This property has a minimum value of 1.
[^72]: This property has a minimum value of 0.
[^176]: This property has a default value of 1024.
[^269]: This property has a default value of 60.