---
layout: page
title: Data Object - ApplicationIconInfo
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.resources.ApplicationIcon.ApplicationIconInfo`

Returned by  
> [ApplicationIcon_Get](vdi.resources.ApplicationIcon.md#get), [ApplicationIcon_GetByApplications](vdi.resources.ApplicationIcon.md#getByApplications), [ApplicationIcon_GetInfos](vdi.resources.ApplicationIcon.md#getInfos)

See also  
> [ApplicationIconBase](vdi.resources.ApplicationIcon.ApplicationIconBase.md), [ApplicationIconId](vdi.entity.ApplicationIconId.md)

Since  
> Horizon View 6.0


## Data Object Description 

ApplicationIconInfo returned on a get()/getInfos()/getByApplications() call. 

##  Queryable Data Object 

This data object is queryable using [QueryService](vdi.query.QueryService.md "QueryService"). 

Only the following fields support filtering: 

  * [base](vdi.resources.ApplicationIcon.ApplicationIconInfo.md#base).[width](vdi.resources.ApplicationIcon.ApplicationIconBase.md#width)
  * [base](vdi.resources.ApplicationIcon.ApplicationIconInfo.md#base).[height](vdi.resources.ApplicationIcon.ApplicationIconBase.md#height)
  * [base](vdi.resources.ApplicationIcon.ApplicationIconInfo.md#base).[iconHash](vdi.resources.ApplicationIcon.ApplicationIconBase.md#iconHash)



Query Privileges 

Privilege |  Description   
---|---  
POOL_VIEW|  This query will return results only for applications the caller has application read privilege on with the corresponding application.   
  


## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [ApplicationIconId](vdi.entity.ApplicationIconId.md)|  ApplicationIcon entityId   


 * This property cannot be updated.

  
**base**| [ApplicationIconBase](vdi.resources.ApplicationIcon.ApplicationIconBase.md)|  Summary View of the Application Icon, represents the metadata of the ApplicationIcon.   
  
  
  
   
  
  
