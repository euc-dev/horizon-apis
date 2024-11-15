---
layout: page
title: View API Reference Documentation - Latest
hide:
#- navigation
- toc
---
![Horizon Server](../../../assets/logos/Horizon-v-lm.png){ align=right }

Welcome to the latest version (v2406) of the View API Reference documentation. This API reference provides comprehensive information about all data structures available through the View API:

* [Service Types](versions/2406/mo-types-landing.md)  
* [Data Object Types](versions/2406/do-types-landing.md)  
* [Fault Types](versions/2406/fault-types-landing.md)  
* [All Types](versions/2406/all-types-landing.md)  
* [All Methods](versions/2406/methods-landing.md)  
* [All Properties](versions/2406/properties-landing.md)  
* [Query Service](versions/2406/queries-landing.md)  

To quickly find any entry, start typing its name in the **Search Bar**.

In addition, the documentation will outline any client library classes that makes the API easier to build against.

## Connecting to the API

The URL of the API is **https://_server-address_/view-vlsi/sdk**

### Client library

The client library provides a **Connection** class to easily connect to the API. This class will be needed to use much of the client library code.

```c#
// Uses try-with-resources to ensure connection is cleaned up after completion.
try (Connection connection = new Connection("https://_server-address_ /view-vlsi/sdk")) {
   connection.login(username, password, domain);

   // Do work
}
```

If a certificate override is needed this can be accomplished using the **HttpConfiguration** settings.

```c#
   HttpConfiguration httpConfig = HttpConfiguration.Factory.newInstance();
   httpConfig.setThumbprintVerifier(new ThumbprintVerifier() {
   
      public Result verify(String thumbprint) {
         if (acceptedThumbprint == null) {
            return Result.UNKNOWN;
         } else if (acceptedThumbprint.equals(thumbprint)) {
            return Result.MATCH;
         } else {
            return Result.MISMATCH;
         }
      }
   
      public void onSuccess(X509Certificate[] chain,
                           String thumbprint,
                           Result verifyResult,
                           boolean trustedChain,
                           boolean verifiedAssertions)
               throws SSLException {
      }
   });
   
   // Uses try-with-resources to ensure connection is cleaned up after completion.
   try (Connection connection = new Connection("https://server-address/view-vlsi/sdk", httpConfig)) {
      connection.login(username, password, domain);
   
      // Do work
   }
```

## Navigating the API Reference

The View API Reference is set of documents, grouped by platform version. Use the navigation menu to the left to select the version, then the Service, Query, Data Object, Fault Types links to display information. To find the description of a specific object type, click the appropriate category name from the menu.

To quickly find an entry, start typing its name in the **Search Bar** field.

!!! Note
    The maximum supported size of any array input to the API is 1000 data objects.
