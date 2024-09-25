---
layout: page
title: Data Object - LocalizedMethodFault
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vim.binding.vmodl.LocalizedMethodFault
See also
     [MethodFault](vmodl.MethodFault.md)
Since 
    vmodl.version.version0

## Data Object Description 

A wrapper class used to pass MethodFault data objects over the wire along with a localized display message for the fault. 

  * This data object must be updated as a whole.



## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**fault**| [MethodFault](vmodl.MethodFault.md)|    
  
**localizedMessage**|  xsd:string|  The localized message that would be sent in the faultstring element of the SOAP Fault. It is optional so that clients are not required to send a localized message to the server, but servers are required to send the localized message to clients.   


[^1]

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
