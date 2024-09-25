---
layout: page
title: Data Object - ApplicationIconSummaryBase
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.ApplicationIcon.ApplicationIconSummaryBase
Property of
     [ApplicationIconSummaryView](vdi.resources.ApplicationIcon.ApplicationIconSummaryView.md#field_detail)
Since 
    Horizon 7.5

## Data Object Description 

Application Summary base that represents the metadata of the application icon. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**width**|  xsd:long|  Icon width   
  
**height**|  xsd:long|  Icon height   
  
**iconHash**|  xsd:string|  Icon hash, to enable quick icon lookup   
  
**iconSource**|  xsd:string|  Source of the ApplicationIcon. If icon is from RDS Agent, iconSource will be Unset.   


[^1]
  * This property will be one of:  
|  Value |  Description   
---|---  
"BROKER"| supported ApplicationIcon sources  

  
  

  

