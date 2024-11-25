---
layout: page
title: Data Object - LicenseInfo
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.infrastructure.License.LicenseInfo`

Returned by
> [License_Get](vdi.infrastructure.License.md#get)

Since
> Horizon View 6.0


## Data Object Description

Information describing the View cluster license.
 [^167]



## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**licensed**|  xsd:boolean|  Whether the View instance is licensed.
**licenseKey**|  xsd:string|  The License Key in partially redacted form  **_Since_** Horizon View 6.2 [^1]
**expirationTime**|  xsd:dateTime|  The expiration date of the View instance. [^1]
**viewComposerEnabled**|  xsd:boolean| **Deprecated.**_This is being deprecated since View Composer will no longer be supported from Horizon version 2012 onwards._ Whether View Composer is enabled.
**desktopLaunchingEnabled**|  xsd:boolean|  Whether Desktop launching is enabled.
**applicationLaunchingEnabled**|  xsd:boolean|  Whether Application launching is enabled.
**instantCloneEnabled**|  xsd:boolean|  Whether Instant Clone is enabled.  **_Since_** Horizon 7.0
**helpDeskEnabled**|  xsd:boolean|  Whether Help Desk is enabled.  **_Since_** Horizon 7.3
**collaborationEnabled**|  xsd:boolean|  Whether Session Collaboration is enabled.  **_Since_** Horizon 7.4
**licenseEdition**|  xsd:string|  The license edition.  **_Since_** Horizon 7.9 [^2]<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"HORIZON_STANDARD_CONCURRENT_USER"</td><td>Omnissa Horizon Standard for View (Concurrent User).</td></tr><tr><td>"HORIZON_ADVANCED_NAMED_USER"</td><td>Omnissa Horizon Advanced for View (Named User)</td></tr><tr><td>"HORIZON_ADVANCED_CONCURRENT_USER"</td><td>Omnissa Horizon Advanced for View (Concurrent User).</td></tr><tr><td>"HORIZON_ENTERPRISE_NAMED_USER"</td><td>Horizon Enterprise (Named User).</td></tr><tr><td>"HORIZON_ENTERPRISE_CONCURRENT_USER"</td><td>Horizon Enterprise (Concurrent User).</td></tr><tr><td>"ENTERPRISE_CONCURRENT_USER"</td><td>Omnissa View Enterprise.</td></tr><tr><td>"HORIZON_APPS_STANDARD_NAMED_USER"</td><td>Omnissa Horizon Apps 7 Standard for View (Named User).</td></tr><tr><td>"HORIZON_APPS_STANDARD_CONCURRENT_USER"</td><td>Omnissa Horizon Apps 7 Standard for View (Concurrent User).</td></tr><tr><td>"HORIZON_APPS_ADVANCED_NAMED_USER"</td><td>Omnissa Horizon Apps 7 Advanced for View (Named User).</td></tr><tr><td>"HORIZON_APPS_ADVANCED_CONCURRENT_USER"</td><td>Omnissa Horizon Apps 7 Advanced for View (Concurrent User).</td></tr><tr><td>"WS1_ENTERPRISE_NAMED_USER"</td><td>Workspace ONE Enterprise.</td></tr><tr><td>"WS1_ENTERPRISE_WITH_VDI_NAMED_USER"</td><td>Workspace ONE Enterprise with VDI.</td></tr></table>
**usageModel**|  xsd:string|  The usage model for this license. [^1]<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"CONCURRENT_USER"</td><td>The is the license usage model for a standalone install.</td></tr><tr><td>"NAMED_USER"</td><td>This is the license mode for an install as part of a suite.</td></tr></table>
**licenseMode**|  xsd:string|  The license mode used.  **_Since_** Horizon 7.6<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"DEFAULT"</td><td>Perpetual license is in use.</td></tr><tr><td>"SUBSCRIPTION"</td><td>Cloud subscription license is in use.</td></tr><tr><td>"PERPETUAL_ONLY"</td><td>Perpetual license is in use.</td></tr></table>
**gracePeriodDays**|  xsd:int|  Set only when [licenseMode](vdi.infrastructure.License.LicenseInfo.md#licenseMode) is set to SUBSCRIPTION value. The grace period in days for subscription slice.  **_Since_** Horizon 7.6 [^1] [^2]
**subscriptionSliceExpiry**|  xsd:dateTime|  Set only when [licenseMode](vdi.infrastructure.License.LicenseInfo.md#licenseMode) is set to SUBSCRIPTION value. The expiry of subscription slice.  **_Since_** Horizon 7.6 [^1] [^2]
**licenseHealth**|  xsd:string|  Set only when [licenseMode](vdi.infrastructure.License.LicenseInfo.md#licenseMode) is set to SUBSCRIPTION value. The license health.  **_Since_** Horizon 7.6 [^1] [^2]<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"RED"</td><td>License is expired.</td></tr><tr><td>"GREEN"</td><td>License is not expired and License update is missed but not more than 7 days.</td></tr><tr><td>"YELLOW"</td><td>License is not expired and License update is missed for more than 7 days.</td></tr></table>




 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^167]: This data object must be updated as a whole.