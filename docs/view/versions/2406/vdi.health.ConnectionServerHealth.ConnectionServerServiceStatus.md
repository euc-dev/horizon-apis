---
layout: page
title: Data Object - ConnectionServerServiceStatus
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.health.ConnectionServerHealth.ConnectionServerServiceStatus
Property of
     [ConnectionServerHealthInfo](vdi.health.ConnectionServerHealth.ConnectionServerHealthInfo.md#field_detail)
Since 
    Horizon 7.10

## Data Object Description 

Information about the status of Connection Server related Services. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**serviceName**|  xsd:string|  Name of the service   


  * This property will be one of:  
|  Value |  Description   
---|---  
"SECURITY_GATEWAY_COMPONENT"| Security Gateway Component Service.  
"PCOIP_SECURE_GATEWAY"| PCoIP Secure Gateway Service.  
"BLAST_SECURE_GATEWAY"| BLAST Secure Gateway Service.  
"CRL_PREFETCH"| CRL prefetch Service.  

  
**status**|  xsd:string|  Status of the service.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"UP"| Service is working properly.  
"DOWN"| Service is not working properly.  

  
  

  

