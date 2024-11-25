---
layout: page
title: Data Object - CertificateSSOEnrollmentServerInfo
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.infrastructure.CertificateSSOEnrollmentServer.CertificateSSOEnrollmentServerInfo`

Returned by
> [CertificateSSOEnrollmentServer_Get](vdi.infrastructure.CertificateSSOEnrollmentServer.md#get), [CertificateSSOEnrollmentServer_List](vdi.infrastructure.CertificateSSOEnrollmentServer.md#list)

See also
> [CertificateSSOEnrollmentServerData](vdi.infrastructure.CertificateSSOEnrollmentServer.CertificateSSOEnrollmentServerData.md), [CertificateSSOEnrollmentServerId](vdi.entity.CertificateSSOEnrollmentServerId.md)

Since
> Horizon 7.0


## Data Object Description

Configuration info for a Certificate SSO Enrollment Server.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**id**| [CertificateSSOEnrollmentServerId](vdi.entity.CertificateSSOEnrollmentServerId.md)|  Reference to this Enrollment Server. [^2]
**data**| [CertificateSSOEnrollmentServerData](vdi.infrastructure.CertificateSSOEnrollmentServer.CertificateSSOEnrollmentServerData.md)|  Configuration data for a Certificate SSO Enrollment Server.


 


[^2]: This property cannot be updated.