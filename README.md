# Ergonomics Engineering Standards

Technology-independent engineering guidance for ergonomic task and interaction
design. The normative standard is located at
`standards/engineering-standards-ergonomics.md`.

## Scope

The repository translates publicly described ergonomics and human-centred
design principles into reviewable engineering rules for software, hardware,
automation, command-line tools, desktop applications, web systems, mobile
applications, and operational workflows.

It is informed by ISO 9241, especially task requirements and human-centred
interaction design. It does not reproduce ISO text and does not by itself
establish conformity or certification against an ISO publication.

## Consumption

Technology repositories should reference this repository as an independent
normative source and add only technology-specific adaptations locally. They
must not copy the complete standard into framework-specific guidance.

## Validation

Run Markdown validation with:

```powershell
npx.cmd --yes markdownlint-cli2 "**/*.md"
```
