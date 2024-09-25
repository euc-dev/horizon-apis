---
layout: page
title: Data Object - VirtualCenterInfo
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.infrastructure.VirtualCenter.VirtualCenterInfo
Returned by
     [VirtualCenter_Get](vdi.infrastructure.VirtualCenter.md#get), [VirtualCenter_List](vdi.infrastructure.VirtualCenter.md#list)
See also
     [CertificateThumbprint](vdi.utils.Certificate.CertificateThumbprint.md), [ServerSpec](vdi.utils.Certificate.ServerSpec.md), [VirtualCenterConcurrentOperationLimits](vdi.infrastructure.VirtualCenter.ConcurrentOperationLimits.md), [VirtualCenterId](vdi.entity.VirtualCenterId.md), [VirtualCenterStorageAcceleratorData](vdi.infrastructure.VirtualCenter.StorageAcceleratorData.md), [VirtualCenterViewComposerData](vdi.infrastructure.VirtualCenter.ViewComposerData.md)
Since 
    Horizon View 6.0

## Data Object Description 

Top-level object describing a virtual center instance. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [VirtualCenterId](vdi.entity.VirtualCenterId.md)|  Client reference to a specific virtual center instance.   
  
**serverSpec**| [ServerSpec](vdi.utils.Certificate.ServerSpec.md)|  Details needed to connect to a virtual center server.   
  
**description**|  xsd:string|  Human readable description of the virtual center instance.   


[^1]
  * This property has a maximum length of 1024 characters. 

  
**displayName**|  xsd:string|  Human readable display name of the virtual center instance.   


[^1]
  * This property has a maximum length of 256 characters. 

  
**version**|  xsd:string|  Virtual center version.  **_Since_** Horizon 7.2  


[^1]

  
**instanceUuid**|  xsd:string|  Virtual center instanceUuid.  **_Since_** Horizon 7.4  


[^1]

  
**certificateOverride**| [CertificateThumbprint](vdi.utils.Certificate.CertificateThumbprint.md)|  Virtual center certificate thumbprint should the client choose to override an invalid certificate.   


[^1]

  
**limits**| [VirtualCenterConcurrentOperationLimits](vdi.infrastructure.VirtualCenter.ConcurrentOperationLimits.md)|  Virtual center and view composer limits for the number of concurrent operations.   
  
**storageAcceleratorData**| [VirtualCenterStorageAcceleratorData](vdi.infrastructure.VirtualCenter.StorageAcceleratorData.md)|  Storage Accelerator configuration details.   
  
**viewComposerData**| [VirtualCenterViewComposerData](vdi.infrastructure.VirtualCenter.ViewComposerData.md)|  View composer details.   
  
**seSparseReclamationEnabled**|  xsd:boolean|  Is Storage Efficiency Sparse (seSparse) reclamation enabled?   
  
**enabled**|  xsd:boolean|  Is the virtual center enabled?   
  
**vmcDeployment**|  xsd:boolean| **Deprecated.**_This property is no longer in use for Horizon Components. The deployment type can now be checked with the[deploymentType](vdi.infrastructure.VirtualCenter.VirtualCenterInfo.md#deploymentType) field. For VMC deployment [deploymentType](vdi.infrastructure.VirtualCenter.VirtualCenterInfo.md#deploymentType) will be set to AWS. _ Is Virtual center deployed in VMC?  **_Since_** Horizon 7.6  


  * This property has a default value of false.
[^1]

  
**isDeletable**|  xsd:boolean|  If true, Virtual Center can be deletable otherwise not. A Virtual Center cannot be deleted if there is atleast one Desktop and/or Farm associated with it.  **_Since_** Horizon 7.8  


[^2]

  
**deploymentType**|  xsd:string|  Describes the type of Horizon deployment.  **_Since_** Horizon 8.0  


  * This property has a default value of "GENERAL".
[^1]
[^2]
  * This property will be one of:  
|  Value |  Description   
---|---  
"GENERAL"| Denotes Horizon is deployed on-premises.  
"AWS"| Denotes Horizon is deployed on AWS.  
"AZURE"| Denotes Horizon is deployed on Azure.  
"DELLEMC"| Denotes Horizon is deployed on Dell EMC.  
"GOOGLE"| Denotes Horizon is deployed on Google Cloud.  
"ORACLE"| Denotes Horizon is deployed on Oracle Cloud.  

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
