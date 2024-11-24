---
layout: page
title: Data Object - GatewayGeneralData
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.infrastructure.Gateway.GeneralData`

Property of
> [GatewayInfo](vdi.infrastructure.Gateway.GatewayInfo.md#field_detail)

Since
> Horizon View 6.0


## Data Object Description

Gateway general data

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**name**|  xsd:string|  Name of the gateway [^2]
**address**|  xsd:string|  IP address of the gateway. [^2]
**gatewayZoneInternal**|  xsd:boolean|  Flag to determine whether the gateway is internal. [^2]
**version**|  xsd:string|  Version of the gateway. [^2]
**type**|  xsd:string|  Type of the gateway. It will identify different types of gateways. [^2]<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"AP"</td><td>AP type is for UAG.</td></tr><tr><td>"F5"</td><td>F5 type is for F5 server.</td></tr><tr><td>"SG"</td><td>SG type is for Security Server.</td></tr><tr><td>"SG-cohosted"</td><td>SG-cohosted type is for Cohosted CS as gateway.</td></tr><tr><td>"Unknown"</td><td>Unknown type is for unrecognized gateway type.</td></tr></table>
 


 


[^2]: This property cannot be updated.