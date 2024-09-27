---
layout: page
title: Data Object - RDSServerBase
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.RDSServer.RDSServerBase  
Property of
     [RDSServerInfo](vdi.resources.RDSServer.RDSServerInfo.md#field_detail), [RDSServerSummaryView](vdi.resources.RDSServer.RDSServerSummaryView.md#field_detail)  
See also
     [AccessGroupId](vdi.entity.AccessGroupId.md), [DesktopId](vdi.entity.DesktopId.md), [FarmId](vdi.entity.FarmId.md)  
Since 
    Horizon View 6.0

## Data Object Description 

RDSServer base 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**name**|  xsd:string|  RDS Server name   


* This property need not be set.
* This property cannot be updated.

  
**description**|  xsd:string|  RDS server description   


* This property need not be set.
* This property cannot be updated.

  
**farm**| [FarmId](vdi.entity.FarmId.md)|  Farm entity ID that the RDS server (optionally) belongs to   


* This property need not be set.
* This property cannot be updated.

  
**desktop**| [DesktopId](vdi.entity.DesktopId.md)|  RDS Desktop Id that the RDS server (optionally) is associated with   


* This property need not be set.
* This property cannot be updated.

  
**accessGroup**| [AccessGroupId](vdi.entity.AccessGroupId.md)|  Access group associated with this RDS Server. If this RDS Server is in a Farm, this will be the Farm's access group. Otherwise, this will be the Root access group.   


* This property cannot be updated.

  
  
  
  
  
  

