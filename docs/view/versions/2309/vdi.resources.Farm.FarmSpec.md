---
layout: page
title: Data Object - FarmSpec
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.resources.Farm.FarmSpec`

Parameter to  
> [Farm_Create](vdi.resources.Farm.md#create)

See also  
> [FarmAutomatedFarmSpec](vdi.resources.Farm.AutomatedFarmSpec.md), [FarmData](vdi.resources.Farm.FarmData.md), [FarmManualFarmSpec](vdi.resources.Farm.ManualFarmSpec.md)

Since  
> Horizon View 6.2


## Data Object Description 

Farm spec data needed to create a Farm 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**type**|  xsd:string|  Type of farm.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"AUTOMATED"| An automated farm creates RDS Servers cloned from a snapshot.  
"MANUAL"| A manual farm allows selection and addition of existing RDS Servers to the farm.  

  
**data**| [FarmData](vdi.resources.Farm.FarmData.md)|  Farm data   
  
**automatedFarmSpec**| [FarmAutomatedFarmSpec](vdi.resources.Farm.AutomatedFarmSpec.md)|  Automated farm spec.   


 * This property need not be set.
  * This property is required if type is set to "AUTOMATED".

  
**manualFarmSpec**| [FarmManualFarmSpec](vdi.resources.Farm.ManualFarmSpec.md)|  Manual Farm spec   


 * This property need not be set.
  * This property is required if type is set to "MANUAL".

  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
