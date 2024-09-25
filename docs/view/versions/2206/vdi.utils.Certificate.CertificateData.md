---
layout: page
title: Data Object - CertificateData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.utils.Certificate.CertificateData
Returned by
     [Certificate_Validate](vdi.utils.Certificate.md#validate), [Certificate_ValidateViewComposerLocalToVC](vdi.utils.Certificate.md#validateViewComposerLocalToVC)
See also
     [CertificateThumbprint](vdi.utils.Certificate.CertificateThumbprint.md)
Since 
    Horizon View 6.0

## Data Object Description 

Details corresponding to a server certificate. 

  * This data object must be updated as a whole.



## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**thumbprint**| [CertificateThumbprint](vdi.utils.Certificate.CertificateThumbprint.md)|  Certificate thumbprint and corresponding algorithm.   


[^1]

  
**certificate**|  xsd:string|  The certificate in a string form.   


[^1]

  
**certificateEncoding**|  xsd:string|  The encoding of the certificate.  **_Since_** Horizon 7.8  


[^1]
  * This property will be one of:  
|  Value |  Description   
---|---  
"DER_BASE64_PEM"| Denotes the Base64 encoded DER certificate.  

  
**invalidReasons**|  xsd:string[]|  The reason(s) why the certificate could not be validated.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"EXPIRED"| Denotes an expired certificate.  
"INVALID_USAGE"| Denotes an invalid usage of a certificate.  
"NAME_MISMATCH"| Denotes a name mismatch with the name in the certificate.  
"NOT_TRUSTED"| Denotes that the certificate is not trusted.  
"NOT_YET_VALID"| Denotes that the certificate is not yet trusted.  
"REVOKED"| Denotes that the certificate has been revoked.  
"CANT_CHECK_REVOKED"| Denotes that the server is unable to check whether the certificate has been revoked.  
"OTHER"| Denotes that the certificate has been considered invalid for a reason other than one listed above.  

  
**allowAdminOverride**|  xsd:boolean|  Reserved for fututre use  **_Since_** Horizon 8.6  


  * This property has a default value of true.

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

