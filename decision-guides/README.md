# AWS Service Decision Guide

Start with the requirement, not the product name. These matrices are recall aids; validate implementation details in current AWS documentation. For sources and qualifications, use [RDS](../topic-guides/09-RDS-Aurora.md), [messaging](../topic-guides/17-SQS-SNS-Kinesis.md), and [KMS](../topic-guides/20-KMS-CloudHSM.md).

SQS consumers must handle redelivery; FIFO orders within a message group and deduplicates sends within its window. SNS has delivery retries and optional FIFO archive/replay. Do not infer exactly-once business effects from a messaging feature name.

## Messaging and events

| Requirement | Strong first candidate | Why |
|---|---|---|
| Buffer work; each message processed by one consumer | SQS | Queue-based decoupling, retries, visibility timeout, DLQ |
| Fan one published message to many subscribers | SNS | Push-based pub/sub fan-out |
| Ordered, replayable, high-volume event stream | Kinesis Data Streams | Retained stream with shards and multiple consumers |
| Route events by content across AWS services or SaaS | EventBridge | Event bus, rules, schema-aware integrations |
| Coordinate multi-step work with state and retries | Step Functions | Workflow orchestration rather than transport |

Ask next: must ordering be strict, must events be replayed, is one or many consumers expected, and who controls retries?

## Relational database resilience

| Requirement | Strong first candidate | Watch for |
|---|---|---|
| Survive an AZ failure | Multi-AZ deployment | DB instance standby is unreadable; DB cluster instances can serve reads |
| Scale read traffic | Read replica | Replication lag and promotion behavior |
| Cross-Region reads or DR | Cross-Region replica / Aurora Global Database | Recovery objectives and write topology |
| Recover from accidental writes | Point-in-time recovery / backup | Failover does not undo logical corruption |

## Network connectivity

| Requirement | Strong first candidate | Watch for |
|---|---|---|
| Connect two VPCs simply | VPC peering | Non-transitive routing |
| Connect many VPCs and on-premises networks | Transit Gateway | Central routing and attachment segmentation |
| Expose one private service to consumers | PrivateLink | Service-level access without full network routing |
| Encrypted hybrid connection quickly | Site-to-Site VPN | Internet path and variable performance |
| Consistent private hybrid capacity | Direct Connect | Provisioning time; encryption is a separate requirement |

## Object access and acceleration

| Requirement | Strong first candidate | Watch for |
|---|---|---|
| Cache HTTP content near users | CloudFront | Content distribution and origin protection |
| Improve global TCP/UDP application paths | Global Accelerator | Static anycast IPs; no content cache |
| Speed distant uploads to one S3 bucket | S3 Transfer Acceleration | Validate benefit and cost for the path |
| Move bulk on-premises data online | DataSync | Migration/transfer rather than ongoing file gateway access |

## Encryption and secrets

| Requirement | Strong first candidate | Watch for |
|---|---|---|
| Managed encryption keys integrated with AWS services | AWS KMS | Key policy and grants |
| Dedicated HSM control | CloudHSM | Customer-operated cluster and higher operational burden |
| Store and automatically rotate application secrets | Secrets Manager | Rotation workflow and supported integration |
| Hierarchical configuration, optionally encrypted | Systems Manager Parameter Store | Rotation is not its defining feature |

## Monitoring, audit, and compliance

| Question asks… | Strong first candidate |
|---|---|
| “What is happening to performance now?” | CloudWatch metrics, logs, and alarms |
| “Who called this API and when?” | CloudTrail |
| “How did this resource configuration change?” | AWS Config |
| “Is this configuration compliant?” | AWS Config rules |
| “How did this request move through services?” | X-Ray |

## The tie-breaker sequence

When two choices still look plausible, apply requirements in this order:

1. Eliminate anything that cannot satisfy a hard constraint: protocol, latency, RPO/RTO, retention, Region, or compliance.
2. Prefer the choice that satisfies availability and durability requirements explicitly.
3. Apply the question's optimization phrase: lowest cost, least operational overhead, highest performance, or fastest implementation.
4. Reject architectures that introduce an unrequested single point of failure or manual recovery step.

