# PROJECT_REPOSITORY_STRUCTURE.md

# Intelligent Security Analytics & Risk Prediction Platform

Repository Architecture Guide

Version 1.0

---

# PURPOSE

This document defines the architectural organization of the project repository.

It explains:

- purpose of every folder
- purpose of every major file
- ownership of generated artifacts
- repository growth strategy
- folder responsibilities
- future expansion rules

Future ChatGPT conversations should use this document whenever recommending new files or folders.

This repository should be treated as an enterprise software project rather than a collection of unrelated scripts.

---

# REPOSITORY PHILOSOPHY

The repository follows one simple principle.

Each folder owns one responsibility.

Folders should never mix unrelated artifacts.

Generated datasets should not be mixed with source code.

Documentation should not be mixed with implementation.

Machine Learning code should not be mixed with backend APIs.

Frontend code should not be mixed with analytics reports.

This separation is intentional.

---

# CURRENT REPOSITORY STRUCTURE

```

Intelligent Security Analytics/

│

├── backend/

├── dataset/

├── docs/

├── frontend/

├── ml/

├── reports/

├── venv/

│

├── ADR_Master.md

├── AI_PROJECT_MEMORY.md

├── PROJECT_CONTEXT_V1.md

├── PROJECT_CONTEXT_V2.md

├── PROJECT_CONTINUATION_CONTEXT.md

└── requirements.txt

```

---

# ROOT DIRECTORY

Purpose

The project root contains only project-level resources.

It should never contain implementation code except for global startup files.

Current files include:

ADR_Master.md

Architecture decision records.

Purpose

Documents permanent architectural decisions.

---

AI_PROJECT_MEMORY.md

Purpose

Preserves reasoning, development philosophy and project evolution.

---

PROJECT_CONTEXT_V1.md

Historical architecture documentation.

Reference only.

---

PROJECT_CONTEXT_V2.md

Current technical architecture specification.

Primary technical documentation.

---

PROJECT_CONTINUATION_CONTEXT.md

Primary continuation document for future ChatGPT conversations.

Represents current project save state.

---

requirements.txt

Python dependency specification.

---

Ownership

Manual.

Future additions to the project root should remain minimal.

---

# backend/

Current Status

Reserved.

Purpose

Backend implementation layer.

This folder will eventually contain the enterprise backend service.

Current Role

Placeholder.

Future Responsibilities

REST APIs

Business Logic

Knowledge Retrieval

Authentication

Authorization

Recommendation Engine APIs

Analytics APIs

Machine Learning APIs

Database Integration

Future Structure

backend/

    api/

    services/

    database/

    models/

    schemas/

    utils/

    config/

    main.py

Ownership

Source code only.

Never store datasets here.

Never store reports here.

Never store documentation here.

---

# frontend/

Current Status

Reserved.

Purpose

Enterprise Analytics Portal.

Current Role

Placeholder.

Future Responsibilities

Executive Dashboard

Assessment Explorer

Knowledge Explorer

Recommendation Center

Risk Dashboard

Compliance Dashboard

Application Explorer

Administration Portal

Future Structure

frontend/

    src/

        components/

        pages/

        layouts/

        services/

        hooks/

        assets/

Ownership

UI source code only.

Do not store backend code.

Do not store datasets.

---

# docs/

Current Status

Reserved.

Purpose

Permanent documentation.

Although documentation currently exists in the project root, the long-term architecture places all documentation inside this folder.

Future Contents

README.md

PROJECT_CONTEXT

PROJECT_CONTINUATION_CONTEXT

ADR_MASTER

AI_PROJECT_MEMORY

PROJECT_REPOSITORY_STRUCTURE

API_DOCUMENTATION

DEPLOYMENT_GUIDE

DEVELOPER_GUIDE

Ownership

Documentation only.

No executable code.

---

# PART 2

---

# dataset/

## Current Status

**Active**

---

## Purpose

The `dataset/` directory stores all **persistent structured datasets** generated and consumed by the platform.

This folder represents the project's **persistent knowledge layer**.

Unlike Python scripts, datasets stored here are intended to be reused by multiple project components, including:

* Backend APIs
* Machine Learning
* Knowledge Engineering
* Analytics
* Recommendation Engine
* Enterprise Portal

Datasets should remain independent from implementation logic.

---

## Current Files

### observation_library.xlsx

**Purpose**

Master Observation Repository.

This is the most important dataset currently present in the repository.

