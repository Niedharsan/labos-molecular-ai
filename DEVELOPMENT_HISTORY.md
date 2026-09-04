# Development History

> LabOS has been developed in a private Git repository since **July 2026**.  
> This public repository is a technical showcase, so the private source history and pull-request links are not exposed. The milestones below are taken from the actual private Git/PR history.

## July 2026 — From molecular tools to a unified AI workspace

- Built a chat-first molecular-engineering interface around the existing CRISPR, primer, cloning and laboratory-library tools.
- Added persistent molecular sessions, structured results and evidence/tool summaries.
- Replaced the earlier fixed/planner-style architecture with a **single autonomous molecular specialist using dynamically loaded skills**.
- Added deterministic completion/validation gates so exact molecular operations remained outside the AI reasoning layer.
- Expanded Library-aware component selection and exact virtual cloning workflows.

## Late July 2026 — Library-grounded cloning and workflow evaluation

- Added biological-role-based Library component resolution rather than searching for whole workflows as one text query.
- Added exact construct simulation and validation for Library-derived cloning workflows.
- Built a separate published-plasmid reconstruction/evaluation service with isolated data and review storage.

## August 2026 — Persistent scientific runtime

- Consolidated the system around one persistent `MolecularDesignGraph` and shared workflow state.
- Added PostgreSQL/Alembic-backed persistence and production-readiness fixes.
- Added real multi-turn molecular conversations rather than treating every reply as a new task.
- Added resumable long-running workflows and provider/runtime recovery.

## August 2026 — Provider and model independence

- Separated the molecular workflow from any one LLM provider.
- Added OpenAI-compatible, Hermes and local-model transport paths behind the same scientific runtime.
- Reduced repeated model context and provider overhead while keeping the same molecular state and deterministic tools.
- Added bounded parallel execution for independent deterministic calls.

## August 2026 — Molecular capability expansion

Expanded deterministic scientific support without creating a separate AI for each task:

- general PCR and exact virtual PCR
- cloning/CRISPR assay design and qPCR modes
- MAFFT/MUSCLE nucleotide and protein alignment
- conservation analysis and shared-target CRISPR design
- exact genomic edit reconstruction and consequence analysis
- Golden Gate/MoClo optimization
- RNA structure and bacterial RBS analysis
- sequence/reference retrieval and source tracking

## August–September 2026 — Single-specialist architecture refinement

The system was progressively simplified so that:

- **one scientific AI retains the full task context**;
- cloning, knockout, knock-in and other abilities are loaded as skills when needed;
- deterministic tools own exact sequence operations and molecular calculations;
- AI owns biological interpretation, component/method choice, replanning and stopping decisions;
- final outputs remain grounded in exact deterministic evidence.

## September 2026 — Evidence-grounded cloning expansion

A separate research workflow was used to systematically investigate **36 cloning and DNA-construction methods**.

The resulting research corpus retained:

- **≥987 source-method evidence instances**
- **≥414 explicitly classified primary/method papers**
- **860 structured practical observations, failure modes and rescue strategies**
- **77 deduplicated reusable capability classes**

These findings were used to expand and consolidate LabOS cloning capabilities rather than creating dozens of duplicate method-specific tools.

## September 2026 — Scientific-engine consolidation

The molecular backend was further simplified around established scientific software where possible:

- pydna for supported cloning/reaction chemistry
- DnaCauldron for Golden Gate/MoClo
- Primer3 for primer design/evaluation
- CRISPRscan/CHOPCHOP and separate specificity evidence for CRISPR
- DNA Chisel for repeat/hairpin evidence
- ViennaRNA/OSTIR for RNA/RBS analysis
- mappy/minimap2 and pyspoa for long-read/full-plasmid QC
- pySBOL3 for sequence/feature interoperability

Legacy and duplicate project-owned implementations were removed where an established backend could become authoritative.

## September 2026 — Validation, provenance and privacy hardening

- Added PCR-history-aware construct-validation planning.
- Added full-plasmid/long-read QC support.
- Improved exact material/reference identity tracking.
- Added central control over external sequence/file data egress.
- Continued expanding regression tests around routing, cloning chemistry, CRISPR evidence and source/material handling.

## Current state

LabOS is an **active research prototype** combining:

- a persistent scientific AI;
- dynamically composed molecular skills;
- deterministic molecular-biology engines;
- laboratory/library context;
- structured validation and source tracking;
- a separate evaluation/training system.

The public repository intentionally exposes only architecture, selected non-sensitive code excerpts, synthetic examples and demonstration media. The active research codebase remains private.
