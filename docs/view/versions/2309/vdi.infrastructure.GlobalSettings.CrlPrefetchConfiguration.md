---
layout: page
title: Data Object - GlobalSettingsCrlPrefetchConfiguration
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.infrastructure.GlobalSettings.CrlPrefetchConfiguration
Property of
     [GlobalSettingsSecurityData](vdi.infrastructure.GlobalSettings.SecurityData.md#field_detail)
Since 
    Horizon 8.11

## Data Object Description 

Supports custom mapping for certificate authentication. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**distributionPoints**|  xsd:string[]|  List of CRL distribution points URLs, from where CRLs needs to be fetched.   


[^1]

  
**folderPath**|  xsd:string|  Storage folder path that will used to store and refresh the CRLs.   


[^1]

  
**refreshPeriodMinutes**|  xsd:int|  Time Interval (in minutes) to refresh CRLs.   


  * This property has a default value of 60.
[^1]
  * This property has a minimum value of 1. 

  
**fileMaxSizeKb**|  xsd:int|  Maximum allowed size for CRL file (in kb).   


  * This property has a default value of 1024.
[^1]
  * This property has a minimum value of 0. 

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

