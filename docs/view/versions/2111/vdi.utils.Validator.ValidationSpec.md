---
layout: page
title: Data Object - ValidationSpec
hide:
#  - navigation
  - toc
---





Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.utils.Validator.ValidationSpec`

Parameter to
> [Validator_validateName](vdi.utils.Validator.md#validateName)


## Data Object Description

Specification of the resource.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**type**|  xsd:string|  Type of resource. <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"DESKTOP"</td><td>Denotes the Desktop Pool.</td></tr><tr><td>"FARM"</td><td>Denotes the Farm.</td></tr><tr><td>"APPLICATION"</td><td>Denotes the Application Pool.</td></tr><tr><td>"MACHINE"</td><td>Denotes the Machines/RDS Hosts.</td></tr></table>
**name**|  xsd:string|  Name of the resource to be validated. [^165]


 


[^165]: If the [type](vdi.utils.Validator.ValidationSpec.md#type) is "MACHINE", then the naming pattern for the machines will be validated.