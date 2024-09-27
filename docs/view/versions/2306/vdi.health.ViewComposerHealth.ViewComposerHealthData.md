---
layout: page
title: Data Object - ViewComposerHealthData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.health.ViewComposerHealth.ViewComposerHealthData  
Property of
     [ViewComposerHealthInfo](vdi.health.ViewComposerHealth.ViewComposerHealthInfo.md#field_detail)  
See also
     [VirtualCenterId](vdi.entity.VirtualCenterId.md)  
Since 
    Horizon View 6.0

## Data Object Description 

Basic data about the View Composer server. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**virtualCenters**| [VirtualCenterId[]](vdi.entity.VirtualCenterId.md)|  The VirtualCenter Ids this View Composer server is pointing to.   


  * This property is an unordered array of unique values.

  
**version**|  xsd:string|  The version of the View Composer server.   


* This property need not be set.

  
**build**|  xsd:string|  The build of the View Composer server.   


* This property need not be set.

  
**apiVersion**|  xsd:string|  The version of the View Composer API used to communicate with the View Composer server.   


* This property need not be set.

  
**minVCVersion**|  xsd:string|  The minimum Virtual Center version required for compatibility with this View Composer server.   


* This property need not be set.

  
**minESXVersion**|  xsd:string|  The minimum ESX version required for compatibility with this View Composer server.   


* This property need not be set.

  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

