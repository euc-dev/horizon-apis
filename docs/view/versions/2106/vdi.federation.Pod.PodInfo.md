---
layout: page
title: Data Object - PodInfo
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.federation.Pod.PodInfo`

Returned by  
> [Pod_Get](vdi.federation.Pod.md#get), [Pod_List](vdi.federation.Pod.md#list)

See also  
> [GlobalApplicationEntitlementId](vdi.entity.GlobalApplicationEntitlementId.md), [GlobalEntitlementId](vdi.entity.GlobalEntitlementId.md), [PodEndpointId](vdi.entity.PodEndpointId.md), [PodId](vdi.entity.PodId.md), [SiteId](vdi.entity.SiteId.md)

Since  
> Horizon View 6.0


## Data Object Description 

PodInfo contain information about a pod in a Multi-DataCenter View Pod Federation.  


## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [PodId](vdi.entity.PodId.md)|  Unique identifier for a Pod   


* This property cannot be updated.

  
**site**| [SiteId](vdi.entity.SiteId.md)|  The Id of the site this pod belongs to   
  
**displayName**|  xsd:string|  Display name for the pod.   


  * This property has a maximum length of 64 characters. 

  
**description**|  xsd:string|  Detailed description of the pod.   


* This property need not be set.
  * This property has a maximum length of 1024 characters. 

  
**localPod**|  xsd:boolean|  Indicates whether this is the local pod that the Pod service request is made. Only one pod out of the PodFederation will return true.   


* This property cannot be updated.

  
**endpoints**| [PodEndpointId[]](vdi.entity.PodEndpointId.md)|  The list of pod endpoints within this pod. An endpoint is basically a connection server in that pod. This list is maintained by the system and is not modifiable.   


* This property need not be set.
* This property cannot be updated.

  
**activeGlobalEntitlements**| [GlobalEntitlementId[]](vdi.entity.GlobalEntitlementId.md)|  The list of Global Entitlements with mappings to desktops in this pod. This list is maintained by the system and is not modifiable.   


* This property need not be set.
* This property cannot be updated.

  
**activeGlobalApplicationEntitlements**| [GlobalApplicationEntitlementId[]](vdi.entity.GlobalApplicationEntitlementId.md)|  The list of Global Application Entitlements with mappings to Applications in this pod. This list is maintained by the system and is not modifiable.  **_Since_** Horizon View 6.2  


* This property need not be set.
* This property cannot be updated.

  
**cloudManaged**|  xsd:boolean|  Indicates whether this pod is managed from cloud.  **_Since_** Horizon 7.9  


* This property need not be set.

  
**refId**|  xsd:string|  Reference ID for this pod.  **_Since_** Horizon 8.1  


* This property need not be set.
* This property cannot be updated.

  
  
  

  
  
