---
layout: page
title: Data Object - DesktopNonPersistentDiskSettings
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.resources.Desktop.NonPersistentDiskSettings`

Property of
> [DesktopViewComposerStorageSettings](vdi.resources.Desktop.ViewComposerStorageSettings.md#field_detail)

Since
> Horizon View 6.0


## Data Object Description

Settings related to a non persistent disk. Changes to this disk are discarded when the user's session ends.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**redirectDisposableFiles**|  xsd:boolean|  Redirect disposable files to a non-persistent disk that will be deleted automatically when a user's session ends. Note(s) :- [^87] [^6] [^2]
**diskSizeMB**|  xsd:int|  Size of the non persistent disk in MB. [^55] [^1] [^56] [^60]
**diskDriveLetter**|  xsd:string|  Non persistent disk drive letter. This must be different than [diskDriveLetter](vdi.resources.Desktop.PersistentDiskSettings.md#diskDriveLetter) if set. [^58] [^1] [^59] [^60]
 


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^6]: This property has a default value of true.
[^55]: This property has a default value of 4096.
[^56]: This property has a minimum value of 512.
[^58]: This property has a default value of Auto.
[^59]: This property must be single letters from D to Z or the word Auto.
[^60]: This property is required if redirectDisposableFiles is set to true.
[^87]: For Instant clone desktops, this setting can only be set to false.