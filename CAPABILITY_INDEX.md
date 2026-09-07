# LabOS — Public Capability Index

> The active LabOS implementation, laboratory data, prompts and research corpus remain private. This page exposes the breadth and structure of the system without publishing private scientific implementation details.

[← Back to main README](README.md)

## September 2026 snapshot

| Capability | Scale |
|---|---:|
| Registered molecular tools | **116** typed molecular tool contracts |
| Cloning methods researched | **36** method families |
| Reviewed species/workflow profiles | **16** profiles across **12** organism/context categories |
| Research references reviewed across cloning methods | **≥987** method-linked source records |
| Practical implementation findings extracted from the research | **860** |
| Reusable engineering capabilities identified from those findings | **77** |

## 1. Current typed molecular contracts

The current private runtime registry contains **116 unique typed contracts**. They are dynamically filtered by task, phase and evidence state; not every contract is exposed to the model on every turn, and some are internal/composed deterministic operations.

### Routing, evidence, protocol and general molecular reasoning

- `parallel_tool_batch`
- `resolve_reference`
- `target_biology_context`
- `retrieve_grounded_evidence`
- `generate_experimental_protocol`
- `plan_validation_assays`
- `troubleshoot_experiment`
- `analyze_rna_structure`
- `analyze_bacterial_rbs`

### CRISPR design and exact edit reasoning

- `design_single_guides`
- `evaluate_supplied_guides`
- `design_crispant`
- `design_dual_deletion`
- `design_knockin`
- `design_marker_knockin`
- `design_genotyping_panel`
- `find_shared_paralog_guides`
- `design_base_edit`
- `design_prime_edit`
- `find_conserved_paralog_ohnolog_guides`
- `find_conserved_ortholog_guides`
- `map_shared_guide_to_all_intended_loci`
- `score_intended_multilocus_targeting`
- `separate_intended_multilocus_hits_from_offtargets`
- `reconstruct_intended_edit_allele`
- `reconstruct_observed_edit_allele`
- `simulate_dual_cut_deletion_product`
- `simulate_hdr_knockin_product`
- `simulate_base_edit_product`
- `simulate_prime_edit_product`
- `calculate_edit_consequences`
- `check_recut_risk`
- `normalize_knockin_target`
- `summarize_crispr_target_evidence`

### Alignment and comparative sequence analysis

- `align_nucleotide_sequences`
- `align_protein_sequences`
- `score_alignment_conservation`
- `identify_conserved_sequence_blocks`
- `map_alignment_to_source_coordinates`
- `compare_paralog_ohnolog_conservation`
- `compare_ortholog_conservation`

### Molecular source, library and construct reasoning

- `compile_cloning_requirements`
- `evaluate_species_requirements`
- `resolve_library_components`
- `search_modules`
- `available_plasmids`
- `raw_sequence`
- `characterize_sequence`
- `propose_construct`
- `validate_construct`
- `suggest_restriction_enzymes`
- `design_cloning_primers`
- `analyze_gene_structure`
- `plan_sequence_source`
- `plan_ivt_mrna_template`
- `export_sequence`
- `build_method_profile`

### PCR, qPCR, screening and Sanger

- `design_general_pcr_primers`
- `check_primer_specificity`
- `simulate_virtual_pcr_product`
- `enumerate_virtual_pcr_products`
- `design_insert_amplification_pcr`
- `design_vector_linearization_pcr`
- `design_inverse_pcr`
- `design_overlap_extension_pcr`
- `design_mutagenesis_pcr`
- `design_colony_pcr`
- `design_insert_presence_pcr`
- `design_insert_orientation_pcr`
- `design_empty_vector_discrimination_pcr`
- `design_plasmid_junction_pcr`
- `design_knockin_5prime_junction_pcr`
- `design_knockin_3prime_junction_pcr`
- `design_deletion_junction_pcr`
- `design_wildtype_vs_edited_size_pcr`
- `design_indel_genotyping_pcr`
- `design_allele_specific_pcr`
- `design_crispr_offtarget_validation_amplicons`
- `design_rt_qpcr_assay`
- `design_genomic_qpcr_assay`
- `design_transcript_specific_qpcr_assay`
- `design_splice_junction_qpcr_assay`
- `design_copy_number_qpcr_assay`
- `evaluate_qpcr_offtarget_amplicons`
- `select_or_design_sanger_sequencing_primer`
- `plan_sanger_primer_walking`
- `design_seamless_replacement_primers`
- `check_primers`
- `plan_pcr_batch`

