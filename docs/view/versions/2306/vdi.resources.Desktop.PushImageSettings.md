---
layout: page
title: Data Object - DesktopPushImageSettings
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.resources.Desktop.PushImageSettings`

Property of
> [DesktopImageManagementPushImageSpec](vdi.resources.Desktop.ImageManagementPushImageSpec.md#field_detail), [DesktopInstantCloneDesktopProvisioningStatusData](vdi.resources.Desktop.InstantCloneProvisioningStatusData.md#field_detail), [DesktopPushImageSpec](vdi.resources.Desktop.PushImageSpec.md#field_detail)

Since
> Horizon 7.0


## Data Object Description

Settings for the push image operation.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**startTime**|  xsd:dateTime|  When to start the operation. If unset or the time is in the past, the operation will begin immediately. [^1]
**logoffSetting**|  xsd:string|  Determines when to perform the operation on machines which have an active session.<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>FORCE_LOGOFF</td><td>Users will be forced to log off when the system is ready to operate on their virtual machines. Before being forcibly logged off, users may have a grace period in which to save their work (Global Settings).</td></tr><tr><td>WAIT_FOR_LOGOFF</td><td>Wait for connected users to disconnect before the task starts. The operation starts immediately on machines without active sessions.</td></tr></table>
**stopOnFirstError**|  xsd:boolean|  Indicates that the operation should stop on first error. [^6]
**addVirtualTPM**|  xsd:boolean|  Whether to add Virtual TPM device.  **_Since_** Horizon 7.7 [^5] [^1]
 


 


[^1]: This property need not be set.
[^5]: This property has a default value of false.
[^6]: This property has a default value of true.