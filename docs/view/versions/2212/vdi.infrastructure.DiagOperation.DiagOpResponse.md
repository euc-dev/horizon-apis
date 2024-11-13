---
layout: page
title: Data Object - DiagOperationResponse
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.infrastructure.DiagOperation.DiagOpResponse`

Returned by
> [DiagOperation_Send](vdi.infrastructure.DiagOperation.md#send)


## Data Object Description

Diagnostic operation response

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**status**|  xsd:string|  Diagnostic operation status [^257] [^2]<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"SUCCESS"</td><td>Diagnostic operation is done successfully.</td></tr><tr><td>"ERROR"</td><td>Diagnostic operation has failed.</td></tr></table>
**message**|  xsd:string|  Message received from Horizon Diagnostic Agent. If the status is ERROR then the value would be error message. [^1] [^2]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^257]: This property has a default value of "SUCCESS".