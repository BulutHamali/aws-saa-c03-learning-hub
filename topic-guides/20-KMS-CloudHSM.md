# Section 20: KMS & CloudHSM

[Topic index](00-README.md)

## The idea

Encryption protects data only if key access and recovery are designed correctly. Separate three questions: who controls key policy, who operates the cryptographic infrastructure, and which compliance requirements apply?

## Choose by ownership and operating model

| Option | Control and operating model | Good fit |
|---|---|---|
| AWS-owned keys | Service-owned; not exposed as keys in your account | Managed encryption without customer key administration |
| AWS-managed KMS keys | AWS manages their lifecycle; limited customer control | Supported service integration with AWS-managed policy |
| Customer-managed KMS keys | You administer policy, grants, lifecycle, and eligible rotation settings | Fine-grained access, audit, and cross-account requirements |
| CloudHSM | Dedicated HSM infrastructure with customer administration of cryptographic users and keys | Requirements for dedicated hardware or supported custom crypto interfaces |

Do not choose CloudHSM solely because a question says “FIPS Level 3.” **KMS uses FIPS 140-3 Security Level 3 validated HSMs.** Validate the required certification and module rather than relying on the obsolete “KMS Level 2” comparison.

Sources: [KMS data protection](https://docs.aws.amazon.com/kms/latest/developerguide/data-protection.html), [CloudHSM overview](https://docs.aws.amazon.com/cloudhsm/latest/userguide/introduction.html).

## Permissions: key policy is central

A KMS key policy can directly authorize principals or enable IAM policies to delegate access. Grants can also authorize specified operations. An identity's broad IAM permission does not bypass the key policy, and explicit denies still matter.

Cross-account access requires the appropriate permission in the owning account's key policy and the caller's account IAM policy. “Both must always contain a direct Allow” is too broad for same-account access.

Source: [KMS key policies](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html).

## Envelope encryption

The symmetric KMS Encrypt operation accepts up to 4,096 bytes. Encrypt larger payloads locally using a data key, and protect that data key with KMS:

```text
GenerateDataKey → plaintext key + encrypted key
plaintext key → encrypt payload locally → discard plaintext key
store encrypted payload + encrypted key
decrypt encrypted key with KMS → decrypt payload locally
```

Source: [KMS Encrypt API](https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html).

## Rotation, deletion, and cost

- Eligible customer-managed keys support automatic rotation with a configurable period; do not assume every key type supports it or that yearly rotation is the only choice.
- Rotation changes key material while preserving the ability to decrypt older ciphertext. It does not re-encrypt stored data automatically.
- Scheduling deletion has a 7–30 day wait. Disabling a key blocks new KMS use sooner, but does not erase plaintext or cached data keys already obtained.
- KMS charges can include key storage and requests. “AWS-managed key = every operation free” is incorrect.
- S3 Bucket Keys can reduce KMS request volume for SSE-KMS workloads. Check audit requirements and applicability.

Sources: [rotation](https://docs.aws.amazon.com/kms/latest/developerguide/rotating-keys-enable.html), [deletion](https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys.html), [pricing](https://aws.amazon.com/kms/pricing/), [S3 Bucket Keys](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-key.html).

## Question patterns

- **“Audit cryptographic API operations”** → KMS with CloudTrail; specify the operations and logging requirements.
- **“Dedicated HSMs with customer crypto administration”** → evaluate CloudHSM.
- **“Encrypt a large file”** → envelope encryption, not one direct KMS Encrypt call.
- **“IAM says Allow but key use fails”** → inspect the key policy, grants, explicit denies, and cross-account requirements.
- **“Rotate the key”** → distinguish key material rotation from data re-encryption.

## Check your understanding

Does “FIPS Level 3 required” by itself eliminate KMS?

<details>
<summary>Expected explanation</summary>

No. KMS uses FIPS 140-3 Security Level 3 validated HSMs. Dedicated tenancy, key custody, interfaces, and the exact compliance requirement distinguish the choices.

</details>

Targeted fact check: 2026-10-10. Adapted from RonitSachdev's guide; revised claims are linked above.
