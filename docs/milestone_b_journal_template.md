# ARC-AGI Milestone B Journal Draft Template

Use this draft to write your Milestone B journal in JDF format and export to PDF for Canvas.
Replace bracketed placeholders before submission.

---

## Header

- Name: [Your Name]
- Date: [Submission Date]
- Course: CS7637 KBAI
- Milestone: B

---

## 1) How does your agent currently function? (Rubric: Agent Description, 3 pts)

### 1.1 High-level architecture
Describe your end-to-end pipeline from input problem to predicted output.

- Input representation: [e.g., NumPy grid(s), object list, graph, etc.]
- Core strategy selection: [single strategy or strategy chooser]
- Candidate generation: [how candidate solutions are produced]
- Candidate scoring/validation: [how you rank/filter candidates]
- Final answer selection: [how one output is chosen]

### 1.2 Problem-solving mechanisms
Explain what transformations or reasoning primitives your agent uses.

- Geometric transforms: [rotate/flip/translate/scale]
- Color transforms: [recolor, palette remap, majority/minority color logic]
- Object operations: [connected components, bounding boxes, overlap rules]
- Rule induction: [how rules are inferred from train pairs]
- Conflict handling: [tie-breakers, confidence, backtracking]

### 1.3 Control flow and fallback behavior
Explain what happens when the primary approach fails.

- Primary path: [describe]
- Fallback path(s): [describe]
- Failure mode behavior: [default output, nearest match, no-op, etc.]

---

## 2) How well does your agent currently perform? (Rubric: Agent Performance, 1 pt)

Provide concrete performance numbers for Set B.

### 2.1 Scores

| Subset | Correct | Total | Percent |
|---|---:|---:|---:|
| Training B | [X] | 16 | [X%] |
| Test B (Gradescope) | [Y] | 16 | [Y%] |

- Milestone threshold target: >= 6/16 on Training B and >= 6/16 on Test B.
- Current status: [Met / Not Met]

### 2.2 Brief result interpretation
Summarize what these numbers suggest about current capability.

[2-4 sentences]

---

## 3) What problems does your agent perform well on? Why? (Rubric: Agent Success, 1 pt)

Identify categories where your approach is reliable.

- Strong category 1: [type]
  - Why it works: [reason tied to algorithmic design]
  - Example problem(s): [IDs if available]
- Strong category 2: [type]
  - Why it works: [reason]
  - Example problem(s): [IDs]
- Strong category 3: [type]
  - Why it works: [reason]
  - Example problem(s): [IDs]

Write 1 short paragraph connecting successes to specific design choices.

---

## 4) What problems does your agent struggle on? Why? (Rubric: Agent Struggles, 1.5 pts)

Describe failure patterns and likely root causes.

- Weak category 1: [type]
  - Typical failure: [wrong size / wrong colors / wrong object relation / etc.]
  - Root cause hypothesis: [why your current method fails]
- Weak category 2: [type]
  - Typical failure: [describe]
  - Root cause hypothesis: [describe]
- Weak category 3: [type]
  - Typical failure: [describe]
  - Root cause hypothesis: [describe]

Add one paragraph on which bottleneck is highest-priority and why.

---

## 5) How efficient is your agent? (Rubric: Agent Efficiency, 1 pt)

Report runtime with concrete measurements and scaling behavior.

### 5.1 Runtime measurements

| Evaluation Slice | Avg Runtime / Problem | Total Runtime | Notes |
|---|---:|---:|---|
| Training B local run | [X sec] | [X sec] | [machine/setup] |
| Validation subset | [X sec] | [X sec] | [if used] |

### 5.2 Complexity discussion

- Dominant expensive step(s): [e.g., candidate search, object matching]
- Rough scaling trend: [e.g., grows with number of objects, grid size, or candidates]
- Slow-case trigger(s): [what patterns cause slowdown]

If you use Big-O, include it here; if not, explain practical scaling qualitatively.

---

## 6) How will you improve performance before final submission? (Rubric: Agent Improvement, 1.5 pts)

Give an actionable plan, not only goals.

### 6.1 Priority roadmap

1. [Improvement task 1]
   - Expected impact: [which errors it should fix]
   - Implementation approach: [how you will implement]
   - Validation plan: [how you will verify improvement]
2. [Improvement task 2]
   - Expected impact: [...]
   - Implementation approach: [...]
   - Validation plan: [...]
3. [Improvement task 3]
   - Expected impact: [...]
   - Implementation approach: [...]
   - Validation plan: [...]

### 6.2 Risk and mitigation

- Main risk: [e.g., overfitting to visible training set]
- Mitigation: [e.g., holdout checks, ablation, simpler rule prioritization]

---

## 7) How will your approach generalize to Set C? (Rubric: Agent Generalization, 1 pt)

Predict where the current architecture will transfer and where it may fail.

- Likely to transfer:
  - [type of reasoning pattern]
  - Why transfer is plausible: [reason]
- Likely to struggle:
  - [type of reasoning pattern]
  - Why it may fail: [reason]
- Planned Set C preparation:
  - [specific adaptation 1]
  - [specific adaptation 2]

---

## 8) What feedback do you want from classmates?

Ask for targeted feedback that helps your next iteration.

- Feedback request 1: [e.g., better abstraction for shape correspondence]
- Feedback request 2: [e.g., pruning strategies for candidate search]
- Feedback request 3: [e.g., balancing interpretability and breadth]

---

## 9) Final quality check before PDF export

- [ ] Journal is in JDF format using the official class template.
- [ ] Every Milestone B prompt is answered.
- [ ] Claims are tied to evidence (scores, timing, examples).
- [ ] Improvement plan includes concrete next actions.
- [ ] Generalization section explicitly discusses Set C.
- [ ] PDF exports correctly and is readable end-to-end.

