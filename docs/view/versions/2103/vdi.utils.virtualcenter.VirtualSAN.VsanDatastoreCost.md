---
layout: page
title: Data Object - VsanDatastoreCost
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.utils.virtualcenter.VirtualSAN.VsanDatastoreCost  
Returned by
     [VirtualSAN_GetVsanDatastoreCostForFullClone](vdi.utils.virtualcenter.VirtualSAN.md#getVsanDatastoreCostForFullClone), [VirtualSAN_GetVsanDatastoreCostForInstantClone](vdi.utils.virtualcenter.VirtualSAN.md#getVsanDatastoreCostForInstantClone), [VirtualSAN_GetVsanDatastoreCostForLinkedClone](vdi.utils.virtualcenter.VirtualSAN.md#getVsanDatastoreCostForLinkedClone)  
Since 
    Horizon 7.4

## Data Object Description 

Represents the cost factor for different types of disks when VSAN is used. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**osFactor**|  xsd:int|  Multiplicative factor for OS disk that is needed to account for the extra copies that are created for VSAN.   

* This property has a default value of 1.
*  This property need not be set.
* This property cannot be updated.

  
**replicaFactor**|  xsd:int|  Multiplicative factor for replica disk that is needed to account for the extra copies that are created for VSAN.   


  * This property has a default value of 1.
*  This property need not be set.
* This property cannot be updated.

  
**userDataFactor**|  xsd:int|  Multiplicative factor for user data disk that is needed to account for the extra copies that are created for VSAN.   


  * This property has a default value of 1.
*  This property need not be set.
* This property cannot be updated.

  
**fullCloneFactor**|  xsd:int|  Multiplicative factor for full clone disk that is needed to account for the extra copies that are created for VSAN.   


  * This property has a default value of 1.
*  This property need not be set.
* This property cannot be updated.

  
  
  

  
  

