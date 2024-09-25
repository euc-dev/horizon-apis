---
layout: page
title: Data Object - DiagOperationResponse
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.infrastructure.DiagOperation.DiagOpResponse
Returned by
     [DiagOperation_Send](vdi.infrastructure.DiagOperation.md#send)

## Data Object Description 

Diagnostic operation response 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**status**|  xsd:string|  Diagnostic operation status   


  * This property has a default value of "SUCCESS".
[^2]
  * This property will be one of:  
|  Value |  Description   
---|---  
"SUCCESS"| Diagnostic operation is done successfully.  
"ERROR"| Diagnostic operation has failed.  

  
**message**|  xsd:string|  Message received from Horizon Diagnostic Agent. If the status is ERROR then the value would be error message.   


[^1]
[^2]

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

