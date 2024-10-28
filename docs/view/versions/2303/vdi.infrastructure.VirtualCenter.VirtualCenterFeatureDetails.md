---
layout: page
title: Data Object - VirtualCenterFeatureDetails
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.infrastructure.VirtualCenter.VirtualCenterFeatureDetails`

Returned by
> [VirtualCenter_GetFeatureDetailsByServerDefinition](vdi.infrastructure.VirtualCenter.md#getFeatureDetailsByServerDefinition)

Since
> Horizon 8.0


## Data Object Description

Virtual Center feature details.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**storageAcceleratorStatus**|  xsd:string|  Determines the storage accelerator status of the given virtual center. [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"SA_VALIDATION_OK"</td><td>Virtual center supports View Storage Accelerator.</td></tr><tr><td>"SA_UNSUPPORTED_VC"</td><td>Virtual center does not support View Storage Accelerator.</td></tr></table>
**spaceReclamationStatus**|  xsd:string|  Determines the space reclamation status of the given virtual center. [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"SR_VALIDATION_OK"</td><td>Virtual center supports space reclamation.</td></tr><tr><td>"SR_UNSUPPORTED_VC"</td><td>Virtual center does not support space reclamation.</td></tr><tr><td>"SR_RECLAMATION_DISABLED"</td><td>The feature has been disabled for the virtual center.</td></tr><tr><td>"SR_FEATURE_DISABLED"</td><td>Space reclamation has been disabled globally.</td></tr></table>
**version**|  xsd:string|  Version of the virtual center. [^2]
 


 


[^2]: This property cannot be updated.