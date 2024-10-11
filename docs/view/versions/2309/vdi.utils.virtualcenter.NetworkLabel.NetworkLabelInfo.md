---
layout: page
title: Data Object - NetworkLabelInfo
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.utils.virtualcenter.NetworkLabel.NetworkLabelInfo`

Returned by  
> [NetworkLabel_ListByHostOrCluster](vdi.utils.virtualcenter.NetworkLabel.md#listByHostOrCluster), [NetworkLabel_ListByNetworkLabelSpec](vdi.utils.virtualcenter.NetworkLabel.md#listByNetworkLabelSpec)

See also  
> [NetworkLabelData](vdi.utils.virtualcenter.NetworkLabel.NetworkLabelData.md), [NetworkLabelId](vdi.entity.NetworkLabelId.md)

Since  
> Horizon View 6.0


## Data Object Description 

Network label information from VC. 

  * This data object must be updated as a whole.



## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [NetworkLabelId](vdi.entity.NetworkLabelId.md)|  Network label id.   


 * This property cannot be updated.

  
**data**| [NetworkLabelData](vdi.utils.virtualcenter.NetworkLabel.NetworkLabelData.md)|  Network label data.   


 * This property cannot be updated.

  
**refId**|  xsd:string|  Reference ID used for this network label.  **_Since_** Horizon 8.1  


 * This property need not be set.
 * This property cannot be updated.

  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
