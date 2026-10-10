# Architecture Workshops

[Home](../README.md) · [Study plan](../learning-paths/4-week-plan.md)

These are design and failure-analysis exercises. You need paper or a text editor, 20–30 minutes per workshop, and the linked guides. No AWS account, deployment, or paid service is required. They complement, rather than replace, hands-on AWS experience.

## Workshop 1: trace both halves of a connection

**Goal:** explain routing and stateless return rules. Read [VPC](../topic-guides/06-VPC.md).

A private application initiates HTTPS to an external API. Its client source port is 51000; the API's destination port is 443. The application uses a zonal public NAT gateway in the same AZ.

1. Draw application → NAT → IGW → API, then the reverse path.
2. Label the private-subnet default route and NAT-subnet internet route.
3. At the application subnet NACL, write the destination port and direction for each packet.
4. Delete only the return rule. Predict the symptom and where to inspect it.
5. Remove the NAT gateway's AZ. Explain the dependency, then compare per-AZ zonal NAT with regional NAT availability mode.

<details>
<summary>Expected result and debugging checks</summary>

- Private route: 0.0.0.0/0 → zonal NAT; public NAT subnet: 0.0.0.0/0 → IGW.
- Application request: outbound destination TCP 443. Response: inbound destination TCP 51000. Source/destination CIDRs must also match; allow rules must precede any matching deny.
- Removing inbound return permission prevents connection completion even if the security group permits the initiated flow.
- A single zonal NAT couples internet egress to its AZ. Local per-AZ NAT routes or a suitable regional NAT design address different operating requirements.
- A full diagnosis also inspects NAT-subnet NACLs, security groups, DNS, routes, and destination behavior. One rule is deliberately isolated in this exercise.

</details>

**Pass:** explain why blindly adding an outbound ephemeral rule is wrong for this particular client flow. Change the app into an HTTPS server and explain how the directions change.

## Workshop 2: availability is not recovery from a mistake

**Goal:** select database protection by failure type. Read [RDS](../topic-guides/09-RDS-Aurora.md) and [DR](../topic-guides/35-Disaster-Recovery.md).

A shop has a relational database, ten-minute maximum acceptable downtime, and five-minute maximum acceptable data loss. A developer deletes rows at 10:00; the problem is discovered at 10:20.

1. Choose a candidate AZ-availability design; say whether its standbys can serve reads.
2. Explain whether failing over at 10:20 recovers the rows.
3. Draft a restore procedure: restore point, isolated validation, application cutover, and treatment of valid writes after 10:00.
4. Identify which timings must be measured before claiming the objectives are met.
5. List the cost categories of continuous standby versus restoring from backup. Use symbols or current regional prices; do not invent a universal dollar total.

<details>
<summary>Expected result and debugging checks</summary>

An RDS Multi-AZ DB instance is a candidate for AZ failure; its standby is unreadable. A Multi-AZ DB cluster has readable additional instances. Neither undoes replicated deletes.

PITR to a point before the mistake can recover earlier data. Validate the restored database before cutover, plan how to reconcile subsequent valid writes, and measure restore, validation, and application reconnect time. Restoring to 09:59 and discarding later writes could violate the five-minute loss objective. A recovery feature alone is insufficient evidence.

Continuous standby incurs ongoing infrastructure cost. Backups incur storage and restore-related costs; rebuilding also consumes time and compute. Choose based on tested objectives and actual prices.

</details>

**Pass:** explain why “backup exists” and “RTO met” are separate claims.

## Workshop 3: the crash between a side effect and deletion

**Goal:** reason about retries and independent consumers. Read [messaging](../topic-guides/17-SQS-SNS-Kinesis.md).

An order event must reach billing and shipping. Billing charges the card, then crashes before deleting the queue message.

1. Draw fan-out with a separate backlog for each application.
2. Write the receive → charge → delete timeline and insert the crash.
3. Explain what visibility expiration does.
4. Propose an idempotency key and where its result is recorded.
5. Test mentally: crash before the charge, after the charge, and after deletion. Does merely recording “processed” before charging introduce a new failure?

<details>
<summary>Expected result and debugging checks</summary>

SNS → billing SQS and shipping SQS lets both applications receive every event. A shared queue would distribute messages instead.

The message can return after visibility expiry. Use a stable order/payment-operation ID with an idempotent payment provider, or an appropriately transactional design. A separate “processed” flag alone leaves a race: writing it first can skip an unperformed charge; writing it afterward can allow a repeated charge. Persist the result and reconcile uncertain outcomes. FIFO send deduplication does not solve this transaction boundary.

Configure retries, queue retention, failure alarms, and a DLQ; deleting a message only after success still requires protection against redelivery.

</details>

**Pass:** explain one scenario where a longer visibility timeout helps and one where only idempotency protects the business effect.
