---
layout: page
title: Data Object - ServiceAccount
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.health.ADDomainHealth.ServiceAccount  
Property of
     [ADDomainHealthInfo](vdi.health.ADDomainHealth.ADDomainHealthInfo.md#field_detail)  
See also
     [UserOrGroupId](vdi.entity.UserOrGroupId.md)  
Since 
    Horizon 8.2

## Data Object Description 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**ownerId**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  The owner of secondary credentials.   


 * This property need not be set.

  
**username**|  xsd:string|  Service account username.   
  
**status**|  xsd:string|  Status of the service account.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"ACTIVE"| The service account credentials are working properly.  
"ERROR"| The service account credentials are not working.  
"UNKNOWN"| Status of the service account credentials is unknown.  

  
  

  

