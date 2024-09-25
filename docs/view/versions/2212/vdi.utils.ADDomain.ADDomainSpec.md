---
layout: page
title: Data Object - ADDomainSpec
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.utils.ADDomain.ADDomainSpec
Parameter to
     [ADDomain_Bind](vdi.utils.ADDomain.md#bind)
See also
     [ADDomainAdvancedSettings](vdi.utils.ADDomain.ADDomainAdvancedSettings.md), [ServiceAccountCredentials](vdi.utils.ADDomain.ServiceAccountCredentials.md)
Since 
    Horizon 8.1

## Data Object Description 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**dnsName**|  xsd:string|  The DNS name of the domain.   


  * This property must be a valid DNS name 

  
**netBiosName**|  xsd:string|  The NetBIOS name of the domain.   
  
**primaryAccount**| [ServiceAccountCredentials](vdi.utils.ADDomain.ServiceAccountCredentials.md)|  Primary service account credentials.   
  
**adDomainAdvancedSettings**| [ADDomainAdvancedSettings](vdi.utils.ADDomain.ADDomainAdvancedSettings.md)|  Advanced information of no trust domain.   
  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
