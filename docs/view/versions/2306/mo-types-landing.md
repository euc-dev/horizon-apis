---
layout: page
title: Service Types Overview
hide:
#- navigation
- toc
---

All service types are listed in the [Service Types index page](index-mo_types.md). Click a name to display the reference documentation for the service.

To quickly find any entry, start typing its name in the **Search Bar** or goto the [Service Types index page](index-mo_types.md).

## Service ManagedObjectReferences

Both the type and value of the [ManagedObjectReference](vmodl.ManagedObjectReference.md) for a service will be the name of the service.

If the [Connection](index.md#connecting-to-the-api) class is used it can provide an instance of a particular service using the class object for that service.

```
PersistentDisk persistentDisk = connection.get(PersistentDisk.class);
```

## Update Methods

If a service has an update method this allows the user to update only a subset of the properties of the object. This is represented as a set of name value pairs, with the name being the [Property Name](do-types-landing.md#cname) of the property to be updated along with the new value. These are presented as an array of [MapEntry](vdi.util.MapEntry.md) objects. The documentation for each update method will specify the base object these property names will be based on.

The client library provides functionality to wrap a data object and track changes made to that object. This will track all changes made through the Client object and will push the updates to the server when the update method of that object is called.

Additionally, the service client class will provide a convenience update function to update a single property. The simplest example of this would be enabling or disabling a resource.

### Example: Adding a Syslog UDP network receiver (and enabling UDP transmission)

```
SyslogInfo info = syslog.get();

String[] networkAddresses = info.getUdpData().getNetworkAddresses();
String[] updatedNetworkAddresses = ...; // Copy network addresses, allocate one new cell at beginning.
updatedNetworkAddresses[0] = "<udp-network-address>";

MapEntry enabledUpdate = new MapEntry();
enabledUpdate.key = "udpData.enabled";
enabledUpdate.value = true;

MapEntry networkAddressesUpdate = new MapEntry();
networkAddressesUpdate.key = "udpData.networkAddresses";
networkAddressesUpdate.value = updatedNetworkAddresses;

syslog.update(new MapEntry[] { enabledUpdate, networkAddressesUpdate });
```

```
SyslogInfoClient info = SyslogClient.read(connection);

// List is unmodifiable
List networkAddresses = info.getUdpData().getNetworkAddresses();
List updatedNetworkAddresses = new ArrayList<>(networkAddresses);
updatedNetworkAddresses.add("<udp-network-address>");

UDPDataClient udpData = info.getUdpData();
udpData.setEnabled(true);
udpData.setNetworkAddresses(updatedNetworkAddresses);
info.update(connection);
```

### Example: Enabling a desktop

```
MapEntry enabledUpdate = new MapEntry();
enabledUpdate.key = "desktopSettings.enabled";
enabledUpdate.value = true;
desktop.update(id, new MapEntry[] { enabledUpdate });
```

```
DesktopInfoClient info = DesktopClient.read(connection, id);
info.getSettings().setEnabled(true);
info.update(connection);
```

```
DesktopClient.update(connection, id, DesktopInfoCName.DESKTOP_INFO_CNAME.desktopSettings.enabled, true);
```

[Back to Home](index.md)



 
