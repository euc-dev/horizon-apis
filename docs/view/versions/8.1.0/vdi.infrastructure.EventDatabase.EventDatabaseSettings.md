---
layout: page
title: Data Object - EventDatabaseSettings
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.infrastructure.EventDatabase.EventDatabaseSettings  
Property of
     [EventDatabaseInfo](vdi.infrastructure.EventDatabase.EventDatabaseInfo.md#field_detail)  
See also
     [SecureString](vdi.util.SecureString.md)  
Since 
    Horizon View 6.0

## Data Object Description 

The EventDatabaseSettings object. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**server**|  xsd:string|  Server that hosts the database which will be used to store events   
  
**type**|  xsd:string|  The type of database to use for the event database.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"MYSQL"| For MYSQL databases; based on Admin UI, this may not be supported  
"SQLSERVER"| For MS SQL Server databases  
"ORACLE"| For Oracle databases  

  
**port**|  xsd:int|  Port number on the database server to which View will send events   
  
**name**|  xsd:string|  Name of the database on the database server to use for storing events. Note that this database must exist on the server or the values cannot be saved.   
  
**userName**|  xsd:string|  Username to use for the connection to the event database.   
  
**password**| [SecureString](vdi.util.SecureString.md)|  Password for the user to use for the connection to the event database.   
  
**tablePrefix**|  xsd:string|  If present, all tables for this instance will start with this prefix. This allows multiple brokers to use the same events database without trampling on other broker data.   


* This property need not be set.
  * This property must start with a letter, may only contain letters, numbers, and the characters @, $, #, and _, and may not be longer than 6 characters. 

  
**queryTimeout**|  xsd:int|  Query execution timeout  **_Since_** Horizon 7.9  


* This property need not be set.

  
  
  
  
  
  

