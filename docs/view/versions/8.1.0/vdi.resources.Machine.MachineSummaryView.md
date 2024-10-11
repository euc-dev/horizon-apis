---
layout: page
title: Data Object - MachineSummaryView
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.resources.Machine.MachineSummaryView`

Returned by  
> [Machine_GetSummaryView](vdi.resources.Machine.md#getSummaryView), [Machine_GetSummaryViews](vdi.resources.Machine.md#getSummaryViews)

See also  
> [MachineBase](vdi.resources.Machine.MachineBase.md), [MachineId](vdi.entity.MachineId.md), [MachineMessageSecurityData](vdi.resources.Machine.MessageSecurityData.md), [MachineSummaryData](vdi.resources.Machine.SummaryData.md)

Since  
> Horizon View 6.0


## Data Object Description 

This View includes summary data of all entities related to this Machine 

##  Queryable Data Object 

This data object is queryable using [QueryService](vdi.query.QueryService.md "QueryService"). 

Cannot filter on the following MachineSummaryView attributes: 

  * [base](vdi.resources.Machine.MachineSummaryView.md#base).[operatingSystem](vdi.resources.Machine.MachineBase.md#operatingSystem)
  * [summaryData](vdi.resources.Machine.MachineSummaryView.md#summaryData).[virtualCenter](vdi.resources.Machine.SummaryData.md#virtualCenter)



Query Privileges 

Privilege |  Description   
---|---  
MACHINE_VIEW|  is required to query MachineNamesView.   
  


## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [MachineId](vdi.entity.MachineId.md)|  The id of the Machine.   


* This property cannot be updated.

  
**base**| [MachineBase](vdi.resources.Machine.MachineBase.md)|  Basic Machine information.   
  
**messageSecurityData**| [MachineMessageSecurityData](vdi.resources.Machine.MessageSecurityData.md)|  Message security data for this machine.  **_Since_** Horizon View 6.1  
  
**summaryData**| [MachineSummaryData](vdi.resources.Machine.SummaryData.md)|  Machine summary data.   


* This property cannot be updated.

  
  
  
  
  
  
