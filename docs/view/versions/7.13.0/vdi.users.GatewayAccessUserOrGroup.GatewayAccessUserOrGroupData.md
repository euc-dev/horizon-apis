---
layout: page
title: Data Object - GatewayAccessUserOrGroupData
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.users.GatewayAccessUserOrGroup.GatewayAccessUserOrGroupData`

Property of
> [GatewayAccessUserOrGroupInfo](vdi.users.GatewayAccessUserOrGroup.GatewayAccessUserOrGroupInfo.md#field_detail)

Parameter to
> [GatewayAccessUserOrGroup_Create](vdi.users.GatewayAccessUserOrGroup.md#create)

Since
> Horizon 7.4


## Data Object Description

Gateway Access user or group data object.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**sid**|  xsd:string|  Security id of this user or group.
**group**|  xsd:boolean|  Whether or not this is a group or a user. [^1]
**domain**|  xsd:string|  The domain the user or group is in. This will be the DNS name of the domain. [^1]
**name**|  xsd:string|  Name of the user or group. [^1]
**phone**|  xsd:string|  Phone number of the user or group. [^1]
**email**|  xsd:string|  Email address of the user or group. [^1]


 


[^1]: This property need not be set.