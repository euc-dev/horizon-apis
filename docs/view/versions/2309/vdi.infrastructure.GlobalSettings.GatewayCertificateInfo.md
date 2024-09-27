---
layout: page
title: Data Object - GatewayCertificateInfo
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.infrastructure.GlobalSettings.GatewayCertificateInfo  
Returned by
     [GlobalSettings_ListGatewayCertificates](vdi.infrastructure.GlobalSettings.md#listGatewayCertificates)  
Since 
    Horizon 8.6

## Data Object Description 

Gateway certificate information 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**certificateName**|  xsd:string|  Certificate identifier in the system.   
  
**commonName**|  xsd:string|  Distinguished name of the entity that is associated with the public key. Represented by subject field of the X509 certificate.   
  
**issuer**|  xsd:string|  Issuer of the certificate. Represented by issuer field of the X509 certificate.   
  
**expiryDate**|  xsd:dateTime|  Time after which the certificate is no longer considered valid. Represented by Not Valid After field of the X509 certificate.   
  
**serialNum**|  xsd:string|  Unique serial number issued by the certificate authority. Represented by Serial Number field of the X509 certificate.   
  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

