---
layout: page
title: Data Object - SiteInfo
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.federation.Site.SiteInfo`

Returned by
> [Site_Get](vdi.federation.Site.md#get), [Site_List](vdi.federation.Site.md#list)

See also
> [PodId](vdi.entity.PodId.md), [SiteBase](vdi.federation.Site.SiteBase.md), [SiteId](vdi.entity.SiteId.md)

Since
> Horizon View 6.0


## Data Object Description

Site Info.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**id**| [SiteId](vdi.entity.SiteId.md)|  Unique identifier for a Site [^2]
**base**| [SiteBase](vdi.federation.Site.SiteBase.md)|  Site base data, this includes displayName and description
**pods**| [PodId[]](vdi.entity.PodId.md)|  Member pods for this site. To update the site of a pod, use Pod.update(). [^1] [^2]
**refId**|  xsd:string|  Reference ID used for this site.  **_Since_** Horizon 7.11 [^1]
 


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.