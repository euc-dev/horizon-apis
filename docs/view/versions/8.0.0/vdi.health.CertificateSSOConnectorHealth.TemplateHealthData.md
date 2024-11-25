---
layout: page
title: Data Object - CertificateSSOConnectorHealthEnrollmentServerTemplateHealthData
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.health.CertificateSSOConnectorHealth.TemplateHealthData`

Property of
> [CertificateSSOConnectorConnectorHealthData](vdi.health.CertificateSSOConnectorHealth.ConnectorHealthData.md#field_detail)

Since
> Horizon 7.0


## Data Object Description

The health data for a CertSSO template.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**name**|  xsd:string|  The name of the template.
**state**|  xsd:string|  The state of the template health, taken as the most severe reported by one of the enrollment servers.<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"OK"</td><td>Template is green.</td></tr><tr><td>"WARN"</td><td>Template is yellow.</td></tr><tr><td>"ERROR"</td><td>Template is red.</td></tr></table>
**primaryEnrollmentServerStateReasons**|  xsd:string[]|  Reasons for the state from the primary enrollment server, if any. [^1]<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"SUPPORTED_NOT_OPTIMAL"</td><td>Warn: This template does not have the ideal properties for CertSSO.</td></tr><tr><td>"NO_CAPABILITY"</td><td>Error: This template does not have CertSSO capability.</td></tr><tr><td>"ENABLED_BUT_UNUSABLE"</td><td>Error: This template is smartcard logon enabled, but cannot be used (INVALID, MANUAL, or UNSUITABLE).</td></tr><tr><td>"NOT_FOUND"</td><td>Error: This template does not exist on the enrollment server domain.</td></tr></table>
**secondaryEnrollmentServerStateReasons**|  xsd:string[]|  Reasons for the state from the secondary enrollment server, if any. [^1]<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"SUPPORTED_NOT_OPTIMAL"</td><td>Warn: This template does not have the ideal properties for CertSSO.</td></tr><tr><td>"NO_CAPABILITY"</td><td>Error: This template does not have CertSSO capability.</td></tr><tr><td>"ENABLED_BUT_UNUSABLE"</td><td>Error: This template is smartcard logon enabled, but cannot be used (INVALID, MANUAL, or UNSUITABLE).</td></tr><tr><td>"NOT_FOUND"</td><td>Error: This template does not exist on the enrollment server domain.</td></tr></table>


 


[^1]: This property need not be set.