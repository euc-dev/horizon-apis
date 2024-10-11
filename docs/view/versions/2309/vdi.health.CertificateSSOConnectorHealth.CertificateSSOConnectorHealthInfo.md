---
layout: page
title: Data Object - CertificateSSOConnectorHealthInfo
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.health.CertificateSSOConnectorHealth.CertificateSSOConnectorHealthInfo`

Returned by  
> [CertificateSSOConnectorHealth_Get](vdi.health.CertificateSSOConnectorHealth.md#get), [CertificateSSOConnectorHealth_List](vdi.health.CertificateSSOConnectorHealth.md#list)

See also  
> [CertificateSSOConnectorConnectorHealthData](vdi.health.CertificateSSOConnectorHealth.ConnectorHealthData.md), [CertificateSSOConnectorId](vdi.entity.CertificateSSOConnectorId.md)

Since  
> Horizon 7.0


## Data Object Description 

Information about the health of a CertSSO connector. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [CertificateSSOConnectorId](vdi.entity.CertificateSSOConnectorId.md)|  The ID of the CertSSO connector.   
  
**displayName**|  xsd:string|  The display name of the connector.   


 * This property need not be set.

  
**enabled**|  xsd:boolean|  Whether or not the connector is enabled.   
  
**data**| [CertificateSSOConnectorConnectorHealthData](vdi.health.CertificateSSOConnectorHealth.ConnectorHealthData.md)|  Base health information about the CertSSO connector.   
  
**refId**|  xsd:string|  Reference ID used for this CertSSO connector.  **_Since_** Horizon 7.11  


 * This property need not be set.

  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
