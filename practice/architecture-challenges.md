# Architecture Challenges

Answer each challenge before expanding the explanation. These are original learning scenarios, not recalled exam questions.

For each answer, award yourself one point for the correct candidate, one for explaining the hard requirement, and one for rejecting the nearest alternative. Record confidence before revealing the explanation. A correct guess still needs review. Use [the diagnostic](diagnostic.md) for multiple-choice practice and [architecture workshops](../labs/README.md) to apply the decisions.

Sources for database and messaging answers: [RDS guide](../topic-guides/09-RDS-Aurora.md), [messaging guide](../topic-guides/17-SQS-SNS-Kinesis.md).

## 1. Burst-resistant image processing

A photo application receives unpredictable upload spikes. Each image must be processed by a fleet that can scale independently. Failed work must be inspectable after several retries. Which architecture fits best?

<details>
<summary>Answer and reasoning</summary>

Send upload events to an **SQS queue**, let the processing fleet poll it, configure a visibility timeout longer than normal processing, and attach a **dead-letter queue** with a sensible receive count.

Make processing idempotent because messages may be redelivered. SQS absorbs spikes and separates producer capacity from consumer capacity. SNS alone would push immediately and would not provide the same worker-buffer semantics. Kinesis is compelling when ordered replayable streaming is required; that is not stated here.

</details>

## 2. Highly available relational database

A transactional application needs automatic recovery from an Availability Zone outage. Its read traffic is modest. The team proposes a read replica as the standby. What should change?

<details>
<summary>Answer and reasoning</summary>

Use an **RDS Multi-AZ DB instance deployment** for managed failover when no read capacity is required. A Multi-AZ DB cluster is another deployment with readable instances. A read replica is primarily a read-scaling tool and is not the default automatic-failover substitute for Multi-AZ. If both availability and read scaling are required, the design may use both capabilities for their separate purposes.

</details>

## 3. Private access to one provider service

Dozens of customer VPCs need private access to one service in a provider VPC. Customers must not gain routes to the rest of the provider network, and overlapping customer CIDRs are common. Choose the connectivity model.

<details>
<summary>Answer and reasoning</summary>

Use **AWS PrivateLink**: publish the service through an endpoint service and let consumers create interface endpoints. PrivateLink exposes the service rather than merging network routes, which handles the isolation and overlapping-CIDR requirements better than peering.

</details>

## 4. Global static entry point for a game

A latency-sensitive game uses TCP and UDP. Clients need two stable global IP addresses, traffic should enter the AWS network close to the player, and there is nothing to cache. What fits?

<details>
<summary>Answer and reasoning</summary>

Use **AWS Global Accelerator**. It provides static anycast IP addresses and routes TCP/UDP traffic over the AWS global network toward healthy regional endpoints. CloudFront is a content delivery network for HTTP-oriented caching and delivery; caching is not the requirement.

</details>

## 5. Undo an operator mistake

A production database is healthy and reachable, but an operator deleted important rows 20 minutes ago. Would a Multi-AZ failover recover the rows?

<details>
<summary>Answer and reasoning</summary>

No. The destructive write is replicated to the standby. Recover using **point-in-time recovery**, an appropriate backup, or a database-specific rewind feature when supported and configured. High availability handles infrastructure failure; it does not replace backups for logical corruption.

</details>

## 6. Audit versus configuration history

A security analyst asks two questions: “Who disabled bucket versioning?” and “How long was the bucket noncompliant?” Which services answer them?

<details>
<summary>Answer and reasoning</summary>

Use **CloudTrail** to identify the API caller and event, and **AWS Config** to inspect configuration history and compliance duration. CloudWatch may alert or aggregate logs, but the two questions map directly to API audit history and resource configuration state.

</details>

## 7. Workflow longer than a function timeout

A document pipeline has six dependent steps, human approval, per-step retries, and execution lasting hours. The current design chains Lambda functions directly. What is the architectural correction?

<details>
<summary>Answer and reasoning</summary>

Use **Step Functions Standard** to orchestrate the states, retries, waits, approval callback, and execution history. Express workflows have a five-minute maximum and do not fit an hours-long human approval. Lambda can still perform individual compute steps. Direct chaining hides workflow state inside application code and makes recovery and audit harder.

</details>

## 8. Cost-conscious disaster recovery

A business can tolerate hours of recovery and some data loss. It wants a tested recovery path but cannot justify continuously running a second full environment. Which DR family is the best starting point?

<details>
<summary>Answer and reasoning</summary>

Start with **backup and restore**, then confirm the achievable RPO and RTO through tests. Pilot light, warm standby, and multi-site designs usually buy faster recovery by keeping progressively more infrastructure running. The stated tolerance favors the least costly family, but measured recovery objectives decide whether it is sufficient.

</details>

## Review rubric

For every miss, write four lines:

1. The hard requirement you overlooked.
2. The service capability that satisfies it.
3. Why the strongest distractor fails.
4. One changed requirement that would make the distractor correct.

