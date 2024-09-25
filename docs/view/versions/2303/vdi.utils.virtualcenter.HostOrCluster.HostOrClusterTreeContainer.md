---
layout: page
title: Data Object - HostOrClusterTreeContainer
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.utils.virtualcenter.HostOrCluster.HostOrClusterTreeContainer
Property of
     [HostOrClusterTreeNode](vdi.utils.virtualcenter.HostOrCluster.HostOrClusterTreeNode.md#field_detail)
See also
     [HostOrClusterTreeNode](vdi.utils.virtualcenter.HostOrCluster.HostOrClusterTreeNode.md)
Since 
    Horizon View 6.0

## Data Object Description 

Information about a host or cluster container. 

  * This data object must be updated as a whole.



## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**name**|  xsd:string|  Host or cluster container node display name.   


[^2]

  
**path**|  xsd:string|  Host or cluster container node path.   


[^2]

  
**type**|  xsd:string|  Type of container.   


[^2]
  * This property will be one of:  
|  Value |  Description   
---|---  
"DATACENTER"| A datacenter container, which is usually the root of the host or cluster tree.  
"FOLDER"| A folder container.  
"OTHER"| Some other container type.  

  
**children**| [HostOrClusterTreeNode[]](vdi.utils.virtualcenter.HostOrCluster.HostOrClusterTreeNode.md)|  Contents of the container. These may be hosts or clusters or further nested containers.   


[^1]
[^2]

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
