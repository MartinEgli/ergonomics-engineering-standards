# Engineering Standards (Ergonomics)

## Purpose And Scope

1. `Must` (`ERG-001`): This standard defines technology-independent engineering rules for
   designing tasks, interactions, information, controls, and operational
   workflows around human capabilities, limitations, goals, and well-being.
2. `Must` (`ERG-002`): It applies to interactive software, hardware, automation,
   administrative tools, command-line systems, control systems, and mixed
   human-technology workflows.
3. `Must` (`ERG-003`): Technology-specific standards may refine this baseline but must not
   weaken it without a documented risk-based exception.
4. `Must` (`ERG-004`): This is derived engineering guidance, not a reproduction of an ISO
   publication and not evidence of ISO certification or conformity.

## Mandatory Outcomes

1. `Must` (`ERG-005`): Intended users can complete representative tasks effectively and
   with effort proportionate to task complexity and risk.
2. `Must` (`ERG-006`): The design avoids unnecessary cognitive, perceptual, and physical
   workload.
3. `Must` (`ERG-007`): Users retain appropriate awareness and control over consequential
   actions, automation, waiting, interruption, recovery, and completion.
4. `Must` (`ERG-008`): Evaluation includes user well-being and workload, not only technical
   correctness or throughput.
5. `Must` (`ERG-009`): Ergonomic decisions are based on evidence from the actual context
   of use rather than designer preference alone.

## Context Of Use And Task Analysis

1. `Must` (`ERG-010`): Identify intended and foreseeable user groups, including relevant
   differences in experience, ability, language, environment, and frequency of
   use.
2. `Must` (`ERG-011`): Describe representative goals, task sequences, inputs, outputs,
   dependencies, interruptions, timing pressure, and consequences of error.
3. `Must` (`ERG-012`): Identify the physical, social, organizational, and technical context
   that changes how work is performed.
4. `Must` (`ERG-013`): Distinguish essential task complexity from complexity introduced by
   the system or organizational workflow.
5. `Should` (`ERG-014`): Validate task models with representative users or subject-matter
   experts before irreversible design decisions.

## Task Design And Workload

1. `Must` (`ERG-015`): Tasks form understandable units with visible entry conditions,
   progress, completion criteria, and outcomes.
2. `Must` (`ERG-016`): Work is not fragmented into avoidable steps, repeated data entry,
   unnecessary mode changes, or excessive navigation.
3. `Must` (`ERG-017`): Allocation between people and automation considers judgment,
   accountability, variability, fatigue, monitoring burden, and failure modes.
4. `Must` (`ERG-018`): Automated behavior remains observable and offers appropriate human
   intervention where risk or uncertainty makes intervention necessary.
5. `Should` (`ERG-019`): Workflows provide meaningful variation, autonomy, feedback, and
   opportunities to recover from sustained demand where the context permits.
6. `Should` (`ERG-020`): Repetitive high-frequency actions minimize reach, precision,
   memory, and confirmation effort without weakening safety.

## Interaction And Information

1. `Must` (`ERG-021`): Available actions and current system state are understandable at the
   point of need.
2. `Must` (`ERG-022`): Behavior is predictable from task context, established conventions,
   and prior user actions.
3. `Must` (`ERG-023`): Information is prioritized for the current decision and avoids
   irrelevant density, hidden dependencies, and competing signals.
4. `Must` (`ERG-024`): Status, warnings, and errors use text or equivalent meaning in
   addition to color, position, sound, or animation.
5. `Must` (`ERG-025`): Controls remain distinguishable, reachable, and operable under the
   supported input methods, display conditions, and user capabilities.
6. `Should` (`ERG-026`): Systems support learning through consistent concepts, safe
   exploration, and assistance near the task rather than requiring memorized
   procedures.

## Waiting, Interruptions, And Attention

1. `Must` (`ERG-027`): Work that is not immediate exposes whether it is queued, active,
   blocked, paused, failed, cancelled, or complete.
2. `Must` (`ERG-028`): Long-running work provides progress or meaningful activity status
   and does not demand continuous attention without operational need.
3. `Must` (`ERG-029`): Timeouts, retry intervals, refresh rates, and notification cadence
   reflect task urgency and human response capability.
4. `Must` (`ERG-030`): Interruptions are proportionate to urgency and consequence; routine
   progress does not compete with critical alerts.
5. `Should` (`ERG-031`): Users can defer, resume, or recover interrupted work without
   reconstructing avoidable context.
