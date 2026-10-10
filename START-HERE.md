# Start Here

[Home](README.md) · [Exam map](EXAM-MAP.md) · [Study plan](learning-paths/4-week-plan.md)

## Choose a starting point

If you already use AWS, take the [diagnostic](practice/diagnostic.md). If you are new, first explain these five ideas in your own words: a server, a database, an IP address, an HTTP request, and permissions. Then work through the vocabulary below and guides 1–6 before attempting timed practice.

The four-week plan is an accelerated revision route. Extend it when you cannot explain a choice without notes. Reading a file is not evidence that you can apply it.

## Vocabulary you will use repeatedly

| Term | Working meaning | Common confusion |
|---|---|---|
| Region | Geographic grouping of AWS infrastructure | A Region contains several AZs |
| Availability Zone (AZ) | Isolated infrastructure location within a Region | Two subnets in the same AZ do not protect against that AZ failing |
| VPC | Your logical network in one Region | A private network still needs permissions and traffic controls |
| Subnet | A segment of that network in one AZ | A name such as “private” does not configure its routes |
| CIDR | IP address range notation, such as 10.0.0.0/24 | Smaller prefix number means a larger range |
| IAM principal | Identity making a request, such as a role session | A role's trust policy and its resource permissions do different jobs |
| Authentication | Establishing who the caller is | Signing in does not grant every permission |
| Authorization | Deciding what the caller may do | API keys are not a general authorization mechanism |
| Availability | Ability to serve requests when needed | Distinct from durability of stored data |
| Durability | Ability to retain stored data | A durable object can still be temporarily inaccessible |
| Scalability | Ability to handle growth | Distinct from automatically scaling |
| Idempotency | Repetition does not repeat the intended side effect | Message send deduplication alone does not prevent a double charge |
| RPO | Maximum acceptable loss measured in time | Not recovery duration |
| RTO | Maximum acceptable recovery duration | Not a service guarantee |
| Latency | Time taken for one operation | Different from throughput, or work per unit time |

## First session: 45–60 minutes

1. Read the [official exam map](EXAM-MAP.md) and choose one domain to improve.
2. Read one linked guide. Write a requirement → choice → reason chain.
3. Close the page and draw the request path from memory.
4. Complete a scenario. Before revealing the answer, write why the nearest alternative fails.
5. Record one weak area in the [tracker](CHECKLIST.md#weak-area-log), then revisit it after a delay.

Example: “An order must reach billing and fulfillment independently, even during downtime → SNS to a separate SQS queue for each → each application has its own backlog.” Then ask what happens on retries.

## How to judge your progress

Use three levels: **recognize** the service, **explain** its constraints, then **apply** it when a requirement changes. Mark a topic complete only at the third level. Compare your answers with sources and independent practice; a small familiar question set is not a pass predictor.

For actual AWS deployments, use a separate learning account, estimate cost, and follow a documented cleanup procedure. The [workshops](labs/README.md) here need no account and create no cloud resources.
