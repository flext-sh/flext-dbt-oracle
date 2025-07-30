# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**flext-dbt-oracle** is a modern DBT adapter for Oracle Database within the FLEXT ecosystem. It provides enterprise-grade Oracle Database integration with DBT for data transformations and analytics workloads. Built with Python 3.13, it leverages FLEXT core infrastructure libraries and follows Clean Architecture principles with Domain-Driven Design patterns.

## Architecture

### Core Components

- **DBT Oracle Adapter**: Custom DBT adapter implementation using FLEXT Oracle services
- **Connection Management**: Enterprise connection pooling via `flext-db-oracle`
- **Configuration**: Comprehensive settings with validation and environment variable support
- **Type Safety**: Full MyPy strict typing with Pydantic models

### Dependencies

Key FLEXT ecosystem dependencies:

- `flext-core`: Foundation library with logging, constants, and DI patterns
- `flext-db-oracle`: Oracle Database connectivity and connection management
- `flext-meltano`: DBT/Singer/Meltano integration components
- `flext-observability`: Monitoring and metrics collection

### Directory Structure

```
src/flext_dbt_oracle/
├── adapters/oracle/           # DBT Oracle adapter implementation
│   ├── impl.py               # Main adapter class
│   ├── connections.py        # Connection manager
│   ├── config.py            # Configuration and settings
│   ├── constants.py         # Oracle adapter constants
│   ├── types.py             # Type definitions
│   └── typedefs.py          # Type aliases
├── exceptions.py            # Custom exceptions
└── infrastructure/          # DI container and infrastructure
    └── di_container.py      # Dependency injection setup
```

## Development Commands

### Essential Quality Gates

Run these commands before committing - all must pass:

```bash
make validate          # Complete validation (lint + type + security + test + dbt-test)
make check            # Essential checks (lint + type + test + dbt-compile)
```

### Core Development Workflow

```bash
# Setup and installation
make setup            # Complete development setup
make install          # Install dependencies with Poetry
make dev-install      # Development mode setup with pre-commit hooks

# Code quality (zero tolerance enforcement)
make lint             # Ruff linting (ALL rules enabled)
make type-check       # MyPy strict type checking
make security         # Security scans (bandit + pip-audit + secrets)
make format          # Format code with ruff
make fix             # Auto-fix all issues (format + lint)

# Testing (90% coverage minimum required)
make test            # Run tests with coverage (90% minimum)
make test-unit       # Unit tests only
make test-integration # Integration tests only
make coverage        # Generate detailed coverage report
```

### DBT Operations

```bash
# Core DBT workflow
make dbt-deps        # Install dbt dependencies
make dbt-debug       # Debug dbt configuration
make dbt-compile     # Compile dbt models
make dbt-run         # Run dbt models
make dbt-test        # Run dbt data tests
make dbt-docs        # Generate dbt documentation

# Oracle-specific operations
make oracle-profile-test     # Test Oracle connection profiles
make oracle-macros          # Test Oracle-specific macros
make oracle-performance     # Analyze Oracle performance
make oracle-staging-models  # Run staging models only
make oracle-marts-models    # Run marts models only
make oracle-full-refresh    # Full refresh of Oracle models
```

### Build and Maintenance

```bash
make build           # Build project with Poetry
make clean           # Remove all artifacts
make deps-update     # Update all dependencies
make deps-audit      # Security audit of dependencies
```

## Testing Strategy

### Test Organization

- **Unit Tests**: `tests/test_*.py` - Component-level testing
- **Integration Tests**: Test database connectivity and adapter integration
- **DBT Tests**: Data quality and model validation tests

### Test Categories

Use pytest markers for selective testing:

```bash
pytest -m unit              # Unit tests only
pytest -m integration       # Integration tests only
pytest -m slow             # Slow tests only
pytest -m "not slow"       # Exclude slow tests
```

### Coverage Requirements