6. `Should` (`ERG-032`): Estimated remaining time is shown only when supported by a
   defensible estimate and is labelled as uncertain when appropriate.

## Error Prevention And Recovery

1. `Must` (`ERG-033`): Designs prevent predictable slips and mistakes before relying on
   error messages.
2. `Must` (`ERG-034`): Destructive or high-consequence actions make scope and result clear
   before commitment and support reversal where feasible.
3. `Must` (`ERG-035`): Error messages identify the affected task, current state, and a safe
   recovery path without blaming the user.
4. `Must` (`ERG-036`): Recovery preserves valid work and context wherever technically and
   operationally feasible.
5. `Should` (`ERG-037`): Repeated user errors trigger investigation of task and interaction
   design rather than additional training alone.

## Accessibility And Individualization

1. `Must` (`ERG-038`): Ergonomic evaluation includes users with relevant sensory, motor,
   cognitive, and language differences.
2. `Must` (`ERG-039`): Essential workflows remain operable through supported keyboard or
   alternative input paths when the platform provides them.
3. `Must` (`ERG-040`): Scaling, contrast, text size, focus, target size, and motion remain
   usable under supported environments.
4. `Should` (`ERG-041`): Users can adapt non-safety-critical presentation, pacing, density,
   and notification behavior when needs vary materially.

## Evaluation And Evidence

1. `Must` (`ERG-042`): Ergonomic requirements have observable acceptance criteria tied to
   representative tasks and users.
2. `Must` (`ERG-043`): Evaluation covers effectiveness, effort, errors, recovery, workload,
   comprehension, and user-reported experience as relevant to risk.
3. `Must` (`ERG-044`): High-risk workflows receive realistic scenario-based evaluation,
   including interruption, degraded performance, and failure paths.
4. `Should` (`ERG-045`): Teams retain findings, decisions, exceptions, and follow-up work
   in a reviewable form.
5. `Must` (`ERG-046`): A claim of ISO conformity requires an authorized copy of the
   applicable standard and an appropriate conformity assessment; this document
   alone is insufficient.

## Anti-Patterns

1. `Must Not` (`ERG-047`): Optimize only click count, speed, or information density while
   ignoring comprehension, error consequence, workload, or well-being.
2. `Must Not` (`ERG-048`): Use color as the sole carrier of status or priority.
3. `Must Not` (`ERG-049`): Hide running work, automation state, irreversible scope, or
   failure behind ambiguous controls.
4. `Must Not` (`ERG-050`): Treat documentation or training as the primary fix for a
   repeatedly confusing workflow.
5. `Must Not` (`ERG-051`): Generalize results from developers or expert users to all user
   groups without evidence.

## Review Checklist

1. `Must` (`ERG-052`): Users, goals, tasks, environment, frequency, and consequences are
   explicit.
2. `Must` (`ERG-053`): Workload, attention, waiting, interruption, errors, and recovery are
   designed intentionally.
3. `Must` (`ERG-054`): State, progress, controls, and outcomes are understandable through
   more than color alone.
4. `Must` (`ERG-055`): Representative evaluation evidence or a documented evaluation plan
   exists.
5. `Should` (`ERG-056`): Open ergonomic risks have owners and follow-up criteria.

## Consumer Adaptation

1. `Must` (`ERG-057`): Technology standards reference this repository rather than copying
   its complete normative content.
2. `Must` (`ERG-058`): Adaptations map these outcomes to concrete platform controls,
   threading, lifecycle, accessibility, scaling, input, and test mechanisms.
3. `Must` (`ERG-059`): Adaptations preserve technology independence in this repository.
4. `Should` (`ERG-060`): Consumer repositories record the version or commit of this
   standard used for review.

## Sources And Derivation

1. `Must` (`ERG-061`): Primary reference: ISO 9241-2:1992, task requirements for visual
   display terminal work, confirmed by ISO in 2020.
2. `Should` (`ERG-062`): Current interaction context is informed by ISO 9241-110:2020,
   ISO 9241-115:2024, ISO 9241-210:2019, ISO 9241-220:2019, and
   ISO/TR 9241-100:2023.
3. `Must` (`ERG-063`): Source status and applicability are rechecked before material
   revisions or conformity-related use.
4. `Must` (`ERG-064`): Official catalogue references:
   - <https://www.iso.org/standard/16874.html>
   - <https://www.iso.org/standard/77520.html>
   - <https://www.iso.org/standard/80773.html>
   - <https://www.iso.org/standard/63462.html>
   - <https://www.iso.org/standard/84402.html>
