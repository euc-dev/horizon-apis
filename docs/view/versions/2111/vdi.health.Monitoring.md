---
layout: page
title: Service - Monitoring
hide:
#  - navigation
  - toc
---







Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.health.Monitoring`

See also
> [APIMetricsInfo](vdi.health.Monitoring.APIMetricsInfo.md), [DesktopCounter](vdi.health.Monitoring.DesktopCounter.md), [DesktopId](vdi.entity.DesktopId.md), [GECounter](vdi.health.Monitoring.GECounter.md), [GlobalEntitlementId](vdi.entity.GlobalEntitlementId.md), [HealthCounter](vdi.health.Monitoring.HealthCounter.md), [PodSessionCounter](vdi.health.Monitoring.PodSessionCounter.md), [SystemStatusCounter](vdi.health.Monitoring.SystemStatusCounter.md)

Since
> Horizon 7.9





## Service Description

Service for retrieving the monitoring information.

**Methods**

Methods defined in this Service:
Monitoring_GetAPIMetrics, Monitoring_GetDesktopCounters, Monitoring_GetGECounter, Monitoring_GetHealthCounters, Monitoring_GetSystemStatusCounter, Monitoring_ListPodSessionCounters




Retrieves information about the services and their counts called from this connection server.

**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Monitoring](vdi.health.Monitoring.md) used to make the method call.



**Return Value**

Type | Description
:---|:---
[APIMetricsInfo](vdi.health.Monitoring.APIMetricsInfo.md)| The number of times the APIs have been called in the connection server since the service start.



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Gets the counter for the list of desktops (except RDS desktops).

**Privileges**

Privilege | Description
:---|:---
POOL_VIEW|  Desktop read privilege with the corresponding access group permission is required to read desktops.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Monitoring](vdi.health.Monitoring.md) used to make the method call.
**ids**| [DesktopId[]](vdi.entity.DesktopId.md)|  list of desktops.




**Return Value**

Type | Description
:---|:---
[DesktopCounter[]](vdi.health.Monitoring.DesktopCounter.md)| The desktops counter.



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Gets the counter for the given global entitlement.

**Privileges**

Privilege | Description
:---|:---
FEDERATED_LDAP_VIEW|  Global LDAP read is required to read a global entitlement.
POOL_VIEW|  privilege is required to read the local desktop(s) in a global entitlement.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Monitoring](vdi.health.Monitoring.md) used to make the method call.
**id**| [GlobalEntitlementId](vdi.entity.GlobalEntitlementId.md)|  unique identifier for global entitlement




**Return Value**

Type | Description
:---|:---
[GECounter](vdi.health.Monitoring.GECounter.md)| The global entitlement counter.



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Gets the health status related information for all the components.

**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Monitoring](vdi.health.Monitoring.md) used to make the method call.



**Return Value**

Type | Description
:---|:---
[HealthCounter[]](vdi.health.Monitoring.HealthCounter.md)| The component's health counters.



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Gets the system status counter of all the categories.

**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Monitoring](vdi.health.Monitoring.md) used to make the method call.



**Return Value**

Type | Description
:---|:---
[SystemStatusCounter](vdi.health.Monitoring.SystemStatusCounter.md)| The system status counter.



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Lists the global session counts related to all Pods in the Pod Federation. This considers the sessions launched using Desktop or Application that are part of Global Entitlement and Global Application Entitlement. Following conditions apply:
 [^309] [^310]



**Privileges**

Privilege | Description
:---|:---
FEDERATED_SESSIONS_VIEW|  Global session read is required to read the information related to pods.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Monitoring](vdi.health.Monitoring.md) used to make the method call.



**Return Value**

Type | Description
:---|:---
[PodSessionCounter[]](vdi.health.Monitoring.PodSessionCounter.md)| The global session counts for all the Pods in Pod Federation.



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidState](vdi.fault.InvalidState.md)| Thrown if the Pod Federation has not been initialized.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition












 


[^309]: For those pods running on older version(before 7.12.0), the values for [numHostedSessions](vdi.health.Monitoring.PodSessionCounter.md#numHostedSessions) and [numBrokeredSessions](vdi.health.Monitoring.PodSessionCounter.md#numBrokeredSessions) will not be set.
[^310]: When there is at least one Pod running on older version(before 7.12.0), numBrokeredSessions for all the pods will not be set.