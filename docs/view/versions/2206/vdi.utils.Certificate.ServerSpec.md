---
layout: page
title: Data Object - ServerSpec
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.utils.Certificate.ServerSpec
Property of
     [ServerDefinition](vdi.utils.Certificate.ServerDefinition.md#field_detail), [VirtualCenterInfo](vdi.infrastructure.VirtualCenter.VirtualCenterInfo.md#field_detail), [VirtualCenterSpec](vdi.infrastructure.VirtualCenter.VirtualCenterSpec.md#field_detail), [VirtualCenterViewComposerData](vdi.infrastructure.VirtualCenter.ViewComposerData.md#field_detail)
See also
     [SecureString](vdi.util.SecureString.md)
Since 
    Horizon View 6.0

## Data Object Description 

Details needed to connect to a server. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**serverName**|  xsd:string|  Url of the server without the protocol prefix - ex. x.com.   
  
**port**|  xsd:int|  Port of the server to connect to.   


  * This property has a minimum value of 1. 
  * This property has a maximum value of 65535. 

  
**useSSL**|  xsd:boolean|  Should SSL be used when connecting to the server?   
  
**userName**|  xsd:string|  User name to use for the connection.   
  
**password**| [SecureString](vdi.util.SecureString.md)|  Password to use for the connection. Can be unset if the server got added prior to this.   


[^1]

  
**serverType**|  xsd:string|  The type of server.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"VIRTUAL_CENTER"| Denotes the virtual center server.  
"VIEW_COMPOSER"| Denotes the view Composer server.  

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

