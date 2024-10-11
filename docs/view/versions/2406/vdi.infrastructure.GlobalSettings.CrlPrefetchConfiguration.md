---
layout: page
title: Data Object - GlobalSettingsCrlPrefetchConfiguration
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.infrastructure.GlobalSettings.CrlPrefetchConfiguration`

Property of  
> [GlobalSettingsSecurityData](vdi.infrastructure.GlobalSettings.SecurityData.md#field_detail)

Since  
> Horizon 8.11


## Data Object Description 

configurations for crl prefetch service. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**distributionPoints**|  xsd:string[]|  List of CRL distribution points URLs, from where CRLs needs to be fetched.   


 * This property need not be set.

  
**refreshPeriodMinutes**|  xsd:int|  Time Interval (in minutes) to refresh CRLs.   


  * This property has a default value of 60.
 * This property need not be set.
  * This property has a minimum value of 1. 

  
**fileMaxSizeKb**|  xsd:int|  Maximum allowed size for CRL file (in kb).   


  * This property has a default value of 1024.
 * This property need not be set.
  * This property has a minimum value of 0. 

  
  

  
