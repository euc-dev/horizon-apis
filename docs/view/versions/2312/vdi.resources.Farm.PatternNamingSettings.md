---
layout: page
title: Data Object - FarmPatternNamingSettings
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.resources.Farm.PatternNamingSettings`

Property of  
> [FarmRDSServerNamingSettings](vdi.resources.Farm.RDSServerNamingSettings.md#field_detail), [FarmRDSServerNamingSpec](vdi.resources.Farm.RDSServerNamingSpec.md#field_detail)

Since  
> Horizon View 6.2


## Data Object Description 

Settings related to specification of VMs with a naming pattern. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**namingPattern**|  xsd:string|  RDS Servers will be named according to the specified naming pattern. By default, view manager appends a unique number to the specified pattern to provide a unique name for each RDS Server. To place this unique number elsewhere in the pattern, use '{n}'. (For example: rds-{n}-sales.) The unique number can also be made a fixed length. (For example: rds-{n:fixed=3}-sales will name RDS Servers from rds-001-sales to rds-999-sales).  
RDS Server names are constrained to a maximum size of 15 characters including the unique number. Therefore, care must be taken when choosing a pattern. If the maximum farm size is 9 RDS servers, the pattern must be at most 14 characters. For 99 RDS servers, 13 characters, for 999 RDS servers, 12 characters. For 9999 RDS servers, 11 characters. If using a fixed size token, use a maximum of 14 characters for "n=1", 13 characters for "n=2", 12 characters for "n=3", and 11 characters for "n=4".  
If {n} is specified with no size, a size of 2 is automatically used and if no {} is specified, {n=2} is automatically appended to the end of the pattern   


  * This property must contain only alphanumerics and dashes. It must contain at least one alpha character. It may also optionally contain a numeric placement token {n} or {n:fixed=#}. If the pattern does not specify the numeric placement token, the maximum length is 14 characters. 

  
**maxNumberOfRDSServers**|  xsd:int|  Maximum number of RDS Servers in the farm.   


  * This property has a default value of 1.
  * This property has a minimum value of 1. 

  
  
  
   
  
  
