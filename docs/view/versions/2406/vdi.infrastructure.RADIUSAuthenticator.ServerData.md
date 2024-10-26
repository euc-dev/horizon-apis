---
layout: page
title: Data Object - RADIUSAuthenticatorServerSpec
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.infrastructure.RADIUSAuthenticator.ServerData`

Property of
> [RADIUSAuthenticatorInfo](vdi.infrastructure.RADIUSAuthenticator.RADIUSAuthenticatorInfo.md#field_detail), [RADIUSAuthenticatorSpec](vdi.infrastructure.RADIUSAuthenticator.RADIUSAuthenticatorSpec.md#field_detail)

See also
> [SecureString](vdi.util.SecureString.md)

Since
> Horizon View 6.0


## Data Object Description

Information about a RADIUS authentication server.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**hostname**|  xsd:string|  The hostname of the RADIUS authentication server.
**authenticationPort**|  xsd:int|  The authentication port of the RADIUS authentication server. [^8] [^189]
**accountingPort**|  xsd:int|  The accounting port of the RADIUS authentication server. [^72] [^189]
**authenticationType**|  xsd:string|  The authentication type of the RADIUS authentication server.<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"PAP"</td><td>Password authentication protocol</td></tr><tr><td>"CHAP"</td><td>Challenge-handshake authentication protocol</td></tr><tr><td>"MSCHAP1"</td><td>Microsoft challenge-handshake authentication protocol, version 1</td></tr><tr><td>"MSCHAP2"</td><td>Microsoft challenge-handshake authentication protocol, version 2</td></tr></table>
**sharedSecret**| [SecureString](vdi.util.SecureString.md)|  The shared secret of the RADIUS authentication server.
**serverTimeoutSeconds**|  xsd:int|  The server timeout (in seconds) of the RADIUS authentication server. [^8]
**maxAttempts**|  xsd:int|  The maximum number of authentication attempts for the RADIUS authentication server. [^8]
**realmPrefix**|  xsd:string|  The realm prefix of the RADIUS authentication server. [^1]
**realmSuffix**|  xsd:string|  The realm suffix of the RADIUS authentication server. [^1]


 


[^1]: This property need not be set.
[^8]: This property has a minimum value of 1.
[^72]: This property has a minimum value of 0.
[^189]: This property has a maximum value of 65535.