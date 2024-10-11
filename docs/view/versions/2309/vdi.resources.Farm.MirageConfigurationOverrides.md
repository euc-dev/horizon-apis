---
layout: page
title: Data Object - FarmMirageConfigurationOverrides
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.resources.Farm.MirageConfigurationOverrides`

Property of  
> [FarmData](vdi.resources.Farm.FarmData.md#field_detail)

Since  
> Horizon View 6.0


## Data Object Description 

Mirage configuration overrides. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**overrideGlobalSetting**|  xsd:boolean|  If set to true, then the Mirage configuration specified here will be used for this Farm. Otherwise the Mirage configuration in [mirageConfiguration](vdi.infrastructure.GlobalSettings.GlobalSettingsInfo.md#mirageConfiguration) will be used.   


  * This property has a default value of false.

  
**enabled**|  xsd:boolean|  Whether a Mirage server is enabled.   


 * This property need not be set.
  * This property is required if overrideGlobalSetting is set to true.

  
**url**|  xsd:string|  The URL of the Mirage server. This should be in the form "<(DNS name)|(IPv4)|(IPv6)><:(port)>". IPv6 addresses must be enclosed in square brackets.   


 * This property need not be set.
  * This property is required if enabled is set to true.

  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
