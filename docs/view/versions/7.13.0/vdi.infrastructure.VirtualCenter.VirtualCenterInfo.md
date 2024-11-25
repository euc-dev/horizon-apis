---
layout: page
title: Data Object - VirtualCenterInfo
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.infrastructure.VirtualCenter.VirtualCenterInfo`

Returned by
> [VirtualCenter_Get](vdi.infrastructure.VirtualCenter.md#get), [VirtualCenter_List](vdi.infrastructure.VirtualCenter.md#list)

See also
> [CertificateThumbprint](vdi.utils.Certificate.CertificateThumbprint.md), [ServerSpec](vdi.utils.Certificate.ServerSpec.md), [VirtualCenterConcurrentOperationLimits](vdi.infrastructure.VirtualCenter.ConcurrentOperationLimits.md), [VirtualCenterId](vdi.entity.VirtualCenterId.md), [VirtualCenterStorageAcceleratorData](vdi.infrastructure.VirtualCenter.StorageAcceleratorData.md), [VirtualCenterViewComposerData](vdi.infrastructure.VirtualCenter.ViewComposerData.md)

Since
> Horizon View 6.0


## Data Object Description

Top-level object describing a virtual center instance.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**id**| [VirtualCenterId](vdi.entity.VirtualCenterId.md)|  Client reference to a specific virtual center instance.
**serverSpec**| [ServerSpec](vdi.utils.Certificate.ServerSpec.md)|  Details needed to connect to a virtual center server.
**description**|  xsd:string|  Human readable description of the virtual center instance. [^1] [^13]
**displayName**|  xsd:string|  Human readable display name of the virtual center instance. [^1] [^12]
**version**|  xsd:string|  Virtual center version.  **_Since_** Horizon 7.2 [^1]
**instanceUuid**|  xsd:string|  Virtual center instanceUuid.  **_Since_** Horizon 7.4 [^1]
**certificateOverride**| [CertificateThumbprint](vdi.utils.Certificate.CertificateThumbprint.md)|  Virtual center certificate thumbprint should the client choose to override an invalid certificate. [^1]
**limits**| [VirtualCenterConcurrentOperationLimits](vdi.infrastructure.VirtualCenter.ConcurrentOperationLimits.md)|  Virtual center and view composer limits for the number of concurrent operations.
**storageAcceleratorData**| [VirtualCenterStorageAcceleratorData](vdi.infrastructure.VirtualCenter.StorageAcceleratorData.md)|  Storage Accelerator configuration details.
**viewComposerData**| [VirtualCenterViewComposerData](vdi.infrastructure.VirtualCenter.ViewComposerData.md)|  View composer details.
**seSparseReclamationEnabled**|  xsd:boolean|  Is Storage Efficiency Sparse (seSparse) reclamation enabled?
**enabled**|  xsd:boolean|  Is the virtual center enabled?
**vmcDeployment**|  xsd:boolean|  Is Virtual center deployed in VMC?  **_Since_** Horizon 7.6 [^5] [^1]
**isDeletable**|  xsd:boolean|  If true, Virtual Center can be deletable otherwise not. A Virtual Center cannot be deleted if there is atleast one Desktop and/or Farm associated with it.  **_Since_** Horizon 7.8 [^2]
**maintenanceMode**|  xsd:boolean|  If maintenance or upgrade task is scheduled on Virtual center or hosts. For example, set this flag when upgrading hosts using VMware vSphere Update Manager (VUM).  **_Since_** Horizon 7.13 [^5] [^1]
**hasVirtualTPMPools**|  xsd:boolean|  If there is any instant clone Desktop pool associated with this Virtual Center which has addVirtualTPM set.  **_Since_** Horizon 7.13 [^5] [^1] [^2]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^5]: This property has a default value of false.
[^12]: This property has a maximum length of 256 characters.
[^13]: This property has a maximum length of 1024 characters.