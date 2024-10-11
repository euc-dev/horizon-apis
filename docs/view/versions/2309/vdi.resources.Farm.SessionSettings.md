---
layout: page
title: Data Object - FarmSessionSettings
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.resources.Farm.SessionSettings`

Property of  
> [FarmData](vdi.resources.Farm.FarmData.md#field_detail)

Since  
> Horizon View 6.0


## Data Object Description 

Farm session settings 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**disconnectedSessionTimeoutPolicy**|  xsd:string|  Log-off policy after disconnected session   


  * This property has a default value of "NEVER".
  * This property will be one of:  
|  Value |  Description   
---|---  
"IMMEDIATE"| Logoff immediately after disconnect.  
"NEVER"| Do not logoff after disconnect.  
"AFTER"| Logoff the specified number of minutes after disconnect.  

  
**disconnectedSessionTimeoutMinutes**|  xsd:int|  Disconnected sessions timeout (in minutes). An empty disconnected session is logged off after the timeout.   


 * This property need not be set.
  * This property has a minimum value of 1. 
  * This property is required if disconnectedSessionTimeoutPolicy is set to "AFTER".

  
**emptySessionTimeoutPolicy**|  xsd:string|  Application empty session timeout policy.   


  * This property has a default value of "AFTER".
  * This property will be one of:  
|  Value |  Description   
---|---  
"IMMEDIATE"| Empty session is disconnected immediately.  
"NEVER"| Empty session is never disconnected.  
"AFTER"| Empty session is disconnected after specified number of minutes.  

  
**emptySessionTimeoutMinutes**|  xsd:int|  Application empty session timeout (in minutes). An empty session (that has no remote-able window) is disconnected after the timeout.   


  * This property has a default value of 1.
 * This property need not be set.
  * This property has a minimum value of 1. 
  * This property is required if emptySessionTimeoutPolicy is set to "AFTER".

  
**logoffAfterTimeout**|  xsd:boolean|  Indicates whether the empty application sessions are logged off (true) or disconnected (false) after timeout.   


  * This property has a default value of false.

  
**preLaunchSessionTimeoutPolicy**|  xsd:string|  Application pre-launch session timeout policy.  **_Since_** Horizon 7.2  


 * This property need not be set.
  * This property will be one of:  
|  Value |  Description   
---|---  
"NEVER"| Pre-launched session is never disconnected.  
"AFTER"| Pre-launched session is disconnected after specified number of minutes.  

  
**preLaunchSessionTimeoutMinutes**|  xsd:int|  Application pre-launch session timeout (in minutes). A pre-launch session is disconnected after the timeout.  **_Since_** Horizon 7.2  


 * This property need not be set.
  * This property has a minimum value of 10. 
  * This property is required if preLaunchSessionTimeoutPolicy is set to "AFTER".

  
**sessionTimeoutPolicy**|  xsd:string|  Specifies the session timeout policy for the applications published from the Farm. This policy indicates whether the launched application session is a forever application session or not.  **_Since_** Horizon 8.3  


  * This property has a default value of "DEFAULT".
 * This property need not be set.
  * This property will be one of:  
|  Value |  Description   
---|---  
"DEFAULT"| Indicates application sessions will be disconnected either on reaching the global idle timeout or on reaching the max session timeout.  
"NEVER"| Indicates application sessions will not be disconnected either on reaching the global idle timeout or on reaching the max session timeout.  

  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
