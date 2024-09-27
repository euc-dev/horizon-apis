---
layout: page
title: Data Object - GatewayGeneralData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.infrastructure.Gateway.GeneralData  
Property of
     [GatewayInfo](vdi.infrastructure.Gateway.GatewayInfo.md#field_detail)  
Since 
    Horizon View 6.0

## Data Object Description 

Gateway general data 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**name**|  xsd:string|  Name of the gateway   


 * This property cannot be updated.

  
**address**|  xsd:string|  IP address of the gateway.   


 * This property cannot be updated.

  
**gatewayZoneInternal**|  xsd:boolean|  Flag to determine whether the gateway is internal.   


 * This property cannot be updated.

  
**version**|  xsd:string|  Version of the gateway.   


 * This property cannot be updated.

  
**type**|  xsd:string|  Type of the gateway. It will identify different types of gateways.   


 * This property cannot be updated.
  * This property will be one of:  
|  Value |  Description   
---|---  
"AP"| AP type is for UAG.  
"F5"| F5 type is for F5 server.  
"SG"| SG type is for Security Server.  
"SG-cohosted"| SG-cohosted type is for Cohosted CS as gateway.  
"Unknown"| Unknown type is for unrecognized gateway type.  

  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

