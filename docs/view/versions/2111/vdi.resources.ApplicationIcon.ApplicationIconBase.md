---
layout: page
title: Data Object - ApplicationIconBase
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.ApplicationIcon.ApplicationIconBase
Property of
     [ApplicationIconInfo](vdi.resources.ApplicationIcon.ApplicationIconInfo.md#field_detail), [ApplicationIconSpec](vdi.resources.ApplicationIcon.ApplicationIconSpec.md#field_detail)
See also
     [ApplicationId](vdi.entity.ApplicationId.md)
Since 
    Horizon View 6.0

## Data Object Description 

Following class represents various attributes of an Application Icon. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**data**|  xsd:base64Binary|  Icon image data   
  
**width**|  xsd:long|  Icon width   
  
**height**|  xsd:long|  Icon height   
  
**iconHash**|  xsd:string|  Icon hash, to enable quick icon lookup   
  
**iconSource**|  xsd:string|  Source of the ApplicationIcon. If icon is from RDS Agent, iconSource will be Unset. Allowed Values: broker  **_Since_** Horizon 7.1  


[^1]

  
**applications**| [ApplicationId[]](vdi.entity.ApplicationId.md)|  An icon could be shared by multiple applications. Array of Application entityIds this icon represents.   


[^1]
  * This property is an unordered array of unique values.

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
