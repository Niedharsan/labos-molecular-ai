# Development History

> LabOS has been developed in a private Git repository since **July 2026**.  
> This public repository is a technical showcase, so private source history, prompts, datasets and pull-request links are not exposed. The milestones below are taken from the actual development history.

## July 2026 — CRISPR and molecular-engine foundation

LabOS began as a set of molecular-biology services that I built around CRISPR design and sequence handling, before the later unified molecular workspace.

Early capabilities included:

- API-first gene and transcript resolution;
- transcript-aware genomic/CDS mapping;
- protein-domain evidence for target selection;
- CRISPR guide generation, ranking and user-guide auditing;
- CRISPRscan/CHOPCHOP activity evidence and Bowtie-based off-target evidence;
- Primer3-backed primer design;
- restriction-site analysis;
- knock-in cassette, donor and validation-primer planning;
- structured GPT hand-offs so biological judgement could be combined with deterministic backend calculations.

The early system was **not a multi-agent molecular architecture**. It combined deterministic scientific services with GPT-assisted biological interpretation/review.

## Late July 2026 — Unified LabOS workspace and single scientific specialist

The CRISPR, primer, cloning, sequence and laboratory-library components were brought into one molecular-engineering workspace.

From the first LangGraph-based molecular runtime, the architecture used **one autonomous molecular specialist rather than a multi-agent swarm**. The aim was to keep the full biological objective and accumulated evidence in one context while loading only the relevant skills and tools for the current task.

This stage added:

- a chat-first molecular interface;
- persistent molecular sessions and structured results;
- repository-controlled cloning, knockout and knock-in skills;
- a typed deterministic tool catalogue;
- exact sequence/material handling outside the LLM;
- deterministic completion and validation gates;
- Library-aware component selection and exact virtual cloning;
- molecular-file import and construct visualisation.

## Late July–August 2026 — Cloning and construct-design expansion

The cloning layer expanded from basic construct operations into a broader molecular-design system covering multiple assembly families and multi-step workflows.

Work included:

- restriction/ligation and seamless assembly;
- Golden Gate and hierarchical MoClo;
- Gateway/MultiSite Gateway;
- USER and yeast-assembly foundations;
- cloning-specific primer/PCR workflows;
- exact intermediate-product reuse across sequential reactions;
- construct identity and junction checks;
- assembly reporting and source-material tracking;
- laboratory-inventory-aware route selection rather than assuming every sequence must be synthesized or re-created.

## August 2026 — Persistent scientific runtime and model independence

The application was hardened from a collection of callable tools into a persistent scientific workflow runtime.

Key changes included:

- one persistent `MolecularDesignGraph` carrying the molecular task state;
- real multi-turn conversations and resumable long-running workflows;
- PostgreSQL/Alembic-backed persistence and checkpoints;
- model/provider abstraction so the same molecular runtime could use different OpenAI-compatible, Hermes or local model paths;
- bounded parallel execution for independent deterministic operations;
- context/evidence compaction so long sequences and repeated tool outputs were not unnecessarily sent back to the model;
- explicit separation between model reasoning, deterministic tool output and completion evidence.

## August 2026 — Broad molecular capability layer

Scientific support expanded substantially while keeping one specialist runtime and reusing shared engines instead of creating one AI agent per capability.

Added or strengthened areas included:

- general PCR and exact virtual PCR;
- insert, vector, mutagenesis, colony, junction and genotyping PCR workflows;
- qPCR and CRISPR validation-assay planning;
- Sanger-primer selection and primer walking;
- nucleotide/protein alignment with MAFFT/MUSCLE;
- conservation analysis across paralogs, ohnologs and orthologs;
- shared-target/multilocus CRISPR design;
- exact reconstruction of deletions, HDR knock-ins, base edits and prime edits;
- coding/protein consequence analysis;
- Golden Gate overhang/breakpoint optimisation;
- RNA structure/accessibility analysis;
- bacterial RBS analysis;
- codon optimisation and sequence-quality checks;
- promoter/reference-sequence resolution;
- sequence, material and external-reference identity handling.

## August 2026 — Separate evaluation and training infrastructure

A separate AI service was developed to construct and evaluate molecular-design tasks without mixing benchmark/evaluation data into the normal LabOS runtime.

It provides controlled task construction, evidence isolation, observable tool/decision traces, human review and reproducible evaluation of molecular workflows. The detailed model-training strategy is intentionally outside the scope of this public repository.

## September 2026 — Evidence-grounded cloning expansion

A separate research workflow was used to systematically investigate **36 cloning and DNA-construction methods** rather than relying on a small set of textbook workflows.

The retained research corpus contained:

- **≥987 source-method evidence instances**;
- **≥414 explicitly classified primary/method papers**;
- **860 structured practical observations, failure modes and rescue strategies**;
- **77 deduplicated reusable capability classes**.

The research was used to identify method-specific constraints, practical failure points, rescue strategies and places where established scientific software could replace redundant project-owned logic.

## September 2026 — Scientific-engine consolidation

The molecular backend was progressively consolidated around established scientific software where appropriate, while LabOS retained biological context, tool coordination and evidence interpretation.

Examples include:

- **pydna** for supported cloning/reaction chemistry;
- **DnaCauldron** for Golden Gate/MoClo;
- **Primer3** for primer design/evaluation;
- **CRISPRscan + CHOPCHOP** for guide-activity evidence;
- **Bowtie / crisprVerse** for specificity evidence;
- **DNA Chisel** for repeat/hairpin analysis;
- **ViennaRNA + OSTIR** for RNA/RBS analysis;
- **mappy/minimap2 + pyspoa** for long-read/full-plasmid QC;
- **pySBOL3** for sequence/feature interoperability.

Where mature scientific engines existed, duplicate internal chemistry/scoring implementations were removed rather than maintained in parallel.

## September 2026 — Routing, QC, material identity and privacy hardening

The later work focused on making complex workflows more reliable and auditable rather than simply adding more features.

This included:

- species/context-aware biological-intent routing;
- multi-part requests with independently completable molecular routes;
- PCR-history-aware validation-depth planning;
- long-read/full-plasmid sequence QC;
- exact material/reference identity and source tracking;
- central control over sequence/file data leaving the local system;
- stronger fail-closed behaviour when required molecular evidence is unavailable;
- continued regression testing around routing, cloning chemistry, CRISPR evidence and construct validation.

## 5 September 2026 — Context efficiency and biological-selection refinement

Recent work focused on reducing unnecessary model-context/token use during long molecular-design runs while preserving exact scientific evidence and deterministic validation. Biological selection was also made more structured so that core biological choices remain clearer and more stable as a task progresses.

The detailed prompt, evidence-management and decision-routing mechanisms behind these changes are intentionally not included in the public showcase.

## Current architecture

LabOS currently combines:

- **one persistent scientific AI** that retains the task context;
- dynamically loaded molecular skills;
- a large typed catalogue of deterministic molecular actions;
- laboratory/library-aware material selection;
- external biological reference integration;
- exact reaction/sequence simulation through scientific software;
- validation and source/material tracking;
- a separate evaluation/training system.

The public repository intentionally exposes only architecture, selected non-sensitive code excerpts, synthetic examples and demonstration media. The active research codebase remains private.

