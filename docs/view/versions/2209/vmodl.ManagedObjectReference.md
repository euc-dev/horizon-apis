---
layout: page
title: Data Object - ManagedObjectReference
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vim.binding.vmodl.ManagedObjectReference`


## Data Object Description 

This class is used to refer to a service. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**type**|  xsd:string|  The name of the service. Allowable values are: | "AccessGroup"|  \- [AccessGroup](vdi.users.AccessGroup.md) Service.  
---|---  
"ADContainer"|  \- [ADContainer](vdi.utils.ADContainer.md) Service.  
"ADDomain"|  \- [ADDomain](vdi.utils.ADDomain.md) Service.  
"ADDomainHealth"|  \- [ADDomainHealth](vdi.health.ADDomainHealth.md) Service.  
"AdminUserOrGroup"|  \- [AdminUserOrGroup](vdi.users.AdminUserOrGroup.md) Service.  
"ADUserOrGroup"|  \- [ADUserOrGroup](vdi.users.ADUserOrGroup.md) Service.  
"AdvancedSettings"|  \- [AdvancedSettings](vdi.utils.AdvancedSettings.md) Service.  
"Application"|  \- [Application](vdi.resources.Application.md) Service.  
"ApplicationIcon"|  \- [ApplicationIcon](vdi.resources.ApplicationIcon.md) Service.  
"AuditEvent"|  \- [AuditEvent](vdi.infrastructure.AuditEvent.md) Service.  
"AuthenticationManager"|  \- [AuthenticationManager](vdi.AuthenticationManager.md) Service.  
"BaseImageSnapshot"|  \- [BaseImageSnapshot](vdi.utils.virtualcenter.BaseImageSnapshot.md) Service.  
"BaseImageVm"|  \- [BaseImageVm](vdi.utils.virtualcenter.BaseImageVm.md) Service.  
"CategoryFolder"|  \- [CategoryFolder](vdi.utils.CategoryFolder.md) Service.  
"CEIP"|  \- [CEIP](vdi.infrastructure.CEIP.md) Service.  
"Certificate"|  \- [Certificate](vdi.utils.Certificate.md) Service.  
"CertificateSSOConnector"|  \- [CertificateSSOConnector](vdi.infrastructure.CertificateSSOConnector.md) Service.  
"CertificateSSOConnectorHealth"|  \- [CertificateSSOConnectorHealth](vdi.health.CertificateSSOConnectorHealth.md) Service.  
"CertificateSSOEnrollmentServer"|  \- [CertificateSSOEnrollmentServer](vdi.infrastructure.CertificateSSOEnrollmentServer.md) Service.  
"Cluster"|  \- [Cluster](vdi.utils.Cluster.md) Service.  
"ConnectionServer"|  \- [ConnectionServer](vdi.infrastructure.ConnectionServer.md) Service.  
"ConnectionServerHealth"|  \- [ConnectionServerHealth](vdi.health.ConnectionServerHealth.md) Service.  
"CustomizationSpec"|  \- [CustomizationSpec](vdi.utils.virtualcenter.CustomizationSpec.md) Service.  
"Datacenter"|  \- [Datacenter](vdi.utils.virtualcenter.Datacenter.md) Service.  
"Datastore"|  \- [Datastore](vdi.utils.virtualcenter.Datastore.md) Service.  
"DatastorePath"|  \- [DatastorePath](vdi.utils.virtualcenter.DatastorePath.md) Service.  
"Desktop"|  \- [Desktop](vdi.resources.Desktop.md) Service.  
"DesktopHealth"|  \- [DesktopHealth](vdi.health.DesktopHealth.md) Service.  
"DesktopTask"|  \- [DesktopTask](vdi.task.DesktopTask.md) Service.  
"DiagOperation"|  \- [DiagOperation](vdi.infrastructure.DiagOperation.md) Service.  
"EntitledUserOrGroup"|  \- [EntitledUserOrGroup](vdi.users.EntitledUserOrGroup.md) Service.  
"EventDatabase"|  \- [EventDatabase](vdi.infrastructure.EventDatabase.md) Service.  
"EventDatabaseHealth"|  \- [EventDatabaseHealth](vdi.health.EventDatabaseHealth.md) Service.  
"Farm"|  \- [Farm](vdi.resources.Farm.md) Service.  
"FarmHealth"|  \- [FarmHealth](vdi.health.FarmHealth.md) Service.  
"Gateway"|  \- [Gateway](vdi.infrastructure.Gateway.md) Service.  
"GatewayAccessUserOrGroup"|  \- [GatewayAccessUserOrGroup](vdi.users.GatewayAccessUserOrGroup.md) Service.  
"GatewayHealth"|  \- [GatewayHealth](vdi.health.GatewayHealth.md) Service.  
"GlobalAccessGroup"|  \- [GlobalAccessGroup](vdi.users.GlobalAccessGroup.md) Service.  
"GlobalApplicationEntitlement"|  \- [GlobalApplicationEntitlement](vdi.federation.GlobalApplicationEntitlement.md) Service.  
"GlobalEntitlement"|  \- [GlobalEntitlement](vdi.federation.GlobalEntitlement.md) Service.  
"GlobalSessionQueryService"|  \- [GlobalSessionQueryService](vdi.users.GlobalSessionQueryService.md) Service.  
"GlobalSettings"|  \- [GlobalSettings](vdi.infrastructure.GlobalSettings.md) Service.  
"GSSAPIAuthenticator"|  \- [GSSAPIAuthenticator](vdi.infrastructure.GSSAPIAuthenticator.md) Service.  
"HostOrCluster"|  \- [HostOrCluster](vdi.utils.virtualcenter.HostOrCluster.md) Service.  
"ImageManagementAsset"|  \- [ImageManagementAsset](vdi.utils.imagemanagement.ImageManagementAsset.md) Service.  
"ImageManagementStream"|  \- [ImageManagementStream](vdi.utils.imagemanagement.ImageManagementStream.md) Service.  
"ImageManagementTag"|  \- [ImageManagementTag](vdi.utils.imagemanagement.ImageManagementTag.md) Service.  
"ImageManagementVersion"|  \- [ImageManagementVersion](vdi.utils.imagemanagement.ImageManagementVersion.md) Service.  
"InstantCloneEngineDomainAdministrator"|  \- [InstantCloneEngineDomainAdministrator](vdi.utils.InstantCloneEngineDomainAdministrator.md) Service.  
"JwtToken"|  \- [JwtToken](vdi.infrastructure.JwtToken.md) Service.  
"License"|  \- [License](vdi.infrastructure.License.md) Service.  
"LogCollector"|  \- [LogCollector](vdi.utils.logcollector.LogCollector.md) Service.  
"LogonTiming"|  \- [LogonTiming](vdi.helpdesk.LogonTiming.md) Service.  
"Machine"|  \- [Machine](vdi.resources.Machine.md) Service.  
"MessageClient"|  \- [MessageClient](vdi.utils.MessageClient.md) Service.  
"Monitoring"|  \- [Monitoring](vdi.health.Monitoring.md) Service.  
"NetworkInterfaceCard"|  \- [NetworkInterfaceCard](vdi.utils.virtualcenter.NetworkInterfaceCard.md) Service.  
"NetworkLabel"|  \- [NetworkLabel](vdi.utils.virtualcenter.NetworkLabel.md) Service.  
"NetworkProxyConfiguration"|  \- [NetworkProxyConfiguration](vdi.infrastructure.NetworkProxyConfiguration.md) Service.  
"Performance"|  \- [Performance](vdi.helpdesk.Performance.md) Service.  
"Permission"|  \- [Permission](vdi.users.Permission.md) Service.  
"PersistentDisk"|  \- [PersistentDisk](vdi.resources.PersistentDisk.md) Service.  
"PersistentDiskQueryService"|  \- [PersistentDiskQueryService](vdi.resources.PersistentDiskQueryService.md) Service.  
"Pod"|  \- [Pod](vdi.federation.Pod.md) Service.  
"PodAssignment"|  \- [PodAssignment](vdi.federation.PodAssignment.md) Service.  
"PodEndpoint"|  \- [PodEndpoint](vdi.federation.PodEndpoint.md) Service.  
"PodFederation"|  \- [PodFederation](vdi.federation.PodFederation.md) Service.  
"PodHealth"|  \- [PodHealth](vdi.health.PodHealth.md) Service.  
"Policies"|  \- [Policies](vdi.users.Policies.md) Service.  
"Privilege"|  \- [Privilege](vdi.users.Privilege.md) Service.  
"QueryService"|  \- [QueryService](vdi.query.QueryService.md) Service.  
"RADIUSAuthenticator"|  \- [RADIUSAuthenticator](vdi.infrastructure.RADIUSAuthenticator.md) Service.  
"RDSServer"|  \- [RDSServer](vdi.resources.RDSServer.md) Service.  
"RegisteredPhysicalMachine"|  \- [RegisteredPhysicalMachine](vdi.resources.RegisteredPhysicalMachine.md) Service.  
"RemoteApplication"|  \- [RemoteApplication](vdi.helpdesk.RemoteApplication.md) Service.  
"RemoteAssistantTicket"|  \- [RemoteAssistantTicket](vdi.helpdesk.RemoteAssistantTicket.md) Service.  
"RemoteProcess"|  \- [RemoteProcess](vdi.helpdesk.RemoteProcess.md) Service.  
"ResourcePool"|  \- [ResourcePool](vdi.utils.virtualcenter.ResourcePool.md) Service.  
"ResourceSettings"|  \- [ResourceSettings](vdi.utils.ResourceSettings.md) Service.  
"Role"|  \- [Role](vdi.users.Role.md) Service.  
"SAMLAuthenticator"|  \- [SAMLAuthenticator](vdi.infrastructure.SAMLAuthenticator.md) Service.  
"SAMLAuthenticatorHealth"|  \- [SAMLAuthenticatorHealth](vdi.health.SAMLAuthenticatorHealth.md) Service.  
"SecondaryCredentials"|  \- [SecondaryCredentials](vdi.users.SecondaryCredentials.md) Service.  
"SecurityServer"|  \- [SecurityServer](vdi.infrastructure.SecurityServer.md) Service.  
"SecurityServerHealth"|  \- [SecurityServerHealth](vdi.health.SecurityServerHealth.md) Service.  
"Session"|  \- [Session](vdi.users.Session.md) Service.  
"SessionStatistics"|  \- [SessionStatistics](vdi.statistics.SessionStatistics.md) Service.  
"Site"|  \- [Site](vdi.federation.Site.md) Service.  
"SpaceReclamation"|  \- [SpaceReclamation](vdi.utils.virtualcenter.SpaceReclamation.md) Service.  
"StorageAccelerator"|  \- [StorageAccelerator](vdi.utils.virtualcenter.StorageAccelerator.md) Service.  
"StorageAcceleratorHost"|  \- [StorageAcceleratorHost](vdi.utils.virtualcenter.StorageAcceleratorHost.md) Service.  
"Syslog"|  \- [Syslog](vdi.infrastructure.Syslog.md) Service.  
"Task"|  \- [Task](vdi.task.Task.md) Service.  
"UnauthenticatedAccessUser"|  \- [UnauthenticatedAccessUser](vdi.users.UnauthenticatedAccessUser.md) Service.  
"URLRedirection"|  \- [URLRedirection](vdi.infrastructure.URLRedirection.md) Service.  
"UsageStatistics"|  \- [UsageStatistics](vdi.statistics.UsageStatistics.md) Service.  
"UserEntitlement"|  \- [UserEntitlement](vdi.users.UserEntitlement.md) Service.  
"UserHomeSite"|  \- [UserHomeSite](vdi.federation.UserHomeSite.md) Service.  
"Validator"|  \- [Validator](vdi.utils.Validator.md) Service.  
"ViewClient"|  \- [ViewClient](vdi.helpdesk.ViewClient.md) Service.  
"ViewComposerDomainAdministrator"|  \- [ViewComposerDomainAdministrator](vdi.utils.viewcomposer.ViewComposerDomainAdministrator.md) Service.  
"ViewComposerHealth"|  \- [ViewComposerHealth](vdi.health.ViewComposerHealth.md) Service.  
"VirtualCenter"|  \- [VirtualCenter](vdi.infrastructure.VirtualCenter.md) Service.  
"VirtualCenterHealth"|  \- [VirtualCenterHealth](vdi.health.VirtualCenterHealth.md) Service.  
"VirtualCenterStatistics"|  \- [VirtualCenterStatistics](vdi.statistics.VirtualCenterStatistics.md) Service.  
"VirtualDisk"|  \- [VirtualDisk](vdi.utils.virtualcenter.VirtualDisk.md) Service.  
"VirtualMachine"|  \- [VirtualMachine](vdi.utils.virtualcenter.VirtualMachine.md) Service.  
"VirtualSAN"|  \- [VirtualSAN](vdi.utils.virtualcenter.VirtualSAN.md) Service.  
"VmFolder"|  \- [VmFolder](vdi.utils.virtualcenter.VmFolder.md) Service.  
"VmTemplate"|  \- [VmTemplate](vdi.utils.virtualcenter.VmTemplate.md) Service.  
"WS1Assist"|  \- [WS1Assist](vdi.helpdesk.WS1Assist.md) Service.  
  
  
**value**|  xsd:string|  The name of the service.   
  
  
  
 
  
  