It contains the complete enterprise observation library generated during Observation Engineering.

Current Status

Completed.

Repository Statistics

* 1220 Enterprise Observations
* 5 Assessment Activities
* 40 Technical Domains

Ownership

Generated.

Should rarely require manual modification.

Acts as the primary knowledge source for future datasets.

---

### master_observation_dataset.xlsx

Purpose

Master normalized observation dataset.

This file provides consolidated observation information suitable for downstream processing.

Future Usage

Knowledge Engineering

Feature Engineering

Analytics

Machine Learning

---

### domain_master.xlsx

Purpose

Master catalog of assessment domains.

This dataset defines the official enterprise assessment domains supported by the platform.

Examples

ITGC

Database Review

DFRA

DFA / DFD

SNA

Future Rule

New domains should only be added when introducing entirely new assessment activities.

---

### application_master_info.xlsx

Purpose

Master application metadata.

This dataset will become increasingly important once Application Dataset Engineering begins.

Future contents may include:

Application Name

Department

Business Owner

Criticality

Technology Stack

Hosting Environment

Assessment Status

Risk Score

Compliance Score

Overall Health

Current Status

Foundation dataset.

Future development target.

---

# Dataset Ownership Rules

Every dataset inside this directory must satisfy the following rules.

✓ Persistent

✓ Structured

✓ Version Controlled

✓ Reusable

✓ Independent

Generated datasets belong here.

Temporary datasets do not.

Experimental datasets do not.

Intermediate processing outputs do not.

---

# Future Datasets

The following datasets have already been architecturally approved.

These datasets will eventually appear inside this folder.

## Knowledge Libraries

control_library.xlsx

recommendation_library.xlsx

risk_library.xlsx

evidence_library.xlsx

compliance_library.xlsx

threat_library.xlsx

asset_library.xlsx

security_domain_library.xlsx

---

## AI Datasets

feature_dataset.xlsx

training_dataset.xlsx

embedding_dataset.xlsx

semantic_similarity_dataset.xlsx

---

## Analytics Datasets

application_assessment_dataset.xlsx

dashboard_dataset.xlsx

risk_trend_dataset.xlsx

executive_summary_dataset.xlsx

---

# Dataset Lifecycle

Every persistent dataset should follow this lifecycle.

Builder Script

↓

Validation

↓

Dataset Generation

↓

Stored inside dataset/

↓

Consumed by Backend

↓

Consumed by ML

↓

Displayed in Frontend

↓

Referenced in Reports

This workflow should remain consistent across every future dataset.

---

# ml/

## Current Status

**Active**

---

## Purpose

The `ml/` directory contains all Python scripts responsible for generating datasets and performing AI/ML-related processing.

At the current project stage, this folder functions primarily as the **Knowledge Engineering workspace**.

Contrary to its name, it is **not yet focused on Machine Learning models**.

Instead, it contains the builder scripts responsible for constructing enterprise knowledge assets.

---

# Current Repository Contents

The folder currently contains approximately **46 Python scripts**.

These scripts follow a standardized naming convention.

Example

build_asset_management_library.py

build_backup_restoration_library.py

build_database_audit_library.py

build_database_configuration_library.py

build_database_encryption_library.py

build_dfd_documentation_library.py

build_dfra_log_retention_library.py

build_firewall_security_library.py

build_logging_monitoring_library.py

build_network_segmentation_library.py

build_patch_management_library.py

build_secure_configuration_library.py

build_sna_architecture_library.py

build_vendor_management_library.py

...

Along with common utility files such as:

observation_template.py

setup_project_data.py

archive_create_observation.py

---

# Builder Script Philosophy

Every builder script owns exactly one enterprise security domain.

Examples

Asset Management Builder

↓

Generates

↓

Asset Management Observations

Database Encryption Builder

↓

Generates

↓

Database Encryption Observations

Firewall Security Builder

↓

Generates

↓

Firewall Security Observations

This modular approach improves maintainability and simplifies repository growth.

---

# Builder Naming Convention

Every builder script should follow the format:

```text
build_<domain_name>_library.py
```

Examples

```text
build_control_library.py

build_recommendation_library.py

build_risk_library.py

build_evidence_library.py

build_threat_library.py
```

Future builder scripts should follow this standard.

---

# Builder Responsibilities

Each builder script should perform only one responsibility.

Load templates.

↓

Create records.

↓

Validate schema.

↓

