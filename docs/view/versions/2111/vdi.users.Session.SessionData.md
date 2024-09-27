---
layout: page
title: Data Object - SessionData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.users.Session.SessionData  
Property of
     [SessionGlobalSummaryView](vdi.users.Session.SessionGlobalSummaryView.md#field_detail), [SessionLocalSummaryView](vdi.users.Session.SessionLocalSummaryView.md#field_detail)  
Since 
    Horizon View 6.0

## Data Object Description 

Session data. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**sessionType**|  xsd:string|  Type of this session.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"DESKTOP"| Desktop or RDS Desktop session  
"APPLICATION"| Application session  

  
**sessionProtocol**|  xsd:string|  Protocol for this session. This will be unset for disconnected sessions.   


* This property need not be set.
  * This property will be one of:  
|  Value |  Description   
---|---  
"PCOIP"| Display protocol is PCoIP  
"RDP"| Display protocol is RDP  
"BLAST"| Display protocol is Blast  
"CONSOLE"| Display protocol is Console  
"UNKNOWN"| Display protocol is unknown  

  
**sessionState**|  xsd:string|  State of this session.   


* This property need not be set.
  * This property will be one of:  
|  Value |  Description   
---|---  
"CONNECTED"| CONNECTED: Session is connected  
"DISCONNECTED"| DISCONNECTED: Session is disconnected  
"PENDING"| PENDING: Session is pending  

  
**startTime**|  xsd:dateTime|  Time when this session was originally logged in. The lifecycle of a session begins at login and ends at logout, with any number of connect and disconnect occurrences between. The first connection time will be shortly after this time.   


* This property need not be set.

  
**disconnectTime**|  xsd:dateTime|  Time when the session was last disconnected. This will be unset on error or if the session has never been disconnected.   


* This property need not be set.

  
**lastSessionDurationMS**|  xsd:long|  Duration of the last connection period of the session in milliseconds. If the session is currently connected, this is the duration that the session has been in connected state. If the session is currently disconnected, this is the duration of its previous connection period. This will be unset on error.   


* This property need not be set.

  
**brokeredRemotely**|  xsd:boolean|  Is this session brokered from a remote pod? It is only populated if the Horizon View agent where the session resides is version 6.0 or later.   


* This property need not be set.

  
**resourcedRemotely**|  xsd:boolean|  Is this session running on a remote pod resource?   
  
**unauthenticated**|  xsd:boolean|  Indicates if this session is of unauthenticated access user.  **_Since_** Horizon 7.1  


* This property need not be set.

  
**idleDuration**|  xsd:long|  Idle time duration in minutes. Indicates how long the end user of this session has been idle.  **_Since_** Horizon 7.4  


* This property need not be set.

  
**foreverSession**|  xsd:boolean|  Indicates whether the application session will be disconnected or not either on reaching the global idle timeout or on reaching the max session timeout.  **_Since_** Horizon 8.3  


* This property cannot be updated.

  
  
  
   
  
  

