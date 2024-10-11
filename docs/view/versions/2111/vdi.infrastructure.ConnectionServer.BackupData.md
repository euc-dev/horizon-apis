---
layout: page
title: Data Object - ConnectionServerBackupData
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.infrastructure.ConnectionServer.BackupData`

Property of  
> [ConnectionServerInfo](vdi.infrastructure.ConnectionServer.ConnectionServerInfo.md#field_detail)

Since  
> Horizon View 6.0


## Data Object Description 

Class for Ldap Backup Configuration. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**ldapBackupFrequencyTime**|  xsd:string|  Ldap Backup Frequency.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"HOUR_1"| Backup every 1 hour.  
"HOUR_6"| Backup every 6 hours.  
"HOUR_12"| Backup every 12 hours.  
"DAY_1"| Backup every 1 day.  
"DAY_2"| Backup every 2 days.  
"WEEK_1"| Backup every 1 week.  
"WEEK_2"| Backup every 2 weeks.  
"HOUR_0"| Never Backup.  

  
**ldapBackupMaxNumber**|  xsd:int|  Maximum number of backups.   


  * This property has a minimum value of 1. 

  
**ldapBackupFolder**|  xsd:string|  Location of the backup folder.   
  
**lastLdapBackupTime**|  xsd:dateTime|  Last Ldap Backup Time.  **_Since_** Horizon 7.8  


* This property need not be set.
* This property cannot be updated.

  
**lastLdapBackupStatus**|  xsd:string|  Last Ldap Backup Status.  **_Since_** Horizon 7.8  


* This property need not be set.
* This property cannot be updated.
  * This property will be one of:  
|  Value |  Description   
---|---  
"OK"| Indicates that the status is OK  
"DiskFull"| Indicates that Disk is full for LDAP to be backed up  
"UnableCreateDir"| Unable to create directory  
"ViewComposerBackupFailed"| View composer backup failed  
"ERROR_UNKNOWN"| Indicates that the error is unknown  

  
**isBackupInProgress**|  xsd:boolean|  Indicates if the backup is in progress.  **_Since_** Horizon 7.8  


  * This property has a default value of false.
* This property cannot be updated.

  
**ldapBackupTimeOffset**|  xsd:int|  Ldap backup time offset in minutes.  **_Since_** Horizon 7.8  


  * This property has a default value of 0.
  * This property has a minimum value of 0. 
  * This property has a maximum value of 59. 

  
  
  
   
  
  