### Assembly, sequence modification and final validation

- `virtual_restriction_assembly`
- `virtual_seamless_insertion`
- `virtual_sequence_replacement`
- `plan_golden_gate_assembly`
- `virtual_golden_gate_assembly`
- `plan_gateway_assembly`
- `virtual_gateway_assembly`
- `build_single_construct_assembly_graph`
- `plan_selected_method_hierarchy`
- `virtual_n_fragment_seamless_assembly`
- `plan_hierarchical_moclo`
- `virtual_hierarchical_moclo`
- `plan_multisite_gateway`
- `virtual_multisite_gateway`
- `plan_user_assembly`
- `virtual_user_assembly`
- `plan_yeast_assembly`
- `virtual_yeast_assembly`
- `generate_single_construct_build_workflow`
- `detect_construct_defects` — internal/composed in the current autonomous model surface
- `apply_sequence_repairs`
- `optimize_coding_sequence`
- `validate_final_construct_sequence`
- `validate_construct_identity`
- `build_assembly_report`
- `generate_cloning_protocol`
- `build_order_package`

## 2. Core molecular engines

The last full implementation audit grouped the shared deterministic implementation into **29 core molecular engine families** rather than counting every wrapper as a separate algorithm. Newer optional backends are listed separately below rather than being folded into this historical audit count.

1. Gene/transcript/CDS/reference resolution.
2. Library/inventory component resolution.
3. General sequence characterization, feature and restriction-site mapping.
4. pLannotate-backed de-novo/provisional plasmid annotation.
5. MAFFT/MUSCLE nucleotide/protein MSA plus conservation/source-coordinate mapping.
6. SpCas9 PAM/protospacer enumeration and deterministic guide geometry.
7. CRISPRscan on-target activity scoring.
8. Bowtie genome-wide CRISPR specificity/off-target search.
9. CHOPCHOP guide cross-check integration.
10. Conservation-aware intended multi-locus guide mapping/classification.
11. Exact genomic edit reconstruction plus CDS/protein consequence calculation.
12. Base-edit design/window/bystander-evidence handling.
13. PrimeDesign prime-edit/pegRNA support.
14. Knock-in donor/junction and complete-allele verification.
15. Shared guide/PAM recut and blocking-mutation analysis.
16. Primer3 primer design plus thermodynamics.
17. BLAST paired-primer/amplicon specificity.
18. Exact virtual-PCR product/enumeration including 5-prime tails.
19. Conventional restriction digest/end/ligation exact simulation.
20. Golden Gate/MoClo exact Type IIS simulation and uniqueness validation, including DnaCauldron paths.
21. Golden Gate empirical ligation-fidelity evidence.
22. Golden Gate overhang/breakpoint optimization above the exact simulator.
23. Exact seamless overlap assembly for Gibson/HiFi/In-Fusion-style workflows.
24. Gateway BP/LR plus MultiSite recombination.
25. USER assembly.
26. Yeast homologous-recombination assembly.
27. DNA Chisel sequence/codon/motif optimization and protected-range repair.
28. Exact construct defect/final-sequence/feature/translation validation.
29. Construct identity/read-alignment/quality/variant/junction verification.

## 3. Cloning methods researched

The cloning reasoning corpus contains a structured research dossier for each of these **36 method families**:

