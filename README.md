# AWS SAA-C03 Learning Hub

A practical, community-friendly path to the **AWS Certified Solutions Architect – Associate (SAA-C03)** exam.

This repository combines 37 concise topic guides with a repeatable learning system: choose a study path, learn the service trade-offs, solve architecture scenarios, track weak areas, and verify details against AWS documentation.

> [!IMPORTANT]
> This is an independent community resource, not an AWS exam dump and not affiliated with or endorsed by AWS. The exam can change. Use the [official AWS exam page](https://aws.amazon.com/certification/certified-solutions-architect-associate/) and documentation as the final authority.

## Choose your path

| If you have… | Start here | Suggested rhythm |
|---|---|---|
| 4–6 weeks | [Four-week learning plan](learning-paths/4-week-plan.md) | Learn → recall → scenario → review |
| 1–2 weeks | [Topic index](topic-guides/00-README.md) | Prioritize core infrastructure, databases, integration, and networking |
| A few days | [Decision guide](decision-guides/README.md) | Practice the service choices you are most likely to confuse |
| An exam booked | [Progress tracker](CHECKLIST.md) | Turn every missed question into a named weak area |

New to AWS? Start with the [prerequisites and glossary](START-HERE.md). Check the [exam-domain map](EXAM-MAP.md) and take the [diagnostic](practice/diagnostic.md) to choose weak areas.

Then test your reasoning with the [architecture challenges](practice/architecture-challenges.md). The answers explain why the tempting alternatives fail—not just which option wins.

## How to learn with this repository

1. **Understand:** read one topic guide without trying to memorize every limit.
2. **Recall:** close it and explain the service in your own words.
3. **Decide:** use the decision guide to compare similar services.
4. **Apply:** solve an architecture challenge before opening its answer.
5. **Repair:** record misses in the progress tracker and revisit them after 48 hours.
6. **Verify:** check volatile facts, quotas, and pricing in current AWS documentation.

## What is included

- [37 topic guides](topic-guides/00-README.md) with analogies, core concepts, traps, scenarios, and pocket cards
- [A four-week plan](learning-paths/4-week-plan.md) organized around active recall and spaced review
- [Decision matrices](decision-guides/README.md) for commonly confused AWS services
- [Architecture challenges](practice/architecture-challenges.md) with expandable explanations
- [A printable progress tracker](CHECKLIST.md) for topics, practice, and weak-area review
- [Architecture workshops](labs/README.md) with expected results; no AWS account required
- [An audit record](AUDIT.md) distinguishing verified corrections from material awaiting review
- Automated checks for internal link targets, heading anchors, study-plan coverage, and attribution

## A healthy way to use exam material

These guides teach architecture judgment rather than recalled exam questions. Do not add confidential exam content, copied practice-test questions, or claims that a question is “from the real exam.” Good contributions explain a durable AWS concept, cite an authoritative source, and make the trade-off easier to understand.

## Accuracy and contributions

AWS services evolve. If you find an outdated limit, ambiguous explanation, or missing trade-off, please open a fact-check issue or submit a pull request. See [CONTRIBUTING.md](CONTRIBUTING.md) for the evidence and writing standards.

## Attribution and license

The 37 numbered topic guides under `topic-guides/` were originally created by [RonitSachdev](https://github.com/RonitSachdev) in [RonitSachdev/aws-saa-c03-guides](https://github.com/RonitSachdev/aws-saa-c03-guides). This repository adapts that CC BY 4.0 work, corrects selected factual claims, and adds learning paths, decision aids, practice scenarios, workshops, community standards, and quality automation. Changes are not endorsed by the original author.

The repository is licensed under [CC BY 4.0](LICENSE). When reusing it, preserve attribution to the original author and indicate your changes.
