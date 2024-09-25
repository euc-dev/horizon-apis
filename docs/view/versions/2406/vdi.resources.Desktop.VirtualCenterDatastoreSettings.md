---
layout: page
title: Data Object - DesktopVirtualCenterDatastoreSettings
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.Desktop.VirtualCenterDatastoreSettings
Property of
     [DesktopPersistentDiskSettings](vdi.resources.Desktop.PersistentDiskSettings.md#field_detail), [DesktopVirtualCenterStorageSettings](vdi.resources.Desktop.VirtualCenterStorageSettings.md#field_detail)
See also
     [DatastoreId](vdi.entity.DatastoreId.md)
Since 
    Horizon View 6.0

## Data Object Description 

Settings for a Virtual Center datastore. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**datastore**| [DatastoreId](vdi.entity.DatastoreId.md)|  Id of the datastore.   
  
**sdrsCluster**|  xsd:boolean|  Set to true if [datastore](vdi.resources.Desktop.VirtualCenterDatastoreSettings.md#datastore) represents a Storage DRS clsuter. Only applicable for full clone desktops.  **_Since_** Horizon 7.2  


  * This property has a default value of false.
[^1]

  
**storageOvercommit**|  xsd:string|  Storage overcommit determines how view places new VMs on the selected datastores. With an aggressive overcommit level, view reserves less space for sparse disk growth, but fits more VMs on the datastore. Note(s) :-  


  * For Instant clone desktops, this setting can only be set to UNBOUNDED.

  


  * This property has a default value of "CONSERVATIVE".
  * This property will be one of:  
|  Value |  Description   
---|---  
"NONE"| No overcommit.  
"CONSERVATIVE"| Conservative.  
"MODERATE"| Moderate.  
"AGGRESSIVE"| Aggressive.  
"UNBOUNDED"| Unbounded.  

  
  

  

