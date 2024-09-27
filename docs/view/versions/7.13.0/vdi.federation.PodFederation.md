---
layout: page
title: Service - PodFederation
hide:
 #- navigation
 - toc
---

  
 
  



Java Class
    com.vmware.vdi.vlsi.binding.vdi.federation.PodFederation  
See also
     [MapEntry](vdi.util.MapEntry.md), [PodFederationInfo](vdi.federation.PodFederation.PodFederationInfo.md), [PodId](vdi.entity.PodId.md), [SecureString](vdi.util.SecureString.md), [TaskInfo](vdi.task.Task.TaskInfo.md)  
Since 
    Horizon View 6.0

  


## Service Description

The interface representing federated pods for Multi-DataCenter View. Creating and Deletion of a PodFederation are done by the system automatically. 

Methods

Methods defined in this Service   
---  
PodFederation_Eject, PodFederation_Get, PodFederation_Initialize, PodFederation_Join, PodFederation_Uninitialize, PodFederation_Unjoin, PodFederation_Update  
  



Forcefully remove a failed pod from the Multi-DataCenter View Pod Federation. This operation should only be performed against a remote pod that is down and no longer functional. If the remote pod is still operational, an unjoin operation should be used on that pod instead.   
Upon successful completion of eject operation, the ejected pod's topology will be removed from the Pod Federation. All GlobalEntitlement data that is relevant to the ejected pod will be modified.  
Eject operation can not be performed against the current pod.  


Privileges 

Privilege |  Description   
---|---  
FEDERATED_LDAP_MANAGE|  Global LDAP management is required to eject a pod from the pod federation.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [PodFederation](vdi.federation.PodFederation.md) used to make the method call.   
**pod**| [PodId](vdi.entity.PodId.md)|  PodId to be forcefully removed.   
  
  


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
[InvalidState](vdi.fault.InvalidState.md)| Thrown if this pod is not in the valid state to perform eject operation.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  


Events 

Event |  Description   
---|---  
VLSI_POD_FEDERATION_EJECT_SUCCESS|  If the specified pod was successfully ejected.   
VLSI_POD_FEDERATION_EJECT_FAILURE|  If the specified pod could not be ejected.   
  
Show WSDL type definition

  
  
  



Get the Multi-DataCenter View Pod Federation that this pod is a member of. Basic Multi-DataCenter View local Pod status is available with the lowest privileges. Other information is populated only with higher privileges. 

Privileges 

Privilege |  Description   
---|---  
FEDERATED_LDAP_VIEW|  Global LDAP read is required to access [PodFederationInfo](vdi.federation.PodFederation.PodFederationInfo.md).   
GLOBAL_CONFIG_VIEW|  Global Configuration read is required to access only [PodFederationLocalConnectionServerStatus](vdi.federation.PodFederation.LocalConnectionServerStatus.md) members of the [PodFederationInfo](vdi.federation.PodFederation.PodFederationInfo.md).   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [PodFederation](vdi.federation.PodFederation.md) used to make the method call.   
  


Return Value 

Type |  Description   
---|---  
[PodFederationInfo](vdi.federation.PodFederation.PodFederationInfo.md)| The PodFederationInfo  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



Initialize a Multi-DataCenter View Pod Federation. The pod on which this command is invoked must not be initialized already. Also, the pod on which this command is invoked must not already be part of a Pod Federation or have replica Connection Servers in transitional states.  
After being initialized, a Pod Federation is created and will have one default member site, which will have a single member pod (the local pod). The Pod Federation topology (Site, Pod, and PodEndpoint) will be automatically populated.  
A TaskInfo object is returned and can be used to track the progress and status of the initialize operation. 

Privileges 

Privilege |  Description   
---|---  
FEDERATED_LDAP_MANAGE|  Global LDAP management is required to initialize the pod federation.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [PodFederation](vdi.federation.PodFederation.md) used to make the method call.   
  


Return Value 

Type |  Description   
---|---  
[TaskInfo](vdi.task.Task.TaskInfo.md)| TaskInfo object to track progress and status  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidState](vdi.fault.InvalidState.md)| Thrown if the pod is not in the valid state to perform initialize operation.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  


Events 

Event |  Description   
---|---  
VLSI_POD_FEDERATION_TASK_TRIGGERED|  If the task to initialize the pod federation was successfully started.   
VLSI_POD_FEDERATION_OP_SUCCESS|  If the task to initialize the pod federation completed successfully.   
VLSI_POD_FEDERATION_CONCURRENT_OP|  If the task to initialize the pod federation could not complete because another pod federation task was running concurrently.   
VLSI_POD_FEDERATION_OP_FAILURE|  If the task to initialize the pod federation failed.   
  
Show WSDL type definition

  
  
  



Perform a join operation against a Multi-DataCenter View Pod Federation. At the successful completion of join operation the current pod will become a new member of the Pod Federation. The joining Pod will be assigned to a default Site and that might need to be updated (via Pod.update() api) post-join. All Pod Federation topology, including the current pod, will be populated.  
Join operation can only be performed on a pod that is not already a member of a Pod Federation. The pod the operation is performed on must not have replica Connection Servers in transitional states.  
Join operation can only be sent to a pod that is already a Pod Federation member. A TaskInfo object is returned and can be used to track the progress and status of the join operation. 

Privileges 

Privilege |  Description   
---|---  
FEDERATED_LDAP_MANAGE|  Global LDAP management is required to join the pod federation.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [PodFederation](vdi.federation.PodFederation.md) used to make the method call.   
**remotePodAddress**|  xsd:string|  the ip address or url for the remote pod.   
  