Generate dataset.

↓

Store dataset.

↓

Display execution summary.

Builder scripts should never contain:

Backend API logic

Frontend logic

Dashboard code

Machine Learning training

Authentication

Database connections

Their only responsibility is dataset generation.

---

# Future ML Folder Evolution

Although currently focused on Knowledge Engineering, the `ml/` folder will gradually expand.

Planned future organization:

```text
ml/

    builders/

    feature_engineering/

    training/

    inference/

    embeddings/

    evaluation/

    utils/
```

This evolution should occur only when Machine Learning implementation begins.

Current builder scripts can later be migrated into the `builders/` subdirectory without changing their functionality.

---

# END OF PART 2

The repository now has a clearly defined separation between:

* Persistent Knowledge (`dataset/`)
* Knowledge Generation (`ml/`)

The next part documents the remaining infrastructure folders (`reports/`, `venv/`), repository governance rules, naming conventions, repository growth strategy, and exact instructions for future ChatGPT on where every new file, folder, API, dataset, model, report, and document should be created.



# PART 3

---

# reports/

## Current Status

Reserved

---

## Purpose

The `reports/` directory stores generated outputs intended for human consumption rather than system processing.

Unlike datasets, reports summarize information.

Reports should never become source datasets.

Instead, they represent presentation artifacts generated from datasets.

---

## Future Contents

Assessment Reports

Executive Summary Reports

Risk Summary Reports

Compliance Reports

Trend Analysis Reports

Machine Learning Evaluation Reports

Dashboard Export Reports

PDF Exports

CSV Exports

Presentation Figures

---

## Ownership

Generated.

Reports should never be edited manually.

If a report requires changes, regenerate it from the underlying datasets.

---

# venv/

## Current Status

Development Environment

---

## Purpose

Contains the local Python virtual environment.

This folder is **not part of the project architecture**.

It exists solely for dependency isolation.

---

## Rules

Never store project files here.

Never store datasets here.

Never store documentation here.

Never commit virtual environment contents to Git.

---

# requirements.txt

## Purpose

Defines the project's Python dependencies.

Acts as the reproducible environment specification.

Future libraries should always be added here after validation.

---

# FILE OWNERSHIP MODEL

Every artifact inside the repository belongs to one ownership category.

---

## Source Code

Examples

backend/

frontend/

ml/

Ownership

Developer maintained.

---

## Generated Datasets

Examples

dataset/

Ownership

Generated.

Should rarely be edited manually.

---

## Documentation

Examples

PROJECT_CONTEXT

ADR

PROJECT_REPOSITORY_STRUCTURE

Ownership

Manual.

Maintained continuously.

---

## Reports

Examples

reports/

Ownership

Generated.

Never considered source data.

---

## Configuration

Examples

requirements.txt

Future .env

Future config/

Ownership

Manual.

---

# REPOSITORY WORKFLOW

The repository follows a strict workflow.

Enterprise Knowledge

↓

Builder Script

↓

Dataset

↓

Backend API

↓

Machine Learning

↓

Recommendation Engine

↓

Frontend Portal

↓

Reports

Every future component should integrate into this workflow.

---

# REPOSITORY GROWTH STRATEGY

The repository has intentionally been designed for gradual expansion.

Current Stage

Knowledge Engineering

↓

Next

Backend APIs

↓

Portal

↓

Machine Learning

↓

Artificial Intelligence

↓

Enterprise Deployment

Future folders should only be introduced when required.

Avoid creating empty folders prematurely.

---

# WHERE FUTURE FILES SHOULD BE CREATED

This section should guide every future implementation.

---

## New Dataset

Location

dataset/

Examples

control_library.xlsx

recommendation_library.xlsx

risk_library.xlsx

---

## New Builder Script

Location

ml/

Examples

build_control_library.py

build_recommendation_library.py

---

## Machine Learning Training Script

Future Location

ml/training/

---

## Feature Engineering

Future Location

ml/feature_engineering/

---

## Embedding Generation

Future Location

ml/embeddings/

---

## Model Evaluation

Future Location

ml/evaluation/

---

## Trained Models

Future Folder

models/

Examples

risk_classifier.pkl

severity_model.pkl

embedding_model.bin

This folder should be created only when model training begins.

---

## Backend APIs

Future Location

backend/api/

Examples

recommendation_api.py

risk_api.py

knowledge_api.py

---

## Backend Business Logic

Future Location

