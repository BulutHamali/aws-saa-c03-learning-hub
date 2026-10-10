# Exam-Domain Map

[Home](README.md) · [Diagnostic](practice/diagnostic.md) · [Tracker](CHECKLIST.md)

The [official SAA-C03 guide](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03.html) lists the weights below. Checked 2026-10-10. The mapping and exit questions are this project's learning aids, not an AWS claim that these notes cover every possible exam topic.

| Domain | Weight | Start with | Apply it |
|---|---|---|---|
| Secure architectures | 30% | [IAM](topic-guides/01-IAM.md), [VPC](topic-guides/06-VPC.md), [KMS](topic-guides/20-KMS-CloudHSM.md), [secrets](topic-guides/21-SecretsManager-ParameterStore.md), [security services](topic-guides/22-WAF-Shield-SecurityServices.md), [Cognito](topic-guides/23-Cognito.md), [directories](topic-guides/24-Directory-Services.md), [Organizations](topic-guides/29-Organizations-ControlTower.md) | Diagnostic 1 and 5; workshop 1 |
| Resilient architectures | 26% | [ELB/scaling](topic-guides/05-ELB-AutoScaling.md), [RDS](topic-guides/09-RDS-Aurora.md), [messaging](topic-guides/17-SQS-SNS-Kinesis.md), [workflows](topic-guides/18-EventBridge-StepFunctions.md), [DR](topic-guides/35-Disaster-Recovery.md) | Diagnostic 2 and 6; workshops 2 and 3 |
| High-performing architectures | 24% | [storage](topic-guides/04-EBS-EFS-InstanceStore.md), [compute](topic-guides/03-EC2.md), [DynamoDB](topic-guides/10-DynamoDB.md), [caching](topic-guides/11-ElastiCache.md), [edge](topic-guides/08-CloudFront-GlobalAccelerator.md), [integration](topic-guides/17-SQS-SNS-Kinesis.md) | Diagnostic 3 and 7; workshop 3 |
| Cost-optimized architectures | 20% | [S3](topic-guides/02-S3.md), [EC2 purchasing](topic-guides/03-EC2.md), [databases](topic-guides/09-RDS-Aurora.md), [cost tools](topic-guides/31-Cost-Management.md), [hybrid networking](topic-guides/32-DirectConnect-VPN.md) | Diagnostic 4 and 8; workshop 2 |

## Exit questions by task

Use the official task IDs to organize your weak-area log. These prompts paraphrase the skills into observable learner outputs.

| Task | Explain or demonstrate without notes |
|---|---|
| 1.1 | How does an app obtain temporary permissions across accounts? |
| 1.2 | Which identity and network controls protect each request hop? |
| 1.3 | Who may decrypt, and how are earlier data and retained records protected? |
| 2.1 | What buffers a spike, and how does each consumer scale independently? |
| 2.2 | What fails when an AZ disappears, and what restores the application? |
| 3.1 | Does the workload require block, file, or object semantics? |
| 3.2 | Which resource or metric actually limits compute performance? |
| 3.3 | Can stale reads, connection pooling, or caching satisfy the access pattern? |
| 3.4 | How do protocol, routing, latency, and bandwidth constrain networking? |
| 3.5 | Does ingestion need replay, transformations, or managed delivery? |
| 4.1 | How do access frequency and retention change storage cost? |
| 4.2 | How do utilization and interruption tolerance change compute purchasing? |
| 4.3 | Can capacity, replicas, or licensing change database cost? |
| 4.4 | Where are transfer, cross-AZ, and gateway costs introduced? |

Task sources: [domain 1](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03-domain1.html), [domain 2](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03-domain2.html), [domain 3](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03-domain3.html), [domain 4](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03-domain4.html).

## Coverage limits

The topic index is a reading list, not proof of mastery. The diagnostic samples only a few decisions per domain. Service quotas, engine-specific features, and the official in-scope list need independent verification. See [the audit record](AUDIT.md) before treating an inherited shortcut as authoritative.
