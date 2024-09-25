---
layout: page
title: Data Object - GlobalSettingsClientRestrictionConfiguration
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.infrastructure.GlobalSettings.ClientRestrictionConfiguration
Property of
     [GlobalSettingsInfo](vdi.infrastructure.GlobalSettings.GlobalSettingsInfo.md#field_detail)
See also
     [GlobalSettingsClientData](vdi.infrastructure.GlobalSettings.ClientData.md)
Since 
    Horizon 7.11

## Data Object Description 

Client Restriction configuration indicates which client type and below what version of the client needs to be blocked for brokering to desktops or applications. Additional client types other than the supported client types can also be restricted for brokering to desktops or applications. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**clientData**| [GlobalSettingsClientData[]](vdi.infrastructure.GlobalSettings.ClientData.md)|  Client type and the version information needed to restrict or show warning message to the users using deprecated client versions.   


[^1]

  
**message**|  xsd:string|  The message to be shown for the blocked clients.   


[^1]
  * This property accepts all characters including new line with a maximum length of 1024 characters. 

  
**blockAdditionalClients**|  xsd:boolean|  Whether additional clients need to be blocked.   


  * This property has a default value of false.
[^1]

  
**warningMessage**|  xsd:string|  The warning message to be shown to the users when the Horizon client version being used matches any of the restricted versions for the given client type  **_Since_** Horizon 8.0  


[^1]
  * This property accepts all characters including new line with a maximum length of 1024 characters. 

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
