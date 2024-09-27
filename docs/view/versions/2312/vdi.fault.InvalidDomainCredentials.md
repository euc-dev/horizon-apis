---
layout: page
title: Fault - InvalidDomainCredentials
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.fault.InvalidDomainCredentials  
Extends
     [ViewRuntimeFault](vdi.fault.ViewRuntimeFault.md)  
See also
     [ADDomainId](vdi.entity.ADDomainId.md), [EntityId](vdi.EntityId.md)  
Since 
    Horizon View 6.0

## Fault Description 

Thrown if the caller does not have the correct secondary credentials to access a one-way trusted domain. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [EntityId](vdi.EntityId.md)|  Entity, if any, whose access caused the error.   


 * This property need not be set.

  
**domain**| [ADDomainId](vdi.entity.ADDomainId.md)|  Domain that caused the error, if known.   


 * This property need not be set.

  
**netbiosDomainName**|  xsd:string|  Netbios domain name of domain that caused the error, if known.   


 * This property need not be set.

  
**dnsDomainName**|  xsd:string|  DNS domain name of domain that caused the error, if known.   


 * This property need not be set.

  
Properties inherited from [ViewRuntimeFault](vdi.fault.ViewRuntimeFault.md)  
[errorMessage](vdi.fault.ViewRuntimeFault.md#errorMessage)  
Properties inherited from [RuntimeFault](vmodl.RuntimeFault.md)  
None  
Properties inherited from [MethodFault](vmodl.MethodFault.md)  
None  
  
  
   
  
  

