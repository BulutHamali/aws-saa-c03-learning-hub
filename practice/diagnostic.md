# Short Diagnostic

[Home](../README.md) · [Exam map](../EXAM-MAP.md) · [Weak-area log](../CHECKLIST.md#weak-area-log)

Allow 15–20 minutes. Write your choice, reasoning, and confidence before opening each answer. For question 5, choose two responses. All scenarios are original. This small diagnostic locates misconceptions; its score does not predict an exam result.

## 1. Credentials for an application

An EC2 application must read one private S3 bucket without long-lived credentials. Which is the best starting design?

A. Put an IAM user's access key in the AMI.
B. Attach an instance profile with a role restricted to the required bucket operations.
C. Make the bucket public and hide its name.
D. Share the account root access key with the application.

<details>
<summary>Answer, alternatives, and next step</summary>

**B.** An instance profile makes role credentials available to EC2. A embeds a long-lived secret; C exposes data; D grants excessive privileges and distributes root credentials. Confirm that bucket policies and other controls also permit the intended access.

Task 1.1. Review [IAM](../topic-guides/01-IAM.md). Change the question: what additional trust and permission configuration is needed if the role is in another account?

</details>

## 2. Readable database redundancy

A requirement explicitly calls for an RDS writer and two readable instances across three AZs with managed failover. Which deployment matches?

A. Single-AZ RDS instance.
B. RDS Multi-AZ DB instance with one standby.
C. RDS Multi-AZ DB cluster.
D. One manual database snapshot per day.

<details>
<summary>Answer, alternatives, and next step</summary>

**C.** A lacks the AZ redundancy; B's single standby does not serve reads; D is recovery material, not a live serving deployment. Verify engine support and regional availability for a real design.

Task 2.2. Review [RDS](../topic-guides/09-RDS-Aurora.md). If readable standbys are unnecessary, what simpler deployment could meet AZ availability?

</details>

## 3. Replay a stream

Two analytics applications must independently read ordered click events and reprocess yesterday's data. Which best fits this access pattern?

A. SQS Standard with both apps competing on the same queue.
B. CloudWatch alarms only.
C. One Lambda invocation whose memory is treated as permanent storage.
D. Kinesis Data Streams with suitable retention and partitioning.

<details>
<summary>Answer, alternatives, and next step</summary>

**D.** Retention supports replay and consumers can independently read the stream. Ordering has a partition/shard scope that the design must respect. A divides work and deletion removes ordinary replay; B is monitoring; C is not durable event history.

Task 3.5. Review [messaging](../topic-guides/17-SQS-SNS-Kinesis.md). What changes if the only requirement is managed delivery into S3?

</details>

## 4. Interruptible compute

A large batch job is checkpointed, can resume on a different instance, and tolerates interruptions. The team wants to reduce compute cost. Which purchasing model should it evaluate first?

A. Spot Instances with interruption handling and capacity fallback.
B. A dedicated host solely because it costs more.
C. Always-on overprovisioned On-Demand instances.
D. Buy capacity commitments without examining utilization.

<details>
<summary>Answer, alternatives, and next step</summary>

**A.** The workload can handle Spot's availability and interruption characteristics. B has no stated tenancy or licensing justification; C pays for avoidable idle capacity; D may waste commitments. “Cheapest” still requires a workable deadline and recovery design.

Task 4.2. Review [EC2](../topic-guides/03-EC2.md). What changes if the workload cannot tolerate interruption?

</details>

## 5. Key-management requirements — choose TWO

A team is evaluating KMS and CloudHSM. Which two statements are sound?

A. KMS must be rejected whenever Level 3 validated hardware is required.
B. Every KMS key type can use every rotation option.
C. Dedicated HSM tenancy and customer crypto administration are reasons to evaluate CloudHSM.
D. A broad IAM Allow automatically bypasses a KMS key policy.
E. KMS uses FIPS 140-3 Security Level 3 validated HSMs.

<details>
<summary>Answers, alternatives, and next step</summary>

**C and E.** A repeats an obsolete comparison. B ignores key eligibility and rotation configuration. D ignores how key policies, grants, IAM delegation, and denies govern access.

Tasks 1.1/1.3. Review [KMS](../topic-guides/20-KMS-CloudHSM.md). Specify which actual requirement would distinguish dedicated HSMs from managed KMS integration.

</details>

## 6. A duplicate charge

A FIFO queue consumer charges a card, then crashes before deleting the message. Which directly addresses the risk of charging again?

A. Assume FIFO guarantees exactly-once external side effects.
B. Increase memory without changing application logic.
C. Use a stable payment idempotency key with a compatible payment API and record/reconcile the result.
D. Delete every message before trying to charge.

<details>
<summary>Answer, alternatives, and next step</summary>

**C.** A confuses send deduplication with transaction effects. B does not close the crash window. D can lose unperformed work. Longer visibility may help normal processing but cannot by itself resolve this failure.

Task 2.1. Review [messaging](../topic-guides/17-SQS-SNS-Kinesis.md) and [workshop 3](../labs/README.md#workshop-3-the-crash-between-a-side-effect-and-deletion).

</details>

## 7. Global game traffic

A game uses TCP and UDP and needs stable global IP entry points and health-based routing to regional endpoints. It has no HTTP objects to cache. Which is the best fit?

A. S3 lifecycle rules.
B. Global Accelerator.
C. CloudFront content caching alone.
D. An IAM permission boundary.

<details>
<summary>Answer, alternatives, and next step</summary>

**B.** It fits the transport and global entry requirements. A manages object transitions; C does not provide this arbitrary TCP/UDP acceleration model; D limits permissions.

Task 3.4. Review [edge services](../topic-guides/08-CloudFront-GlobalAccelerator.md). What changes for cacheable HTTPS images?

</details>

## 8. Recovery at lower cost

A business accepts hours of recovery and its tested backup-and-restore process meets the stated loss and downtime objectives. It has no need for continuous service in a second Region. Which is the most reasonable baseline?

A. Full active-active capacity solely to minimize cost.
B. Keep no backups because downtime is allowed.
C. Use a read replica as the only protection against mistaken deletes.
D. Keep the tested backup-and-restore design and review it as requirements change.

<details>
<summary>Answer, alternatives, and next step</summary>

**D.** The stated tests establish feasibility. A adds an unjustified continuous footprint; B cannot recover data; C replicates logical errors. In another workload, backup-and-restore might fail the objectives and a warmer design could be necessary.

Tasks 4.1/4.3 and 2.2. Review [DR](../topic-guides/35-Disaster-Recovery.md) and [workshop 2](../labs/README.md#workshop-2-availability-is-not-recovery-from-a-mistake).

</details>

## Use your results

Treat each item as one diagnostic decision. For question 5, record a miss unless you chose exactly both correct statements. Log a guessed answer or a high-confidence miss even if your total looks good. Revisit the linked concept, explain one changed requirement, and retry after 48 hours without reading the answer first.
