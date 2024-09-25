---
layout: page
title: Data Object - DesktopRDSDesktopSpec
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.Desktop.RDSDesktopSpec
Property of
     [DesktopSpec](vdi.resources.Desktop.DesktopSpec.md#field_detail)
See also
     [FarmId](vdi.entity.FarmId.md)
Since 
    Horizon View 6.0

## Data Object Description 

Specification for a RDS Desktop. An RDS Desktop has a Farm that contains one or more RDS servers. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**farm**| [FarmId](vdi.entity.FarmId.md)|  Farm needed to create RDS Desktop. This Farm must not already be associated with another RDS desktop.   


[^2]

  
**cloudBrokered**|  xsd:boolean|  Indicates whether the RDS Desktop pool is brokered by cloud broker.  **_Since_** Horizon 8.2  


  * This property has a default value of false.
[^1]

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
