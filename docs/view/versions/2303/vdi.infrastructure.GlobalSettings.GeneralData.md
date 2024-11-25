---
layout: page
title: Data Object - GlobalSettingsGeneralData
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.infrastructure.GlobalSettings.GeneralData`

Property of
> [GlobalSettingsInfo](vdi.infrastructure.GlobalSettings.GlobalSettingsInfo.md#field_detail)

Since
> Horizon View 6.0


## Data Object Description

General global settings determine session time-out lengths, status updates in View Administrator, and whether prelogin and warning messages are displayed.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**clientMaxSessionTimePolicy**|  xsd:string|  Client max session lifetime policy. [^270] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"TIMEOUT_AFTER"</td><td>Indicates that the client session times out after a configurable session length (in minutes)</td></tr><tr><td>"NEVER"</td><td>Indicates no absolute client session length (sessions only end due to inactivity)</td></tr></table>
**clientMaxSessionTimeMinutes**|  xsd:int|  Determines how long a user can keep a session open after logging in to View Connection Server. The value is set in minutes. When a session times out, the session is terminated and the View client is disconnected from the resource. [^271] [^1] [^272] [^273]
**clientIdleSessionTimeoutPolicy**|  xsd:string|  Specifies the policy for the maximum time that a that a user can be idle before the broker takes measure to protect the session. [^121] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"NEVER"</td><td>Indicates that the client session is never locked.</td></tr><tr><td>"TIMEOUT_AFTER"</td><td>Indicates that the user session can be idle for a configurable max time (in minutes) before the broker takes measure to protect the session.</td></tr></table>
**clientIdleSessionTimeoutMinutes**|  xsd:int|  Determines how long a that a user can be idle before the broker takes measure to protect the session. The value is set in minutes. [^274] [^1] [^275]
**clientSessionTimeoutMinutes**|  xsd:int|  Determines the maximum length of time that a Broker session will be kept active if there is no traffic between a client and the Broker. The value is set in minutes. [^276] [^272]
**desktopSSOTimeoutPolicy**|  xsd:string|  The single sign on setting for when a user connects to View Connection Server.<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"DISABLE_AFTER"</td><td>SSO is disabled the specified number of minutes after a user connects to View Connection Server.</td></tr><tr><td>"DISABLED"</td><td>Single sign on is always disabled.</td></tr><tr><td>"ALWAYS_ENABLED"</td><td>Single sign on is always enabled.</td></tr></table>
**desktopSSOTimeoutMinutes**|  xsd:int|  SSO is disabled the specified number of minutes after a user connects to View Connection Server. [^1] [^8] [^277]
**applicationSSOTimeoutPolicy**|  xsd:string|  The single sign on timeout policy for application sessions. [^278]<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"DISABLE_AFTER"</td><td>SSO is disabled the specified number of minutes after a user connects to View Connection Server.</td></tr><tr><td>"DISABLED"</td><td>Single sign on is always disabled.</td></tr><tr><td>"ALWAYS_ENABLED"</td><td>Single sign on is always enabled.</td></tr></table>
**applicationSSOTimeoutMinutes**|  xsd:int|  The time allowed (in minutes) to elapse after a user has authenticated before the application SSO credentials are locked unless the user's client supports idle sessions and the user remains active. [^1] [^8] [^279]
**viewAPISessionTimeoutMinutes**|  xsd:int|  Determines how long (in minutes) an idle View API session continues before the session times out. Setting the View API session timeout to a high number of minutes increases the risk of unauthorized use of View API. Use caution when you allow an idle session to persist a long time. [^45] [^8] [^280]
**displayPreLoginMessage**|  xsd:boolean|  Indicates whether to show a disclaimer or other message when the View Client user logs in.<br>This change will take effect on next login for each user.  **_Since_** Horizon 7.9 [^5] [^1]
**preLoginMessage**|  xsd:string|  Displays a disclaimer or another message to View Client users when they log in. No message will be displayed if this is null. [^1]
**displayWarningBeforeForcedLogoff**|  xsd:boolean|  Displays a warning message when users are forced to log off because a scheduled or immediate update such as a machine-refresh operation is about to start.
**forcedLogoffTimeoutMinutes**|  xsd:int|  The number of minutes to wait after the warning is displayed and before logging off the user. [^1] [^8] [^281]
**forcedLogoffMessage**|  xsd:string|  The warning to be displayed before logging off the user. [^1] [^281]
**enableServerInSingleUserMode**|  xsd:boolean|  Permits certain RDSServer operating systems to be used for non-RDS Desktops.
**storeCALOnBroker**|  xsd:boolean|  Used for configuring whether or not to store the RDS Per Device CAL on Broker.  **_Since_** Horizon 7.0 [^5]
**storeCALOnClient**|  xsd:boolean|  Used for configuring whether or not to store the RDS Per Device CAL on client devices. This value can be true only if the [storeCALOnBroker](vdi.infrastructure.GlobalSettings.GeneralData.md#storeCALOnBroker) is true.  **_Since_** Horizon 7.0 [^5]
**enableUIUsernameCaching**|  xsd:boolean|  For UI based clients: [^282] [^283]<br>Non UI based clients should ignore this property.  **_Since_** Horizon 7.5 [^6] [^1]
**consoleSessionTimeoutMinutes**|  xsd:int|  Determines how long (in minutes) an idle admin console session continues before the session times out.  **_Since_** Horizon 7.5 [^284] [^1]
**enableAutomaticStatusUpdates**|  xsd:boolean|  Enable updation of the global status of the application periodically. The Dashboard Information is also updated at regular intervals when Dashboard page is active.  **_Since_** Horizon 7.9 [^5] [^1]
**sendDomainList**|  xsd:boolean|  Indicates whether the domain list will be sent to the client.<br>Since domain list will be sent before user is authenticated with server, it could disclose domain information to external users.  **_Since_** Horizon 7.9 [^5] [^1]
**enableCredentialCleanupForHTMLAccess**|  xsd:boolean|  Indicates whether to clean up broker session credentials when one tab connecting to remote desktop/app is closed.  **_Since_** Horizon 7.9 [^5] [^1]
**hideServerInformationInClient**|  xsd:boolean|  Indicates whether to hide the server URL in the client user interface.  **_Since_** Horizon 7.9 [^5] [^1]
**hideDomainListInClient**|  xsd:boolean|  Whether to hide the list of domains in the client user interface.<br>If value set to true, the user will need to provide a UPN (e.g. user@domain) or a logon name in the format domain\\\user when logging in.  **_Since_** Horizon 7.9 [^6] [^1]
**enableMultiFactorReAuth**|  xsd:boolean|  Enable/Disable multifactor re-authentication. Enabling this would prompt end user with RSA/RADIUS screen after idle session timeout during unlock. This would have no effect if 2-factor authentication is disabled.  **_Since_** Horizon 7.11 [^5] [^1]
**disconnectWarningTime**|  xsd:int|  The time prior to the forcibly disconnect timeout when a warning message would be shown by the client  **_Since_** Horizon 8.6 [^1] [^72] [^285]
**disconnectWarningMessage**|  xsd:string|  The warning to be displayed before forcibly disconnect timeout.  **_Since_** Horizon 8.6 [^286] [^1]
**disconnectMessage**|  xsd:string|  The message to be displayed at the time of forced disconnect.  **_Since_** Horizon 8.6 [^287] [^1]
**displayPreLoginAdminBanner**|  xsd:boolean|  Enable/Disable the display of prelogin banner before user logins to Horizon Admin Console.  **_Since_** Horizon 8.7 [^5] [^1]
**preLoginAdminBannerHeader**|  xsd:string|  The banner header to be displayed before user logins to Horizon Admin Console.  **_Since_** Horizon 8.7 [^288] [^1] [^289]
**preLoginAdminBannerMessage**|  xsd:string|  The banner message to be displayed before user logins to Horizon Admin Console.  **_Since_** Horizon 8.7 [^307] [^1] [^289]
**enforceCsrfProtection**|  xsd:boolean|  Restricts XML-API usage to safer clients which support CSRF protection.  **_Since_** Horizon 8.8 [^5] [^1]
**enforceE2EEncryption**|  xsd:boolean|  Restricts XML-API usage to safer clients which support E2E encryption.  **_Since_** Horizon 8.8 [^5] [^1]
 


 


[^1]: This property need not be set.
[^5]: This property has a default value of false.
[^6]: This property has a default value of true.
[^8]: This property has a minimum value of 1.
[^45]: This property has a default value of 10.
[^72]: This property has a minimum value of 0.
[^121]: This property has a default value of 'NEVER'.
[^270]: This property has a default value of "TIMEOUT_AFTER".
[^271]: This property has a default value of 600.
[^272]: This property has a minimum value of 5.
[^273]: This property is required if clientMaxSessionTimePolicy is set to "TIMEOUT_AFTER".
[^274]: This property has a default value of 15.
[^275]: This property is required if clientIdleSessionTimeoutPolicy is set to "TIMEOUT_AFTER".
[^276]: This property has a default value of 1200.
[^277]: This property is required if desktopSSOTimeoutPolicy is set to "DISABLE_AFTER".
[^278]: This property has a default value of "ALWAYS_ENABLED".
[^279]: This property is required if applicationSSOTimeoutPolicy is set to "DISABLE_AFTER".
[^280]: This property has a maximum value of 4320.
[^281]: This property is required if displayWarningBeforeForcedLogoff is set to true.
[^282]: If set true, UI clients should show a "Remember me" check box option on the login page.
[^283]: If set false, UI clients should not show the "Remember me" check box option on the login page.
[^284]: This property has a default value of 30.
[^285]: This property has a maximum value of 30.
[^286]: This property has a default value of Your virtual session is going to be logged off. Please save your work.
[^287]: This property has a default value of Your session has expired. Please re-connect to the portal and restart the session.
[^288]: This property has a default value of Attention.
[^289]: This property is required if displayPreLoginAdminBanner is set to true.
[^307]: This property has a default value of On proceeding, you agree that you fully comply with the laws of this organisation.