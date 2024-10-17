---
layout: page
title: Data Object - GSSAPIAuthenticatorSpec
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.infrastructure.GSSAPIAuthenticator.GSSAPIAuthenticatorSpec`

Parameter to  
> [GSSAPIAuthenticator_Create](vdi.infrastructure.GSSAPIAuthenticator.md#create)

See also  
> [ConnectionServerId](vdi.entity.ConnectionServerId.md), [GSSAPIAuthenticatorGeneralData](vdi.infrastructure.GSSAPIAuthenticator.GeneralData.md)

Since  
> Horizon 7.13


## Data Object Description 

The specification for creating a GSSAPI authenticator. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**general**| [GSSAPIAuthenticatorGeneralData](vdi.infrastructure.GSSAPIAuthenticator.GeneralData.md)|  General data on the GSSAPI Authenticator.   
  
**connectionServers**| [ConnectionServerId[]](vdi.entity.ConnectionServerId.md)|  The list of Connection Servers for which this GSSAPI authenticator is enabled.   


  [^14]

  
  
  
 
  
  


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^3]: This property must contain only alphanumerics, spaces, underscores, and dashes. The maximum length is 32 characters.
[^4]: This property has a maximum length of 400 characters.
[^5]: This property has a default value of false.
[^6]: This property has a default value of true.
[^7]: If specified, this property is limited to letters, numbers, punctuation, spaces, and tabs.
[^8]: This property has a minimum value of 1.
[^9]: This property is required if maxSessionsType is set to 'LIMITED'.
[^10]: This property has a default value of 1.
[^11]: This property must contain only alphanumerics, underscores, and dashes. The maximum length is 64 characters.
[^12]: This property has a maximum length of 256 characters.
[^13]: This property has a maximum length of 1024 characters.
[^14]: This property is an unordered array of unique values.
[^15]: This property is required if enableAntiAffinityRules is set to true.
[^16]: This property has a maximum value of 20.
[^17]: This property has a default value of 'DISABLED'.
[^18]: This property is required if multiSessionMode is set to 'ENABLED_DEFAULT_OFF', 'ENABLED_DEFAULT_ON', or 'ENABLED_ENFORCED'.
[^19]: This property has a default value of 0.
[^20]: This property cannot contain ? characters.
[^21]: This property must contain the time in 24 hours format. e.g. 14:30.
[^22]: This property must be in the form hh:mm in 24 hours format.
[^23]: This property is required if customizationType is set to 'NONE'.
[^24]: This property is required if customizationType is set to 'SYS_PREP'.
[^25]: This property is required if customizationType is set to 'QUICK_PREP'.
[^26]: This property is required if type is set to 'MANUAL'.
[^27]: This property is required if type is set to 'RDS'.
[^28]: This property has a default value of 'DESKTOP'.
[^29]: This property is required if type is set to 'AUTOMATED'.
[^30]: This property has a default value of ['PCOIP', 'RDP', 'BLAST'].
[^31]: This property is required if operation is set to 'INITIAL_PUBLISH', 'SCHEDULE_PUSH_IMAGE', 'CANCEL_SCHEDULED_PUSH_IMAGE', or 'INFRASTRUCTURE_CHANGE'.
[^32]: This property is required if operation is set to 'SCHEDULE_PUSH_IMAGE'.
[^33]: For Instant clone desktops this setting can only be set to ALWAYS_POWERED_ON.
[^34]: This property has a default value of 'TAKE_NO_POWER_ACTION'.
[^35]: This property has a default value of 'NEVER'.
[^36]: This property has a default value of 120.
[^37]: This property is required if automaticLogoffPolicy is set to 'AFTER'.
[^38]: This is applicable for automated desktops with virtual machines names based on pattern naming. This is not applicable for desktops that are using specified naming since dynamic creation and deletion of VMs is not supported.
[^39]: For Instant clone desktops this setting can only be set to DELETE.
[^40]: This property is required if refreshOsDiskAfterLogoff is set to 'EVERY'.
[^41]: This property has a maximum value of 100.
[^42]: This property is required if refreshOsDiskAfterLogoff is set to 'AT_SIZE'.
[^43]: This property has a default value of 'AFTER'.
[^44]: This property is required if emptySessionTimeoutPolicy is set to 'AFTER'.
[^45]: This property has a default value of 10.
[^46]: This property has a minimum value of 10.
[^47]: This property is required if preLaunchSessionTimeoutPolicy is set to 'AFTER'.
[^48]: This property has a default value of 'DEFAULT'.
[^49]: This property has a default value of 'BLOCK_ACCESS'.
[^50]: This property is required if source is set to 'VIRTUAL_CENTER'.
[^51]: For Instant clone desktops this setting can only be set to false.
[^52]: This property is required if overrideGlobalSetting is set to true.
[^53]: This property is required if enabled is set to true.
[^54]: This property is required if maxLabelType is set to 'LIMITED'.
[^55]: This property has a default value of 4096.
[^56]: This property has a minimum value of 512.
[^57]: This property is required if redirectDisposableFiles is set to true.
[^58]: This property has a default value of Auto.
[^59]: This property must be single letters from D to Z or the word Auto.
[^60]: This property is required if redirectDisposableFiles is set to true.
[^61]: This property has a default value of 96.
[^62]: This property has a minimum value of 64.
[^63]: This property has a maximum value of 512.
[^64]: This property is required if renderer3D is set to 'AUTOMATIC', 'SOFTWARE', or 'HARDWARE'.
[^65]: This property has a default value of 2.
[^66]: This property has a maximum value of 4.
[^67]: This property is required if renderer3D is set to 'AUTOMATIC', 'SOFTWARE', 'HARDWARE', or 'DISABLED'.
[^68]: This property has a default value of 'WUXGA'.
[^69]: This property is required if renderer3D is set to 'AUTOMATIC', 'SOFTWARE', 'HARDWARE', or 'DISABLED'.
[^70]: This property must contain only alphanumerics and dashes. It must contain at least one alpha character. It may also optionally contain a numeric placement token {n} or {n:fixed=#}. If the pattern does not specify the numeric placement token, the maximum length is 14 characters.
[^71]: This property has a default value of 'UP_FRONT'.
[^72]: This property has a minimum value of 0.
[^73]: This property is required if provisioningTime is set to 'ON_DEMAND'.
[^74]: This property is required if redirectWindowsProfile is set to true.
[^75]: This property is required if useSeparateDatastoresPersistentAndOSDisks is set to true.
[^76]: This property has a default value of 2048.
[^77]: This property has a minimum value of 128.
[^78]: This property has a default value of D.
[^79]: This property is required if reclaimVmDiskSpace is set to true.
[^80]: This property must contain only alphanumerics and dashes. It must contain at least one alpha character. The maximum length is 15 characters.
[^81]: This property is required if userAssignment is set to 'DEDICATED'.
[^82]: Fast NFS Clones (VAAI) will be unavailable if the Replica disks are stored separately from the OS disks.
[^83]: Datastores with file system type VVOL will also be unavailable if the Replica disks are stored separately from the OS disks.
[^84]: This setting is applicable to both View Composer and Instant clone engine sourced desktops.
[^85]: For Instant clone desktops, this can be modified only if there are no current operations ( [operation](vdi.resources.Desktop.InstantCloneProvisioningStatusData.md#operation) is NONE).
[^86]: This property is required if useSeparateDatastoresReplicaAndOSDisks is set to true.
[^87]: For Instant clone desktops, this setting can only be set to false.
[^88]: This is applicable only to Virtual Center, View Composer, or Instant Clone Engine sourced manual or automatic desktops.
[^89]: If true, VirtualCenter.StorageAcceleratorData#enabled must also be enabled.
[^90]: This value cannot be updated for Instant Clone Engine sourced desktops.
[^91]: This property has a default value of 'OS_DISKS'.
[^92]: This property is required if useViewStorageAccelerator is set to true.
[^93]: This property has a default value of 7.
[^94]: This property has a maximum value of 999.
[^95]: For Instant clone desktops, this setting can only be set to UNBOUNDED.
[^96]: This property has a default value of 'CONSERVATIVE'.
[^97]: This property has a default value of 'VM'.
[^98]: For Instant clone desktops only it can be only a cluster and not a host.
[^99]: For Instant clone desktops, this can be modified only if there are no current operations ( [operation](vdi.resources.Desktop.InstantCloneProvisioningStatusData.md#operation) is NONE).
[^100]: If the naming method is PATTERN, this value must be less than [minNumberOfMachines](vdi.resources.Desktop.PatternNamingSettings.md#minNumberOfMachines). If the naming method is SPECIFIED and this is a create, this value must be less than the number of specified names. If the naming method is SPECIFIED and this value is updated, it must be less than the total number of existing machines in the desktop. The above checks are not done if this value is 0.
[^101]: For Full clone desktops, if Storage DRS cluster is used then it can only have one element.
[^102]: This property is required if namingMethod is set to 'PATTERN'.
[^103]: This property is required if namingMethod is set to 'SPECIFIED'.
[^104]: For Instant clone desktops, this setting can only be set to PATTERN.
[^105]: License is not applied to the system.
[^106]: Applied license is expired.
[^107]: Applied license does not have instant clone feature enabled.
[^108]: This parameter is an update map based on [DesktopInfo](vdi.resources.Desktop.DesktopInfo.md 'DesktopInfo').
[^109]: Both instant and linked clones share the same base image and use less storage space than full virtual machines.
[^110]: The user profile for both types clones can be redirected to persistent disks that will be unaffected by OS updates and refreshes.
[^111]: This property has a default value of 'PCOIP'.
[^112]: This property is required if enableGRIDvGPUs is set to true.
[^113]: This property has a default value of 'LIMITED'.
[^114]: This property is required if operation is set to 'INITIAL_PUBLISH', 'CANCEL_SCHEDULED_MAINTENANCE', or 'INFRASTRUCTURE_CHANGE'.
[^115]: This property has a maximum value of 100.
[^116]: This property has a maximum value of 150.
[^117]: This property is required if useCustomScript is set to false.
[^118]: This property is required if maintenanceMode is set to 'RECURRING'.
[^119]: This property has a maximum value of 31.
[^120]: This property is required if maintenancePeriod is set to 'WEEKLY' or 'MONTHLY'.
[^121]: This property has a default value of 'NEVER'.
[^122]: This property is required if disconnectedSessionTimeoutPolicy is set to 'AFTER'.
[^123]: This property has a minimum value of 10.
[^124]: This property has a default value of 'VM'.
[^125]: For Instant clone farms only it can be only a cluster and not a host.
[^126]: For Instant clone farms, this can be modified only if there are no current operations ( [operation](vdi.resources.Farm.InstantCloneProvisioningStatusData.md#operation) is NONE).
[^127]: This must be between 1 and 255 characters.
[^128]: This property has a maximum length of 64 characters.
[^129]: This property has a default value of 'ANY'.
[^130]: This property has a default value of 'NONE'.
[^131]: This property has a default value of ['PCOIP', 'BLAST'].
[^132]: This property defines valid folder names with a max length of 64 characters and up to 4 subdirectory levels. The subdirectories can be specified using a backslash, e.g. (dir1\dir2\dir3\dir4). Folder names can't start or end with a backslash nor can there be 2 or more backslashes together. Combinations such as (\dir1, dir1\dir2\, dir1\\dir2, dir1\\\dir2) are invalid. The windows reserved keywords (CON, PRN, NUL, AUX, COM1 - COM9, LPT1 - LPT9 etc.) are not allowed in subdirectory names.

[^133]: This property has a default value of "AFTER."
[^134]: This property has a default value of "UNCONFIGURED".
[^135]: This parameter need not be set.
[^136]: This parameter is an update map based on [RoleInfo](vdi.users.Role.RoleInfo.md "RoleInfo").
[^137]: This parameter is an update map based on [SecondaryCredentialsInfo](vdi.users.SecondaryCredentials.SecondaryCredentialsInfo.md "SecondaryCredentialsInfo").
[^138]: This property is required if hybridLogonConfig is set to "password".
[^139]: This property has a maximum value of 65535.
[^140]: This property must be a valid IP address or DNS name.
[^141]: This property must be a valid DNS name.
[^142]: This parameter is an update map based on [ADDomainInfo](vdi.utils.ADDomain.ADDomainInfo.md "ADDomainInfo").
[^143]: This property must not be empty and has a maximum length of 256 characters.
[^144]: Image management stream is in AVAILABLE or PARTIALLY_AVAILABLE state.
[^145]: There is at least one image management version in AVAILABLE or PARTIALLY_AVAILABLE state for this stream.
[^146]: There is at least one image management tag associated with the image management version.
[^147]: This parameter is an update map based on [ImageManagementStreamInfo](vdi.utils.imagemanagement.ImageManagementStream.ImageManagementStreamInfo.md "ImageManagementStreamInfo").
[^148]: This property must contain only alphanumerics, underscores and dashes. The maximum length is 64 characters.
[^149]: This parameter is an update map based on [ImageManagementTagInfo](vdi.utils.imagemanagement.ImageManagementTag.ImageManagementTagInfo.md "ImageManagementTagInfo").
[^150]: This property must contain only alphanumerics, dot, underscores, and dashes. The maximum length is 64 characters.
[^151]: This parameter is an update map based on [ImageManagementVersionInfo](vdi.utils.imagemanagement.ImageManagementVersion.ImageManagementVersionInfo.md "ImageManagementVersionInfo").
[^152]: This property must not be empty and has a maximum length of 256 characters.
[^153]: This parameter is an update map based on [InstantCloneEngineDomainAdministratorInfo](vdi.utils.InstantCloneEngineDomainAdministrator.InstantCloneEngineDomainAdministratorInfo.md "InstantCloneEngineDomainAdministratorInfo").
[^154]: This property is required if logCollectorComponentType is set to "CONNECTION_SERVER".
[^155]: This property is required if logCollectorComponentType is set to "AGENT_RDS".
[^156]: This property is required if logCollectorComponentType is set to "AGENT_RDS".
[^157]: This property has a default value of ["DEFAULT"].
[^158]: This property is required if reset is set to false.
[^159]: Contains null for which the request is processed successfully.
[^160]: [LogCollectorFault](vdi.fault.LogCollectorFault.md) for failed ones.
[^161]: Contains array of [LogCollectorTaskInfo](vdi.utils.logcollector.LogCollector.LogCollectorTaskInfo.md) for which the request is processed successfully.
[^162]: All available log collector task information is returned if no parameter used.
[^163]: Log collector task information for specified user returned if parameter used.
[^164]: This property has a default value of 5.
[^165]: If the [type](vdi.utils.Validator.ValidationSpec.md#type) is "MACHINE", then the naming pattern for the machines will be validated.
[^166]: This parameter is an update map based on [ViewComposerDomainAdministratorInfo](vdi.utils.viewcomposer.ViewComposerDomainAdministrator.ViewComposerDomainAdministratorInfo.md "ViewComposerDomainAdministratorInfo").
[^167]: This data object must be updated as a whole.
[^168]: This property is required if source is set to "VIEW_COMPOSER" or "INSTANT_CLONE_ENGINE".
[^169]: This property is required if source is set to "FULL_CLONE".
[^170]: This value will be considered only in case of Dedicated Linked Pool.
[^171]: It will be ignored for other Pools and Farms.
[^172]: This property is required if isPersistent is set to true.
[^173]: Applicable only in case of Linked Clones and Instant Clones.
[^174]: Set to true only in case of DEDICATED LINKED_CLONE Pool.
[^175]: It will be ignored in case of Farms and other Pools.
[^176]: This property has a default value of 1024.
[^177]: This property has a minimum value of 100.
[^178]: This property has a maximum value of 32768.
[^179]: This property is required if viewComposerType is set to "LOCAL_TO_VC" or "STANDALONE".
[^180]: This property has a default value of "GENERAL".
[^181]: This property cannot contain forward slashes.
[^182]: This parameter is an update map based on [ApplicationInfo](vdi.resources.Application.ApplicationInfo.md "ApplicationInfo").
[^183]: This property has a default value of "NO_CONTROL".
[^184]: This property has a default value of "AFTER".
[^185]: This property must be single letters from D to Z.
[^186]: This parameter is an update map based on [FarmInfo](vdi.resources.Farm.FarmInfo.md "FarmInfo").
[^187]: For Instant clone farms, this can be modified only if there are no current operations ( [operation](vdi.resources.Farm.InstantCloneProvisioningStatusData.md#operation) is NONE).
[^188]: This parameter is an update map based on [RoleInfo](vdi.users.Role.RoleInfo.md "RoleInfo").
[^189]: This property has a maximum value of 65535.
[^190]: This parameter is an update map based on [ADDomainInfo](vdi.utils.ADDomain.ADDomainInfo.md "ADDomainInfo").
[^191]: This parameter is an update map based on [ImageManagementAssetInfo](vdi.utils.imagemanagement.ImageManagementAsset.ImageManagementAssetInfo.md "ImageManagementAssetInfo").

[^192]: This property is required if configured is set to true.
[^193]: For Instant clone desktops, this setting can only be set to false.
[^194]: This parameter is an update map based on [MachineInfo](vdi.resources.Machine.MachineInfo.md "MachineInfo").
[^195]: This parameter is an update map based on [PersistentDiskInfo](vdi.resources.PersistentDisk.PersistentDiskInfo.md "PersistentDiskInfo").
[^196]: This property must contain only alphanumerics, underscores, and dashes. It must contain at least one alpha character. The maximum length is 15 characters.
[^197]: This property has a default value of 1000.
[^198]: This parameter is an update map based on [RDSServerInfo](vdi.resources.RDSServer.RDSServerInfo.md "RDSServerInfo").
[^199]: Admin user has single role which is of type either HELP_DESK_ADMIN or HELP_DESK_ADMIN_READ_ONLY.
[^200]: This parameter is an update map based on [PoliciesSettings](vdi.users.Policies.PoliciesSettings.md "PoliciesSettings").
[^201]: This property is required if allowPCoIPHardwareAcceleration is set to "Allow".
[^202]: This property is required if logCollectorComponentType is set to "AGENT".
[^203]: This property is required if type is set to "APPLICATION".
[^204]: This property is required if type is set to "DESKTOP".
[^205]: This parameter is an update map based on [URLRedirectionInfo](vdi.infrastructure.URLRedirection.URLRedirectionInfo.md "URLRedirectionInfo").
[^206]: This property has a default value of 20.
[^207]: This property has a default value of 50.
[^208]: This property has a default value of 12.
[^209]: This parameter is an update map based on [VirtualCenterInfo](vdi.infrastructure.VirtualCenter.VirtualCenterInfo.md "VirtualCenterInfo").
[^210]: [user](vdi.resources.Desktop.SpecifiedName.md#user) is provided.
[^211]: [enabled](vdi.resources.Desktop.DesktopSettings.md#enabled) is false.
[^212]: [supportedSessionType](vdi.resources.Desktop.DesktopSettings.md#supportedSessionType) is not "DESKTOP".
[^213]: [globalEntitlement](vdi.resources.Desktop.GlobalEntitlementData.md#globalEntitlement) is set.
[^214]: [userAssignment](vdi.resources.Desktop.UserAssignment.md#userAssignment) is "DEDICATED" and [automaticAssignment](vdi.resources.Desktop.UserAssignment.md#automaticAssignment) is false.
[^215]: Local entitlements are configured.
[^216]: Any of the machines in the pool have users assigned.
[^217]: [connectionServerRestrictions](vdi.resources.Desktop.DesktopSettings.md#connectionServerRestrictions) is not set.
[^218]: [type](vdi.resources.Desktop.DesktopSpec.md#type) is MANUAL.
[^219]: This parameter is an update map based on [MachineInfo](vdi.resources.Machine.MachineInfo.md "MachineInfo").
[^220]: Admin user has single role which is of type either HELP_DESK_ADMIN or HELP_DESK_ADMIN_READ_ONLY.
[^221]: [DesktopId](vdi.entity.DesktopId.md).
[^222]: [GlobalApplicationEntitlementId](vdi.entity.GlobalApplicationEntitlementId.md).
[^223]: [GlobalEntitlementId](vdi.entity.GlobalEntitlementId.md).
[^224]: [URLRedirectionId](vdi.entity.URLRedirectionId.md).
[^225]: [ServerSpec](vdi.utils.Certificate.ServerSpec.md).
[^226]: [SAMLAuthenticatorServerData](vdi.infrastructure.SAMLAuthenticator.ServerData.md).
[^227]: This property is a set of entries with unique "key" members.
[^228]: This parameter is an update map based on [GlobalApplicationEntitlementInfo](vdi.federation.GlobalApplicationEntitlement.GlobalApplicationEntitlementInfo.md "GlobalApplicationEntitlementInfo").
[^229]: This parameter is an update map based on [GlobalEntitlementInfo](vdi.federation.GlobalEntitlement.GlobalEntitlementInfo.md "GlobalEntitlementInfo").
[^230]: This parameter is an update map based on [PodInfo](vdi.federation.Pod.PodInfo.md "PodInfo").
[^231]: This parameter is an update map based on [PodFederationInfo](vdi.federation.PodFederation.PodFederationInfo.md "PodFederationInfo").
[^232]: This parameter is an update map based on [SiteInfo](vdi.federation.Site.SiteInfo.md "SiteInfo").
[^233]: This property has a default value of "CONNECTION_SERVER_DOMAIN".
[^234]: When all of the secure gateways (HTTP(S)/PCOIP/BLAST) are enabled, this field denotes the maximum load of connections allowed for the connection server. Once the number of connections to this connection server reaches this value, the subsequent connections from the horizon client will be blocked by secure gateway.
[^235]: The application is missing in all the machines of the desktop.
[^236]: Desktop do not have any provisioned machines.
[^237]: One or more server(s) is either in WARNING or ERROR (not exceeding the predefined threshold) state.
[^238]: The RDSServers in this Farm present a mix of both known and unknown load preferences.
[^239]: For dedicated assignment desktop, it is the number of assigned machine count.
[^240]: For floating assignment desktop, it is the summation of the connected and disconnected sessions.
[^241]: For dedicated assignments, it is the total number of assigned machine count.
[^242]: For floating assignments, it will be sum of all the connected and disconnected sessions.
[^243]: This property is required if thumbprintAccepted is set to false.
[^244]: This property is required if thumbprintAccepted is set to false.
[^245]: This parameter is an update map based on [CEIPInfo](vdi.infrastructure.CEIP.CEIPInfo.md "CEIPInfo").
[^246]: This parameter is an update map based on [CertificateSSOConnectorInfo](vdi.infrastructure.CertificateSSOConnector.CertificateSSOConnectorInfo.md "CertificateSSOConnectorInfo").
[^247]: This property has a maximum value of 59.
[^248]: This property is required if hostRedirection is set to true.
[^249]: This parameter is an update map based on [ConnectionServerInfo](vdi.infrastructure.ConnectionServer.ConnectionServerInfo.md "ConnectionServerInfo").
[^250]: This property is required if radiusEnabled is set to true.
[^251]: This property is required if samlSupport is set to "ENABLED" or "REQUIRED".
[^252]: This property is required if samlSupport is set to "MULTI_ENABLED" or "MULTI_REQUIRED".
[^253]: This property has a maximum value of 1440.
[^254]: This property has a default value of 21.
[^255]: This property has a minimum value of 14.
[^256]: This property is required if workspaceOneModeEnabled is set to true.
[^257]: This property has a default value of "SUCCESS".
[^258]: This property is required if eventDatabaseSet is set to true.
[^259]: This property must start with a letter, may only contain letters, numbers, and the characters @, $, #, and _, and may not be longer than 6 characters.
[^260]: This property has a maximum value of 3.
[^261]: This property has a default value of 2000.
[^262]: This property has a maximum value of 7.
[^263]: This parameter is an update map based on [EventDatabaseInfo](vdi.infrastructure.EventDatabase.EventDatabaseInfo.md "EventDatabaseInfo").
[^264]: One of [version](vdi.infrastructure.GlobalSettings.ClientData.md#version), [blockSpecificVersions](vdi.infrastructure.GlobalSettings.ClientData.md#blockSpecificVersions), [warnSpecificVersions](vdi.infrastructure.GlobalSettings.ClientData.md#warnSpecificVersions) is mandatory.
[^265]: Only one of [version](vdi.infrastructure.GlobalSettings.ClientData.md#version) or [blockSpecificVersions](vdi.infrastructure.GlobalSettings.ClientData.md#blockSpecificVersions) can be set.
[^266]: This property cannot be used for [type](vdi.infrastructure.GlobalSettings.ClientData.md#type) "WINSTORE", "HTMLACCESS".
[^267]: This property has a maximum length of 128 characters.
[^268]: This property accepts all characters including new line with a maximum length of 1024 characters.
[^269]: This property has a default value of 60.
[^270]: This property has a default value of "TIMEOUT_AFTER".
[^271]: This property has a default value of 600.
[^272]: This property has a minimum value of 5.
[^273]: This property is required if clientMaxSessionTimePolicy is set to "TIMEOUT_AFTER".
[^274]: This property has a default value of 15.
[^275]: This property is required if clientIdleSessionTimeoutPolicy is set to "TIMEOUT_AFTER".
[^276]: This property has a default value of 1200.
[^277]: This property is required if desktopSSOTimeoutPolicy is set to "DISABLE_AFTER".
[^278]: This property has a default value of "ALWAYS_ENABLED".
[^279]: This property is required if applicationSSOTimeoutPolicy is set to "DISABLE_AFTER".
[^280]: This property has a maximum value of 4320.
[^281]: This property is required if displayWarningBeforeForcedLogoff is set to true.
[^282]: If set true, UI clients should show a "Remember me" check box option on the login page.
[^283]: If set false, UI clients should not show the "Remember me" check box option on the login page.
[^284]: This property has a default value of 30.
[^285]: This property has a maximum value of 30.
[^286]: This property has a default value of Your virtual session is going to be logged off. Please save your work.
[^287]: This property has a default value of Your session has expired. Please re-connect to the portal and restart the session.
[^288]: This property has a default value of Attention.
[^289]: This property is required if displayPreLoginAdminBanner is set to true.
[^290]: This parameter is an update map based on [GlobalSettingsInfo](vdi.infrastructure.GlobalSettings.GlobalSettingsInfo.md "GlobalSettingsInfo").
[^291]: This parameter is an update map based on [GSSAPIAuthenticatorInfo](vdi.infrastructure.GSSAPIAuthenticator.GSSAPIAuthenticatorInfo.md "GSSAPIAuthenticatorInfo").
[^292]: This parameter is an update map based on [NetworkProxyConfigurationDetail](vdi.infrastructure.NetworkProxyConfiguration.NetworkProxyConfigurationDetail.md "NetworkProxyConfigurationDetail").
[^293]: This property is required if networkAutoProxy is set to false.
[^294]: This property has a maximum length of 50 characters.
[^295]: This property has a maximum length of 20 characters.
[^296]: This parameter is an update map based on [RADIUSAuthenticatorInfo](vdi.infrastructure.RADIUSAuthenticator.RADIUSAuthenticatorInfo.md "RADIUSAuthenticatorInfo").
[^297]: This property has a maximum length of 32 characters.
[^298]: This parameter is an update map based on [SAMLAuthenticatorInfo](vdi.infrastructure.SAMLAuthenticator.SAMLAuthenticatorInfo.md "SAMLAuthenticatorInfo").
[^299]: This property has a default value of "DYNAMIC".
[^300]: This property is required if authenticatorType is set to "DYNAMIC".
[^301]: This property is required if authenticatorType is set to "STATIC".
[^302]: This parameter is an update map based on [SecurityServerInfo](vdi.infrastructure.SecurityServer.SecurityServerInfo.md "SecurityServerInfo").
[^303]: This parameter is an update map based on [SyslogInfo](vdi.infrastructure.Syslog.SyslogInfo.md "SyslogInfo").
[^304]: When all of the secure gateways (HTTP(S)/PCOIP/BLAST) are enabled, this field denotes the maximum load of connections allowed for the connection server. Once the number of connections to this connection server reaches this value, the subsequent connections from the horizon client will be blocked by secure gateway.
[^305]: When none of the secure gateways(HTTP(S)/PCOIP/BLAST) are enabled, sessionThreshold value will not be set.
[^306]: This property has a default value of "BOTH".
[^307]: This property has a default value of On proceeding, you agree that you fully comply with the laws of this organisation.
[^308]: This property is required if triggerMode is set to "ENABLE_ALWAYS" or "REQUIRE_ALWAYS".
[^309]: For those pods running on older version(before 7.12.0), the values for [numHostedSessions](vdi.health.Monitoring.PodSessionCounter.md#numHostedSessions) and [numBrokeredSessions](vdi.health.Monitoring.PodSessionCounter.md#numBrokeredSessions) will not be set.
[^310]: When there is at least one Pod running on older version(before 7.12.0), numBrokeredSessions for all the pods will not be set.
[^311]: [ApplicationId](vdi.entity.ApplicationId.md).
[^312]: When none of the secure gateways(HTTP(S)/PCOIP/BLAST) are enabled, sessionThreshold value will not be set.