import json
import pytest
from src.validate import validate_csv


def test_validate_csv_passes_with_valid_data(tmp_path):
    csv_file = tmp_path / "valid.csv"
    schema_file = tmp_path / "schema.json"

    csv_file.write_text("url,label\nhttp://example.com,0\nhttp://google.com,1\n")
    schema_file.write_text(json.dumps({"required": ["url", "label"]}))

    validate_csv(csv_file, schema_file)


def test_validate_csv_fails_when_column_missing(tmp_path):
    csv_file = tmp_path / "missing_label.csv"
    schema_file = tmp_path / "schema.json"

    csv_file.write_text("url\nhttp://example.com\n")
    schema_file.write_text(json.dumps({"required": ["url", "label"]}))

    with pytest.raises(ValueError, match="Missing required columns"):
        validate_csv(csv_file, schema_file)


def test_validate_csv_fails_when_label_invalid(tmp_path):
    csv_file = tmp_path / "bad_label.csv"
    schema_file = tmp_path / "schema.json"

    csv_file.write_text("url,label\nhttp://example.com,2\n")
    schema_file.write_text(json.dumps({"required": ["url", "label"]}))

    with pytest.raises(ValueError, match="Label column contains invalid values"):
        validate_csv(csv_file, schema_file)