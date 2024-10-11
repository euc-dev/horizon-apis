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
  
**companySize**|  xsd:string|  The size of the company.   


 * This property need not be set.
  * This property will be one of:  
|  Value |  Description   
---|---  
"SIZE_1_100"| Company size between 1 and 100.  
"SIZE_101_500"| Company size between 101 and 500.  
"SIZE_501_1000"| Company size between 501 and 1000.  
"SIZE_1001_5000"| Company size between 1001 and 5000.  
"SIZE_5001_10000"| Company size between 5001 and 10000.  
"SIZE_10001"| Company size greater than 10000.  

  
**geolocation**|  xsd:string|  The geolocation of the company.   


 * This property need not be set.
  * This property will be one of:  
|  Value |  Description   
---|---  
"AFRICA"| Africa geolocation.  
"AMERICA_NORTH"| North America geolocation.  
"AMERICA_SOUTH_CENTRAL"| Central or South America geolocation.  
"ASIA_PACIFIC"| Asia Pacific geolocation.  
"AUSTRALIA"| Australia geolocation.  
"EUROPE"| Europe geolocation.  
"MIDDLE_EAST"| Middle East geolocation.  

  
**vertical**|  xsd:string|  The vertical of the company.   


 * This property need not be set.
  * This property will be one of:  
|  Value |  Description   
---|---  
"AGRICULTURE"| Agriculture vertical.  
"BANKING_FINANCE"| Banking and Finance vertical.  
"BUSINESS_SERVICES"| Business Services vertical.  
"COMMUNICATIONS"| Communications vertical.  
"CONSTRUCTION"| Construction vertical.  
"EDUCATION"| Education vertical.  
"ENERGY_MINING"| Energy and Mining vertical.  
"GOV_FEDERAL_NATIONAL"| Federal or National Government vertical.  
"GOV_STATE_LOCAL"| State or Local Government vertical.  
"HEALTH_CARE"| Health Care vertical.  
"HIGH_TECH"| High Tech vertical.  
"LIFE_SCIENCES"| Life Sciences vertical.  
"MANUFACTURE_DISCRETE"| Discrete Manufacturing vertical (deprecated).  
"MANUFACTURE_PROCESS"| Manufacturing Processes vertical (deprecated).  
"MANUFACTURING_DISCRETE"| Discrete Manufacturing vertical.  
"MANUFACTURING_PROCESS"| Manufacturing Processes vertical.  
"MEDIA_ENTERTAINMENT"| Media and Entertainment vertical.  
"OTHER"| Other vertical.  
"PHARMACEUTICAL"| Pharmaceutical vertical.  
"RETAIL_WHOLESALE"| Retail and Wholesale vertical.  
"SERVICES"| Services vertical.  
"TRANSPORTATION"| Transportation vertical.  
"UTILITIES"| Utilities vertical.  

  
  
  
   
  
  
