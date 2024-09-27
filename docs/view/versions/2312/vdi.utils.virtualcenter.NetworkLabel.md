---
layout: page
title: Service - NetworkLabel
hide:
 #- navigation
 - toc
---

  
 
  



Java Class
    com.vmware.vdi.vlsi.binding.vdi.utils.virtualcenter.NetworkLabel  
See also
     [HostOrClusterId](vdi.entity.HostOrClusterId.md), [NetworkLabelInfo](vdi.utils.virtualcenter.NetworkLabel.NetworkLabelInfo.md), [NetworkLabelSpec](vdi.utils.virtualcenter.NetworkLabel.NetworkLabelSpec.md)  
Since 
    Horizon View 6.0

  


## Service Description

The service for fetching network labels from VirtualCenter.   
Each port group is identified by a network label, which is unique to the current host. Network labels are used to make virtual machine configuration portable across hosts. All port groups in a datacenter that are physically connected to the same network (in the sense that each can receive broadcasts from the others) are given the same label. Conversely, if two port groups cannot receive broadcasts from each other, they have distinct labels.   
Each network interface card on a virtual machine can be assigned a network label to specify its port group. Network labels may serve as shorthand for settings like VLAN tag and DHCP IP address range information. 

Methods

Methods defined in this Service   
---  
NetworkLabel_ListByHostOrCluster, NetworkLabel_ListByNetworkLabelSpec  
  



Returns all network labels on the given host or cluster that may be suitable for configuration with a desktop's network interface card. This includes both standard and distributed virtual switch network label types. Requires at least one of the listed privileges. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_VIEW|  privilege is required to get the NetworkLabelInfos.   
VC_CONFIG_VIEW|  privilege is required to get the NetworkLabelInfos.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [NetworkLabel](vdi.utils.virtualcenter.NetworkLabel.md) used to make the method call.   
**cluster**| [HostOrClusterId](vdi.entity.HostOrClusterId.md)|  The cluster id   
  
  


Return Value 

Type |  Description   
---|---  
[NetworkLabelInfo[]](vdi.utils.virtualcenter.NetworkLabel.NetworkLabelInfo.md)| An array of NetworkLabelInfos  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



Returns all the network labels on the given host or cluster by filtering on the network type that may be suitable for configuration with a desktop's network interface card. Requires at least one of the listed privileges. 

Privileges 

Privilege |  Description   
---|---  
VC_CONFIG_VIEW|  privilege is required to get the NetworkLabelInfos.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [NetworkLabel](vdi.utils.virtualcenter.NetworkLabel.md) used to make the method call.   
**spec**| [NetworkLabelSpec](vdi.utils.virtualcenter.NetworkLabel.NetworkLabelSpec.md)|  NetworkLabelSpec   
  
  


Return Value 

Type |  Description   
---|---  
[NetworkLabelInfo[]](vdi.utils.virtualcenter.NetworkLabel.NetworkLabelInfo.md)| An array of NetworkLabelInfos  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  
  
  
  
  

