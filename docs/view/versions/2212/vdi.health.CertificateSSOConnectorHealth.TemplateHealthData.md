---
layout: page
title: Data Object - CertificateSSOConnectorHealthEnrollmentServerTemplateHealthData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.health.CertificateSSOConnectorHealth.TemplateHealthData  
Property of
     [CertificateSSOConnectorConnectorHealthData](vdi.health.CertificateSSOConnectorHealth.ConnectorHealthData.md#field_detail)  
Since 
    Horizon 7.0

## Data Object Description 

The health data for a CertSSO template. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**name**|  xsd:string|  The name of the template.   
  
**state**|  xsd:string|  The state of the template health, taken as the most severe reported by one of the enrollment servers.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"OK"| Template is green.  
"WARN"| Template is yellow.  
"ERROR"| Template is red.  

  
**primaryEnrollmentServerStateReasons**|  xsd:string[]|  Reasons for the state from the primary enrollment server, if any.   


* This property need not be set.
  * This property will be one of:  
|  Value |  Description   
---|---  
"SUPPORTED_NOT_OPTIMAL"| Warn: This template does not have the ideal properties for CertSSO.  
"NO_CAPABILITY"| Error: This template does not have CertSSO capability.  
"ENABLED_BUT_UNUSABLE"| Error: This template is smartcard logon enabled, but cannot be used (INVALID, MANUAL, or UNSUITABLE).  
"NOT_FOUND"| Error: This template does not exist on the enrollment server domain.  

  
**secondaryEnrollmentServerStateReasons**|  xsd:string[]|  Reasons for the state from the secondary enrollment server, if any.   


* This property need not be set.
  * This property will be one of:  
|  Value |  Description   
---|---  
"SUPPORTED_NOT_OPTIMAL"| Warn: This template does not have the ideal properties for CertSSO.  
"NO_CAPABILITY"| Error: This template does not have CertSSO capability.  
"ENABLED_BUT_UNUSABLE"| Error: This template is smartcard logon enabled, but cannot be used (INVALID, MANUAL, or UNSUITABLE).  
"NOT_FOUND"| Error: This template does not exist on the enrollment server domain.  

  
  
  
  
  
  

