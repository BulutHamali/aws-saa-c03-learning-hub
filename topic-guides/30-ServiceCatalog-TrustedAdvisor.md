# Section 30: Service Catalog & Trusted Advisor

## The idea

Two small services, one shared theme: keeping humans out of trouble.

**AWS Service Catalog** is a **vending machine of pre-approved infrastructure**. The cloud team stocks the machine; everyone else just presses a button and gets a compliant, working stack — no keys to the kitchen required. Concretely: administrators define **products** (which are really **CloudFormation templates**) and group them into **portfolios**, then grant end users access to launch them. The magic trick: users can launch these stacks **without holding broad IAM permissions themselves** — Service Catalog launches on their behalf using its own constrained role. So a data scientist can spin up "the approved EMR cluster" without ever having permission to create EMR clusters directly.

Signal phrase: "allow teams to deploy **only approved, standardized, compliant configurations** via self-service" → **Service Catalog**.

**Trusted Advisor** is your **automated AWS consultant** — a robot auditor that continuously scans your account and nags you about the exact things a human consultant would bill you for.

## Trusted Advisor check categories

| Pillar | Example checks |
|---|---|
| **Cost Optimization** | Idle EC2 instances, unattached Elastic IPs, underused RDS |
| **Performance** | Overutilized instances, high-latency configs |
| **Security** | Security groups open to 0.0.0.0/0, **MFA missing on root**, public S3 buckets |
| **Fault Tolerance** | Missing Multi-AZ, snapshots not taken, single-AZ exposure |
| **Service Limits** | You're approaching a **service quota** (e.g., near your VPC or EC2 limit) |
| **Operational Excellence** | Operational practices and service-use recommendations |

**Check support entitlement:** Basic Support exposes a subset of checks. Current documentation identifies Business Support+, Enterprise Support, and Unified Operations for the full set, with legacy-plan transitions and exceptions. If checks are missing, inspect both entitlement and permissions. [Support documentation](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html).

Also worth one neuron each:
- Trusted Advisor **recommends**; it doesn't fix. Pair it with EventBridge/CloudWatch for alerting on check status changes.
- Distinguish from neighbors: **Config** = "is this resource *compliant with my rules*?"; **Inspector** = software vulnerabilities on workloads; **Trusted Advisor** = broad best-practice checks across its check categories, including cost and limits.

## Question patterns

> *"Non-technical teams must deploy infrastructure, but only pre-approved configurations, without granting them broad IAM permissions"* → **Service Catalog** (vending machine: products in portfolios, launch-on-behalf)

> *"Identify idle instances and unattached Elastic IPs to reduce the bill"* → **Trusted Advisor** (Cost Optimization pillar)

> *"Team can only see a few Trusted Advisor checks — why?"* → **Support plan** (check current support entitlement and permissions)

> *"Get warned before hitting an AWS service quota"* → **Trusted Advisor Service Limits check** (limits = its own pillar)

> *"Flag security groups allowing unrestricted access and missing root MFA"* → **Trusted Advisor** (Security pillar)

> *"Central IT curates standard CloudFormation-based products for business units"* → **Service Catalog portfolios** (products live in portfolios, shared to users/accounts)

## Pocket card

| Keyword | Answer |
|---|---|
| Self-service approved stacks, minimal IAM | Service Catalog |
| Product / portfolio | Service Catalog terms (CFN template / group of products) |
| Idle / unused / unattached resources | Trusted Advisor (Cost) |
| Approaching quota warning | Trusted Advisor (Service Limits) |
| Open SGs, root MFA check | Trusted Advisor (Security) |
| Full checks unavailable | Check current support entitlement and permissions |
| Six categories | Cost, Performance, Security, Fault Tolerance, Service Limits, Operational Excellence |

Trusted Advisor tells you the bill *could* be smaller — the cost management tool zoo in the next section is how you actually see, alert on, and shrink it.

Targeted review: 2026-10-10. [AWS check-category reference](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor-check-reference.html).
