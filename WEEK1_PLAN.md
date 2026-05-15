Day 0
Dataset chosen: PhiUSIIL Phishing URL Dataset (UCI)
Source: https://archive.ics.uci.edu/dataset/967/phiusiil+phishing+url+dataset
Why chosen: large, labeled, current phishing dataset with no missing values; good for schema validation and split testing.
Label mapping: 1 = legitimate, 0 = phishing
Planned use: ingest raw CSV, validate schema, create deterministic train/val/test splits.


# Week 1 Plan — MLSecOps Data Pipeline

## Week 1 objective
Build a reproducible security-data pipeline that ingests a public phishing URL dataset, validates schema and label integrity, and creates deterministic train/validation/test splits.

## Dataset decision
- **Chosen dataset:** PhiUSIIL Phishing URL Dataset
- **Source:** https://archive.ics.uci.edu/dataset/967/phiusiil+phishing+url+dataset
- **Why chosen:** large, labeled, academically credible, suitable for schema validation and split testing

## Label mapping
- `1 = legitimate`
- `0 = phishing`

## Expected dataset fields
At minimum:
- `url`
- `label`

If additional columns exist in the dataset, document them after inspection and include them in `schema.json` only if they are required for the pipeline.

## Success metrics
By the end of Week 1:
- Raw dataset is ingested into `data/raw/`
- Schema validation passes on clean data
- Invalid rows or bad labels fail validation cleanly
- Train/validation/test split is deterministic
- At least 5 tests pass
- README and dataset card are complete

## Scope for this week
### In scope
- Repository setup
- Dataset ingestion
- Schema validation
- Train/validation/test splitting
- Unit tests
- Documentation

### Out of scope
- Model training
- MLflow
- model registry
- deployment
- observability
- LLM security

## Planned files
- `src/ingest.py`
- `src/validate.py`
- `src/split.py`
- `tests/test_validation.py`
- `schema.json`
- `artifacts/dataset_card.md`

## Notes
- Keep the pipeline simple and reproducible.
- Prefer clear errors over silent failures.
- Commit frequently and keep changes small.
