---
layout: page
title: Data Object - HealthCounter
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.health.Monitoring.HealthCounter  
Property of
     [SystemStatusCounter](vdi.health.Monitoring.SystemStatusCounter.md#field_detail)  
Returned by
     [Monitoring_GetHealthCounters](vdi.health.Monitoring.md#getHealthCounters)  
See also
     [MapEntry](vdi.util.MapEntry.md)  

## Data Object Description 

The health status information. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**category**|  xsd:string|  Component category.   


* This property cannot be updated.
  * This property will be one of:  
|  Value |  Description   
---|---  
"CONNECTION_SERVER"| The Connection Server.  
"EVENT_DATABASE"| The Event Database.  
"CERTIFICATE_SSO"| The Certificate SSO Connector.  
"VIRTUAL_CENTER"| The Virtual Center.  
"ESX_HOST"| The ESX Host managed by one of the Virtual Center Configured.  
"DATASTORE"| Datastore of the ESX Host.  
"GATEWAY"| The Gateway configured.  
"FARM"| The Farm.  
"RDS_SERVER"| RDS Server.  
"VIEW_COMPOSER"| View Composer.  
"AD_DOMAIN"| AD Domain controller.  
"SAML_AUTHENTICATOR"| SAML 2.0 Authenticator.  
"REMOTE_CONNECTION_SERVER"| Connection Server from the Remote Pod.  
"LICENSE"| License added to the connection server.  
"ALL"| Represents all the categories.  

  
**totalCount**|  xsd:int|  Total number of items of the category.   


* This property cannot be updated.

  
**healthyCount**|  xsd:int|  Number of healthy items of the category.   


* This property cannot be updated.

  
**errorCount**|  xsd:int|  Number of items in the system those are in error state.  **_Since_** Horizon 7.12  


* This property cannot be updated.

  
**warningCount**|  xsd:int|  Number of items in the system those are in warning state.  **_Since_** Horizon 7.12  


* This property cannot be updated.

  
**unknownCount**|  xsd:int|  Number of items in the system those are in unknown state.  **_Since_** Horizon 7.12  


* This property cannot be updated.

  
**details**| [MapEntry[]](vdi.util.MapEntry.md)|  Additional details.   


* This property cannot be updated.

  
  
  
 
  
  

