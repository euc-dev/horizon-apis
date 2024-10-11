---
layout: page
title: Data Object - MapEntry
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.util.MapEntry`

Property of  
> [HealthCounter](vdi.health.Monitoring.HealthCounter.md#field_detail), [ImageManagementAssetBase](vdi.utils.imagemanagement.ImageManagementAsset.ImageManagementAssetBase.md#field_detail), [ImageManagementAssetSpec](vdi.utils.imagemanagement.ImageManagementAsset.ImageManagementAssetSpec.md#field_detail), [ImageManagementStreamBase](vdi.utils.imagemanagement.ImageManagementStream.ImageManagementStreamBase.md#field_detail), [ImageManagementTagBase](vdi.utils.imagemanagement.ImageManagementTag.ImageManagementTagBase.md#field_detail), [ImageManagementVersionBase](vdi.utils.imagemanagement.ImageManagementVersion.ImageManagementVersionBase.md#field_detail), [InvalidCredentials](vdi.fault.InvalidCredentials.md#field_detail), [PodFederationLocalConnectionServerStatus](vdi.federation.PodFederation.LocalConnectionServerStatus.md#field_detail), [TaskResult](vdi.task.Task.TaskResult.md#field_detail), [UnexpectedFault](vdi.fault.UnexpectedFault.md#field_detail)

Parameter to  
> [AdvancedSettings_Perform](vdi.utils.AdvancedSettings.md#perform), [AdvancedSettings_Set](vdi.utils.AdvancedSettings.md#set), [Application_Update](vdi.resources.Application.md#update), [CEIP_Update](vdi.infrastructure.CEIP.md#update), [CertificateSSOConnector_Update](vdi.infrastructure.CertificateSSOConnector.md#update), [ConnectionServer_Update](vdi.infrastructure.ConnectionServer.md#update), [Desktop_Update](vdi.resources.Desktop.md#update), [EventDatabase_Update](vdi.infrastructure.EventDatabase.md#update), [Farm_Update](vdi.resources.Farm.md#update), [GlobalApplicationEntitlement_Update](vdi.federation.GlobalApplicationEntitlement.md#update), [GlobalEntitlement_Update](vdi.federation.GlobalEntitlement.md#update), [GlobalSettings_Update](vdi.infrastructure.GlobalSettings.md#update), [ImageManagementAsset_Update](vdi.utils.imagemanagement.ImageManagementAsset.md#update), [ImageManagementStream_Update](vdi.utils.imagemanagement.ImageManagementStream.md#update), [ImageManagementTag_Update](vdi.utils.imagemanagement.ImageManagementTag.md#update), [ImageManagementVersion_Update](vdi.utils.imagemanagement.ImageManagementVersion.md#update), [InstantCloneEngineDomainAdministrator_Update](vdi.utils.InstantCloneEngineDomainAdministrator.md#update), [Machine_Update](vdi.resources.Machine.md#update), [NetworkProxyConfiguration_Update](vdi.infrastructure.NetworkProxyConfiguration.md#update), [PersistentDisk_Update](vdi.resources.PersistentDisk.md#update), [Pod_Update](vdi.federation.Pod.md#update), [PodFederation_Update](vdi.federation.PodFederation.md#update), [Policies_Update](vdi.users.Policies.md#update), [RADIUSAuthenticator_Update](vdi.infrastructure.RADIUSAuthenticator.md#update), [RDSServer_Update](vdi.resources.RDSServer.md#update), [Role_Update](vdi.users.Role.md#update), [SAMLAuthenticator_Update](vdi.infrastructure.SAMLAuthenticator.md#update), [SecondaryCredentials_Update](vdi.users.SecondaryCredentials.md#update), [SecurityServer_Update](vdi.infrastructure.SecurityServer.md#update), [Site_Update](vdi.federation.Site.md#update), [Syslog_Update](vdi.infrastructure.Syslog.md#update), [URLRedirection_Update](vdi.infrastructure.URLRedirection.md#update), [ViewComposerDomainAdministrator_Update](vdi.utils.viewcomposer.ViewComposerDomainAdministrator.md#update), [ViewComposerDomainAdministrator_UpdateByServerDefinition](vdi.utils.viewcomposer.ViewComposerDomainAdministrator.md#updateByServerDefinition), [VirtualCenter_Update](vdi.infrastructure.VirtualCenter.md#update)

Returned by  
> [AdvancedSettings_Get](vdi.utils.AdvancedSettings.md#get)


## Data Object Description 

Represents the pairing of a canonical name and a value. An array of these will be an argument to update methods. 

  * This data object must be updated as a whole.



## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**key**|  xsd:string|  Represents the canonical name of the field.   
  
**value**|  xsd:anyType|  The value of the field.   


* This property need not be set.

  
  
  

  
  