1. Annealed-Oligo Insertion
2. BASIC Assembly
3. BioBrick / 3A Assembly
4. Blunt-End Ligation Cloning
5. Bxb1 Serine-Integrase Cloning / Cassette Exchange
6. Circular Polymerase Extension Cloning (CPEC)
7. Cre–loxP Recombinase-Mediated Cloning — Univector / Creator
8. CRISPR-Assisted DNA Capture / CATCH
9. De Novo Synthetic Construction
10. Enzyme-Free Cloning (EFC) / Staggered-Overhang PCR Cloning
11. FastCloning
12. FEN1 / Flap-Endonuclease-Mediated Assembly (SureVector-style)
13. Gateway Recombinational Cloning
14. Gibson Assembly
15. Golden Gate Assembly / Type IIS Cloning
16. In-Fusion Cloning
17. Direct In-Vivo *E. coli* Assembly — IVA / AQUA / iVEC
18. Ligase Cycling Reaction (LCR)
19. MASTER Ligation
20. MetClo — Methylase-Assisted Hierarchical Type IIS Assembly
21. Nimble Cloning
22. Overlap-Extension PCR / SOE-PCR
23. Pairwise Selection Assembly (PSA)
24. PIPE Cloning
25. Polymerase Cycling Assembly (PCA) / Assembly PCR
26. Recombineering (λ Red / RecET)
27. Restriction–Ligation Cloning
28. RF Cloning / Megaprimer Cloning
29. Site-Directed Mutagenesis
30. SLIC / LIC
31. SLiCE (Seamless Ligation Cloning Extract)
32. Conventional TA Cloning
33. TEDA / T5 Exonuclease-Dependent Assembly
34. TOPO Cloning / TA-TOPO / Blunt-TOPO / Directional TOPO
35. USER Cloning / USER Fusion
36. Yeast Homologous Recombination / TAR Cloning

Several related methods share the same underlying molecular operations, so the research-method count should not be interpreted as a count of separate software engines.

## 4. Scientific software and runtime integrations

### Frozen audited core — 20 active integrations

1. pandas
2. Biopython
3. SnapGene Reader
4. Primer3 / `primer3-py`
5. pydna
6. DNA Chisel
7. DnaCauldron
8. LangGraph
9. MAFFT
10. MUSCLE
11. Bowtie
12. BLAST+
13. R runtime
14. crisprVerse-family R integration
15. crisprDesign-family R functionality
16. crisprScore-family scoring functionality
17. CRISPRscan
18. CHOPCHOP integration
19. PrimeDesign
20. pLannotate

### Additional integrated / optional scientific backends added to the evolving system

- **seqfold** — permissive DNA/RNA MFE fallback.
- **ViennaRNA** — isolated optional sidecar for RNA MFE, ensemble accessibility and cofold calculations.
- **OSTIR** — isolated optional bacterial translation-initiation/RBS backend.
- **mappy / minimap2** — long-read/full-plasmid construct mapping and coverage evidence.
- **pyspoa** — partial-order consensus for compatible noisy long reads before remapping to the expected construct.
- **pySBOL3 / SBOL-utilities** — sequence/feature interchange and coordinate-preserving SBOL handling.

### Installed/catalogued but not claimed as active scientific backends

- OpenCloning-LinkML — construction-lineage interchange support.
- OpenCloning — isolated sidecar/catalogued; no active LabOS scientific adapter in the reviewed state.
- DNAWeaver — registry placeholder.
- DNA Features Viewer — registry placeholder.

This status separation is intentional: installation or registry presence is not presented as scientific implementation.

## 5. External APIs, reference services and biological data

### External/reference service paths

- **Ensembl REST** — active gene, transcript, CDS/cDNA and genomic-region reference resolution.
- **NCBI E-utilities** — active explicit accession/version retrieval; PubMed/NCBI evidence paths are also used for literature/reference grounding.
- **ZFIN client/reference paths** — organism/gene cross-reference evidence when configured.
- **UniProt client/reference paths** — protein/gene cross-reference evidence when configured; unsupported external validation is surfaced rather than silently fabricated.
- **Addgene-linked records** — exact records already stored in LabOS can be resolved; the system does not guess or scrape an absent authoritative plasmid sequence.

CRISPRscan and CHOPCHOP are treated as local scientific engine/integration paths rather than pretending that an unsupported public REST API exists.

### Local/versioned data resources

Representative resources include:

- laboratory PostgreSQL plasmid, sequence, feature, primer, construct and inventory records;
- Ensembl/reference transcript and annotation data;
- imported GTF/GFF3 annotation packages;
- GRCz11/danRer11 and other validated reference/index assets;
- local Bowtie/BLAST/genome indexes;
- codon-usage tables;
- versioned cloning-method profiles and rules;
- species/workflow profiles and validation rules;
- empirical Golden Gate ligation datasets with pinned provenance;
- curated evidence and reference mappings.

