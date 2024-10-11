---
layout: page
title: Data Object - CertificateSSOConnectorHealthEnrollmentServerHealthData
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.health.CertificateSSOConnectorHealth.EnrollmentServerHealthData`

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
  
**state**|  xsd:string|  The state of the enrollment server health.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"OK"| Enrollment server is green.  
"ERROR"| Enrollment server is red.  

  
**stateReasons**|  xsd:string[]|  Reasons for the state, if any.   


 * This property need not be set.
  * This property will be one of:  
|  Value |  Description   
---|---  
"UNREACHABLE_ON_POD"| Error: The enrollment server cannot be contacted by the pod.  
"UNREACHABLE_ON_LOCAL_BROKER"| Error: The enrollment server cannot be contacted by the local broker.  

  
  

  
