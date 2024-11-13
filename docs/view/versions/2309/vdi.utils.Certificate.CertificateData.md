---
layout: page
title: Data Object - CertificateData
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.utils.Certificate.CertificateData`

Returned by
> [Certificate_Validate](vdi.utils.Certificate.md#validate), [Certificate_ValidateViewComposerLocalToVC](vdi.utils.Certificate.md#validateViewComposerLocalToVC)

See also
> [CertificateThumbprint](vdi.utils.Certificate.CertificateThumbprint.md)

Since
> Horizon View 6.0


## Data Object Description

Details corresponding to a server certificate.
 [^167]



## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**thumbprint**| [CertificateThumbprint](vdi.utils.Certificate.CertificateThumbprint.md)|  Certificate thumbprint and corresponding algorithm. [^1]
**certificate**|  xsd:string|  The certificate in a string form. [^1]
**certificateEncoding**|  xsd:string|  The encoding of the certificate.  **_Since_** Horizon 7.8 [^1] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>DER_BASE64_PEM</td><td>Denotes the Base64 encoded DER certificate.</td></tr></table>
**invalidReasons**|  xsd:string[]|  The reason(s) why the certificate could not be validated. <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>EXPIRED</td><td>Denotes an expired certificate.</td></tr><tr><td>INVALID_USAGE</td><td>Denotes an invalid usage of a certificate.</td></tr><tr><td>NAME_MISMATCH</td><td>Denotes a name mismatch with the name in the certificate.</td></tr><tr><td>NOT_TRUSTED</td><td>Denotes that the certificate is not trusted.</td></tr><tr><td>NOT_YET_VALID</td><td>Denotes that the certificate is not yet trusted.</td></tr><tr><td>REVOKED</td><td>Denotes that the certificate has been revoked.</td></tr><tr><td>CANT_CHECK_REVOKED</td><td>Denotes that the server is unable to check whether the certificate has been revoked.</td></tr><tr><td>WEAK_CRYPTO</td><td>Denotes that the certificate has weak signature algorithm.</td></tr><tr><td>OTHER</td><td>Denotes that the certificate has been considered invalid for a reason other than one listed above.</td></tr></table>
**allowAdminOverride**|  xsd:boolean|  Reserved for fututre use  **_Since_** Horizon 8.6 [^6]
 


 


[^1]: This property need not be set.
[^6]: This property has a default value of true.
[^167]: This data object must be updated as a whole.