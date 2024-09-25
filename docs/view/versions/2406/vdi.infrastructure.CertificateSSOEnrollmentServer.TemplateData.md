---
layout: page
title: Data Object - CertificateSSOTemplateData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.infrastructure.CertificateSSOEnrollmentServer.TemplateData
Property of
     [CertificateSSOCertificateDomainData](vdi.infrastructure.CertificateSSOEnrollmentServer.DomainData.md#field_detail)
Since 
    Horizon 7.0

## Data Object Description 

Certificate template data. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**name**|  xsd:string|  Unique name for this template.   
  
**minimumKeyLength**|  xsd:int|  Minimum key-length of the private/public key associated with the certificate.   


[^1]

  
**hashAlgorithm**|  xsd:string|  Hash algorithm used in the certificate signing request.   


[^1]

  
**validitySeconds**|  xsd:long|  Length of time, in seconds, that certificates issues with this template remain valid.   


[^1]

  
**status**|  xsd:string|  The status of this template.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"SUPPORTED_OPTIMAL"| This template has the optimal properties for CertSSO.  
"SUPPORTED_NOT_OPTIMAL"| This template does not have the ideal properties for CertSSO.  
"UNKNOWN"| This status of this template is unknown. A template with this status cannot be used in connector creation.  
"NO_CAPABILITY"| This template is not configured to perform CertSSO. A template with this status cannot be used in connector creation.  
"INVALID"| This template is smartcard logon enabled, but some setting is invalid. A template with this status cannot be used in connector creation.  
"MANUAL"| This template is smartcard logon enabled, but manual enrollment is needed. A template with this status cannot be used in connector creation.  
"UNSUITABLE"| This template is smartcard logon enabled, but is unsuitable. A template with this status cannot be used in connector creation.  

  
**statusReason**|  xsd:string|  Additional non-localized explanation of the status.   


[^1]

  
  

  

