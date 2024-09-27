---
layout: page
title: Data Object - GlobalSettingsClientData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.infrastructure.GlobalSettings.ClientData  
Property of
     [GlobalSettingsClientRestrictionConfiguration](vdi.infrastructure.GlobalSettings.ClientRestrictionConfiguration.md#field_detail)  
Since 
    Horizon 7.11

## Data Object Description 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**type**|  xsd:string|  The type of the client.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"WINDOWS"| Client type is Windows client  
"MAC"| Client type is Mac client  
"HTMLACCESS"| Client type is web client  
"LINUX"| Client type is Linux client  
"IOS"| Client type is iOS client  
"ANDROID"| Client type is Android client  
"WINSTORE"| Client type is UWP client  
"CHROME"| Client type is chrome client  

  
**version**|  xsd:string|  Restrict access for all the Horizon clients that have version less than the [version](vdi.infrastructure.GlobalSettings.ClientData.md#version). This is applicable only for Horizon Clients 4.5.0 or later (or Horizon Client for Chrome 4.8.0 or later) 

  * One of [version](vdi.infrastructure.GlobalSettings.ClientData.md#version), [blockSpecificVersions](vdi.infrastructure.GlobalSettings.ClientData.md#blockSpecificVersions), [warnSpecificVersions](vdi.infrastructure.GlobalSettings.ClientData.md#warnSpecificVersions) is mandatory.
  * Only one of [version](vdi.infrastructure.GlobalSettings.ClientData.md#version) or [blockSpecificVersions](vdi.infrastructure.GlobalSettings.ClientData.md#blockSpecificVersions) can be set.

  


* This property need not be set.

  
**warnSpecificVersions**|  xsd:string|  Warn users when connecting with the Horizon client having version that matches any of the comma separated specified versions. This is applicable only for Horizon Clients 8.0.0 or later 

  * One of [version](vdi.infrastructure.GlobalSettings.ClientData.md#version), [blockSpecificVersions](vdi.infrastructure.GlobalSettings.ClientData.md#blockSpecificVersions), [warnSpecificVersions](vdi.infrastructure.GlobalSettings.ClientData.md#warnSpecificVersions) is mandatory.
  * This property cannot be used for [type](vdi.infrastructure.GlobalSettings.ClientData.md#type) "WINSTORE", "HTMLACCESS".

**_Since_** Horizon 8.0  


* This property need not be set.
  * This property has a maximum length of 128 characters. 

  
**blockSpecificVersions**|  xsd:string|  Restrict users when connecting with the Horizon client having version that matches any of the comma separated specified versions. This is applicable only for Horizon Clients 4.5.0 or later (or Horizon Client for Chrome 4.8.0 or later) 

  * One of [version](vdi.infrastructure.GlobalSettings.ClientData.md#version), [blockSpecificVersions](vdi.infrastructure.GlobalSettings.ClientData.md#blockSpecificVersions), [warnSpecificVersions](vdi.infrastructure.GlobalSettings.ClientData.md#warnSpecificVersions) is mandatory.
  * Only one of [version](vdi.infrastructure.GlobalSettings.ClientData.md#version) or [blockSpecificVersions](vdi.infrastructure.GlobalSettings.ClientData.md#blockSpecificVersions) can be set.
  * This property cannot be used for [type](vdi.infrastructure.GlobalSettings.ClientData.md#type) "WINSTORE", "HTMLACCESS".

**_Since_** Horizon 8.0  


* This property need not be set.
  * This property has a maximum length of 128 characters. 

  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