backend/services/

---

## Database Layer

Future Location

backend/database/

---

## Pydantic Schemas

Future Location

backend/schemas/

---

## Utility Functions

Future Location

backend/utils/

---

## React Pages

Future Location

frontend/src/pages/

---

## React Components

Future Location

frontend/src/components/

---

## Shared Services

Future Location

frontend/src/services/

---

## Dashboard Assets

Future Location

frontend/src/assets/

---

## Documentation

Future Location

docs/

Every permanent documentation file belongs here.

---

## Generated Reports

Location

reports/

---

# FOLDER CREATION POLICY

A new folder should only be created if:

The responsibility cannot logically belong to an existing folder.

OR

The number of files inside an existing folder becomes sufficiently large to justify subdivision.

Do not create folders simply because they may be useful later.

Architecture should grow organically.

---

# NAMING CONVENTIONS

Python Scripts

snake_case.py

Builder Scripts

build_<library_name>.py

Datasets

snake_case.xlsx

Documentation

UPPER_CASE.md

Models

descriptive_name.pkl

API Files

feature_api.py

React Components

PascalCase.jsx

Environment Files

.env

Configuration

config.py

Consistency should always take precedence over personal preference.

---

# REPOSITORY GOVERNANCE RULES

The repository should satisfy the following principles.

One folder.

One responsibility.

Generated artifacts separated from source code.

Knowledge separated from implementation.

Documentation separated from execution.

Reusable components preferred over duplication.

Architecture should remain understandable without extensive explanation.

Future ChatGPT conversations should preserve these principles.

---

# END OF PART 3

At this point the repository architecture has been completely defined.

The final part will document:

• Repository evolution roadmap.

• Folder lifecycle.

• Development lifecycle.

• Repository decision matrix.

• Future ChatGPT operational instructions.

• Examples of where every future feature should be implemented.

• Repository constitution.

This final part effectively becomes the **operating manual** for the entire repository.

# PROJECT_REPOSITORY_STRUCTURE.md

# PART 4 (FINAL)

---

# REPOSITORY EVOLUTION ROADMAP

The repository has intentionally been designed to evolve gradually rather than being fully populated from the beginning.

Each major project phase introduces additional folders only when they become necessary.

This approach minimizes unnecessary complexity while preserving scalability.

---

## Phase 1

Project Initialization

Repository Structure

```
backend/

dataset/

docs/

frontend/

ml/

reports/
```

Status

Completed.

---

## Phase 2

Observation Engineering

Repository Growth

```
dataset/

Observation Repository

Application Master

Domain Master

Master Observation Dataset

ml/

Builder Scripts

Templates

Utilities
```

Status

Completed.

---

## Phase 3

Knowledge Engineering

Future Additions

```
dataset/

control_library.xlsx

recommendation_library.xlsx

risk_library.xlsx

evidence_library.xlsx

compliance_library.xlsx

threat_library.xlsx
```

```
ml/

build_control_library.py

build_recommendation_library.py

build_risk_library.py

build_evidence_library.py

build_compliance_library.py
```

Status

Next Phase.

---

## Phase 4

Backend Development

Future Repository

```
backend/

api/

services/

database/

schemas/

utils/

config/

main.py
```

Status

Future.

---

## Phase 5

Frontend Development

Future Repository

```
frontend/

src/

components/

pages/

layouts/

services/

hooks/

assets/

App.jsx
```

Status

Future.

---

## Phase 6

Machine Learning

Future Repository

```
ml/

feature_engineering/

training/

evaluation/

embeddings/

inference/

utils/
```

Future root folder

```
models/
```

Status

Future.

---

## Phase 7

Enterprise Platform

Additional folders may include:

```
tests/

deployment/

docker/

logs/

experiments/

monitoring/

```

Only create these when implementation requires them.

---

# FOLDER LIFECYCLE

Every new feature should follow the same lifecycle.

Business Requirement

↓

Architecture Discussion

↓

Builder Script (if required)

↓

Dataset Generation

↓

Backend Integration

↓

Machine Learning Integration

↓

Frontend Visualization

↓

Reporting

↓

Documentation

This lifecycle should remain consistent throughout the project.

---

# FILE PLACEMENT DECISION MATRIX

Whenever a new artifact is introduced, determine its location using the following rules.

---

## Question

"Is it a persistent dataset?"

Yes

↓

Place inside

```
dataset/
```

---

## Question

