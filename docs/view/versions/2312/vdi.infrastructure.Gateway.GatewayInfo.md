---
layout: page
title: Data Object - GatewayInfo
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.infrastructure.Gateway.GatewayInfo`

Returned by
> [Gateway_Get](vdi.infrastructure.Gateway.md#get), [Gateway_List](vdi.infrastructure.Gateway.md#list)

See also
> [GatewayGeneralData](vdi.infrastructure.Gateway.GeneralData.md), [GatewayId](vdi.entity.GatewayId.md)

Since
> Horizon 7.7


## Data Object Description

Gateway Detail Information

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**id**| [GatewayId](vdi.entity.GatewayId.md)|  Id for the gateway
**generalData**| [GatewayGeneralData](vdi.infrastructure.Gateway.GeneralData.md)|  General data for the gateway
**refId**|  xsd:string|  Reference ID used for this Gateway.  **_Since_** Horizon 8.8 [^1] [^2]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.