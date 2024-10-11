---
layout: page
title: Data Object - EventDatabaseHealthData
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.health.EventDatabaseHealth.EventDatabaseHealthData`

Property of  
> [EventDatabaseHealthInfo](vdi.health.EventDatabaseHealth.EventDatabaseHealthInfo.md#field_detail)

Since  
> Horizon View 6.0


## Data Object Description 

The health of a configured database connection. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**serverName**|  xsd:string|  The name of the database server.   
  
**port**|  xsd:int|  The port of the database server   
  
**databaseType**|  xsd:string|  The type of the database.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"ORACLE"| An Oracle database  
"SQLSERVER"| A SQL server database.  
"UNDEFINED"| An undefined database type.  

  
**userName**|  xsd:string|  The username used to connect to the database   
  
**databaseName**|  xsd:string|  The name of the database.   
  
**tablePrefix**|  xsd:string|  The prefix of tables within the database.   
  
**state**|  xsd:string|  The state of the database connection.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"CONNECTED"| The connection is connected to the database.  
"CONNECTING"| The connection is connecting to the database.  
"DISCONNECTED"| The connection is disconnected from the database.  
"RECONNECTING"| The connection is reconnecting to the database.  
"ERROR"| There is an error with the database connection.  

  
**error**|  xsd:string|  Any error with the database connection.   


* This property need not be set.

  
  
  
  
  
  
