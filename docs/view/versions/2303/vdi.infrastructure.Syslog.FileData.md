---
layout: page
title: Data Object - SyslogFileData
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.infrastructure.Syslog.FileData`

Property of
> [SyslogInfo](vdi.infrastructure.Syslog.SyslogInfo.md#field_detail)

See also
> [SecureString](vdi.util.SecureString.md)

Since
> Horizon View 6.0


## Data Object Description

Configuration relevant to file based syslog logging.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**enabled**|  xsd:boolean|  Whether or not local/remote file based logging is enabled for all events.
**enabledOnError**|  xsd:boolean|  Whether or not local/remote file based logging is enabled for audit events when there is any error in writing events to EventDatabase or syslog. Note that if both attributes [enabled](vdi.infrastructure.Syslog.FileData.md#enabled) and [enabledOnError](vdi.infrastructure.Syslog.FileData.md#enabledOnError) are set, then precedence would be given to [enabled](vdi.infrastructure.Syslog.FileData.md#enabled).  **_Since_** Horizon 7.9 [^1]
**uncPath**|  xsd:string|  The remote UNC path for syslog to move files. If null, logs are local only. This field is required if any of the uncUserName, uncPassword, uncDomain is set. [^1]
**uncUserName**|  xsd:string|  The remote UNC user name. This field is required if any of the uncPath, uncPassword, uncDomain is set. [^1]
**uncPassword**| [SecureString](vdi.util.SecureString.md)|  The remote UNC password. This field is required if uncUserName is set. [^1]
**uncDomain**|  xsd:string|  The remote UNC domain. [^1]
 


 


[^1]: This property need not be set.