---
layout: page
title: Data Object - VirtualCenterSpec
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.infrastructure.VirtualCenter.VirtualCenterSpec`

Parameter to
> [VirtualCenter_Create](vdi.infrastructure.VirtualCenter.md#create)

See also
> [CertificateThumbprint](vdi.utils.Certificate.CertificateThumbprint.md), [ServerSpec](vdi.utils.Certificate.ServerSpec.md), [VirtualCenterConcurrentOperationLimits](vdi.infrastructure.VirtualCenter.ConcurrentOperationLimits.md), [VirtualCenterStorageAcceleratorData](vdi.infrastructure.VirtualCenter.StorageAcceleratorData.md), [VirtualCenterViewComposerData](vdi.infrastructure.VirtualCenter.ViewComposerData.md)

Since
> Horizon View 6.0


## Data Object Description

Details needed to create a virtual center instance.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**serverSpec**| [ServerSpec](vdi.utils.Certificate.ServerSpec.md)|  Details needed to connect to a virtual center server.
**description**|  xsd:string|  Human readable description of the virtual center instance. [^1] [^13]
**displayName**|  xsd:string|  Human readable display name of the virtual center instance. [^1] [^12]
**certificateOverride**| [CertificateThumbprint](vdi.utils.Certificate.CertificateThumbprint.md)|  Virtual center certificate thumbprint should the client choose to override an invalid certificate. [^1]
**disableVCInventoryLicenseAlarm**|  xsd:boolean| **Deprecated.**_This should always be set to true_ Should the virtual center inventory license alarm be disabled? [^6]
**limits**| [VirtualCenterConcurrentOperationLimits](vdi.infrastructure.VirtualCenter.ConcurrentOperationLimits.md)|  Virtual center and view composer limits for the number of concurrent operations.
**storageAcceleratorData**| [VirtualCenterStorageAcceleratorData](vdi.infrastructure.VirtualCenter.StorageAcceleratorData.md)|  Storage Accelerator configuration details.
**viewComposerData**| [VirtualCenterViewComposerData](vdi.infrastructure.VirtualCenter.ViewComposerData.md)|  View composer details.
**seSparseReclamationEnabled**|  xsd:boolean|  Is Storage Efficiency Sparse (seSparse) reclamation enabled?
**vmcDeployment**|  xsd:boolean|  Is Virtual center deployed in VMC?  **_Since_** Horizon 7.6 [^5] [^1]


 
