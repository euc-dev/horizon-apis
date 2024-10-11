---
layout: page
title: Service - LogonTiming
hide:
 #- navigation
 - toc
---

  
  
  



Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.helpdesk.LogonTiming`

See also  
> [LogonSegmentRecord](vdi.helpdesk.LogonTiming.LogonSegmentRecord.md), [SessionId](vdi.entity.SessionId.md)

Since  
> Horizon 7.2


  


## Service Description

Methods

Methods defined in this Service   
---  
LogonTiming_GetClientLogonTimingData, LogonTiming_GetLogonSegment  
  



Retrieves the session timing data from endpoint machine registry. The result is a JSON string which includes timings of all phases of session log on. This information is recorded in Events Database. The interface provides an easy way to get it.  
The timings are organized as a tree in following format.   
v1  
-broker  
\--existingSessionSearch (LMV only)  
\--brokerLaunch-{targetId} (LMV only)  
\--brokerLaunch{-targetId / null} (LMV remote/local launch success)  
\---machineSelection  
\---machinePowerOn  
\----brokerStartVmOp  
\-----vcConnect  
\-----prepareVmStart  
\-----vcExecuteVmStart  
\----agentStart  
\----agentReady  
\---raiseTunnel (local launch only)  
\---machinePrepare  
\----agentPrepare   
\-----userScript  
\-----protocolStartup  
\--raiseTunnel (LMV only)  
-agent  
\--clientConnectWait  
\--clientLogon  
\---userProfile  
\----hiveLoad  
\----profileSync  
\---userGpo  
\---hellLoad  
\--appLaunch  
  
  
Every phase includes the following fields: 

  * u: unaccounted time.
  * d: duration.
  * s: start time.
  * e: end time.
  * unadjusted-s: start timestamp from desktop VM
  * unadjusted-e: end timestamp from desktop VM
  * unadjusted-d: duration calculated by unadjusted-e and unadjusted-s

  
  
All phases are listed in the following table.  Parent | Breakdown | Description  
---|---|---  
root | broker | Total time spent on broker processing XML request  
broker | authentication | Time spent checking that client is still authenticated. This is normally not present because the duration is zero  
broker | existingSessionSearch | CPA only. Broker handling client request synchronously tries other brokers in pod until request is handled.  
broker | brokerLaunch{-id} | Parent breakdown for various launch/reconnect activities. When CPA is enabled the {-id} is present and multiple brokerLaunch breakdowns can be present. Only one broker will successfully handle the launch/reconnect, the other entries are time taken probing brokers that can not fulfil the request.  
broker \ brokerLaunch{-id} | machineSelection | Search for best matching VM that can fulfil the launch/reconnect.   
broker \ brokerLaunch{-id} \ machineSelection | machinePowerOn | Total time taken to startup a VM. This includes booting the OS, or resuming a suspended machine, and View agent signally it's ready for a connection.  
broker \ brokerLaunch{-id} \ machineSelection \ machinePowerOn | brokerStartVmOp | Time taken to instruct vSphere to perform the power on operation  
broker \ brokerLaunch{-id} \ machineSelection \ machinePowerOn \ brokerStartVmOp | vcConnect, prepareVmStart, vcExecuteVmStart | vSphere connect, prepare and start power on operation  
broker \ brokerLaunch{-id} \ machineSelection \ machinePowerOn | agentStart | Time for machine start, OS to boot and agent to startup  
broker \ brokerLaunch{-id} \ machineSelection \ machinePowerOn | agentReady | Time between agent startup completion and agent ready to accept connections  
broker \ brokerLaunch{-id} \ machineSelection \ machinePowerOn | brokerStartVmPostOp | Post processing after agent ready and broker continues on  
broker \ brokerLaunch{-id} | raiseTunnel | Instruct Security Server to prepare a tunnel connection.  
broker \ brokerLaunch{-id} | sessionScript | Run broker session script  
broker \ brokerLaunch{-id} | machinePrepare | Once a VM is selected the broker contacts the VM agent to prepare it for an incoming connection  
broker \ brokerLaunch{-id} \ machinePrepare | agentPrepare | Timing taken on the agent and prepare the VM for incoming connection   
broker \ brokerLaunch{-id} \ machinePrepare \ agentPrepare | userScript | Time take to run user defined script  
broker \ brokerLaunch{-id} \ machinePrepare \ agentPrepare | protocolStartup | Time taken to startup the protocol; PCoIP, Blast or RDP  
root | agent | Total time spent on agent to process a launch/reconnect  
agent | clientConnectWait | The time betwee agentPrepare completing and View Client connecting. At this point the client has opened a socket, and authenticated to the Windows machine,  
agent | clientLogon | Time taken to create a Windows session  
agent \ clientLogon | userProfile | Time Windows user profile processing  
agent \ clientLogon \ userProfile | profileSync | In the case of roaming profile this is the time Windows takes to download user profile  
agent \ clientLogon \ userProfile | hiveLoad | Time Windows takes to load user registry hive  
agent \ clientLogon | userGpo | Windows Group Policy processing  
agent \ clientLogon | shellLoad | How long does it take to load the Windows shell (i.e. explorer.exe)   
agent | appLaunch | For RSDH this times application launching. This only times how long it takes to start the process, not when the application is initialized and functioning.  
**Please Note** , the format of the JSON returned may change between releases. 

Privileges 

Privilege |  Description   
---|---  
MACHINE_VIEW|  Machine read with the corresponding access group permission is sufficient to get a session's timing data.   
POOL_VIEW|  Desktop read with the corresponding access group permission is sufficient to get a session's timing data.   
FEDERATED_SESSIONS_VIEW|  Global session read is sufficient to get a session's timing data.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [LogonTiming](vdi.helpdesk.LogonTiming.md) used to make the method call.   
**id**| [SessionId](vdi.entity.SessionId.md)|  SessionID to get the timing data for.   
  
  


Return Value 

Type |  Description   
---|---  
xsd:string| Session timing data when View client logs on.  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



Retrieves the session timing data from Events Database. The result is a JSON string which includes timings of all phases of session log on. The timings are organized as a tree in following format.   
v1  
-broker  
\--existingSessionSearch (LMV only)  
\--brokerLaunch-{targetId} (LMV only)  
\--brokerLaunch{-targetId / null} (LMV remote/local launch success)  
\---machineSelection  
\---machinePowerOn  
\----brokerStartVmOp  
\-----vcConnect  
\-----prepareVmStart  
\-----vcExecuteVmStart  
\----agentStart  
\----agentReady  
\---raiseTunnel (local launch only)  
\---machinePrepare  
\----agentPrepare   
\-----userScript  
\-----protocolStartup  
\--raiseTunnel (LMV only)  
-agent  
\--clientConnectWait  
\--clientLogon  
\---userProfile  
\----hiveLoad  
\----profileSync  
\---userGpo  
\---hellLoad  
\--appLaunch  
  
  
Every phase includes the following fields: 

  * u: unaccounted time.
  * d: duration.
  * s: start time.
  * e: end time.
  * unadjusted-s: start timestamp from desktop VM
  * unadjusted-e: end timestamp from desktop VM
  * unadjusted-d: duration calculated by unadjusted-e and unadjusted-s

  
  
All phases are listed in the following table.  Parent | Breakdown | Description  
---|---|---  
root | broker | Total time spent on broker processing XML request  
broker | authentication | Time spent checking that client is still authenticated. This is normally not present because the duration is zero  
broker | existingSessionSearch | CPA only. Broker handling client request synchronously tries other brokers in pod until request is handled.  
broker | brokerLaunch{-id} | Parent breakdown for various launch/reconnect activities. When CPA is enabled the {-id} is present and multiple brokerLaunch breakdowns can be present. Only one broker will successfully handle the launch/reconnect, the other entries are time taken probing brokers that can not fulfil the request.  
broker \ brokerLaunch{-id} | machineSelection | Search for best matching VM that can fulfil the launch/reconnect.   
broker \ brokerLaunch{-id} \ machineSelection | machinePowerOn | Total time taken to startup a VM. This includes booting the OS, or resuming a suspended machine, and View agent signally it's ready for a connection.  
broker \ brokerLaunch{-id} \ machineSelection \ machinePowerOn | brokerStartVmOp | Time taken to instruct vSphere to perform the power on operation  
broker \ brokerLaunch{-id} \ machineSelection \ machinePowerOn \ brokerStartVmOp | vcConnect, prepareVmStart, vcExecuteVmStart | vSphere connect, prepare and start power on operation  
broker \ brokerLaunch{-id} \ machineSelection \ machinePowerOn | agentStart | Time for machine start, OS to boot and agent to startup  
broker \ brokerLaunch{-id} \ machineSelection \ machinePowerOn | agentReady | Time between agent startup completion and agent ready to accept connections  
broker \ brokerLaunch{-id} \ machineSelection \ machinePowerOn | brokerStartVmPostOp | Post processing after agent ready and broker continues on  
broker \ brokerLaunch{-id} | raiseTunnel | Instruct Security Server to prepare a tunnel connection.  
broker \ brokerLaunch{-id} | sessionScript | Run broker session script  
broker \ brokerLaunch{-id} | machinePrepare | Once a VM is selected the broker contacts the VM agent to prepare it for an incoming connection  
broker \ brokerLaunch{-id} \ machinePrepare | agentPrepare | Timing taken on the agent and prepare the VM for incoming connection   
broker \ brokerLaunch{-id} \ machinePrepare \ agentPrepare | userScript | Time take to run user defined script  
broker \ brokerLaunch{-id} \ machinePrepare \ agentPrepare | protocolStartup | Time taken to startup the protocol; PCoIP, Blast or RDP  
root | agent | Total time spent on agent to process a launch/reconnect  
agent | clientConnectWait | The time betwee agentPrepare completing and View Client connecting. At this point the client has opened a socket, and authenticated to the Windows machine,  
agent | clientLogon | Time taken to create a Windows session  
agent \ clientLogon | userProfile | Time Windows user profile processing  
agent \ clientLogon \ userProfile | profileSync | In the case of roaming profile this is the time Windows takes to download user profile  
agent \ clientLogon \ userProfile | hiveLoad | Time Windows takes to load user registry hive  
agent \ clientLogon | userGpo | Windows Group Policy processing  
agent \ clientLogon | shellLoad | How long does it take to load the Windows shell (i.e. explorer.exe)   
agent | appLaunch | For RSDH this times application launching. This only times how long it takes to start the process, not when the application is initialized and functioning.  
  
Privileges 

Privilege |  Description   
---|---  
MACHINE_VIEW|  Machine read permission is sufficient to get session's timing data.   
POOL_VIEW|  Pool read permission is sufficient to get session's timing data.   
FEDERATED_SESSIONS_VIEW|  Global session read permission is sufficient to get session's timing data.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [LogonTiming](vdi.helpdesk.LogonTiming.md) used to make the method call.   
**sessionId**| [SessionId](vdi.entity.SessionId.md)|    
  
  


Return Value 

Type |  Description   
---|---  
[LogonSegmentRecord](vdi.helpdesk.LogonTiming.LogonSegmentRecord.md)| Session timing data  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  
  
  
  
  
