---
layout: page
title: Data Object - FarmVirtualCenterDatastoreSettings
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.resources.Farm.VirtualCenterDatastoreSettings`

Property of  
> [FarmVirtualCenterStorageSettings](vdi.resources.Farm.VirtualCenterStorageSettings.md#field_detail)

See also  
> [DatastoreId](vdi.entity.DatastoreId.md)

Since  
> Horizon View 6.2


## Data Object Description 

Settings for a Virtual Center datastore. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**datastore**| [DatastoreId](vdi.entity.DatastoreId.md)|  Id of the datastore.   
  
**storageOvercommit**|  xsd:string|  Storage overcommit determines how view places new RDS Servers on the selected datastores. With an aggressive overcommit level, view reserves less space for sparse disk growth, but fits more RDS Servers on the datastore.   


  * This property has a default value of "CONSERVATIVE".
  * This property will be one of:  
|  Value |  Description   
---|---  
"NONE"| No overcommit.  
"CONSERVATIVE"| Conservative.  
"MODERATE"| Moderate.  
"AGGRESSIVE"| Aggressive.  
"UNBOUNDED"| Unbounded.  

  
  

  
