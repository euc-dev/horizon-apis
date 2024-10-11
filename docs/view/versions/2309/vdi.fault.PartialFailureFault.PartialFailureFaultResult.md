---
layout: page
title: Data Object - PartialFailureFaultResult
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.fault.PartialFailureFault.PartialFailureFaultResult`

Property of  
> [PartialFailureFault](vdi.fault.PartialFailureFault.md#field_detail)

See also  
> [MethodFault](vmodl.MethodFault.md)

Since  
> Horizon View 6.0


## Data Object Description 

The result of one individual operation. This will contain either a fault in the event that the operation failed or a result (if one exists) of the operation on success. At most one of these fields will be populated. 

  * This data object must be updated as a whole.



## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**fault**| [MethodFault](vmodl.MethodFault.md)|  The error if the individual operation failed.   


 * This property need not be set.

  
**result**|  xsd:anyType|  The result (if any) of the function if the individual operation succeeded.   


 * This property need not be set.

  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
