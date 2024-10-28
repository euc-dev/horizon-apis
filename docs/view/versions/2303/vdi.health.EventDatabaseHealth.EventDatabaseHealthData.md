---
layout: page
title: Data Object - EventDatabaseHealthData
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.health.EventDatabaseHealth.EventDatabaseHealthData`

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
**databaseType**|  xsd:string|  The type of the database.<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"ORACLE"</td><td>An Oracle database.</td></tr><tr><td>"SQLSERVER"</td><td>A SQL server database.</td></tr><tr><td>"POSTGRESQL"</td><td>A PostgreSQL database.</td></tr><tr><td>"UNDEFINED"</td><td>An undefined database type.</td></tr></table>
**userName**|  xsd:string|  The username used to connect to the database
**databaseName**|  xsd:string|  The name of the database.
**tablePrefix**|  xsd:string|  The prefix of tables within the database.
**state**|  xsd:string|  The state of the database connection.<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"CONNECTED"</td><td>The connection is connected to the database.</td></tr><tr><td>"CONNECTING"</td><td>The connection is connecting to the database.</td></tr><tr><td>"DISCONNECTED"</td><td>The connection is disconnected from the database.</td></tr><tr><td>"RECONNECTING"</td><td>The connection is reconnecting to the database.</td></tr><tr><td>"ERROR"</td><td>There is an error with the database connection.</td></tr></table>
**error**|  xsd:string|  Any error with the database connection. [^1]
 


 


[^1]: This property need not be set.