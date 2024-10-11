---
layout: page
title: Service - NetworkProxyConfiguration
hide:
 #- navigation
 - toc
---

  
   
  



Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.infrastructure.NetworkProxyConfiguration`

See also  
> [MapEntry](vdi.util.MapEntry.md), [NetworkProxyConfigurationDetail](vdi.infrastructure.NetworkProxyConfiguration.NetworkProxyConfigurationDetail.md)

Since  
> Horizon 7.3


  


## Service Description

The Network proxy configuration service interface. 

Methods

Methods defined in this Service   
---  
NetworkProxyConfiguration_Get, NetworkProxyConfiguration_Update  
  



Gets the NetworkProxyConfigurationDetail. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_VIEW|  Global configuration view privilege is required to retrieve the Network Proxy Configuration.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [NetworkProxyConfiguration](vdi.infrastructure.NetworkProxyConfiguration.md) used to make the method call.   
  


Return Value 

Type |  Description   
---|---  
[NetworkProxyConfigurationDetail](vdi.infrastructure.NetworkProxyConfiguration.NetworkProxyConfigurationDetail.md)| The NetworkProxyConfigurationDetail.  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



Updates the NetworkProxyConfigurationDetail using the update map. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_MANAGEMENT|  Global configuration management privilege is required to modify the Network Proxy Configuration.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [NetworkProxyConfiguration](vdi.infrastructure.NetworkProxyConfiguration.md) used to make the method call.   
**updates**| [MapEntry[]](vdi.util.MapEntry.md)|  The updates to apply.   


  * This parameter is an update map based on [NetworkProxyConfigurationDetail](vdi.infrastructure.NetworkProxyConfiguration.NetworkProxyConfigurationDetail.md "NetworkProxyConfigurationDetail"). 

  
  


Return Value 

Type |  Description   
---|---  
None  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  


Events 

Event |  Description   
---|---  
VLSI_NETWORK_PROXY_CONFIGURATION_UPDATED|  If all members were successfully updated, this will be sent for each updated member in the update map.   
VLSI_NETWORK_PROXY_CONFIGURATION_UPDATE_FAILED|  If any member could not be updated.   
  
Show WSDL type definition

  
  
  
  
  
  
  
