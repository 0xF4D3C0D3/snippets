> All the contents here are excerpted from DDIA(Designing Data-Intensive Application by Martin Kleppmann).


#### In the last decade, there are many interesting developments in databases and distributed systems:
- Facebook, Amazon, Netflix, Google are handling huge volumes of data and traffic, so they need new tools to handle such scale efficiently.
- Businesses need to be agile, so they need to keep develpoment cycle short and data models flexible.
- The number of core and network speeds are increasing, but CPU clock speeds are barely so, it means parallelism is only gonna increase
- Thanks to Infra-structure as a Service, you can now build distributed systems across many machines and even multiple geographic regions.
- Many services are now expected to be highly available; extended downtime due to outages or maintenance is becoming increasingly unacceptable.


#### A data-intensive application is typically built from standard building blocks that provide commonly needed functionality:
- Store data so that they, or another application, can find it again later <- databases
- Remember the result of an expensive operation, to speed up reads <- caches
- Allows users to search data by keyword or filter it in various ways <- search indexes
- Send a message to another process, to be handled asynchronously <- stream processing
- Periodically crunch a large amount of accumulated data <- batch processing


#### Three concerns that are important in most software systems:
- Reliability: The system should continue to work correctly
- Scalability: As the system grows in data volume, traffic volume, or complexity, there should be resonable ways of dealing with that growth
- Maintainability: Over time, many different people will work on the system, and they should all be to work on it productively

#### What is fault and fault-tolerant
- Faults: The things that can go wrong
- Fault-tolerant or resilient: Systems that anticipate faults and can cope with them
- ※ Fault-tolerant doesn't mean to be tolerant for every possilbe faults. it means for only certain types of faults
- ※ Fault is not the same as a failure. A fault is usually defined as one component of the system deviating from its spec, whereas a failure is when the system as a whole stops providing the required service to the user. 

#### Response time vs Latency
- Reponse time: what the client sees: the actual time to process the requst + network delays + queueing delays
- Latency: the duration that a request is waiting to be handled
- Even if you only make the same request over and over again, you'll get a slightly different response time on every try. In practice, in a system handling a variety of requests, the response time can vary a lot. We therefore need to think of response time not as a single number, but as a *distribution* of values that you can measure
- After sorting the list of response times from fastest to slowest, and assume that the median is 200ms, then you can say the half of requests take less than 200ms and the half of requests take more than 200ms and that's the p50. If p95 is 1.5 seconds, that means 95 out of 100 requests take less than 1.5 seconds and 5 out of 100 requests take 1.5 seconds or more.



