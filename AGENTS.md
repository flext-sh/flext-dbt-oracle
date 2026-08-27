# AGENTS.md — flext-dbt-oracle

> **Parent workspace law** lives in [`../AGENTS.md`](../AGENTS.md) — read it first.
> Universal engineering core: `~/.agents/UNIVERSAL_CORE.md`. Composition: global skills + parent/root `AGENTS.md` + this scope delta. Do not re-embed universal law.
>
> **Standalone / independent mode:** when `../AGENTS.md` does not resolve, pin the parent raw `AGENTS.md` URL to the same branch/release as this package (never `main`).

<!-- AIHUB-AGENTS-SCOPE-LOCAL-BEGIN -->
**Package:** `flext_dbt_oracle` · deps: `flext-core`, `flext-db-oracle`, `flext-meltano`

## Overview

dbt models for Oracle Database. Thin driver over `flext-meltano` dbt runner (ADR-006).

## Structure

```text
src/flext_dbt_oracle/
├── base.py           # FlextDbtOracleServiceBase (.connection_profile) — NO api.py facet
├── models.py         # DbtOracle.DbtConnectionProfile, OracleConnectionConfig
├── adapters.py connections.py   # thin/re-export stubs (no operational symbols)
├── constants.py typings.py protocols.py utilities.py   # AUTO-GENERATED facets
└── _config.py _settings.py
```

## Code Map

| Symbol | Kind | Location | Role |
|--------|------|----------|------|
| `FlextDbtOracleServiceBase` | class | `base.py` | service base; `connection_profile` entry |
| `DbtConnectionProfile` | model | `models.py` | typed `m.DbtOracle.*` profile |
| `OracleConnectionConfig` | model | `models.py` | connection config |

## Conventions (specific to this package)

- No `api.py` facet — the entry is `FlextDbtOracleServiceBase`. Connection profile is a typed `m.DbtOracle.*` model.
- DB access via `flext-db-oracle` (`settings.DbOracle.*`).
- Config/settings canonical pattern: ADR-012.
- Codemod governance (ast-grep + make mod): ADR-014.

## Anti-Patterns / Gotchas

- `adapters.py` / `connections.py` are thin/re-export stubs with no operational symbols — don't assume behavior lives there.

## Commands

```bash
make check PROJECT=flext-dbt-oracle
make test  PROJECT=flext-dbt-oracle       # tests/unit
```
<!-- AIHUB-AGENTS-SCOPE-LOCAL-END -->
