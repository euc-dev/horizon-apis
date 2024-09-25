---
layout: page
title: Data Object - EnvironmentSettings
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.infrastructure.GlobalSettings.EnvironmentSettings
Returned by
     [GlobalSettings_GetEnvironmentSettings](vdi.infrastructure.GlobalSettings.md#getEnvironmentSettings)
Since 
    Horizon 7.6

## Data Object Description 

Environment settings information. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**ipMode**|  xsd:string|  Indicates the IP mode of the environment.   


[^1]
  * This property will be one of:  
|  Value |  Description   
---|---  
"IPv4"| This Connection Server is running in IPv4 environment.  
"IPv6"| This Connection Server is running in IPv6 environment.  

  
**fipsModeEnabled**|  xsd:boolean|  Indicates if FIPS mode is enabled.   


  * This property has a default value of false.
[^1]

  
**clusterName**|  xsd:string|  The name of a group of connection servers sharing the same configuration.  **_Since_** Horizon 7.7  


[^1]

  
**clusterGuid**|  xsd:string|  The GUID of a group of connection servers sharing the same configuration.  **_Since_** Horizon 7.7  


[^1]

  
**localPodName**|  xsd:string|  The name of the current pod in the Multi-DataCenter View Pod, the value will be null when PodFederation is not initialized.  **_Since_** Horizon 7.7  


[^1]

  
**timezoneOffset**|  xsd:int|  Represents this Connection Server's time zone offset from UTC in seconds.  **_Since_** Horizon 7.7  


[^1]

  
**deploymentType**|  xsd:string|  Describes the type of Horizon deployment.  **_Since_** Horizon 8.0  


  * This property has a default value of "GENERAL".
[^1]
  * This property will be one of:  
|  Value |  Description   
---|---  
"GENERAL"| Denotes Horizon is deployed on-premises.  
"AWS"| Denotes Horizon is deployed on AWS.  
"AZURE"| Denotes Horizon is deployed on Azure.  
"DELLEMC"| Denotes Horizon is deployed on Dell EMC.  
"GOOGLE"| Denotes Horizon is deployed on Google Cloud.  
"ORACLE"| Denotes Horizon is deployed on Oracle Cloud.  

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