- **Minimum**: 90% coverage required (enforced by `make test`)
- **Reports**: HTML coverage reports in `reports/coverage/`
- **Exclusions**: Test files and external libraries excluded

## Configuration

### Environment Variables

The adapter supports comprehensive environment variable configuration with `DBT_ORACLE_` prefix:

```bash
# Required Oracle connection settings
DBT_ORACLE_ORACLE_HOST=localhost
DBT_ORACLE_ORACLE_PORT=1521
DBT_ORACLE_ORACLE_SERVICE_NAME=ORCL
DBT_ORACLE_ORACLE_USERNAME=user
DBT_ORACLE_ORACLE_PASSWORD=password

# Optional performance settings
DBT_ORACLE_ORACLE_POOL_MIN_SIZE=1
DBT_ORACLE_ORACLE_POOL_MAX_SIZE=10
DBT_ORACLE_ORACLE_QUERY_TIMEOUT=30
```

### DBT Profiles

DBT profiles should be configured in `profiles/` directory:

```yaml
flext_dbt_oracle:
  target: dev
  outputs:
    dev:
      type: oracle
      host: "{{ env_var('DBT_ORACLE_HOST') }}"
      port: "{{ env_var('DBT_ORACLE_PORT') | int }}"
      service_name: "{{ env_var('DBT_ORACLE_SERVICE_NAME') }}"
      username: "{{ env_var('DBT_ORACLE_USERNAME') }}"
      password: "{{ env_var('DBT_ORACLE_PASSWORD') }}"
      schema: "{{ env_var('DBT_ORACLE_SCHEMA', 'ANALYTICS') }}"
```

## Code Patterns

### Configuration Classes

Use the established configuration pattern:

```python
from flext_dbt_oracle.adapters.oracle.config import DBTOracleConfig, DBTOracleSettings

# Environment-based settings
settings = DBTOracleSettings()
config = settings.to_dbt_config()

# Direct configuration
config = DBTOracleConfig(
    host="localhost",
    port=1521,
    service_name="ORCL",
    username="user",
    password="password"
)
```

### Connection Management

Leverage the FLEXT Oracle services:

```python
from flext_dbt_oracle.adapters.oracle.connections import OracleConnectionManager

# Connection manager handles pooling and lifecycle
connection_manager = OracleConnectionManager(profile)
```

### Error Handling

Use FLEXT core patterns for consistent error handling:

```python
from flext_core import get_logger
from flext_meltano import DbtDatabaseError, DbtRuntimeError

logger = get_logger(__name__)

try:
    # Oracle operations
    result = execute_query()
except Exception as e:
    logger.error("Query execution failed", exc_info=True)
    raise DbtDatabaseError(f"Oracle query failed: {e}") from e
```

## Quality Standards

### Code Quality (Zero Tolerance)

- **Linting**: Ruff with ALL rules enabled (17+ categories)
- **Type Checking**: MyPy strict mode - zero errors tolerated
- **Security**: Bandit security scanning + pip-audit
- **Formatting**: Ruff formatter with consistent style

### Performance Standards

- **Connection Pooling**: Configurable min/max pool sizes
- **Query Optimization**: Oracle-specific SQL generation
- **Timeouts**: Configurable connection and query timeouts
- **Resource Management**: Proper connection lifecycle management

### Documentation Requirements

- **Docstrings**: All public APIs must have comprehensive docstrings
- **Type Hints**: Full type annotations for all functions and methods
- **DBT Docs**: Models must include descriptions and column documentation

## Debugging and Troubleshooting

### Common Issues

**Connection Problems**:

```bash
make oracle-profile-test     # Test Oracle connectivity
make dbt-debug              # Debug DBT configuration
```

**Performance Issues**:

```bash
make oracle-performance     # Analyze query performance
make oracle-explain-plan    # Generate explain plans
```

**Configuration Validation**:

```bash
# Check environment variables
env | grep DBT_ORACLE_

# Validate configuration
python -c "from flext_dbt_oracle.adapters.oracle.config import DBTOracleSettings; print(DBTOracleSettings().to_dbt_config())"
```

