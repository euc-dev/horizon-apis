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


* This property need not be set.

  
**applications**| [ApplicationId[]](vdi.entity.ApplicationId.md)|  An icon could be shared by multiple applications. Array of Application entityIds this icon represents.   


* This property need not be set.
  * This property is an unordered array of unique values.

  
  
  

  
  

