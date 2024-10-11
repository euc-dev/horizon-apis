---
layout: page
title: Data Object - ResourcePoolData
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.utils.virtualcenter.ResourcePool.ResourcePoolData`

Property of  
> [ResourcePoolInfo](vdi.utils.virtualcenter.ResourcePool.ResourcePoolInfo.md#field_detail)

Since  
> Horizon View 6.0


## Data Object Description 

ResourcePoolData is a set of attributes for a ResourcePool retrieved from the VC. 

  * This data object must be updated as a whole.



## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**name**|  xsd:string|  ResourcePool display name   


 * This property cannot be updated.

  
**path**|  xsd:string|  ResourcePool path   


 * This property cannot be updated.

  
**type**|  xsd:string|  The type of this resource pool node. Some types may not be suitable for desktop creation.   


 * This property cannot be updated.
  * This property will be one of:  
|  Value |  Description   
---|---  
"HOST_OR_CLUSTER"| A host or cluster used as a resource pool suitable for use in desktop creation.  
"RESOURCE_POOL"| A regular resource pool suitable for use in desktop creation.  
"OTHER"| Some other resource type that cannot be used in desktop creation.  

  
**isCluster**|  xsd:boolean|  Whether the Resource Pool is a Cluster Node.  **_Since_** Horizon 7.9  


 * This property cannot be updated.

  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
