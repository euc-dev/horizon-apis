---
layout: page
title: Data Object Types Overview
hide:
 #- navigation
 - toc
---


All data object types are listed in the [Data Types Index Page](index-do_types.md). Click a name to display the reference documentation for the data object. Reference documentation for data object types typically includes: 

  * Description of purpose and usage.
  * Names of properties and their data types that comprise the data object type (the so-called members of the data object type).

To quickly find any entry, start typing its name in the **Search Bar**. 

### Property Names

The name of a property is a commonly used value in View API. It is used in update methods, query filters, and query sorting. This will be the dotted path from the root object (either the Info object for the service or the queryable data object) to the property.

To aid in the development of client code, many data object types have a corresponding **CName** (for "canonical name") class accompanying them. This class provides both compile time verification that a given property name is valid, as well as compile time type checking when paired with a possible value.

For updatable and queryable types a static instance is provided in each class.
    
```
    RDSServerInfoCName INFO_CNAME = RDSServerInfoCName.RDS_SERVER_INFO_CNAME;
    CName<Boolean> ENABLED_CNAME = INFO_CNAME.settings.enabled;
    String ENABLED_PROPERTY_NAME = ENABLED_CNAME.cname(); // provides "settings.enabled"
```

[Back to Home](index.md)
