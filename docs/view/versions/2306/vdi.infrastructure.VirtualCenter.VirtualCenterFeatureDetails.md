---
layout: page
title: Data Object - VirtualCenterFeatureDetails
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.infrastructure.VirtualCenter.VirtualCenterFeatureDetails`

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
**storageAcceleratorStatus**|  xsd:string|  Determines the storage accelerator status of the given virtual center.   


* This property cannot be updated.
  * This property will be one of:  
|  Value |  Description   
---|---  
"SA_VALIDATION_OK"| Virtual center supports View Storage Accelerator.  
"SA_UNSUPPORTED_VC"| Virtual center does not support View Storage Accelerator.  

  
**spaceReclamationStatus**|  xsd:string|  Determines the space reclamation status of the given virtual center.   


* This property cannot be updated.
  * This property will be one of:  
|  Value |  Description   
---|---  
"SR_VALIDATION_OK"| Virtual center supports space reclamation.  
"SR_UNSUPPORTED_VC"| Virtual center does not support space reclamation.  
"SR_RECLAMATION_DISABLED"| The feature has been disabled for the virtual center.  
"SR_FEATURE_DISABLED"| Space reclamation has been disabled globally.  

  
**version**|  xsd:string|  Version of the virtual center.   


* This property cannot be updated.

  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
