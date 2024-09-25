---
layout: page
title: Data Object - CertificateSSOConnectorData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.infrastructure.CertificateSSOConnector.CertificateSSOConnectorData
Property of
     [CertificateSSOConnectorInfo](vdi.infrastructure.CertificateSSOConnector.CertificateSSOConnectorInfo.md#field_detail), [CertificateSSOConnectorSpec](vdi.infrastructure.CertificateSSOConnector.CertificateSSOConnectorSpec.md#field_detail)
See also
     [ADDomainId](vdi.entity.ADDomainId.md), [CertificateSSOEnrollmentServerId](vdi.entity.CertificateSSOEnrollmentServerId.md)
Since 
    Horizon 7.0

## Data Object Description 

Configuration data for a Certificate SSO Connector. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**displayName**|  xsd:string|  Human readable display name for this connector. It must be unique among all other connectors.   


  * This property has a maximum length of 64 characters. 

  
**description**|  xsd:string|  Description of this connector.   


[^1]
  * This property has a maximum length of 1024 characters. 

  
**enabled**|  xsd:boolean|  Whether or not the connector is enabled.   


  * This property has a default value of true.

  
**primaryEnrollmentServer**| [CertificateSSOEnrollmentServerId](vdi.entity.CertificateSSOEnrollmentServerId.md)|  The primary enrollment server.   
  
**secondaryEnrollmentServer**| [CertificateSSOEnrollmentServerId](vdi.entity.CertificateSSOEnrollmentServerId.md)|  The secondary enrollment server if the primary isn't available. This cannot be the same as the primary.   


[^1]

  
**domain**| [ADDomainId](vdi.entity.ADDomainId.md)|  The AD domain that this connector applies to. This domain must be unique among all connectors. This domain must be accessible to all enrollment servers configured on this connector. This cannot be changed once created.   


[^2]

  
**templateName**|  xsd:string|  Name of the certificate template to use for this domain. This template must be accessible to all enrollment servers configured on this connector.   
  
**certificateServerNames**|  xsd:string[]|  Specifies the certificate server (common) names to send certificate signing requests to. The enrollment service will round-robin the requests to available certificate servers.   


  * This property is an unordered array of unique values.

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