**userName**|  xsd:string|  the user name with sufficient privilege to perform a global LDAP join against the remote pod. If the userName is not supplied, password field will be ignored. In that case, the remote server must be configured to grant sufficient privilege for the computer account for the local system.   


  * This parameter need not be set.

  
**password**| [SecureString](vdi.util.SecureString.md)|  the password for the user   


  * This parameter need not be set.

  
  


Return Value 

Type |  Description   
---|---  
[TaskInfo](vdi.task.Task.TaskInfo.md)| TaskInfo object to track progress and status  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidState](vdi.fault.InvalidState.md)| Thrown if this pod is not in the valid state to perform join operation.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  


Events 

Event |  Description   
---|---  
VLSI_POD_FEDERATION_TASK_TRIGGERED|  If the task to join the pod federation was successfully started.   
VLSI_POD_FEDERATION_JOIN_SUCCESS|  If the task to join the pod federation completed successfully.   
VLSI_POD_FEDERATION_CONCURRENT_OP|  If the task to join the pod federation could not complete because another pod federation task was running concurrently.   
VLSI_POD_FEDERATION_JOIN_FAILURE|  If the task to join the pod federation failed.   
  
Show WSDL type definition

  
  
  



Tear down a Multi-Data Center View Pod Federation. The pod on which this command is invoked must be the only remaining member in the Pod Federation. Invoking uninitialize when there is more than one pod in the Pod Federation will fail. The pod the operation is performed on must not have replica Connection Servers in transitional states.  
At the completion of uninitialize, the Pod Federation topology information will be removed and it becomes a non-federated pod. A TaskInfo object is returned and can be used to track the progress and status of the uninitialize operation. 

Privileges 

Privilege |  Description   
---|---  
FEDERATED_LDAP_MANAGE|  Global LDAP management is required to uninitialize the pod federation.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [PodFederation](vdi.federation.PodFederation.md) used to make the method call.   
  


Return Value 

Type |  Description   
---|---  
[TaskInfo](vdi.task.Task.TaskInfo.md)| TaskInfo object to track progress and status  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidState](vdi.fault.InvalidState.md)| Thrown if the pod is not in the valid state to perform uninitialize operation.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  


Events 

Event |  Description   
---|---  
VLSI_POD_FEDERATION_TASK_TRIGGERED|  If the task to uninitialize the pod federation was successfully started.   
VLSI_POD_FEDERATION_OP_SUCCESS|  If the task to uninitialize the pod federation completed successfully.   
VLSI_POD_FEDERATION_CONCURRENT_OP|  If the task to uninitialize the pod federation could not complete because another pod federation task was running concurrently.   
VLSI_POD_FEDERATION_OP_FAILURE|  If the task to uninitialize the pod federation failed.   
  
Show WSDL type definition

  
  
  



Perform an unjoin operation against the Multi-DataCenter View Pod Federation. At the successful completion of the unjoin operation the current pod will become a non-federated pod that is no longer a member of the Pod Federation. All Pod Federation topology data will be removed from the current pod.  
GlobalEntitlement reference to this pod will be updated with an unjoin.   
Unjoin operation can only be performed if the current pod is not the only/last member of a Pod Federation; an uninitialize operation should be performed instead. The pod the operation is performed on must not have replica Connection Servers in transitional states.  
A TaskInfo object is returned and can be used to track the progress and status of the unjoin operation. 

Privileges 

Privilege |  Description   
---|---  
FEDERATED_LDAP_MANAGE|  Global LDAP management is required to unjoin the pod federation.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [PodFederation](vdi.federation.PodFederation.md) used to make the method call.   
  


Return Value 

Type |  Description   
---|---  
[TaskInfo](vdi.task.Task.TaskInfo.md)| TaskInfo object to track progress and status  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidState](vdi.fault.InvalidState.md)| Thrown if this pod is not in the valid state to perform unjoin operation.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  


Events 

Event |  Description   
---|---  
VLSI_POD_FEDERATION_TASK_TRIGGERED|  If the task to unjoin the pod federation was successfully started.   
VLSI_POD_FEDERATION_OP_SUCCESS|  If the task to unjoin the pod federation completed successfully.   
VLSI_POD_FEDERATION_CONCURRENT_OP|  If the task to unjoin the pod federation could not complete because another pod federation task was running concurrently.   
VLSI_POD_FEDERATION_OP_FAILURE|  If the task to unjoin the pod federation failed.   
  
Show WSDL type definition

  
  
  



Update the display name of this Multi-DataCenter View Pod Federation. 

Privileges 

Privilege |  Description   
---|---  
FEDERATED_LDAP_MANAGE|  Global LDAP management is required to update the pod federation.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [PodFederation](vdi.federation.PodFederation.md) used to make the method call.   
**updates**| [MapEntry[]](vdi.util.MapEntry.md)|  key value pairs describing attributes to be updated. Only displayName is permitted for update.   


  * This parameter is an update map based on [PodFederationInfo](vdi.federation.PodFederation.PodFederationInfo.md "PodFederationInfo"). 

  
  


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
[InvalidRequest](vdi.fault.InvalidRequest.md)| Thrown if the update map contains invalid or non-permitted fields.  
[InvalidState](vdi.fault.InvalidState.md)| Thrown if the pod is not in the valid state to perform update operation.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  


Events 

Event |  Description   
---|---  
VLSI_POD_FEDERATION_OP_SUCCESS|  If the pod federation was successfully updated.   
VLSI_POD_FEDERATION_OP_FAILURE|  If the pod federation could not be updated.   
  
Show WSDL type definition

  
  
  
  
  
  
  

