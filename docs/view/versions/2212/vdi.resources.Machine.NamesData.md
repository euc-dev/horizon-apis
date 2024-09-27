---
layout: page
title: Data Object - MachineNamesData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.Machine.NamesData  
Property of
     [MachineNamesView](vdi.resources.Machine.MachineNamesView.md#field_detail)  
Since 
    Horizon View 6.0

## Data Object Description 

Names of other entities related to this Machine. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**desktopName**|  xsd:string|  The name of the Desktop to which this Machine belongs.   


* This property cannot be updated.

  
**userName**|  xsd:string| **Deprecated.**_use[userNames](vdi.resources.Machine.NamesData.md#userNames) instead. This field will not be populated for machine belonging to pool which support multiple assignment. _ The name of the user to whom this Machine has been assigned.  
  


* This property need not be set.
* This property cannot be updated.

  
**userNames**|  xsd:string[]|  Names of the users assigned to this Machine. This cannot be a group.  **_Since_** Horizon 7.12  


* This property need not be set.
* This property cannot be updated.

  
  
  
  
  
  

