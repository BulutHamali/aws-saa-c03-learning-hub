# Section 9: RDS & Aurora

[Topic index](00-README.md) · [Decision guide](../decision-guides/README.md)

## The idea

A managed relational database lets the team focus on data and queries while AWS handles infrastructure tasks. Standard RDS restricts OS access; workloads that require it need a different operating model, such as EC2 or a supported RDS Custom configuration.

Start with four separate questions: **Must the database survive a failure? Must reads scale? Must data survive a Region outage? Must accidental changes be recoverable?** An extra copy does not answer all four.

## Multi-AZ is a deployment family

| Option | Purpose | Can the additional instances serve reads? | Recovery |
|---|---|---|---|
| RDS Multi-AZ **DB instance** | Availability across AZs | No: its single synchronous standby does not serve queries | Managed failover |
| RDS Multi-AZ **DB cluster** | Availability plus read capacity | Yes: one writer and two readable instances in three AZs | Managed failover |
| RDS DB instance read replica | Read scaling; sometimes a DR component | Yes; replication is asynchronous | Promotion is a separate operation |
| Aurora cluster with readers | Availability and read scaling with shared cluster storage | Yes | A reader can be promoted during managed failover |

Do not memorize “Multi-AZ never serves reads.” First identify **DB instance versus DB cluster** and the engine. Replica counts, feature support, and failover timings vary. A replica can lag; the application must tolerate that for reads sent to it.

Sources: [RDS Multi-AZ options](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html), [readable Multi-AZ clusters](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html), [RDS read replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html).

## Backups answer a different question

Replication copies a mistaken DELETE too. Use point-in-time recovery (PITR) or a suitable snapshot to recover earlier data.

- RDS automated backup retention can extend to 35 days.
- Manual snapshots remain until deleted; long-term retention may also use AWS Backup policies.
- On deleting a DB instance, retained automated backups are an explicit option; they expire under the configured retention period. That option does not apply to Multi-AZ DB clusters.
- Restoring creates a database to which the application must reconnect. Practice the restore and application cutover, not just backup creation.

Source: [retaining automated backups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.Retaining.html).

## Encryption migration

For an unencrypted RDS DB instance, use **snapshot → encrypted snapshot copy → restore → application cutover**. Plan downtime, data synchronization, permissions on the KMS key, and rollback. This is a migration, not an in-place toggle.

Source: [RDS encryption](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html).

## Connections and Aurora

**RDS Proxy** pools database connections. It is a strong candidate when bursts of clients, including Lambda functions, exhaust connections. It is not mandatory for every Lambda-to-RDS design; check supported engines, transaction behavior, and cost.

Aurora separates database compute from distributed storage. Its writer and reader endpoints help applications direct writes and reads correctly. Aurora Serverless v2 scales compute capacity, Aurora Global Database supports cross-Region reads and recovery, and cloning supports development copies. Aurora MySQL Backtrack can rewind supported, configured databases; it is not a universal restore feature.

Do not treat typical recovery times or storage capacities as unconditional guarantees. Engine/version support, configuration, workload, and recovery tests determine what is achievable.

Sources: [RDS Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html), [Aurora overview](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html), [Aurora Backtrack](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Managing.Backtrack.html).

## Question patterns

- **“One standby, automatic AZ failover, no reporting requirement”** → RDS Multi-AZ DB instance.
- **“Two readable standbys and automatic failover”** → RDS Multi-AZ DB cluster.
- **“Offload reporting; tolerate stale reads”** → evaluate a read replica.
- **“Recover rows deleted yesterday”** → PITR or an appropriate snapshot, not failover.
- **“Lambda bursts exhaust connections”** → evaluate RDS Proxy and concurrency controls.
- **“Cross-Region recovery with demanding objectives”** → evaluate Aurora Global Database and test the complete recovery path.

## Check your understanding

A learner says, “A Multi-AZ database cannot serve reads from its standby.” What information is missing?

<details>
<summary>Expected explanation</summary>

The deployment type. That statement fits the single-standby RDS Multi-AZ DB instance; a Multi-AZ DB cluster has readable additional instances. Aurora has its own cluster architecture.

</details>

## Pocket card

| Requirement | First question |
|---|---|
| AZ resilience | Which Multi-AZ deployment and failover path? |
| Read scaling | Is replica lag acceptable? |
| Logical-error recovery | What restore point and application cutover? |
| Cross-Region DR | What measured RPO and RTO? |
| Connection storm | Can pooling and concurrency controls help? |
| Long backup retention | What snapshot or AWS Backup retention policy? |

Targeted fact check: 2026-10-10. Adapted from RonitSachdev's guide; sources above cover the revised claims.
