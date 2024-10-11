---
layout: page
title: Data Object - ServerDefinition
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.utils.Certificate.ServerDefinition`

Parameter to  
> [SpaceReclamation_IsSupportedByServerDefinition](vdi.utils.virtualcenter.SpaceReclamation.md#isSupportedByServerDefinition), [StorageAccelerator_IsSupportedByServerDefinition](vdi.utils.virtualcenter.StorageAccelerator.md#isSupportedByServerDefinition), [StorageAcceleratorHost_ListByServerDefinition](vdi.utils.virtualcenter.StorageAcceleratorHost.md#listByServerDefinition), [ViewComposerDomainAdministrator_CreateByServerDefinition](vdi.utils.viewcomposer.ViewComposerDomainAdministrator.md#createByServerDefinition), [ViewComposerDomainAdministrator_DeleteByServerDefinition](vdi.utils.viewcomposer.ViewComposerDomainAdministrator.md#deleteByServerDefinition), [ViewComposerDomainAdministrator_ListByServerDefinition](vdi.utils.viewcomposer.ViewComposerDomainAdministrator.md#listByServerDefinition), [ViewComposerDomainAdministrator_UpdateByServerDefinition](vdi.utils.viewcomposer.ViewComposerDomainAdministrator.md#updateByServerDefinition), [VirtualCenter_GetFeatureDetailsByServerDefinition](vdi.infrastructure.VirtualCenter.md#getFeatureDetailsByServerDefinition)

See also  
> [CertificateThumbprint](vdi.utils.Certificate.CertificateThumbprint.md), [ServerSpec](vdi.utils.Certificate.ServerSpec.md)

Since  
> Horizon View 6.0


## Data Object Description 

Details needed to connect to a server, with optional certificate. 

  * This data object must be updated as a whole.



## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**serverSpec**| [ServerSpec](vdi.utils.Certificate.ServerSpec.md)|  Details needed to connect to a server   
  
**certificateThumbprint**| [CertificateThumbprint](vdi.utils.Certificate.CertificateThumbprint.md)|  Certificate thumbprint and corresponding algorithm. If not specified, will assume the certificate has been accepted. If specified, will accept the certificate just for this operation.   


 * This property need not be set.

  
  
  
   
  
  
