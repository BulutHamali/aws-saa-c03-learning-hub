# Section 27: Offline Transfer and Snow Service Lifecycle

[Topic index](00-README.md)

## The durable idea: calculate before choosing transport

Physical transfer can help when the network cannot meet a migration deadline. But a familiar service name is useful only if the customer can still order and use it.

For decimal units:

```text
seconds = data_TB × 10^12 × 8 / (bandwidth_Mbps × 10^6 × utilization)
```

Example: 100 TB over 100 Mbps takes about **92.6 days at 100% utilization**, or **132.3 days at 70%**, before transfer overhead, verification, and retries. Compare that with the deadline and the full logistics time of any offline option.

## Lifecycle status checked 2026-10-10

| Product | How to treat it |
|---|---|
| Snowcone | Historical material: device ordering ended November 12, 2024 |
| Snowball Edge | Availability is restricted; AWS announces commercial-Region end of support on December 31, 2026, with stated exceptions |
| Snowmobile | Historical material: do not infer current availability from old study notes |

The current [Snowball page](https://aws.amazon.com/snowball/) and [Snow service update](https://aws.amazon.com/blogs/storage/aws-snow-device-updates/) take precedence over older capacity tables. The published exam scope and commercial product availability are different questions; check both rather than assuming a retirement immediately removes a topic from the exam.

## Choosing a migration approach

1. Measure the data size, usable bandwidth, and deadline.
2. Include changed data during the migration and the final cutover.
3. Evaluate online transfer using DataSync, available connectivity, and parallel transfer where appropriate.
4. If online transfer cannot meet the deadline, verify available offline options and customer eligibility with current AWS guidance.
5. Plan integrity checks, encryption, access control, and source-system rollback.

Do not select a device just because transfer exceeds a week. Shipping, availability, processing, device generation, and customer eligibility all affect the decision.

## Check your understanding

A team has 40 TB to move in ten days over a dedicated 1 Gbps connection at 50% utilization. Does the data size alone require a physical device?

<details>
<summary>Expected explanation</summary>

No. Ideal transfer time is about 7.4 days at the stated utilization. The remaining time must cover setup, validation, retries, and changed data. Compare online feasibility and actual available offline options; there is no automatic “large data = Snow” rule.

</details>

## Pocket card

| Requirement | Reasoning step |
|---|---|
| Deadline versus bandwidth | Calculate transfer time with utilization |
| Offline transfer | Verify availability and full logistics time |
| Ongoing access to cloud-backed files | Evaluate Storage Gateway |
| Online bulk transfer | Evaluate DataSync |
| Database migration with ongoing changes | Evaluate DMS and cutover requirements |
