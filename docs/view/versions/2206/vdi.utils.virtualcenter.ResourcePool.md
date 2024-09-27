---
layout: page
title: Service - ResourcePool
hide:
 #- navigation
 - toc
---

  
  
  



Java Class
    com.vmware.vdi.vlsi.binding.vdi.utils.virtualcenter.ResourcePool  
See also
     [HostOrClusterId](vdi.entity.HostOrClusterId.md), [ResourcePoolInfo](vdi.utils.virtualcenter.ResourcePool.ResourcePoolInfo.md)  
Since 
    Horizon View 6.0

  


## Service Description

The service for fetching ResourcePools from VirtualCenter. 

Methods

Methods defined in this Service   
---  
ResourcePool_GetResourcePoolTree  
  



Gets the given host or cluster's resource pool tree from VC. Nodes of this tree may be suitable for use in desktop creation. Requires at least one of the listed privileges. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_VIEW|  privilege is required to get the ResourcePoolInfo.   
VC_CONFIG_VIEW|  privilege is required to get the ResourcePoolInfo.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ResourcePool](vdi.utils.virtualcenter.ResourcePool.md) used to make the method call.   
**hostOrCluster**| [HostOrClusterId](vdi.entity.HostOrClusterId.md)|  The host or cluster from which to get the resource pool tree   
  
  


Return Value 

Type |  Description   
---|---  
[ResourcePoolInfo](vdi.utils.virtualcenter.ResourcePool.ResourcePoolInfo.md)| ResourcePoolInfo the root resource pool of the tree  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  
  
  
  
  

