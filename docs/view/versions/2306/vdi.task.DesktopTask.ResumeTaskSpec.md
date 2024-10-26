---
layout: page
title: Data Object - ResumeTaskSpec
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.task.DesktopTask.ResumeTaskSpec`

Parameter to
> [DesktopTask_Resume](vdi.task.DesktopTask.md#resume)

Since
> Horizon 7.4


## Data Object Description

Specifications for resuming a task.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**retryFailedVMs**|  xsd:boolean|  Whether to restart the task for virtual machines whose task status is in error state [^5] [^1]
**stopOnError**|  xsd:boolean|  Whether to stop the task at first error [^6] [^1]
 


 


[^1]: This property need not be set.
[^5]: This property has a default value of false.
[^6]: This property has a default value of true.