"Is it responsible for generating datasets?"

Yes

↓

Place inside

```
ml/
```

---

## Question

"Is it an API?"

Yes

↓

Place inside

```
backend/api/
```

---

## Question

"Is it business logic?"

Yes

↓

Place inside

```
backend/services/
```

---

## Question

"Is it a trained model?"

Yes

↓

Place inside

```
models/
```

(Create this folder only when model training begins.)

---

## Question

"Is it a React component?"

Yes

↓

Place inside

```
frontend/src/components/
```

---

## Question

"Is it documentation?"

Yes

↓

Place inside

```
docs/
```

---

## Question

"Is it a generated report?"

Yes

↓

Place inside

```
reports/
```

---

# REPOSITORY DECISION RULES

Before creating any new folder, answer the following questions.

Does an existing folder already own this responsibility?

If Yes

↓

Reuse the existing folder.

---

Will this folder contain multiple related files?

If No

↓

Do not create a new folder.

---

Does the new folder improve repository clarity?

If No

↓

Do not create it.

---

Will this folder remain useful throughout the project?

If No

↓

Avoid creating it.

---

Architecture should grow naturally.

Never create folders simply because they might be useful in the future.

---

# FUTURE CHATGPT INSTRUCTIONS

Whenever continuing this repository, assume:

The repository structure is already architecturally approved.

Every folder owns one responsibility.

Generated datasets belong only inside

```
dataset/
```

Builder scripts belong only inside

```
ml/
```

Backend implementation belongs only inside

```
backend/
```

Frontend implementation belongs only inside

```
frontend/
```

Permanent documentation belongs only inside

```
docs/
```

Generated reports belong only inside

```
reports/
```

If a future response recommends creating a file, it should also specify the exact repository location.

If a future response recommends creating a new folder, it should explain why an existing folder cannot be reused.

Repository consistency should always take precedence over convenience.

---

# REPOSITORY CONSTITUTION

The repository follows the following permanent principles.

One Folder

↓

One Responsibility

Knowledge

↓

Implementation

↓

Presentation

↓

Documentation

Generated Artifacts

↓

Persistent Storage

↓

Analytics

↓

Visualization

Architecture

↓

Implementation

↓

Documentation

These principles should never be violated without strong architectural justification.

---

# COMPLETE REPOSITORY VISION

The intended long-term repository will resemble the following.

```
Intelligent Security Analytics/

│

├── backend/

│      api/

│      services/

│      database/

│      schemas/

│      utils/

│      config/

│      main.py

│

├── frontend/

│      src/

│          pages/

│          components/

│          layouts/

│          hooks/

│          services/

│          assets/

│

├── dataset/

│      observation_library.xlsx

│      control_library.xlsx

│      recommendation_library.xlsx

│      risk_library.xlsx

│      evidence_library.xlsx

│      compliance_library.xlsx

│      threat_library.xlsx

│      application_dataset.xlsx

│

├── ml/

│      builders/

│      feature_engineering/

│      training/

│      inference/

│      evaluation/

│      embeddings/

│      utils/

│

├── models/

│

├── reports/

│

├── docs/

│      PROJECT_CONTEXT_V2.md

│      PROJECT_CONTINUATION_CONTEXT.md

│      AI_PROJECT_MEMORY.md

│      ADR_MASTER.md

│      PROJECT_REPOSITORY_STRUCTURE.md

│

├── tests/

├── scripts/

├── deployment/

├── requirements.txt

└── README.md
```

This represents the architectural target of the repository.

It should evolve naturally rather than being created all at once.

---

# FINAL NOTE FOR FUTURE CHATGPT

If you are reading this document at the beginning of a new conversation:

Assume the repository architecture has already been finalized.

Do not recommend arbitrary folder creation.

Always preserve repository consistency.

Always specify the exact location for every new file you recommend.

Always explain why a new folder is necessary before introducing it.

Treat the repository as an enterprise software project.

Your responsibility is to extend the repository while preserving its architectural integrity.

---

# END OF PROJECT_REPOSITORY_STRUCTURE.md

Document Status

Completed

Version

1.0

Purpose

Repository Architecture Guide

Relationship

This document complements:

* PROJECT_CONTINUATION_CONTEXT.md
* PROJECT_CONTEXT_V2.md

Together, these documents define:

* **What the project is**
* **What has been completed**
* **How the repository is organized**
* **Where future implementation should occur**
* **How the repository should evolve**
