---
layout: page
title: Data Object - NetworkLabelIncompatibleReasons
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.utils.virtualcenter.NetworkLabel.NetworkLabelIncompatibleReasons  
Property of
     [NetworkLabelData](vdi.utils.virtualcenter.NetworkLabel.NetworkLabelData.md#field_detail)  
Since 
    Horizon View 6.0

## Data Object Description 

Reasons that may preclude this NetworkLabel from being used to configure desktops. 

  * This data object must be updated as a whole.



## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**notConfiguredOnAllHosts**|  xsd:boolean|  Whether or not the network label is configured on all hosts in a cluster. If true, this network label cannot be used in desktop configuration.   


* This property cannot be updated.

  
**dvsUplinkPort**|  xsd:boolean|  Whether or not the network label has the standard name of the distributed virtual switch uplink port, which cannot be assigned to virtual machines. If true, this network label cannot be used in desktop configuration.   


* This property cannot be updated.

  
**vmcNetworks**|  xsd:boolean|  Whether or not network label belongs to "VMC Networks". If true, this network label cannot be used in desktop configuration.  **_Since_** Horizon 7.8  


* This property cannot be updated.

  
  
  
 
  
  

