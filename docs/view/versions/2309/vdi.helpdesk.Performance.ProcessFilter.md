---
layout: page
title: Data Object - ProcessFilter
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.helpdesk.Performance.ProcessFilter`

Parameter to
> [Performance_GetProcessPerformanceData](vdi.helpdesk.Performance.md#getProcessPerformanceData)

Since
> Horizon 7.6


## Data Object Description

The filter for processes

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**processSessionFilter**|  xsd:string|  Filter process by process session info [^1] [^2]<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"CURRENT_USER_SESSION"</td><td>The processes which run in the current user session</td></tr><tr><td>"SYSTEM_AND_CURRENT_USER_SESSION"</td><td>The union of the system processes and current user session processes.</td></tr></table>
 


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.