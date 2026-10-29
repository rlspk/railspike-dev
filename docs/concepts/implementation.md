# Shared implementation standards

**Purpose:** preserve the same substantive implementation requirements across staged and one-shot execution.

**Operational principle:** before adding a component, the agent inspects existing implementations and records reuse or a justified new equivalent. Either execution mode verifies its normal-entry outcome and recovery, reviews the diff, and reports incomplete evidence without claiming success; planning and commit cadence remain mode-specific.

**Where it lives:** [shared contract](../../../railspike/docs/workflow/implementation_standards.md), [mode selection](../../../railspike/RAILSPIKE.md#choose-the-execution-mode), [staged execution](../../../railspike/docs/workflow/step4_implementation_do.md), and [one-shot execution](../../../railspike/docs/workflow/one_shot.md).
