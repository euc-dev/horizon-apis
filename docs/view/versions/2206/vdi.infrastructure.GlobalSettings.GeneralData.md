---
layout: page
title: Data Object - GlobalSettingsGeneralData
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.infrastructure.GlobalSettings.GeneralData`

Property of  
> [GlobalSettingsInfo](vdi.infrastructure.GlobalSettings.GlobalSettingsInfo.md#field_detail)

Since  
> Horizon View 6.0


## Data Object Description 

General global settings determine session time-out lengths, status updates in View Administrator, and whether prelogin and warning messages are displayed. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**clientMaxSessionTimePolicy**|  xsd:string|  Client max session lifetime policy.   


  * This property has a default value of "TIMEOUT_AFTER".
  * This property will be one of:  
|  Value |  Description   
---|---  
"TIMEOUT_AFTER"| Indicates that the client session times out after a configurable session length (in minutes)  
"NEVER"| Indicates no absolute client session length (sessions only end due to inactivity  

  
**clientMaxSessionTimeMinutes**|  xsd:int|  Determines how long a user can keep a session open after logging in to View Connection Server. The value is set in minutes. When a session times out, the session is terminated and the View client is disconnected from the resource.   


  * This property has a default value of 600.
* This property need not be set.
  * This property has a minimum value of 5. 
  * This property is required if clientMaxSessionTimePolicy is set to "TIMEOUT_AFTER".

  
**clientIdleSessionTimeoutPolicy**|  xsd:string|  Specifies the policy for the maximum time that a that a user can be idle before the broker takes measure to protect the session.   


  * This property has a default value of "NEVER".
  * This property will be one of:  
|  Value |  Description   
---|---  
"NEVER"| Indicates that the client session is never locked.  
"TIMEOUT_AFTER"| Indicates that the user session can be idle for a configurable max time (in minutes) before the broker takes measure to protect the session.  

  
**clientIdleSessionTimeoutMinutes**|  xsd:int|  Determines how long a that a user can be idle before the broker takes measure to protect the session. The value is set in minutes.   


  * This property has a default value of 15.
* This property need not be set.
  * This property is required if clientIdleSessionTimeoutPolicy is set to "TIMEOUT_AFTER".

  
**clientSessionTimeoutMinutes**|  xsd:int|  Determines the maximum length of time that a Broker session will be kept active if there is no traffic between a client and the Broker. The value is set in minutes.   


  * This property has a default value of 1200.
  * This property has a minimum value of 5. 

  
**desktopSSOTimeoutPolicy**|  xsd:string|  The single sign on setting for when a user connects to View Connection Server.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"DISABLE_AFTER"| SSO is disabled the specified number of minutes after a user connects to View Connection Server.  
"DISABLED"| Single sign on is always disabled.  
"ALWAYS_ENABLED"| Single sign on is always enabled.  

  
**desktopSSOTimeoutMinutes**|  xsd:int|  SSO is disabled the specified number of minutes after a user connects to View Connection Server.   


* This property need not be set.
  * This property has a minimum value of 1. 
  * This property is required if desktopSSOTimeoutPolicy is set to "DISABLE_AFTER".

  
**applicationSSOTimeoutPolicy**|  xsd:string|  The single sign on timeout policy for application sessions.   


  * This property has a default value of "ALWAYS_ENABLED".
  * This property will be one of:  
|  Value |  Description   
---|---  
"DISABLE_AFTER"| SSO is disabled the specified number of minutes after a user connects to View Connection Server.  
"DISABLED"| Single sign on is always disabled.  
"ALWAYS_ENABLED"| Single sign on is always enabled.  

  
**applicationSSOTimeoutMinutes**|  xsd:int|  The time allowed (in minutes) to elapse after a user has authenticated before the application SSO credentials are locked unless the user's client supports idle sessions and the user remains active.   


* This property need not be set.
  * This property has a minimum value of 1. 
  * This property is required if applicationSSOTimeoutPolicy is set to "DISABLE_AFTER".

  
**viewAPISessionTimeoutMinutes**|  xsd:int|  Determines how long (in minutes) an idle View API session continues before the session times out. Setting the View API session timeout to a high number of minutes increases the risk of unauthorized use of View API. Use caution when you allow an idle session to persist a long time.   


  * This property has a default value of 10.
  * This property has a minimum value of 1. 
  * This property has a maximum value of 4320. 

  
**displayPreLoginMessage**|  xsd:boolean|  Indicates whether to show a disclaimer or other message when the View Client user logs in.  
This change will take effect on next login for each user.  **_Since_** Horizon 7.9  


  * This property has a default value of false.
* This property need not be set.

  
**preLoginMessage**|  xsd:string|  Displays a disclaimer or another message to View Client users when they log in. No message will be displayed if this is null.   


* This property need not be set.

  
**displayWarningBeforeForcedLogoff**|  xsd:boolean|  Displays a warning message when users are forced to log off because a scheduled or immediate update such as a machine-refresh operation is about to start.   
  
**forcedLogoffTimeoutMinutes**|  xsd:int|  The number of minutes to wait after the warning is displayed and before logging off the user.   


* This property need not be set.
  * This property has a minimum value of 1. 
  * This property is required if displayWarningBeforeForcedLogoff is set to true.

  
**forcedLogoffMessage**|  xsd:string|  The warning to be displayed before logging off the user.   


* This property need not be set.
  * This property is required if displayWarningBeforeForcedLogoff is set to true.

  
**enableServerInSingleUserMode**|  xsd:boolean|  Permits certain RDSServer operating systems to be used for non-RDS Desktops.   
  
**storeCALOnBroker**|  xsd:boolean|  Used for configuring whether or not to store the RDS Per Device CAL on Broker.  **_Since_** Horizon 7.0  


  * This property has a default value of false.

  
**storeCALOnClient**|  xsd:boolean|  Used for configuring whether or not to store the RDS Per Device CAL on client devices. This value can be true only if the [storeCALOnBroker](vdi.infrastructure.GlobalSettings.GeneralData.md#storeCALOnBroker) is true.  **_Since_** Horizon 7.0  


  * This property has a default value of false.

  
**enableUIUsernameCaching**|  xsd:boolean|  For UI based clients: 

  * if set true, UI clients should show a "Remember me" check box option on login page.
  * if set false, UI clients should not show the "Remember me" check box option on login page.

Non UI based clients should ignore this property.  **_Since_** Horizon 7.5  


  * This property has a default value of true.
* This property need not be set.

  
**consoleSessionTimeoutMinutes**|  xsd:int|  Determines how long (in minutes) an idle admin console session continues before the session times out.  **_Since_** Horizon 7.5  


  * This property has a default value of 30.
* This property need not be set.

  
**enableAutomaticStatusUpdates**|  xsd:boolean|  Enable updation of the global status of the application periodically. The Dashboard Information is also updated at regular intervals when Dashboard page is active.  **_Since_** Horizon 7.9  


  * This property has a default value of false.
* This property need not be set.

  
**sendDomainList**|  xsd:boolean|  Indicates whether the domain list will be sent to the client.  
Since domain list will be sent before user is authenticated with server, it could disclose domain information to external users.  **_Since_** Horizon 7.9  
> 


  * This property has a default value of false.
* This property need not be set.

  
**enableCredentialCleanupForHTMLAccess**|  xsd:boolean|  Indicates whether to clean up broker session credentials when one tab connecting to remote desktop/app is closed.  **_Since_** Horizon 7.9  


  * This property has a default value of false.
* This property need not be set.

  
**hideServerInformationInClient**|  xsd:boolean|  Indicates whether to hide the server URL in the client user interface.  **_Since_** Horizon 7.9  


  * This property has a default value of false.
* This property need not be set.

  
**hideDomainListInClient**|  xsd:boolean|  Whether to hide the list of domains in the client user interface.  
If value set to true, the user will need to provide a UPN (e.g. user@domain) or a logon name in the format domain\\\user when logging in.  **_Since_** Horizon 7.9  


  * This property has a default value of true.
* This property need not be set.

  
**enableMultiFactorReAuth**|  xsd:boolean|  Enable/Disable multifactor re-authentication. Enabling this would prompt end user with RSA/RADIUS screen after idle session timeout during unlock. This would have no effect if 2-factor authentication is disabled.  **_Since_** Horizon 7.11  


  * This property has a default value of false.
* This property need not be set.

  
**disconnectWarningTime**|  xsd:int|  The time prior to the forcibly disconnect timeout when a warning message would be shown by the client  **_Since_** Horizon 8.6  


* This property need not be set.
  * This property has a minimum value of 0. 
  * This property has a maximum value of 30. 

  
**disconnectWarningMessage**|  xsd:string|  The warning to be displayed before forcibly disconnect timeout.  **_Since_** Horizon 8.6  


  * This property has a default value of Your virtual session is going to be logged off. Please save your work..
* This property need not be set.

  
**disconnectMessage**|  xsd:string|  The message to be displayed at the time of forced disconnect.  **_Since_** Horizon 8.6  


  * This property has a default value of Your session has expired. Please re-connect to the portal and restart the session..
* This property need not be set.

  
  
  
 
  
  
