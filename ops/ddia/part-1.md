> All the contents here are excerpted from DDIA(Designing Data-Intensive Application by Martin Kleppmann).

In the last decade, there are many interesting developments in databases and distributed systems:
- Facebook, Amazon, Netflix, Google are handling huge volumes of data and traffic, so they need new tools to handle such scale efficiently.
- Businesses need to be agile, so they need to keep develpoment cycle short and data models flexible.
- The number of core and network speeds are increasing, but CPU clock speeds are barely so, it means parallelism is only gonna increase
- Thanks to Infra-structure as a Service, you can now build distributed systems across many machines and even multiple geographic regions.
- Many services are now expected to be highly available; extended downtime due to outages or maintenance is becoming increasingly unacceptable.

A data-intensive application is typically built from standard building blocks that provide commonly needed functionality:
- Store data so that they, or another application, can find it again later <- databases
- Remember the result of an expensive operation, to speed up reads <- caches
- Allows users to search data by keyword or filter it in various ways <- search indexes
- Send a message to another process, to be handled asynchronously <- stream processing
- Periodically crunch a large amount of accumulated data <- batch processing

Three concerns that are important in most software systems:
- Reliability: The system should continue to work correctly
- Scalability: As the system grows in data volume, traffic volume, or complexity, there should be resonable ways of dealing with that growth
- Maintainability: Over time, many different people will work on the system, and they should all be to work on it productively
