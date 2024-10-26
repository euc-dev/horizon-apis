---
layout: page
title: Data Object - CEIPInfo
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.infrastructure.CEIP.CEIPInfo`

Returned by
> [CEIP_Get](vdi.infrastructure.CEIP.md#get)

Since
> Horizon View 6.0


## Data Object Description

Configuration info for the customer experience improvement program.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**enabled**|  xsd:boolean|  Whether to send information to VMware.
**companySize**|  xsd:string|  The size of the company. [^1]<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"SIZE_1_100"</td><td>Company size between 1 and 100.</td></tr><tr><td>"SIZE_101_500"</td><td>Company size between 101 and 500.</td></tr><tr><td>"SIZE_501_1000"</td><td>Company size between 501 and 1000.</td></tr><tr><td>"SIZE_1001_5000"</td><td>Company size between 1001 and 5000.</td></tr><tr><td>"SIZE_5001_10000"</td><td>Company size between 5001 and 10000.</td></tr><tr><td>"SIZE_10001"</td><td>Company size greater than 10000.</td></tr></table>
**geolocation**|  xsd:string|  The geolocation of the company. [^1]<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"AFRICA"</td><td>Africa geolocation.</td></tr><tr><td>"AMERICA_NORTH"</td><td>North America geolocation.</td></tr><tr><td>"AMERICA_SOUTH_CENTRAL"</td><td>Central or South America geolocation.</td></tr><tr><td>"ASIA_PACIFIC"</td><td>Asia Pacific geolocation.</td></tr><tr><td>"AUSTRALIA"</td><td>Australia geolocation.</td></tr><tr><td>"EUROPE"</td><td>Europe geolocation.</td></tr><tr><td>"MIDDLE_EAST"</td><td>Middle East geolocation.</td></tr></table>
**vertical**|  xsd:string|  The vertical of the company. [^1]<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"AGRICULTURE"</td><td>Agriculture vertical.</td></tr><tr><td>"BANKING_FINANCE"</td><td>Banking and Finance vertical.</td></tr><tr><td>"BUSINESS_SERVICES"</td><td>Business Services vertical.</td></tr><tr><td>"COMMUNICATIONS"</td><td>Communications vertical.</td></tr><tr><td>"CONSTRUCTION"</td><td>Construction vertical.</td></tr><tr><td>"EDUCATION"</td><td>Education vertical.</td></tr><tr><td>"ENERGY_MINING"</td><td>Energy and Mining vertical.</td></tr><tr><td>"GOV_FEDERAL_NATIONAL"</td><td>Federal or National Government vertical.</td></tr><tr><td>"GOV_STATE_LOCAL"</td><td>State or Local Government vertical.</td></tr><tr><td>"HEALTH_CARE"</td><td>Health Care vertical.</td></tr><tr><td>"HIGH_TECH"</td><td>High Tech vertical.</td></tr><tr><td>"LIFE_SCIENCES"</td><td>Life Sciences vertical.</td></tr><tr><td>"MANUFACTURE_DISCRETE"</td><td>Discrete Manufacturing vertical.</td></tr><tr><td>"MANUFACTURE_PROCESS"</td><td>Manufacturing Processes vertical.</td></tr><tr><td>"MEDIA_ENTERTAINMENT"</td><td>Media and Entertainment vertical.</td></tr><tr><td>"OTHER"</td><td>Other vertical.</td></tr><tr><td>"PHARMACEUTICAL"</td><td>Pharmaceutical vertical.</td></tr><tr><td>"RETAIL_WHOLESALE"</td><td>Retail and Wholesale vertical.</td></tr><tr><td>"SERVICES"</td><td>Services vertical.</td></tr><tr><td>"TRANSPORTATION"</td><td>Transportation vertical.</td></tr><tr><td>"UTILITIES"</td><td>Utilities vertical.</td></tr></table>




 


[^1]: This property need not be set.