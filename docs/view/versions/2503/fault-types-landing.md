---
layout: page
title: Fault Types Overview
hide:
#  - navigation
  - toc
---

A **fault** type is a data structure that conveys information about errors, such as processing errors, raised by the server. Information can include the nature of the problem, such as “[InsufficientPermission](../2406/vdi.fault.InsufficientPermission.md)” or “[InvalidArgument](../2406/vdi.fault.InvalidArgument.md).”

For example, an [InsufficientPermission](../2406/vdi.fault.InsufficientPermission.md) fault is returned to the client by the server when it denies an operation due to insufficient client privileges. Note that the [InsufficientPermission](../2406/vdi.fault.InsufficientPermission.md) fault includes a property (object) comprising the [EntityId](../2406/vdi.EntityId.md) of the target entity for which the client has insufficient privileges.

To quickly find any entry, start typing its name in the **Search Bar** or goto the [All Fault Types](index-faults.md) page. Click a name to display reference documentation for a given fault type. Documentation may include:

* Name of the operation that raised the fault.
* The fault type from which the fault extends.
* Descendent fault types.
* Description of purpose and usage.
* Privileges required to generate the fault.
* Parameters this fault type accepts.
* Values this fault type returns.

[Back to Home](index.md)



 
