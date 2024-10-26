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
**disconnectedSessionTimeoutPolicy**|  xsd:string|  Log-off policy after disconnected session [^121] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"IMMEDIATE"</td><td>Logoff immediately after disconnect.</td></tr><tr><td>"NEVER"</td><td>Do not logoff after disconnect.</td></tr><tr><td>"AFTER"</td><td>Logoff the specified number of minutes after disconnect.</td></tr></table>
**disconnectedSessionTimeoutMinutes**|  xsd:int|  Disconnected sessions timeout (in minutes). An empty disconnected session is logged off after the timeout. [^1] [^8] [^122]
**emptySessionTimeoutPolicy**|  xsd:string|  Application empty session timeout policy. [^184] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"IMMEDIATE"</td><td>Empty session is disconnected immediately.</td></tr><tr><td>"NEVER"</td><td>Empty session is never disconnected.</td></tr><tr><td>"AFTER"</td><td>Empty session is disconnected after specified number of minutes.</td></tr></table>
**emptySessionTimeoutMinutes**|  xsd:int|  Application empty session timeout (in minutes). An empty session (that has no remote-able window) is disconnected after the timeout. [^10] [^1] [^8] [^44]
**logoffAfterTimeout**|  xsd:boolean|  Indicates whether the empty application sessions are logged off (true) or disconnected (false) after timeout. [^5]
**preLaunchSessionTimeoutPolicy**|  xsd:string|  Application pre-launch session timeout policy.  **_Since_** Horizon 7.2 [^1] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"NEVER"</td><td>Pre-launched session is never disconnected.</td></tr><tr><td>"AFTER"</td><td>Pre-launched session is disconnected after specified number of minutes.</td></tr></table>
**preLaunchSessionTimeoutMinutes**|  xsd:int|  Application pre-launch session timeout (in minutes). A pre-launch session is disconnected after the timeout.  **_Since_** Horizon 7.2 [^1] [^123] [^47]
**sessionTimeoutPolicy**|  xsd:string|  Specifies the session timeout policy for the applications published from the Farm. This policy indicates whether the launched application session is a forever application session or not.  **_Since_** Horizon 8.3 [^48] [^1] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"DEFAULT"</td><td>Indicates application sessions will be disconnected either on reaching the global idle timeout or on reaching the max session timeout.</td></tr><tr><td>"NEVER"</td><td>Indicates application sessions will not be disconnected either on reaching the global idle timeout or on reaching the max session timeout.</td></tr></table>


 
