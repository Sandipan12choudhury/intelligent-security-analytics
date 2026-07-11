## Repository State & Development Rules

The project repository has already been initialized and is actively being developed.

Before suggesting any implementation, assume the following repository structure already exists and should be reused rather than redesigned.

### Current Repository

```
Intelligent Security Analytics/
│
├── backend/              # Reserved for FastAPI backend (currently mostly empty)
├── dataset/              # Stores all generated datasets (.xlsx)
├── docs/                 # Project documentation
├── frontend/             # Reserved for React frontend
├── ml/                   # Contains all Python builder scripts and future ML code
├── reports/              # Generated reports
├── venv/                 # Python virtual environment (ignore)
│
├── requirements.txt
└── Project documentation (.md files)
```

---

## Current Folder Responsibilities

### dataset/

This is the permanent storage location for every generated dataset.

Current datasets include:

- observation_library.xlsx
- master_observation_dataset.xlsx
- domain_master.xlsx
- application_master_info.xlsx

Every future knowledge library should also be created here.

Examples:

- control_library.xlsx
- recommendation_library.xlsx
- risk_library.xlsx
- evidence_library.xlsx
- compliance_library.xlsx
- threat_library.xlsx

No Python code belongs here.

---

### ml/

This is currently the active development folder.

It already contains all builder scripts used to generate the Observation Repository.

Each builder script owns one enterprise security domain.

Examples include:

- build_asset_management_library.py
- build_firewall_security_library.py
- build_logging_monitoring_library.py
- build_network_segmentation_library.py
- etc.

Whenever we create a new knowledge library, the corresponding builder script should also be created inside `ml/`.

For example:

```
ml/
    build_control_library.py
    build_recommendation_library.py
    build_risk_library.py
```

This folder is also where future Feature Engineering and ML scripts will live.

---

### backend/

Currently reserved.

When backend development begins, APIs, services, schemas and database logic will be added here.

Do not place dataset builders here.

---

### frontend/

Currently reserved.

React components and pages will be created here later.

Do not place backend or ML code here.

---

### reports/

Contains generated reports only.

No source code or datasets belong here.

---

## Repository Development Rules

Before suggesting a new file, first determine whether an existing folder already owns that responsibility.

Follow these rules:

- New dataset → `dataset/`
- Dataset builder → `ml/`
- Backend API → `backend/`
- Frontend component → `frontend/`
- Report → `reports/`
- Documentation → `docs/`

Do not create unnecessary folders.

Do not duplicate datasets.

Do not move existing files unless explicitly instructed.

Whenever recommending a new file, always mention its exact repository path.

Example:

```
Create:

ml/build_control_library.py

This script will generate:

dataset/control_library.xlsx
```

rather than simply saying "create a Python file."

Always assume the existing repository architecture should be preserved and extended rather than redesigned.