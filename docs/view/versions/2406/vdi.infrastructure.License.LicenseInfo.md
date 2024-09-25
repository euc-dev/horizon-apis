---
layout: page
title: Data Object - LicenseInfo
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.infrastructure.License.LicenseInfo
Returned by
     [License_Get](vdi.infrastructure.License.md#get)
Since 
    Horizon View 6.0

## Data Object Description 

Information describing the View cluster license. 

  * This data object must be updated as a whole.



## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**licensed**|  xsd:boolean|  Whether the View instance is licensed.   
  
**licenseKey**|  xsd:string|  The License Key in partially redacted form  **_Since_** Horizon View 6.2  


[^1]

  
**expirationTime**|  xsd:dateTime|  The expiration date of the View instance.   


[^1]

  
**viewComposerEnabled**|  xsd:boolean| **Deprecated.**_This is being deprecated since View Composer will no longer be supported from Horizon version 2012 onwards._ Whether View Composer is enabled.   
  
**desktopLaunchingEnabled**|  xsd:boolean|  Whether Desktop launching is enabled.   
  
**applicationLaunchingEnabled**|  xsd:boolean|  Whether Application launching is enabled.   
  
**instantCloneEnabled**|  xsd:boolean|  Whether Instant Clone is enabled.  **_Since_** Horizon 7.0  
  
**helpDeskEnabled**|  xsd:boolean|  Whether Help Desk is enabled.  **_Since_** Horizon 7.3  
  
**collaborationEnabled**|  xsd:boolean|  Whether Session Collaboration is enabled.  **_Since_** Horizon 7.4  
  
**agentAutoUpgradeEnabled**|  xsd:boolean|  Whether Agent Auto Upgrade is enabled.  **_Since_** Horizon 8.8  
  
**licenseEdition**|  xsd:string|  The license edition.  **_Since_** Horizon 7.9  


[^2]
  * This property will be one of:  
|  Value |  Description   
---|---  
"HORIZON_STANDARD_CONCURRENT_USER"| VMware Horizon Standard for View (Concurrent User).  
"HORIZON_ADVANCED_NAMED_USER"| VMware Horizon Advanced for View (Named User)  
"HORIZON_ADVANCED_CONCURRENT_USER"| VMware Horizon Advanced for View (Concurrent User).  
"HORIZON_ENTERPRISE_NAMED_USER"| Horizon Enterprise (Named User).  
"HORIZON_ENTERPRISE_CONCURRENT_USER"| Horizon Enterprise (Concurrent User).  
"ENTERPRISE_CONCURRENT_USER"| VMware View Enterprise.  
"HORIZON_APPS_STANDARD_NAMED_USER"| VMware Horizon Apps 7 Standard for View (Named User).  
"HORIZON_APPS_STANDARD_CONCURRENT_USER"| VMware Horizon Apps 7 Standard for View (Concurrent User).  
"HORIZON_APPS_ADVANCED_NAMED_USER"| VMware Horizon Apps 7 Advanced for View (Named User).  
"HORIZON_APPS_ADVANCED_CONCURRENT_USER"| VMware Horizon Apps 7 Advanced for View (Concurrent User).  
"WS1_ENTERPRISE_NAMED_USER"| Workspace ONE Enterprise.  
"WS1_ENTERPRISE_WITH_VDI_NAMED_USER"| Workspace ONE Enterprise with VDI.  

  
**usageModel**|  xsd:string|  The usage model for this license.   


[^1]
  * This property will be one of:  
|  Value |  Description   
---|---  
"CONCURRENT_USER"| The is the license usage model for a standalone install.  
"NAMED_USER"| This is the license mode for an install as part of a suite.  

  
**licenseMode**|  xsd:string|  The license mode used.  **_Since_** Horizon 7.6  


  * This property will be one of:  
|  Value |  Description   
---|---  
"DEFAULT"| Perpetual license is in use.  
"SUBSCRIPTION"| Cloud subscription license is in use.  
"PERPETUAL_ONLY"| Perpetual license is in use.  

  
**gracePeriodDays**|  xsd:int|  Set only when [licenseMode](vdi.infrastructure.License.LicenseInfo.md#licenseMode) is set to SUBSCRIPTION value. The grace period in days for subscription slice.  **_Since_** Horizon 7.6  


[^1]
[^2]

  
**subscriptionSliceExpiry**|  xsd:dateTime|  Set only when [licenseMode](vdi.infrastructure.License.LicenseInfo.md#licenseMode) is set to SUBSCRIPTION value. The expiry of subscription slice.  **_Since_** Horizon 7.6  


[^1]
[^2]

  
**licenseHealth**|  xsd:string|  Set only when [licenseMode](vdi.infrastructure.License.LicenseInfo.md#licenseMode) is set to SUBSCRIPTION value. The license health.  **_Since_** Horizon 7.6  


[^1]
[^2]
  * This property will be one of:  
|  Value |  Description   
---|---  
"RED"| License is expired.  
"GREEN"| License is not expired.  
"YELLOW"| License is expiring.  

  
**licenseSyncTime**|  xsd:dateTime|  Set only when [licenseMode](vdi.infrastructure.License.LicenseInfo.md#licenseMode) is set to SUBSCRIPTION value. Last license sync time.  **_Since_** Horizon 8.13  


[^1]

  
**consent**|  xsd:boolean|  Specifies for a perpetual key if the admin has provided a consent stating that the admin owns this perpetual key and have no other Horizon license.  **_Since_** Horizon 8.13  


  * This property has a default value of false.
[^1]

  
**originator**|  xsd:boolean|  Used only when [licenseMode](vdi.infrastructure.License.LicenseInfo.md#licenseMode) is set to SUBSCRIPTION value. Originator of set subscription license request. True = Edge and False = Non-Edge/Unknown.  **_Since_** Horizon 8.13  


  * This property has a default value of false.
[^1]

  
  

  

