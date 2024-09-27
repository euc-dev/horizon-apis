---
layout: page
title: Fault - InvalidState
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.fault.InvalidState  
Thrown by
     [EntitledUserOrGroup_GetGlobalSummaryView](vdi.users.EntitledUserOrGroup.md#getGlobalSummaryView), [EntitledUserOrGroup_GetGlobalSummaryViews](vdi.users.EntitledUserOrGroup.md#getGlobalSummaryViews), [GlobalApplicationEntitlement_Create](vdi.federation.GlobalApplicationEntitlement.md#create), [GlobalApplicationEntitlement_Delete](vdi.federation.GlobalApplicationEntitlement.md#delete), [GlobalApplicationEntitlement_Get](vdi.federation.GlobalApplicationEntitlement.md#get), [GlobalApplicationEntitlement_Update](vdi.federation.GlobalApplicationEntitlement.md#update), [GlobalEntitlement_Create](vdi.federation.GlobalEntitlement.md#create), [GlobalEntitlement_Delete](vdi.federation.GlobalEntitlement.md#delete), [GlobalEntitlement_Get](vdi.federation.GlobalEntitlement.md#get), [GlobalEntitlement_GetSummaryView](vdi.federation.GlobalEntitlement.md#getSummaryView), [GlobalEntitlement_GetSummaryViews](vdi.federation.GlobalEntitlement.md#getSummaryViews), [GlobalEntitlement_Update](vdi.federation.GlobalEntitlement.md#update), [License_Set](vdi.infrastructure.License.md#set), [Monitoring_ListPodSessionCounters](vdi.health.Monitoring.md#listPodSessionCounters), [PersistentDisk_Update](vdi.resources.PersistentDisk.md#update), [Pod_Get](vdi.federation.Pod.md#get), [Pod_List](vdi.federation.Pod.md#list), [Pod_Update](vdi.federation.Pod.md#update), [PodAssignment_Get](vdi.federation.PodAssignment.md#get), [PodAssignment_GetInfos](vdi.federation.PodAssignment.md#getInfos), [PodEndpoint_Get](vdi.federation.PodEndpoint.md#get), [PodEndpoint_List](vdi.federation.PodEndpoint.md#list), [PodFederation_Eject](vdi.federation.PodFederation.md#eject), [PodFederation_Initialize](vdi.federation.PodFederation.md#initialize), [PodFederation_Join](vdi.federation.PodFederation.md#join), [PodFederation_RotateKeyPair](vdi.federation.PodFederation.md#rotateKeypair), [PodFederation_Uninitialize](vdi.federation.PodFederation.md#uninitialize), [PodFederation_Unjoin](vdi.federation.PodFederation.md#unjoin), [PodFederation_Update](vdi.federation.PodFederation.md#update), [PodHealth_Get](vdi.health.PodHealth.md#get), [PodHealth_List](vdi.health.PodHealth.md#list), [QueryService_Create](vdi.query.QueryService.md#create), [Session_Disconnect](vdi.users.Session.md#disconnect), [Session_Logoff](vdi.users.Session.md#logoff), [Session_LogoffForced](vdi.users.Session.md#logoffForced), [Site_Create](vdi.federation.Site.md#create), [Site_Delete](vdi.federation.Site.md#delete), [Site_Get](vdi.federation.Site.md#get), [Site_List](vdi.federation.Site.md#list), [Site_Update](vdi.federation.Site.md#update), [UserHomeSite_Create](vdi.federation.UserHomeSite.md#create), [UserHomeSite_CreateOrUpdate](vdi.federation.UserHomeSite.md#createOrUpdate), [UserHomeSite_Delete](vdi.federation.UserHomeSite.md#delete), [UserHomeSite_DeleteUserHomeSites](vdi.federation.UserHomeSite.md#deleteUserHomeSites), [UserHomeSite_Get](vdi.federation.UserHomeSite.md#get), [UserHomeSite_GetInfos](vdi.federation.UserHomeSite.md#getInfos), [UserHomeSite_List](vdi.federation.UserHomeSite.md#list), [UserHomeSite_Resolve](vdi.federation.UserHomeSite.md#resolve), [UserHomeSite_ResolveForGAE](vdi.federation.UserHomeSite.md#resolveForGAE), [UserHomeSite_ResolveHomeSites](vdi.federation.UserHomeSite.md#resolveHomeSites), [VirtualCenter_Delete](vdi.infrastructure.VirtualCenter.md#delete)  
Extends
     [ViewRuntimeFault](vdi.fault.ViewRuntimeFault.md)  
See also
     [EntityId](vdi.EntityId.md)  
Since 
    Horizon View 6.0

## Fault Description 

Thrown if the entity is in an invalid state for the operation performed. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [EntityId](vdi.EntityId.md)|  Indicates the ID of the entity that is in an invalid state (if applicable).   


* This property need not be set.

  
Properties inherited from [ViewRuntimeFault](vdi.fault.ViewRuntimeFault.md)  
[errorMessage](vdi.fault.ViewRuntimeFault.md#errorMessage)  
Properties inherited from [RuntimeFault](vmodl.RuntimeFault.md)  
None  
Properties inherited from [MethodFault](vmodl.MethodFault.md)  
None  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

