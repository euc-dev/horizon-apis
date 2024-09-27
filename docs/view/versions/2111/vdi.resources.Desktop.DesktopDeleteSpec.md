---
layout: page
title: Data Object - DesktopDeleteSpec
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.Desktop.DesktopDeleteSpec  
Parameter to
     [Desktop_Delete](vdi.resources.Desktop.md#delete)  
See also
     [DatastorePathId](vdi.entity.DatastorePathId.md)  
Since 
    Horizon View 6.0

## Data Object Description 

Specifications for deleting a desktop. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**deleteFromDisk**|  xsd:boolean|  Determines whether the machine VMs should be deleted from vCenter Server. This must always be true for linked clone desktops. This must be false for RDS and unmanaged desktops. If unset, defaults to true for linked clone desktops and false for all other desktops.   


* This property need not be set.

  
**archivePersistentDisk**|  xsd:boolean|  Determines whether to detach the persistent user disk and save it for future use. This can only be specified for linked-clone desktops with [redirectWindowsProfile](vdi.resources.Desktop.PersistentDiskSettings.md#redirectWindowsProfile) enabled, in which case it defaults to true if unset.   


* This property need not be set.

  
**archiveDatastorePath**| [DatastorePathId](vdi.entity.DatastorePathId.md)|  Determines the location where the persistent user disk will be saved for future use. If this is unset and [archivePersistentDisk](vdi.resources.Desktop.DesktopDeleteSpec.md#archivePersistentDisk) is specified, the persistent disk is archived in place.   


* This property need not be set.

  
  
  
   
  
  

