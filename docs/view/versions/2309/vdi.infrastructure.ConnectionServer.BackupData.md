---
layout: page
title: Data Object - ConnectionServerBackupData
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.infrastructure.ConnectionServer.BackupData`

Property of
> [ConnectionServerInfo](vdi.infrastructure.ConnectionServer.ConnectionServerInfo.md#field_detail)

Since
> Horizon View 6.0


## Data Object Description

Class for Ldap Backup Configuration.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**ldapBackupFrequencyTime**|  xsd:string|  Ldap Backup Frequency.<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"HOUR_1"</td><td>Backup every 1 hour.</td></tr><tr><td>"HOUR_6"</td><td>Backup every 6 hours.</td></tr><tr><td>"HOUR_12"</td><td>Backup every 12 hours.</td></tr><tr><td>"DAY_1"</td><td>Backup every 1 day.</td></tr><tr><td>"DAY_2"</td><td>Backup every 2 days.</td></tr><tr><td>"WEEK_1"</td><td>Backup every 1 week.</td></tr><tr><td>"WEEK_2"</td><td>Backup every 2 weeks.</td></tr><tr><td>"HOUR_0"</td><td>Never Backup.</td></tr></table>
**ldapBackupMaxNumber**|  xsd:int|  Maximum number of backups. [^8]
**ldapBackupFolder**|  xsd:string|  Location of the backup folder.
**lastLdapBackupTime**|  xsd:dateTime|  Last Ldap Backup Time.  **_Since_** Horizon 7.8 [^1] [^2]
**lastLdapBackupStatus**|  xsd:string|  Last Ldap Backup Status.  **_Since_** Horizon 7.8 [^1] [^2]<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"OK"</td><td>Indicates that the status is OK</td></tr><tr><td>"DiskFull"</td><td>Indicates that Disk is full for LDAP to be backed up</td></tr><tr><td>"UnableCreateDir"</td><td>Unable to create directory</td></tr><tr><td>"ViewComposerBackupFailed"</td><td>View composer backup failed</td></tr><tr><td>"ERROR_UNKNOWN"</td><td>Indicates that the error is unknown</td></tr></table>
**isBackupInProgress**|  xsd:boolean|  Indicates if the backup is in progress.  **_Since_** Horizon 7.8 [^5] [^2]
**ldapBackupTimeOffset**|  xsd:int|  Ldap backup time offset in minutes.  **_Since_** Horizon 7.8 [^19] [^72] [^247]
 


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^5]: This property has a default value of false.
[^8]: This property has a minimum value of 1.
[^19]: This property has a default value of 0.
[^72]: This property has a minimum value of 0.
[^247]: This property has a maximum value of 59.