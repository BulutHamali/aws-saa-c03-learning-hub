# Contributing

Thank you for helping learners make better architecture decisions.

## What makes a useful contribution

- Correct an outdated or ambiguous statement and link to authoritative AWS documentation.
- Add a clear decision rule, diagram, or original scenario.
- Improve accessibility, navigation, or plain-language explanations.
- Report a broken link or a statement that needs verification.

Do not submit exam dumps, recalled live questions, copied commercial practice questions, secrets, account identifiers, or claims of guaranteed exam coverage.

## Fact-check standard

For factual changes, include:

1. The exact claim being changed.
2. A link to current AWS documentation, an AWS FAQ, or the official exam guide.
3. The date you checked it.
4. Whether the fact is regional, quota-dependent, configurable, or pricing-sensitive.

Prefer durable selection criteria over hard-coded limits. When a number is essential, identify whether it is a default, an adjustable quota, or a hard limit.

## Writing style

- Lead with the learner's requirement and trade-off.
- Expand acronyms on first use.
- Explain why a tempting alternative fails.
- Use original scenarios; do not imitate proprietary question wording.
- Keep product claims precise and avoid “always” or “never” unless the documentation supports them.

## Pull requests

Keep each pull request focused. Run the repository checks before submitting:

```bash
python3 scripts/check_repository.py
python3 -m unittest discover -s scripts -p 'test_*.py'
```

By contributing, you agree that your contribution is available under this repository's CC BY 4.0 license.

The checks validate inline Markdown links/images, heading anchors, study-plan coverage, and attribution. They do not fetch external URLs, validate all Markdown syntax, or establish factual accuracy. For technical changes, follow the source and scope standard in [the audit record](AUDIT.md).

