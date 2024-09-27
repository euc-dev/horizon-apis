---
layout: page
title: Data Object - FarmMissingApplicationInstallationData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.Farm.MissingApplicationInstallationData  
Returned by
     [Farm_ValidateInstalledApplications](vdi.resources.Farm.md#validateInstalledApplications)  
Since 
    Horizon View 6.0

## Data Object Description 

Represents information about an Application that has not been installed in the Farm, along with an array of RDSServer names that it is missing from. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**applicationExePath**|  xsd:string|  Details of the missing Application exePath   
  
**rdsServerNames**|  xsd:string[]|  Array of RDS server names that this application has not been installed on   
  
  

  

