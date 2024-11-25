---
layout: page
title: Data Object - ADDomainHealthConnectionServerConnectionData
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.health.ADDomainHealth.ConnectionServerConnectionData`

Property of
> [ADDomainHealthInfo](vdi.health.ADDomainHealth.ADDomainHealthInfo.md#field_detail)

See also
> [ConnectionServerId](vdi.entity.ConnectionServerId.md)

Since
> Horizon View 6.0


## Data Object Description

The domain connection health for a connection server.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**id**| [ConnectionServerId](vdi.entity.ConnectionServerId.md)|  The ID of the connection server.
**connectionServerName**|  xsd:string|  The name of the connection server.
**status**|  xsd:string|  The status of the connection to the domain.<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"OK"</td><td>Domain is accepting LDAP bind operations and has full functionality.</td></tr><tr><td>"WARN"</td><td>Domain is only accepting LDAP ping operations and has limited functionality. This may indicate a one-way trust relationship with this domain.</td></tr><tr><td>"ERROR"</td><td>Domain can not be contacted.</td></tr><tr><td>"UNKNOWN"</td><td>Domain health could not be determined.</td></tr></table>
**trustRelationship**|  xsd:string|  The trust relationship for the domain.<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"PRIMARYDOMAIN"</td><td>The domain is the domain that the broker is present in.</td></tr><tr><td>"FROMBROKER"</td><td>The domain is trusted by the domain that the broker is in.</td></tr><tr><td>"TOBROKER"</td><td>The domain trusts the broker's domain (this is for completeness and generally will not be used).</td></tr><tr><td>"TWOWAY"</td><td>The domain has a two way trust relationship with the broker's domain.</td></tr><tr><td>"TWOWAY_FOREST"</td><td>The domain is in the same forest as the broker domain, implies two way trust.</td></tr><tr><td>"MANUAL"</td><td>The domain was manually configured (the trust has not been detected).</td></tr><tr><td>"UNKNOWN"</td><td>The trust relationship could not be determined.</td></tr><tr><td>"NOTRUST"</td><td>The domain not having trust with broker domain.</td></tr></table>
**contactable**|  xsd:string|  Whether the domain can be contacted.<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"UNCONTACTABLE"</td><td>No domain controllers appear to be present on the network for this domain.</td></tr><tr><td>"FULLYACCESSIBLE"</td><td>The domain controller(s) are accepting bind operations.</td></tr><tr><td>"CANNOTBIND"</td><td>The domain controller(s) are only accepting LDAP ping operations.</td></tr><tr><td>"UNKNOWN"</td><td>Cannot determine accessibility.</td></tr></table>
**refId**|  xsd:string|  Reference ID of the connection server.  **_Since_** Horizon 7.10 [^1]
**lastUpdatedTimestamp**|  xsd:long|  The timestamp in milliseconds when the last update was obtained. Measured as epoch time.  **_Since_** Horizon 7.12 [^1] [^2]
 


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.