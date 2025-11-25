# FLEXT-DBT-Oracle Project Guidelines

**Reference**: See [../CLAUDE.md](../CLAUDE.md) for FLEXT ecosystem standards and general rules.

---

## Project Overview

**FLEXT-DBT-Oracle** is the dbt client integration library for Oracle Database within the FLEXT ecosystem (NOT a custom dbt adapter, but high-level orchestration via flext-db-oracle + flext-meltano).

**Version**: 2.1.0  
**Status**: Production-ready  
**Python**: 3.13+

**CRITICAL INTEGRATION DEPENDENCIES**:
- **flext-meltano**: MANDATORY for ALL DBT operations (ZERO TOLERANCE for direct dbt imports)
- **flext-db-oracle**: MANDATORY for ALL Oracle operations (ZERO TOLERANCE for direct SQLAlchemy/oracledb imports)
- **flext-core**: Foundation patterns (FlextResult, FlextService, FlextContainer)
- **flext-cli**: MANDATORY for ALL CLI operations (ZERO TOLERANCE for direct click/rich imports)

---

## Essential Commands

```bash
# Setup and validation
make setup                    # Complete development environment setup
make validate                 # Complete validation (lint + type + security + test)
make check                    # Quick check (lint + type)

# Quality gates
make lint                     # Ruff linting
make type-check               # Pyrefly type checking
make security                 # Bandit security scan
make test                     # Run tests
```

---

## Key Patterns

### DBT Orchestration

```python
from flext_core import FlextResult
from flext_dbt_oracle import FlextDbtOracle

dbt = FlextDbtOracle()

# Run DBT models
result = dbt.run_models(models=["model1", "model2"])
if result.is_success:
    output = result.unwrap()
```

---

## Critical Development Rules

### ZERO TOLERANCE Policies

**ABSOLUTELY FORBIDDEN**:
- ❌ Direct dbt imports (use flext-meltano)
- ❌ Direct SQLAlchemy/oracledb imports (use flext-db-oracle)
- ❌ Direct click/rich imports (use flext-cli)
- ❌ Exception-based error handling (use FlextResult)
- ❌ Type ignores or `Any` types

**MANDATORY**:
- ✅ Use `FlextResult[T]` for all operations
- ✅ Use flext-meltano for DBT operations
- ✅ Use flext-db-oracle for Oracle operations
- ✅ Use flext-cli for CLI operations
- ✅ Complete type annotations
- ✅ Zero Ruff violations

---

**Additional Resources**: [../CLAUDE.md](../CLAUDE.md) (workspace), [README.md](README.md) (overview)
