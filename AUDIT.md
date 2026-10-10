# Learner-Usefulness Audit

Review date: 2026-10-10. Scope: navigation and study-plan coverage across the repository, teaching patterns, practice feedback, and targeted verification of high-impact factual claims against AWS sources.

## Verdict

The repository is useful as a companion study resource. Before this review, navigation improved access to inherited notes but several outdated or overgeneralized rules could teach incorrect decisions. This revision fixes the confirmed issues below and adds ways to demonstrate understanding.

This is not a line-by-line certification of all 37 guides. Technical checks validate navigation and structure, not AWS factual truth. The remaining inherited material should be read alongside current documentation and independent practice.

## Findings and resolutions

| Priority | Finding | Resolution and evidence |
|---|---|---|
| High | “All Multi-AZ standbys are unreadable”; one replica count/failover timing applied across products | Rewrote [RDS](topic-guides/09-RDS-Aurora.md) to distinguish instance and cluster deployments; removed universal timing claims |
| High | SQS 256 KB payload, fixed FIFO ceiling, and exactly-once worker claims | Corrected [messaging](topic-guides/17-SQS-SNS-Kinesis.md): 1 MiB, configurable throughput, per-group order, idempotent consumers |
| High | SNS described as storing nothing with no retries | Documented endpoint-specific retries and optional FIFO archive/replay in the messaging guide |
| High | API Gateway timeout described as an unchangeable universal 29 seconds | Qualified [API types and timeouts](topic-guides/16-API-Gateway.md); clarified durable async acceptance and native HTTP JWT auth |
| High | KMS described as Level 2; IAM and key policies always required direct dual Allow | Rewrote [KMS](topic-guides/20-KMS-CloudHSM.md) using current validation and authorization documentation |
| High | QLDB and Snow products recommended without lifecycle context | Added QLDB retirement status and replaced [Snow guide](topic-guides/27-Snow-Family.md) with calculations and current availability checks |
| High | NACL reply direction was reversed for an outbound client; all NAT gateways described as zonal | Corrected [VPC](topic-guides/06-VPC.md) for flow direction and regional/zonal availability modes |
| Medium | Lambda event-source failures treated as identical across queues and streams | Qualified [invocations](topic-guides/13-Lambda.md), retries, concurrency, and current Managed Instances timeout exceptions |
| Medium | Step Functions retries described as state types, and orchestration history as free | Clarified [workflow coordination](topic-guides/18-EventBridge-StepFunctions.md) and SNS filtering overlap |
| Medium | Trusted Advisor categories and support-plan names outdated | Updated [check categories and entitlement](topic-guides/30-ServiceCatalog-TrustedAdvisor.md) with current references |
| Medium | ACM public certificates described as universally non-exportable | Corrected [ACM section](topic-guides/37-GapFill-Services.md) for exportable certificates, eligibility, charges, and renewal deployment |
| Medium | DR strategy names treated as guarantees of zero loss or fixed recovery time | Qualified [DR heuristics](topic-guides/35-Disaster-Recovery.md) and required measured application recovery |
| Medium | Study plan omitted guides and lacked beginner prerequisites | Added [start page](START-HERE.md), all-guide plan coverage, and [domain map](EXAM-MAP.md) |
| Medium | Eight open-ended scenarios lacked calibration and applied exercises | Added [diagnostic](practice/diagnostic.md) with alternatives/remediation and three [workshops](labs/README.md) with expected results |
| Medium | Link checker ignored anchors and plan omissions | Extended navigation validation and added negative tests |

Corrected shortcuts were also updated in the decision guide, practice answers, and final-review pocket card to reduce contradictions.

## What remains to review

These are follow-up review areas, not assertions that every statement in them is wrong:

- Engine-specific quotas, prices, support matrices, and service defaults in the other inherited guides.
- Broad “always/never” choices and unsupported claims about how often individual services appear on the exam.
- Product changes in security, caching, transfer protocols, and identity features outside the targeted corrections above.
- Real deployment exercises with reproducible setup, measured results, cost bounds, and cleanup. Current workshops are design exercises only.

## Maintenance standard

For each factual correction, include a primary source, date, and scope. Mark a claim as checked rather than marking an entire guide “current” based on one correction. Use the [fact-check issue template](.github/ISSUE_TEMPLATE/fact-check.yml) for unresolved claims. Before an exam, compare the [official scope](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03.html) with your own weak-area log.
