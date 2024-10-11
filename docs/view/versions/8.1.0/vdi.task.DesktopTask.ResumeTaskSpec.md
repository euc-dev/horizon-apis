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
**retryFailedVMs**|  xsd:boolean|  Whether to restart the task for virtual machines whose task status is in error state   


  * This property has a default value of false.
* This property need not be set.

  
**stopOnError**|  xsd:boolean|  Whether to stop the task at first error   


  * This property has a default value of true.
* This property need not be set.

  
  
  
  
  
  
