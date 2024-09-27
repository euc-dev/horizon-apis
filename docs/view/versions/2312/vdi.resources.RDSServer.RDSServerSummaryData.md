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


 * This property need not be set.
 * This property cannot be updated.

  
**desktopName**|  xsd:string|  Desktop name that the RDS server (optionally) is associated with   


 * This property need not be set.
 * This property cannot be updated.

  
**farmType**|  xsd:string|  Represents the Farm type that RDS Server is part of.  **_Since_** Horizon 7.6  


  * This property has a default value of "NONE".
 * This property need not be set.
 * This property cannot be updated.
  * This property will be one of:  
|  Value |  Description   
---|---  
"AUTOMATED"| This RDS Server is part of Automated Farm.  
"MANUAL"| This RDS Server is part of Manual Farm.  
"NONE"| This RDS Server is not part of any Farm.  

  
  
  
   
  
  

