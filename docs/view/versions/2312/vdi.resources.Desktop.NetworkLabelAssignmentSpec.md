---
layout: page
title: Data Object - DesktopNetworkLabelAssignmentSpec
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.Desktop.NetworkLabelAssignmentSpec  
Property of
     [DesktopNetworkInterfaceCardSettings](vdi.resources.Desktop.NetworkInterfaceCardSettings.md#field_detail)  
See also
     [NetworkLabelId](vdi.entity.NetworkLabelId.md)  
Since 
    Horizon View 6.0

## Data Object Description 

Specification for an individual network label assignment, stipulating the label and how many times it may be assigned to machines with this spec. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**enabled**|  xsd:boolean|  Whether or not this spec is enabled. While this spec is disabled, automatic network label assigment for this desktop will skip over the network label in this spec.   


  * This property has a default value of true.

  
**networkLabel**| [NetworkLabelId](vdi.entity.NetworkLabelId.md)|  The network label id for this spec. This network label must not have any incompatibility reasons that would preclude it from automatic machine assignment.   
  
**maxLabelType**|  xsd:string|  This type specifies whether or not there is a maximum limit to the number of times this label may be assigned to machines within this spec. While this spec is enabled and unlimited, specs after this one in the NIC's network label spec list will never be used.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"UNLIMITED"| The network label assignment spec has no limit on the number of labels to assign.  
"LIMITED"| The network label assignment spec has a limited number of labels to assign.  

  
**maxLabel**|  xsd:int|  The maximum number of times this label can be assigned to a machine. Note this count only encompasses this spec. That is, this label may be used for other NICs and in other Desktops, but those assignments will not be counted towards this total. This count also does not include assignments of this label to machines not under the control of View.   


 * This property need not be set.
  * This property has a minimum value of 1. 
  * This property is required if maxLabelType is set to "LIMITED".

  
  
  
   
  
  

