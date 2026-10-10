# Four-Week Learning Plan

This accelerated revision plan assumes AWS fundamentals and roughly 60–90 minutes on weekdays plus longer weekend sessions. Beginners should first use [Start here](../START-HERE.md), and may need 6–8 weeks or more. There is no guaranteed completion time. Take the [diagnostic](../practice/diagnostic.md), then prioritize your weak [exam domains](../EXAM-MAP.md).

## The daily loop

1. **Learn (30–40 min):** read the assigned guide and draw one diagram.
2. **Recall (10 min):** close the guide and write five facts or decisions from memory.
3. **Apply (15–25 min):** answer scenario questions and explain why each distractor fails.
4. **Review (5 min):** add every uncertainty to the [weak-area log](../CHECKLIST.md#weak-area-log).

## Week 1 — Build the network and compute foundation

| Day | Focus | Output |
|---|---|---|
| 1 | [IAM](../topic-guides/01-IAM.md) | Policy-evaluation sketch: explicit deny, identity policy, resource policy, SCP |
| 2 | [EC2](../topic-guides/03-EC2.md) | Purchase-model comparison for steady, bursty, and interruptible work |
| 3 | [EBS, EFS, instance store](../topic-guides/04-EBS-EFS-InstanceStore.md) | Storage choice for five workloads |
| 4 | [ELB and Auto Scaling](../topic-guides/05-ELB-AutoScaling.md) | ALB/NLB/GWLB decision tree |
| 5–6 | [VPC](../topic-guides/06-VPC.md) | Diagram public/private subnets across two AZs, including routes |
| 7 | Review | Re-answer misses without notes; teach the diagram aloud |

## Week 2 — Data, storage, and edge

| Day | Focus | Output |
|---|---|---|
| 8 | [S3](../topic-guides/02-S3.md) | Lifecycle for hot, cool, and archival objects |
| 9 | [RDS and Aurora](../topic-guides/09-RDS-Aurora.md) | Multi-AZ vs replica vs Global Database table |
| 10 | [DynamoDB](../topic-guides/10-DynamoDB.md) | Partition-key and secondary-index examples |
| 11 | [ElastiCache](../topic-guides/11-ElastiCache.md) and [other databases](../topic-guides/12-Other-Databases.md) | Database selection by access pattern |
| 12 | [Route 53](../topic-guides/07-Route53.md) | Routing-policy examples |
| 13 | [CloudFront and Global Accelerator](../topic-guides/08-CloudFront-GlobalAccelerator.md) | Edge-service decision table |
| 14 | Review | Complete challenges 1–4 in the [practice set](../practice/architecture-challenges.md) |

## Week 3 — Decoupling, security, and operations

| Day | Focus | Output |
|---|---|---|
| 15 | [Lambda](../topic-guides/13-Lambda.md) and [API Gateway](../topic-guides/16-API-Gateway.md) | Sync, async, and polling invocation map |
| 16 | [SQS, SNS, and Kinesis](../topic-guides/17-SQS-SNS-Kinesis.md) | Messaging decision tree |
| 17 | [EventBridge and Step Functions](../topic-guides/18-EventBridge-StepFunctions.md) | Event routing vs orchestration example |
| 18 | [Containers](../topic-guides/14-ECS-EKS-Fargate.md) and [Beanstalk](../topic-guides/15-Elastic-Beanstalk.md) | Compute abstraction ladder |
| 19 | [KMS](../topic-guides/20-KMS-CloudHSM.md) and [secrets](../topic-guides/21-SecretsManager-ParameterStore.md) | Key ownership and secret-rotation matrix |
| 20 | [Security services](../topic-guides/22-WAF-Shield-SecurityServices.md), [Cognito](../topic-guides/23-Cognito.md), [directories](../topic-guides/24-Directory-Services.md) | Threat and identity selection map; split across sessions if new |
| 21 | [Observability](../topic-guides/19-CloudWatch-CloudTrail-Config.md) | “metric, API event, resource state” comparison |

## Week 4 — Resilience, governance, and exam readiness

| Day | Focus | Output |
|---|---|---|
| 22 | [Disaster recovery](../topic-guides/35-Disaster-Recovery.md) | DR strategy ranked by RTO, RPO, and cost |
| 23 | [Hybrid networking](../topic-guides/32-DirectConnect-VPN.md) and [Transit Gateway](../topic-guides/33-Transit-Gateway.md) | Hybrid connectivity diagram |
| 24 | [Migration](../topic-guides/25-StorageGateway-DataSync-TransferFamily.md), [FSx](../topic-guides/26-FSx.md), [offline transfer lifecycle](../topic-guides/27-Snow-Family.md) | File/protocol choices and transfer-time calculation |
| 25 | [Organizations](../topic-guides/29-Organizations-ControlTower.md), [CloudFormation](../topic-guides/28-CloudFormation.md), [Service Catalog/Trusted Advisor](../topic-guides/30-ServiceCatalog-TrustedAdvisor.md) | Multi-account governance model |
| 26 | [Cost](../topic-guides/31-Cost-Management.md) and [Well-Architected](../topic-guides/34-Well-Architected.md) | Cost/operations trade-off review |
| 27 | Timed practice | Categorize every miss in the weak-area log |
| 28 | [Contextual traps](../topic-guides/36-Exam-Traps-KeyPatterns.md), [additional services](../topic-guides/37-GapFill-Services.md) | Review weak areas and [decision matrices](../decision-guides/README.md); introduce no new topic on exam morning |

## When to slow down

Do not move on just because a day ended. Repeat a topic if you cannot explain the selection criteria without brand-name guessing. The useful unit of progress is a decision you can defend.


## Weekend application checkpoints

- Week 1: complete workshop 1 in [architecture workshops](../labs/README.md) and trace both request and response packets.
- Week 2: complete workshop 2 and explain availability versus data recovery.
- Week 3: complete workshop 3 and explain redelivery versus idempotency.
- Week 4: retake missed diagnostic items after a delay, then use an independent timed practice assessment. This repository's small question set cannot estimate exam pass probability.

