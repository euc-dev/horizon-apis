---
layout: page
title: Data Object - CertificateSSOConnectorHealthEnrollmentServerHealthData
hide:
#- navigation
- toc
---





Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.health.CertificateSSOConnectorHealth.EnrollmentServerHealthData`

Property of
> [CertificateSSOConnectorConnectorHealthData](vdi.health.CertificateSSOConnectorHealth.ConnectorHealthData.md#field_detail)

See also
> [CertificateSSOEnrollmentServerId](vdi.entity.CertificateSSOEnrollmentServerId.md)

Since
> Horizon 7.0


## Data Object Description

The health data for a CertSSO connector enrollment server.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**enrollmentServer**| [CertificateSSOEnrollmentServerId](vdi.entity.CertificateSSOEnrollmentServerId.md)|  The id of the enrollment server.
**dnsName**|  xsd:string|  The DNS name of the enrollment server.
**state**|  xsd:string|  The state of the enrollment server health.<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"OK"</td><td>Enrollment server is green.</td></tr><tr><td>"ERROR"</td><td>Enrollment server is red.</td></tr></table>
**stateReasons**|  xsd:string[]|  Reasons for the state, if any. [^1]<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"UNREACHABLE_ON_POD"</td><td>Error: The enrollment server cannot be contacted by the pod.</td></tr><tr><td>"UNREACHABLE_ON_LOCAL_BROKER"</td><td>Error: The enrollment server cannot be contacted by the local broker.</td></tr></table>


 


[^1]: This property need not be set.