These resources include external databases, local genome/reference files, indexes and curated laboratory/reference data. Because they do not live in one machine-authoritative manifest, this page no longer presents a single approximate package count as if it were a precise current metric.

## 6. Species and workflow-context coverage

The current registry contains **16 reviewed species/workflow profiles across 12 organism/context categories**. The 16 is a profile count, not a species count: several organisms have more than one workflow profile. The 12 routing categories comprise **9 named species** plus broader mammalian-cell, plant and insect-cell contexts.

- *Danio rerio* — Tol2 transgenesis and IVT mRNA profiles, with endogenous-editing context handled by the molecular workflow.
- *Nothobranchius furzeri* — Tol2 transgenesis and endogenous knock-in profiles.
- *Oryzias latipes* — Tol2 transgenesis.
- *Mus musculus* — pronuclear/random transgenesis and targeted conditional-allele profiles.
- *Xenopus laevis* — transgenesis context.
- *Xenopus tropicalis* — transgenesis context.
- *Drosophila melanogaster* — phiC31 transgenesis.
- *Caenorhabditis elegans* — MosSCI/single-copy insertion.
- *Saccharomyces cerevisiae* — expression/vector context.
- mammalian-cell expression — transient-transfection and stable-integration profiles.
- plant — Agrobacterium/T-DNA context.
- insect-cell — baculovirus expression context.

Species routing is evidence-aware; a method being chemically possible does not imply that regulatory architecture or genomic coordinates are transferable across organisms.

## 7. AI, provider and evaluation architecture

- **Persistent scientific AI:** one LangGraph molecular specialist retains access to the task objective, decisions and deterministic evidence while domain skills are dynamically composed.
- **Current live provider route:** Hermes provider path → OpenAI Codex provider → `gpt-5.6-terra` for current validation runs.
- **Typed scientific boundary:** AI selects/reasons/replans; deterministic tools perform exact sequence, chemistry, primer, assembly and validation operations.
- **Context/token optimization:** evidence residency, archival, exact temporary-product tracking, failed-product invalidation and validation-loop control reduce unnecessary repeated context.
- **Measured example:** one long molecular task decreased from **1,046,320 total tokens / 13 model calls** to **459,246 tokens / 10 model calls**, a **~56% reduction**.

### Separate private research AI

The 36-method cloning corpus was created with a **separate private research AI system that is not included in this public repository or the active LabOS code repository**. It was used to conduct and structure method-by-method evidence mining and to generate one structured Markdown research dossier per method from papers, manufacturer/authoritative documentation, protocols, software/design resources, repositories and troubleshooting searches.

Across the corpus, individual dossiers reviewed **22–33 sources** before additional troubleshooting/saturation searches. The complete private dossier set contains approximately **354,426 words** of synthesized technical analysis.

### Separate Custom-GPT teacher / curriculum/evaluation service

A different private service supports controlled AI evaluation and future improvement. Its architecture separates the Custom-GPT teacher surface, training PostgreSQL, main runtime, protected validator PostgreSQL and human review. Held-out validation/test material cannot be promoted into positive training examples, and failed decisions are excluded from positive targets.

## 8. Research-to-engineering pipeline

The research pipeline was intentionally depth-first:

**36 cloning methods researched → ≥987 method-linked source records reviewed → ~354,426 words of synthesis → 860 practical implementation findings → 77 reusable engineering capabilities**

The **860 findings were consolidated into 77 reusable engineering capabilities** because many cloning methods rely on the same underlying molecular operations. Method-specific chemistry and evidence remain in their profiles, while genuinely shared operations are implemented once as reusable deterministic primitives.

## Interpretation

The system is therefore not a single prompt wrapped around a cloning calculator. It combines:

- a persistent scientific reasoning runtime;
- a large typed molecular action surface;
- shared deterministic biological engines;
- established third-party scientific software;
- external and local biological data resources;
- a deep method-specific research corpus;
- exact sequence/provenance validation;
- controlled evaluation/training-data infrastructure; and
- runtime/context optimization for long molecular workflows.

[← Back to main README](README.md)