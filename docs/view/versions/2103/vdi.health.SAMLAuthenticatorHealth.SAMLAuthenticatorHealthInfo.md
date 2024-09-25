---
layout: page
title: Data Object - SAMLAuthenticatorHealthInfo
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.health.SAMLAuthenticatorHealth.SAMLAuthenticatorHealthInfo
Returned by
     [SAMLAuthenticatorHealth_Get](vdi.health.SAMLAuthenticatorHealth.md#get), [SAMLAuthenticatorHealth_List](vdi.health.SAMLAuthenticatorHealth.md#list)
See also
     [SAMLAuthenticatorHealthConnectionServerConnectionData](vdi.health.SAMLAuthenticatorHealth.ConnectionServerConnectionData.md), [SAMLAuthenticatorHealthData](vdi.health.SAMLAuthenticatorHealth.SAMLAuthenticatorHealthData.md), [SAMLAuthenticatorId](vdi.entity.SAMLAuthenticatorId.md)
Since 
    Horizon View 6.0

## Data Object Description 

Information about the health of a SAML authenticator. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [SAMLAuthenticatorId](vdi.entity.SAMLAuthenticatorId.md)|  The ID of the SAML Authenticator.   
  
**data**| [SAMLAuthenticatorHealthData](vdi.health.SAMLAuthenticatorHealth.SAMLAuthenticatorHealthData.md)|  Basic information about the SAML authenticator.   
  
**connectionServerData**| [SAMLAuthenticatorHealthConnectionServerConnectionData[]](vdi.health.SAMLAuthenticatorHealth.ConnectionServerConnectionData.md)|  Information about the SAML authenticator connections from each configured connection server.   


[^1]

  
**refId**|  xsd:string|  Reference ID of the SAML Authenticator.  **_Since_** Horizon 7.10  


[^1]

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
