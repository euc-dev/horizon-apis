---
layout: page
title: Data Object - RDSServerSummaryData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.RDSServer.RDSServerSummaryData
Property of
     [RDSServerSummaryView](vdi.resources.RDSServer.RDSServerSummaryView.md#field_detail)
Since 
    Horizon View 6.0

## Data Object Description 

RDSServerSummaryData 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**farmName**|  xsd:string|  Farm name that the RDS server (optionally) belongs to   


[^1]
[^2]

  
**desktopName**|  xsd:string|  Desktop name that the RDS server (optionally) is associated with   


[^1]
[^2]

  
**farmType**|  xsd:string|  Represents the Farm type that RDS Server is part of.  **_Since_** Horizon 7.6  


  * This property has a default value of "NONE".
[^1]
[^2]
  * This property will be one of:  
|  Value |  Description   
---|---  
"AUTOMATED"| This RDS Server is part of Automated Farm.  
"MANUAL"| This RDS Server is part of Manual Farm.  
"NONE"| This RDS Server is not part of any Farm.  

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
