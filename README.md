# Mosaic Contracts

Versioned, implementation-neutral contracts shared across Mosaic components.

## Purpose

This repository is the source of truth for data exchanged between:

- Mosaic Fit and Inventory modules on Android
- Mosaic Server on the VPS
- Mosaic Core on the home computer
- Future Mosaic domain applications

## Rules

- Contracts must be versioned.
- Breaking changes require a new major contract version.
- JSON Schema is the canonical wire-format definition.
- Generated Kotlin and Python models may be added later, but generated files are not the source of truth.
- Contracts describe exchanged data, not domain business logic or infrastructure.
- Domain records and model-generated analyses are separate contracts.

## Initial domains

- Meal analysis
- Confirmed nutrition records
- Inventory consumption requests
- Body measurements
- Workouts and swimming sessions
- Synchronization envelopes

## Layout

```text
schemas/
├── common/                 # reusable value objects
├── nutrition/              # meal analysis and confirmed meal records
├── inventory/              # inventory-facing requests and events
├── fitness/
└── sync/                   # event envelopes and idempotent batches

examples/
├── nutrition/
└── sync/

scripts/
└── validate_examples.py
```

## Phase 1 contracts

- `meal-analysis.v1.schema.json` describes an unconfirmed model-generated estimate.
- `meal-record.v1.schema.json` describes the user-owned operational meal record.
- `event-envelope.v1.schema.json` provides stable event identity, provenance and correlation.
- `sync-batch.v1.schema.json` groups retry-safe events for Android-to-Core synchronization.
- `consumption-request.v1.schema.json` allows confirmed meal components to propose Inventory deductions without granting the nutrition domain ownership of stock levels.

Inventory links remain optional. Meals from restaurants, incomplete Inventory data and unresolved raw-to-cooked conversions must not block meal capture.

## Validation

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_examples.py
```

The validator checks repository examples against their canonical schemas, including JSON Schema formats and relative references.

## Compatibility

Within contract major version 1:

- new optional fields may be added;
- existing required fields and enum values must not be removed or reinterpreted;
- consumers must ignore unknown event types only when their integration policy explicitly permits it;
- destructive or stock-changing behavior must require domain validation and, during Phase 1, explicit user confirmation.

## Status

Phase 1 foundation. The repository now defines both model-generated meal analysis and confirmed meal/synchronization contracts suitable for Android, Server and Core implementations.
