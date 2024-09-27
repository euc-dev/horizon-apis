---
layout: page
title: Data Object - PodAssignmentInfo
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.federation.PodAssignment.PodAssignmentInfo  
Returned by
     [PodAssignment_Get](vdi.federation.PodAssignment.md#get), [PodAssignment_GetInfos](vdi.federation.PodAssignment.md#getInfos)  
See also
     [PodAssignmentData](vdi.federation.PodAssignment.PodAssignmentData.md), [PodAssignmentId](vdi.entity.PodAssignmentId.md)  
Since 
    Horizon View 6.0

## Data Object Description 

The pod assignment info class. 

##  Queryable Data Object 

This data object is queryable using [QueryService](vdi.query.QueryService.md "QueryService"). 

The query for Pod assignments. 

Query Privileges 

Privilege |  Description   
---|---  
FEDERATED_LDAP_VIEW|  Global LDAP read access is required to query for Pod assignments.   
  


## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [PodAssignmentId](vdi.entity.PodAssignmentId.md)|  Id of the pod assignment configuration   


* This property cannot be updated.

  
**data**| [PodAssignmentData](vdi.federation.PodAssignment.PodAssignmentData.md)|  Data for the pod assignment configuration.   


* This property cannot be updated.

  
  
  

  
  