### Logging

Enable detailed logging for debugging:

```bash
export DBT_ORACLE_LOG_LEVEL=DEBUG
export DBT_ORACLE_ENABLE_SQL_LOGGING=true
```

## TODO: GAPS DE ARQUITETURA IDENTIFICADOS - PRIORIDADE ALTA

### 🚨 GAP 1: DBT Adapter vs DBT Project Confusion

**Status**: ALTO - Projeto é adapter mas pode ter dbt project features mixed
**Problema**:

- flext-dbt-oracle é DBT adapter mas commands sugerem dbt project functionality
- Oracle-specific operations podem não be appropriate para adapter
- Architecture confusion entre adapter implementation vs dbt project

**TODO**:

- [ ] Clarify se projeto é DBT adapter ou dbt project com Oracle models
- [ ] Separate adapter functionality from dbt project concerns
- [ ] Document clear boundaries entre adapter e project responsibilities
- [ ] Remove inappropriate commands se é pure adapter

### 🚨 GAP 2: Oracle Database Integration Overlap

**Status**: ALTO - Integration com flext-db-oracle pode criar duplication
**Problema**:

- DBT adapter usando flext-db-oracle mas pode duplicate connection logic
- Oracle connectivity patterns podem divergir between adapter e library
- Connection management pode be duplicated

**TODO**:

- [ ] Optimize integration com flext-db-oracle library
- [ ] Eliminate duplication de Oracle connection functionality
- [ ] Align connection management patterns
- [ ] Leverage Oracle-specific optimizations from library

### 🚨 GAP 3: DBT Adapter Integration Complexity

**Status**: ALTO - Custom DBT adapter pode ser over-engineered
**Problema**:

- Custom DBT adapter com DI container pode be overkill
- Infrastructure layer em adapter pode não be necessary
- Adapter complexity pode not justify benefits over standard Oracle adapter

**TODO**:

- [ ] Review necessity de custom DBT adapter vs standard options
- [ ] Simplify adapter architecture se appropriate
- [ ] Evaluate DI container need em adapter context
- [ ] Document adapter architectural decisions

### 🚨 GAP 4: Singer Ecosystem Integration Unclear

**Status**: ALTO - DBT adapter relationship com Singer ecosystem não clear
**Problema**:

- DBT adapter integration com flext-meltano pode não be optimal
- Relationship com flext-tap-oracle patterns não documented
- Adapter role em broader data pipeline não clear

**TODO**:

- [ ] Define clear integration patterns com flext-meltano
- [ ] Document adapter role em Singer ecosystem
- [ ] Optimize integration com Oracle taps e targets
- [ ] Create integrated pipeline documentation

## FLEXT Ecosystem Integration

This adapter integrates with the broader FLEXT ecosystem:

- **flext-core**: Provides logging, constants, and base patterns
- **flext-db-oracle**: Handles Oracle Database connectivity
- **flext-meltano**: Provides DBT framework integration
- **flext-observability**: Adds monitoring and metrics

### Workspace Commands

```bash
make workspace-sync         # Sync with workspace dependencies
make ecosystem-check        # Verify FLEXT ecosystem compatibility
make workspace-info         # Show workspace integration details
```

## Development Guidelines

### Adding New Features

1. Follow FLEXT core patterns and use dependency injection
2. Add comprehensive type hints and validation
3. Include unit and integration tests (90%+ coverage)
4. Update configuration classes if new settings are needed
5. Document new functionality with docstrings and examples

### Modifying Oracle Adapter

1. Extend `OracleAdapter` class in `impl.py`
2. Update connection logic in `connections.py` if needed
3. Add configuration options to `config.py`
4. Update constants in `constants.py`
5. Add corresponding tests

### Performance Optimization

1. Use Oracle-specific SQL optimizations
2. Leverage connection pooling effectively
3. Monitor query performance with explain plans
4. Use batch operations where appropriate
5. Profile and benchmark critical paths
