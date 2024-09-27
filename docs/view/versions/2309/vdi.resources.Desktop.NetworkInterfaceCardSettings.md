---
layout: page
title: Data Object - DesktopNetworkInterfaceCardSettings
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.Desktop.NetworkInterfaceCardSettings  
Property of
     [DesktopVirtualCenterNetworkingSettings](vdi.resources.Desktop.VirtualCenterNetworkingSettings.md#field_detail)  
See also
     [DesktopNetworkLabelAssignmentSpec](vdi.resources.Desktop.NetworkLabelAssignmentSpec.md), [NetworkInterfaceCardId](vdi.entity.NetworkInterfaceCardId.md)  
Since 
    Horizon View 6.0

## Data Object Description 

Network interface card settings for machines provisioned for this desktop. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**nic**| [NetworkInterfaceCardId](vdi.entity.NetworkInterfaceCardId.md)|  The network interface card id for these settings.   
  
**networkLabelAssignmentSpecs**| [DesktopNetworkLabelAssignmentSpec[]](vdi.resources.Desktop.NetworkLabelAssignmentSpec.md)|  Automatic network label assignment feature settings for this NIC. By default, newly provisioned machines of an automated desktop retain their parent image's network labels on each of their network interface cards. In certain circumstances, notably dealing with VLAN subset sizing and DHCP IP address availability, it may be desirable for the desktop to instead use different network labels for these newly provisioned machines. This feature allows an administrator to provide a per NIC list of network labels and their maximum availability to be automatically distributed to newly provisioned machines.   
  
If this is unset, the feature is disabled.  
  
Starting at the _alphabetically_ first network label spec in the list that has not yet been assigned its maximum count for this NIC on this desktop, the desktop will have its next provisioned machine's NIC assigned that label. If all network labels in this list have reached their maximum count, this desktop will have further provisioned machines assigned the last label in the list over capacity, and an error will be logged. Not all labels need be configured.   
  
NOTE: Any changes to these settings will be applicable only to machines provisioned after the change. Already provisioned machines will never have their network label assignments altered by this feature.   


 * This property need not be set.

  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

