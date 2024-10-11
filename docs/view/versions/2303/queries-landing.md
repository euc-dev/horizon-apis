---
layout: page
title: Query Service Overview
hide:
 #- navigation
 - toc
---

The Query Service is a generic service for listing or filtering large sets of results. 

To quickly find any entry, start typing its name in the **Search Bar** or goto the [Query Service index page](index-queries.md).  

## Using the Query Service

The query service supports two types of querying: **paged** and **virtual list**. 

  * A paged query creates a cursor for iterating though query results efficiently. Subsequent pages can be retrieved by requesting the next page from the server. This query type consumes resources on the server to track the query state. The query should be explicitly deleted when it is no longer needed to free the server resources. If a query is never deleted, it will expire after a predefined time and the server will reclaim the resources. 
    * To use the paging model, create a query with the [QueryService_Create](vdi.query.QueryService.md#create) method, get successive results with the [QueryService_GetNext](vdi.query.QueryService.md#getNext) method, then release server-side resources with the [QueryService_Delete](vdi.query.QueryService.md#delete) method. 

**Note:** only 5 active paged queries can exist at a time on a single connection. Attempting to create additional queries when that limit is reached will result in an error. 

  * A virtual list query will only return one page of results to the client and will not consume any server resources after returning the results. If more results are desired these can be retrieved by modifying the result controls, but successive queries may be significantly less performant as a result. 
    * To use the "virtual list" model, use the [QueryService_Query](vdi.query.QueryService.md#query) method to get one page of results at the offset of your choice.


### Filtering

The Query Service provides the ability to filter on properties of the resulting data object. The exact list of supported filters is detailed in the [Query Service Index Page](index-queries.md). Further restrictions on which properties can be used as part of a filter will be specified as part of the documentation on that specific data object or the specific filter. Not all fields can be used to filter. In particular, the "id" field of any data object cannot be used as a field to filter upon. 

### Result controls

There are various types of controls that can be used to control the result set. These are documented in the [QueryDefinition](vdi.query.QueryDefinition.md). 

### Client Library

Included in the Java client library are the classes **Query** , **QueryFilter** , and **QueryControls**. The QueryFilter class provides a wrapper around the supported filters to provide compile time type checking by using the [CName](do-types-landing.md#cname) classes. The Query class abstracts away the paging mechanism as well as the type-casting that is necessary when using the bare metal Query Service interface. 

## Examples

Here are a few examples of using the Query Service. Each example has been implemented two ways. The first will use only data structures and methods that are present in the WSDL, the second will leverage the additional functionality present in the client library. 

### Example: Enumerating all Farms

This example demonstrates how to handle the results from the QueryResults or Query objects. This will be omitted in the remaining examples. 
    
```
    QueryDefinition defn = new QueryDefinition();
    defn.setQueryEntityType(new TypeNameImpl("FarmInfo"));
    QueryResults queryResults = queryService.create(defn);
    
    // Handle results
    try {
       while (queryResults.getResults() != null) {
          for (Object result : queryResults.getResults()) {
             FarmInfo info = (FarmInfo) result;
             // Do work.
          }
    
          // Fetch next page
          if (queryResults.getId() == null) {
             break;
          }
          queryResults = queryService.getNext(queryResults.getId());
       }
    } finally {
       if (queryResults.getId() != null) {
          queryService.delete(queryResults.getId());
       }
    }
```
    
```
    // Uses try-with-resources to ensure query is cleaned up after completion.
    try (Query<FarmInfo> query = new Query<>(connection, FarmInfo.class)) {
       // Handle results
       for (FarmInfo info : query) {
          // Do work.
       }
    }
```

### Example: List enabled RDS Servers
    
```
    QueryDefinition defn = new QueryDefinition();
    defn.setQueryEntityType(new TypeNameImpl("RDSServerInfo"));
    defn.setFilter(new Equals("settings.enabled", true));
    QueryResults queryResults = queryService.create(defn);
    // Handle results
```
    
```
    QueryFilter filter = QueryFilter.equals(RDSServerInfoCName.RDS_SERVER_INFO_CNAME.settings.enabled, true);
    try (Query<RDSServerInfo> query = new Query<>(connection, RDSServerInfo.class, filter)) {
       // Handle results
    }
```

### Example: List desktops (by name in descending order)
    
```
    QueryDefinition defn = new QueryDefinition();
    defn.setQueryEntityType(new TypeNameImpl("DesktopSummaryView"));
    defn.setSortBy("desktopSummaryData.name");
    defn.setSortDescending(true);
    QueryResults queryResults = queryService.create(defn);
    // Handle results
```
    
```
    QueryControls controls = new QueryControls();
    controls.setSortBy(DesktopSummaryViewCName.DESKTOP_SUMMARY_VIEW_CNAME.desktopSummaryData.name);
    controls.setSortDescending(true);
    try (Query<DesktopSummaryView> query = new Query<>(connection, DesktopSummaryView.class, null, controls)) {
       // Handle results
    }
```

### Example: Virtual List query

This example will retrieve the third page of 10 ApplicationInfo objects, without needing to access the first two pages. 
    
```
    QueryDefinition defn = new QueryDefinition();
    defn.setQueryEntityType(new TypeNameImpl("ApplicationInfo"));
    defn.setStartingOffset(20);
    defn.setLimit(10);
    QueryResults queryResults = queryService.query(defn);
    // Handle results.  Don't need to delete query as there is no server side clean-up needed.
```
    
```
    QueryControls controls = new QueryControls();
    controls.setStartingOffset(20);
    controls.setLimit(10);
    Query<ApplicationInfo> query = Query.query(connection, ApplicationInfo.class, null, controls);
    // Handle results.  Don't need to close query as there is no server side clean-up needed.
```

### Example: Count persistent disks with names starting with "a"
    
```
    QueryDefinition defn = new QueryDefinition();
    defn.setQueryEntityType(new TypeNameImpl("PersistentDiskInfo"));
    defn.setFilter(new StartsWith("general.name", "a"));
    int count = queryService.getCount(defn);
```
    
```
    QueryFilter filter = QueryFilter.startsWith(PersistentDiskInfoCName.PERSISTENT_DISK_INFO_CNAME.general.name, "a");
    int count = Query.count(connection, PersistentDiskInfo.class, filter);
```

[Back to Home](index.md)