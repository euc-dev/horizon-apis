---
layout: page
title: Data Object - DesktopOrFarmDatastoreUsageInfo
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.utils.virtualcenter.Datastore.DesktopOrFarmDatastoreUsageInfo
Returned by
     [Datastore_GetUsage](vdi.utils.virtualcenter.Datastore.md#getUsage)
Since 
    Horizon 7.9

## Data Object Description 

Desktop or Farm datastore usage information. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**name**|  xsd:string|  Name of the Desktop or Farm.   


[^2]

  
**isFarm**|  xsd:boolean|  Represents if this is a Farm.   


  * This property has a default value of false.
[^2]

  
**source**|  xsd:string|  The Source or the Provisioning Type of machines in this Desktop or Farm.   
**Note:** The value FULL_CLONE is not applicable in case of farms.   


[^2]
  * This property will be one of:  
|  Value |  Description   
---|---  
"VIEW_COMPOSER"| View composer linked clones managed as view machines.  
"INSTANT_CLONE_ENGINE"| Instant clone engine created 'instant clones' managed as view machines.  
"FULL_CLONE"| Full Virtual Machines that are created from a vCenter Server template.  

  
**isPersistent**|  xsd:boolean|  User assignment of the Destop: Dedicated (Persistent) / Floating.   
Can be ignored in case of Farm.   


[^1]
[^2]

  
**usedSpaceMB**|  xsd:long|  Used capacity of the datastore (in MB) for this Desktop or Farm.   


[^2]

  
**otherDatastoreNames**|  xsd:string[]|  Other datastore(s) in-use for this Desktop or Farm.   


[^1]
[^2]

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

