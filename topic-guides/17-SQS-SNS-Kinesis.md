# Section 17: SQS, SNS & Kinesis

[Topic index](00-README.md) · [Decision guide](../decision-guides/README.md)

## The idea

Messaging separates acceptance of work from processing it. A queue absorbs bursts, but it cannot make a failing consumer reliable by itself: design retries, retention, failure handling, and idempotency.

**Idempotency** means that repeating a request has the same intended effect as processing it once. A payment handler must not charge twice when a message is redelivered.

## SQS: distribute work to consumers

A worker receives a message, processes it, then deletes it. Receiving hides the message during its **visibility timeout**; it does not remove it. If processing or deletion fails, the message can return.

| Behavior | Standard queue | FIFO queue |
|---|---|---|
| Delivery | At least once; duplicates are possible | Send deduplication within a five-minute window; consumer retries still require idempotency |
| Ordering | Best effort | Ordered **within a message group**, not globally across all groups |
| Throughput | High throughput; check applicable quotas | Depends on mode, Region, batching, and message-group distribution |
| Typical use | Independent background work | Ordered operations per entity |

FIFO's “exactly-once processing” terminology does not make database updates or external side effects transactional with message deletion.

Useful settings:

- **Visibility timeout:** match it to processing and retry behavior. Increasing it can prevent premature redelivery; it does not eliminate all duplicates.
- **Dead-letter queue (DLQ):** use a redrive policy and `maxReceiveCount` to isolate repeated failures.
- **Long polling:** waits up to 20 seconds to reduce empty receives.
- **Payload:** maximum 1 MiB (1,048,576 bytes). For larger content, store it in S3 and pass a reference with suitable access and lifecycle management.
- **Retention:** default four days; configurable up to fourteen days. Deletion ends ordinary queue replay.

Sources: [message quotas](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/quotas-messages.html), [FIFO deduplication](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues-exactly-once-processing.html), [high throughput FIFO](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/high-throughput-fifo.html).

## SNS: publish to subscribers

SNS routes one publication to multiple subscribers. Its delivery retry policy depends on the endpoint; a failed first attempt does not automatically mean permanent loss. Configure subscription DLQs where appropriate. SNS FIFO topics also support optional archive and replay.

A common pattern is **SNS → one SQS queue per downstream application**. Each application gets its own backlog and can drain it independently. A single shared SQS queue would distribute work among consumers rather than give every application every event.

Sources: [SNS retries](https://docs.aws.amazon.com/sns/latest/dg/sns-message-delivery-retries.html), [FIFO archive and replay](https://docs.aws.amazon.com/sns/latest/dg/fifo-message-archiving-replay.html).

## Streams and delivery pipelines

**Kinesis Data Streams** fits retained streaming data that independent consumers must read and replay. Plan partition keys, ordering scope, retention, and consumer capacity.

**Amazon Data Firehose** delivers streaming data to supported destinations such as S3 with managed buffering and optional transformations. Delivery latency depends on configuration and destination; “exactly 60 seconds” is not a universal guarantee. Firehose is the current name for the service formerly called Kinesis Data Firehose.

**Amazon MQ** fits applications requiring supported ActiveMQ or RabbitMQ protocols. A familiar protocol can reduce migration changes, but compatibility still needs testing.

Sources: [Kinesis concepts](https://docs.aws.amazon.com/streams/latest/dev/key-concepts.html), [Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html), [Amazon MQ](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/welcome.html).

## Decision patterns

| Requirement | Candidate | Why the closest alternative may fail |
|---|---|---|
| Buffer independent jobs | SQS | SNS alone does not provide each worker fleet a queue backlog |
| Give billing and fulfillment every event | SNS → separate SQS queues | Competing workers on one queue divide the work |
| Reprocess a retained ordered stream with independent consumers | Kinesis Data Streams | Deleted SQS messages are not retained stream history |
| Deliver telemetry to S3 with managed buffering | Data Firehose | Custom stream consumers add operational work |
| Preserve a broker protocol during migration | Amazon MQ | SQS/SNS require different client interfaces |
| Route SaaS or AWS events by content | EventBridge | Evaluate event sources and integrations, not just fan-out |

## Check your understanding

A FIFO consumer charges a card, then crashes before deleting the message. Will FIFO alone prevent another charge?

<details>
<summary>Expected explanation</summary>

No. The consumer can see the message again after visibility expires. Use an idempotency key and a durable record or a payment API with idempotent requests. Queue send deduplication is different from exactly-once business effects.

</details>

## Pocket card

- Queue = independent work distribution; topic = fan-out; stream = retained history.
- SQS payload ceiling = 1 MiB, not the older 256 KiB.
- FIFO order is per message group; throughput is configuration-dependent.
- Visibility timeout controls redelivery timing; idempotency controls repeated effects.
- SNS has retries; FIFO archive/replay is an optional capability.

Targeted fact check: 2026-10-10. Adapted from RonitSachdev's guide; revised claims are linked above.
