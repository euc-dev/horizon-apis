---
layout: page
title: Data Object - ValidationSpec
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.utils.Validator.ValidationSpec
Parameter to
     [Validator_validateName](vdi.utils.Validator.md#validateName)
Since 
    Horizon View 6.0

## Data Object Description 

Specification of the resource. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**type**|  xsd:string|  Type of resource.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"DESKTOP"| Denotes the Desktop Pool.  
"FARM"| Denotes the Farm.  
"APPLICATION"| Denotes the Application Pool.  
"MACHINE"| Denotes the Machines/RDS Hosts.  

  
**name**|  xsd:string|  Name of the resource to be validated. 
* If the [type](vdi.utils.Validator.ValidationSpec.md#type) is "MACHINE", then the naming pattern for the machines will be validated.
  
  
  

  

