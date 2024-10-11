---
layout: page
title: Data Object - GlobalSettingsInfo
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.infrastructure.GlobalSettings.GlobalSettingsInfo`

Returned by  
> [GlobalSettings_Get](vdi.infrastructure.GlobalSettings.md#get)

See also  
> [GlobalFeatureSettings](vdi.infrastructure.GlobalSettings.FeatureSettings.md), [GlobalSettingsClientRestrictionConfiguration](vdi.infrastructure.GlobalSettings.ClientRestrictionConfiguration.md), [GlobalSettingsDataRecoveryPasswordData](vdi.infrastructure.GlobalSettings.DataRecoveryPasswordData.md), [GlobalSettingsGeneralData](vdi.infrastructure.GlobalSettings.GeneralData.md), [GlobalSettingsJmpConfiguration](vdi.infrastructure.GlobalSettings.JmpConfiguration.md), [GlobalSettingsMirageConfiguration](vdi.infrastructure.GlobalSettings.MirageConfiguration.md), [GlobalSettingsSecurityData](vdi.infrastructure.GlobalSettings.SecurityData.md)

Since  
> Horizon View 6.0


## Data Object Description 

The Global Settings information. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**generalData**| [GlobalSettingsGeneralData](vdi.infrastructure.GlobalSettings.GeneralData.md)|  The general settings data.   
  
**securityData**| [GlobalSettingsSecurityData](vdi.infrastructure.GlobalSettings.SecurityData.md)|  The global security data.   
  
**mirageConfiguration**| [GlobalSettingsMirageConfiguration](vdi.infrastructure.GlobalSettings.MirageConfiguration.md)|  The Mirage configuration data.   
  
**dataRecoveryPasswordData**| [GlobalSettingsDataRecoveryPasswordData](vdi.infrastructure.GlobalSettings.DataRecoveryPasswordData.md)|  The data recovery password data.   
  
**jmpConfiguration**| [GlobalSettingsJmpConfiguration](vdi.infrastructure.GlobalSettings.JmpConfiguration.md)| **Deprecated.**_This is being deprecated since JMP configuration will no longer be supported in future releases._ The JMP configuration data.  **_Since_** Horizon 7.4  


* This property need not be set.

  
**clientRestrictionConfiguration**| [GlobalSettingsClientRestrictionConfiguration](vdi.infrastructure.GlobalSettings.ClientRestrictionConfiguration.md)|  The Client restriction configuration data.  **_Since_** Horizon 7.11  


* This property need not be set.

  
**featureSettings**| [GlobalFeatureSettings](vdi.infrastructure.GlobalSettings.FeatureSettings.md)|  The feature settings data.  **_Since_** Horizon 7.11  


* This property need not be set.

  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
