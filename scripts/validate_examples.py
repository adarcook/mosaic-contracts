#!/usr/bin/env python3
"""Validate repository examples against their canonical JSON Schemas."""

from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker, RefResolver

ROOT = Path(__file__).resolve().parents[1]

CASES = [
    (
        ROOT / "schemas/nutrition/meal-record.v1.schema.json",
        ROOT / "examples/nutrition/meal-record.v1.json",
    ),
    (
        ROOT / "schemas/sync/sync-batch.v1.schema.json",
        ROOT / "examples/sync/meal-recorded-batch.v1.json",
    ),
]


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def main() -> None:
    failed = False

    for schema_path, example_path in CASES:
        schema = load_json(schema_path)
        example = load_json(example_path)
        resolver = RefResolver(base_uri=schema_path.as_uri(), referrer=schema)
        validator = Draft202012Validator(
            schema,
            resolver=resolver,
            format_checker=FormatChecker(),
        )
        errors = sorted(validator.iter_errors(example), key=lambda error: list(error.path))

        if errors:
            failed = True
            print(f"FAIL {example_path.relative_to(ROOT)}")
            for error in errors:
                location = ".".join(str(part) for part in error.path) or "<root>"
                print(f"  {location}: {error.message}")
        else:
            print(f"PASS {example_path.relative_to(ROOT)}")

    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
