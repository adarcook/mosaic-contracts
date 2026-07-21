# Mosaic Contracts

Versioned, implementation-neutral contracts shared across Mosaic components.

## Purpose

This repository is the source of truth for data exchanged between:

- Mosaic Fit on Android
- Mosaic Server on the VPS
- Mosaic Core on the home computer
- Future Mosaic domain applications

## Rules

- Contracts must be versioned.
- Breaking changes require a new major contract version.
- JSON Schema is the canonical wire-format definition.
- Generated Kotlin and Python models may be added later, but generated files are not the source of truth.
- Contracts describe data, not business logic or infrastructure.

## Initial domains

- Meal analysis
- Nutrition logs
- Body measurements
- Workouts and swimming sessions
- Synchronization envelopes

## Layout

```text
schemas/
├── nutrition/
├── fitness/
└── sync/
```

## Status

Foundation stage. The first schema defines a model-generated meal analysis that still requires user confirmation.
