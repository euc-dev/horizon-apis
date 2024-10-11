---
layout: page
title: Data Object - DesktopOrFarmDatastoreUsageInfo
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.utils.virtualcenter.Datastore.DesktopOrFarmDatastoreUsageInfo`

Returned by  
> [Datastore_GetUsage](vdi.utils.virtualcenter.Datastore.md#getUsage)

Since  
> Horizon 7.9


## Data Object Description 

Desktop or Farm datastore usage information. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**name**|  xsd:string|  Name of the Desktop or Farm.   


* This property cannot be updated.

  
**isFarm**|  xsd:boolean|  Represents if this is a Farm.   


  * This property has a default value of false.
* This property cannot be updated.

  
**source**|  xsd:string|  The Source or the Provisioning Type of machines in this Desktop or Farm.   
**Note:** The value FULL_CLONE is not applicable in case of farms.   


* This property cannot be updated.
  * This property will be one of:  
|  Value |  Description   
---|---  
"VIEW_COMPOSER"| View composer linked clones managed as view machines.  
"INSTANT_CLONE_ENGINE"| Instant clone engine created 'instant clones' managed as view machines.  
"FULL_CLONE"| Full Virtual Machines that are created from a vCenter Server template.  

  
**isPersistent**|  xsd:boolean|  User assignment of the Destop: Dedicated (Persistent) / Floating.   
Can be ignored in case of Farm.   


* This property need not be set.
* This property cannot be updated.

  
**usedSpaceMB**|  xsd:long|  Used capacity of the datastore (in MB) for this Desktop or Farm.   


* This property cannot be updated.

  
**otherDatastoreNames**|  xsd:string[]|  Other datastore(s) in-use for this Desktop or Farm.   


* This property need not be set.
* This property cannot be updated.

  
  
  
 
  
  
