---
layout: page
title: Data Object - PodFederationData
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.federation.PodFederation.PodFederationData`

Property of
> [PodFederationInfo](vdi.federation.PodFederation.PodFederationInfo.md#field_detail)

See also
> [SiteId](vdi.entity.SiteId.md)

Since
> Horizon View 6.0


## Data Object Description

Data relevant to this Pod Federation.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**displayName**|  xsd:string|  Description of the Pod Federation. [^1] <br>* This property has a maximum length of 64 characters.
**sites**| [SiteId[]](vdi.entity.SiteId.md)|  Member sites in the Pod Federation. Pods are member of sites. [^1] [^2]
**guid**|  xsd:string|  GUID of the pod federation.  **_Since_** Horizon 7.9 [^1] [^2]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.