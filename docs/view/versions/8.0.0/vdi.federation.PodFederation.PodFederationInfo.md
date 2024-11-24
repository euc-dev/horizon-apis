---
layout: page
title: Data Object - PodFederationInfo
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.federation.PodFederation.PodFederationInfo`

Returned by
> [PodFederation_Get](vdi.federation.PodFederation.md#get)

See also
> [PodFederationData](vdi.federation.PodFederation.PodFederationData.md), [PodFederationLocalPodStatus](vdi.federation.PodFederation.LocalPodStatus.md)

Since
> Horizon View 6.0


## Data Object Description

Info object for Pod Federation.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**data**| [PodFederationData](vdi.federation.PodFederation.PodFederationData.md)|  Data relevant to this Pod Federation. It will be null if:<br>1\. The PodFederation has not been initialized or has not been joined.<br>2\. The PodFederation is undergoing initialize, uninitialize, join, or unjoin operation.<br>3\. Required read privileges are not met. [^1]
**localPodStatus**| [PodFederationLocalPodStatus](vdi.federation.PodFederation.LocalPodStatus.md)|  Multi-DataCenter View status for the local Pod. [^2]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.