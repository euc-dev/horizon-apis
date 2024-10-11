---
layout: page
title: Data Object - DesktopUserAssignment
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.resources.Desktop.UserAssignment`

Property of  
> [DesktopAutomatedDesktopData](vdi.resources.Desktop.AutomatedDesktopData.md#field_detail), [DesktopAutomatedDesktopSpec](vdi.resources.Desktop.AutomatedDesktopSpec.md#field_detail), [DesktopManualDesktopData](vdi.resources.Desktop.ManualDesktopData.md#field_detail), [DesktopManualDesktopSpec](vdi.resources.Desktop.ManualDesktopSpec.md#field_detail)

Since  
> Horizon View 6.0


## Data Object Description 

A machine desktop may be configured so that users have dedicated assignments or floating assignments to the machines in the desktop. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**userAssignment**|  xsd:string|  User assignment scheme.   


 * This property cannot be updated.
  * This property will be one of:  
|  Value |  Description   
---|---  
"DEDICATED"| With dedicated assignment, a user returns to the same machine at each session.  
"FLOATING"| With floating assignment, a user may return to one of the available virtual machines for the next session.  

  
**automaticAssignment**|  xsd:boolean|  Automatic assignment of a user the first time they access the machine.   


  * This property has a default value of true.
 * This property need not be set.
  * This property is required if userAssignment is set to "DEDICATED".

  
**allowMultipleAssignments**|  xsd:boolean|  Whether assignment of multiple users to a single machine is allowed. This is only applicable for dedicated pools (except Linked Clone pools) with manual user assignment. If this is true then [automaticAssignment](vdi.resources.Desktop.UserAssignment.md#automaticAssignment) should be false.  **_Since_** Horizon 7.12  


  * This property has a default value of false.
 * This property need not be set.

  
  

  
