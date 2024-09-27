---
layout: page
title: Data Object - PodFederationData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.federation.PodFederation.PodFederationData  
Property of
     [PodFederationInfo](vdi.federation.PodFederation.PodFederationInfo.md#field_detail)  
See also
     [SiteId](vdi.entity.SiteId.md)  
Since 
    Horizon View 6.0

## Data Object Description 

Data relevant to this Pod Federation. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**displayName**|  xsd:string|  Description of the Pod Federation.   


* This property need not be set.
  * This property has a maximum length of 64 characters. 

  
**sites**| [SiteId[]](vdi.entity.SiteId.md)|  Member sites in the Pod Federation. Pods are member of sites.   


* This property need not be set.
* This property cannot be updated.

  
**guid**|  xsd:string|  GUID of the pod federation.  **_Since_** Horizon 7.9  


* This property need not be set.
* This property cannot be updated.

  
  
  

  
  

