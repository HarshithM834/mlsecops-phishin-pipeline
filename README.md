# MLSecOps Phishing Pipeline

This repository is a Week 1 project in a 16-week MLSecOps / AI Security roadmap.

## Goal
Build a reproducible pipeline that ingests a public phishing URL dataset, validates its schema, and creates deterministic train/validation/test splits.

## Dataset
- **Dataset:** PhiUSIIL Phishing URL Dataset
- **Source:** UCI Machine Learning Repository
- **Label mapping:** `1 = legitimate`, `0 = phishing`

## Week 1 deliverables
- Repo scaffolded
- Dataset selected and documented
- Schema defined
- Ingestion script built
- Validation script built
- Train/validation/test split script built
- Tests added
- Dataset card written

## Project structure
- `src/` — ingestion, validation, split logic
- `tests/` — unit tests
- `data/raw/` — raw dataset files
- `data/processed/` — cleaned and split data
- `artifacts/` — notes, dataset card, demo materials
- `schema.json` — expected dataset schema
- `WEEK1_PLAN.md` — roadmap for the current week

## Why this project matters
This project is designed to build practical skills in:
- Python
- Git
- data validation
- reproducible ML pipelines
- MLOps / MLSecOps fundamentals
- security-minded data handling

## Current status
Day 0 - 5/15/2026 - Completed. Week 1 begins with scoping, dataset setup, and pipeline implementation.

Day 1 - 5/16/2026 - Completed validation and tested with pytest on whether validation works or not.
