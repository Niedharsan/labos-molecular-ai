# LabOS Architecture

LabOS uses one persistent scientific AI and loads the domain skills needed for the current molecular task.

```mermaid
flowchart TB
    USER[Researcher] --> UI[Web workspace]
    UI --> API[FastAPI]
    API --> AI[Persistent scientific AI]

    AI --> CONTEXT[Objective + biological context]
    CONTEXT --> SKILLS[Dynamic skill selection]
    SKILLS --> LOOP[Scientific decision loop]

    LOOP --> CLONE[Cloning tools]
    LOOP --> CRISPR[CRISPR tools]
    LOOP --> PCR[PCR / Primer tools]
    LOOP --> QC[Sequence / QC tools]

    CLONE --> CHECK[Deterministic validation]
    CRISPR --> CHECK
    PCR --> CHECK
    QC --> CHECK

    CHECK --> DB[(PostgreSQL)]
    CHECK --> LOOP
    CHECK --> UI

    TRAIN[Separate evaluation / training system] -.-> AI
```

## Core design rule

**AI interprets and chooses; deterministic scientific tools calculate and verify.**

The molecular runtime was consolidated from earlier multi-agent experiments into one persistent AI so that context is retained across the complete task while domain abilities can be loaded dynamically.
