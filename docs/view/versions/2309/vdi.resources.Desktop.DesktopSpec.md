---
layout: page
title: Data Object - DesktopSpec
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.resources.Desktop.DesktopSpec`

Parameter to
> [Desktop_Create](vdi.resources.Desktop.md#create)

See also
> [DesktopAutomatedDesktopSpec](vdi.resources.Desktop.AutomatedDesktopSpec.md), [DesktopBase](vdi.resources.Desktop.DesktopBase.md), [DesktopGlobalEntitlementData](vdi.resources.Desktop.GlobalEntitlementData.md), [DesktopManualDesktopSpec](vdi.resources.Desktop.ManualDesktopSpec.md), [DesktopRDSDesktopSpec](vdi.resources.Desktop.RDSDesktopSpec.md), [DesktopSettings](vdi.resources.Desktop.DesktopSettings.md)

Since
> Horizon View 6.0


## Data Object Description

Specification of a desktop.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**base**| [DesktopBase](vdi.resources.Desktop.DesktopBase.md)|  Desktop identification information.
**desktopSettings**| [DesktopSettings](vdi.resources.Desktop.DesktopSettings.md)|  Configuration settings for the desktop. Sets default and/or required values if unset. [^1]
**type**|  xsd:string|  Type of desktop.<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>AUTOMATED</td><td>An automated desktop creates virtual machines cloned from a base template or snapshot.</td></tr><tr><td>MANUAL</td><td>A manual machine desktop allows selection of existing virtual machines and addition to the desktop of available machines to connect to.</td></tr><tr><td>RDS</td><td>An RDS Desktop.</td></tr></table>
**automatedDesktopSpec**| [DesktopAutomatedDesktopSpec](vdi.resources.Desktop.AutomatedDesktopSpec.md)|  Automated desktop spec. [^1] [^29]
**manualDesktopSpec**| [DesktopManualDesktopSpec](vdi.resources.Desktop.ManualDesktopSpec.md)|  Manual desktop spec. [^1] [^26]
**rdsDesktopSpec**| [DesktopRDSDesktopSpec](vdi.resources.Desktop.RDSDesktopSpec.md)|  RDS Desktop spec. [^1] [^27]
**globalEntitlementData**| [DesktopGlobalEntitlementData](vdi.resources.Desktop.GlobalEntitlementData.md)|  Global entitlement data. Sets default values if unset. [^1]
 


 


[^1]: This property need not be set.
[^26]: This property is required if type is set to 'MANUAL'.
[^27]: This property is required if type is set to 'RDS'.
[^29]: This property is required if type is set to 'AUTOMATED'.