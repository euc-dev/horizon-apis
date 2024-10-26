---
layout: page
title: Data Object - FarmBlackoutTime
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.resources.Farm.BlackoutTime`

Property of
> [FarmSpaceReclamationSettings](vdi.resources.Farm.SpaceReclamationSettings.md#field_detail)

Since
> Horizon View 6.2


## Data Object Description

Fields for specifying blackout time for space reclamation settings RDS server disk space reclamation do not occur during blackout times.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**days**|  xsd:string[]|  List of days for a given range of time.<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>MONDAY</td><td>Monday</td></tr><tr><td>TUESDAY</td><td>Tuesday</td></tr><tr><td>WEDNESDAY</td><td>Wednesday</td></tr><tr><td>THURSDAY</td><td>Thursday</td></tr><tr><td>FRIDAY</td><td>Friday</td></tr><tr><td>SATURDAY</td><td>Saturday</td></tr><tr><td>SUNDAY</td><td>Sunday</td></tr><tr><td>ALL</td><td>All seven days of the week</td></tr></table>
**startTime**|  xsd:string|  Starting time for the blackout. [^22]
**endTime**|  xsd:string|  Ending time for the blackout. [^22]


 


[^22]: This property must be in the form hh:mm in 24 hours format.