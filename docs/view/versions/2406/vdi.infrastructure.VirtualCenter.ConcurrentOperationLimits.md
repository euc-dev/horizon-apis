---
layout: page
title: Data Object - VirtualCenterConcurrentOperationLimits
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.infrastructure.VirtualCenter.ConcurrentOperationLimits`

Property of
> [VirtualCenterInfo](vdi.infrastructure.VirtualCenter.VirtualCenterInfo.md#field_detail), [VirtualCenterSpec](vdi.infrastructure.VirtualCenter.VirtualCenterSpec.md#field_detail)

Since
> Horizon View 6.0


## Data Object Description

Virtual center and view composer limits for the number of concurrent operations.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**vcProvisioningLimit**|  xsd:int|  Maximum concurrent virtual center provisioning operations. [^206] [^8]
**vcPowerOperationsLimit**|  xsd:int|  Maximum concurrent virtual center power operations. [^207] [^8]
**viewComposerProvisioningLimit**|  xsd:int| **Deprecated.**_This property is being deprecated since View Composer will no longer be supported from Horizon version 2012 onwards._ Maximum concurrent view composer provisioning operations. [^208]
**viewComposerMaintenanceLimit**|  xsd:int|  Maximum concurrent view composer refit operations. [^208] [^8]
**instantCloneEngineProvisioningLimit**|  xsd:int|  Maximum concurrent instant clone engine provisioning operations.  **_Since_** Horizon 7.0 [^206] [^8]


 


[^8]: This property has a minimum value of 1.
[^206]: This property has a default value of 20.
[^207]: This property has a default value of 50.
[^208]: This property has a default value of 12.