---
layout: page
title: Data Object - PartnerDesktopSettings
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.resources.Desktop.PartnerDesktopSettings`

Property of
> [DesktopAutomatedDesktopData](vdi.resources.Desktop.AutomatedDesktopData.md#field_detail), [DesktopAutomatedDesktopSpec](vdi.resources.Desktop.AutomatedDesktopSpec.md#field_detail), [DesktopProvisioningView](vdi.resources.Desktop.DesktopProvisioningView.md#field_detail)

See also
> [AWSCoreDesktopSettings](vdi.resources.Desktop.AWSCoreDesktopSettings.md)

Since
> Horizon 8.13


## Data Object Description

Specification for an partner desktop.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**capacityProviderId**|  xsd:string|  ID of the capacity provider
**awsCoreDesktopSettings**| [AWSCoreDesktopSettings](vdi.resources.Desktop.AWSCoreDesktopSettings.md)|  Specification for an AWS core desktop. [^1]


 


[^1]: This property need not be set.