# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**flext-dbt-oracle** is a DBT client integration library for Oracle Database within the FLEXT ecosystem. This is NOT a custom DBT adapter but rather a high-level client that orchestrates Oracle database operations with DBT transformations using the existing FLEXT infrastructure. Built with Python 3.13, it leverages FLEXT core libraries and follows Clean Architecture principles.

## Architecture

### Core Components

- **FlextDbtOracleClient**: High-level client for orchestrating Oracle operations with DBT
- **FlextDbtOracleConfig**: Configuration management using FLEXT core patterns
- **Oracle Integration**: Uses `flext-db-oracle` for database connectivity
- **DBT Integration**: Uses `flext-meltano` for DBT execution and model management
- **Type Safety**: Full MyPy strict typing with comprehensive validation

### Key Dependencies

Essential FLEXT ecosystem dependencies:

- `flext-core`: Foundation library with FlextResult, logging, and configuration patterns
- `flext-db-oracle`: Oracle Database connectivity and operations
- `flext-meltano`: DBT/Singer/Meltano integration platform
- `flext-observability`: Monitoring and metrics collection
- `dbt-common`: DBT core common utilities

### Actual Directory Structure

```
src/flext_dbt_oracle/
├── __init__.py              # Public API exports
├── dbt_client.py           # Main FlextDbtOracleClient class
├── dbt_config.py           # Configuration management
├── dbt_exceptions.py       # Custom exceptions
├── dbt_models.py           # DBT model abstractions
├── dbt_services.py         # Workflow and monitoring services
├── models.py               # Data models
└── constants.py            # Project constants
```

## Development Commands

### Essential Quality Gates

Run these commands before committing - all must pass:

```bash
make validate          # Complete validation (lint + type + security + test + dbt-test)
make check            # Essential checks (lint + type + dbt-compile)
```

### Core Development Workflow

```bash
# Setup and installation
make setup            # Complete development setup
make install          # Install dependencies with Poetry

# Code quality (zero tolerance enforcement)
make lint             # Ruff linting with strict rules
make type-check       # MyPy strict type checking (currently has errors)
make security         # Security scans (bandit + pip-audit)
make format          # Format code with ruff
make fix             # Auto-fix code issues

# Testing (90% coverage target)
make test            # Run tests with coverage
make test-unit       # Unit tests only
make test-integration # Integration tests only
make test-fast       # Run tests without coverage
make coverage-html   # Generate HTML coverage report
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
make dbt-clean       # Clean dbt artifacts

# Oracle-specific operations
make oracle-macros     # Test Oracle-specific macros
make oracle-staging    # Run Oracle staging models
make oracle-marts      # Run Oracle marts models
make oracle-full-refresh # Full refresh Oracle models
make oracle-performance  # Analyze Oracle query performance
```

### Build and Maintenance

```bash
make build           # Build project with Poetry
make clean           # Remove build artifacts
make clean-all       # Deep clean including venv
make deps-update     # Update all dependencies
make deps-audit      # Security audit dependencies
make diagnose        # Show environment diagnostics
make doctor          # Full health check
```

## Testing Strategy

### Test Organization

- **Unit Tests**: `tests/test_*.py` - Component-level testing
- **Integration Tests**: Test Oracle connectivity and DBT integration
- **Configuration Tests**: Comprehensive configuration validation

### Test Categories

Use pytest markers for selective testing:

```bash
pytest -m unit              # Unit tests only
pytest -m integration       # Integration tests only
pytest -m slow             # Slow tests only
pytest -m "not slow"       # Exclude slow tests
pytest -m oracle           # Oracle-specific tests
pytest -m dbt              # DBT-specific tests
```

### Coverage Requirements

- **Target**: 90% coverage (enforced by pytest configuration)
- **Reports**: HTML coverage reports in `reports/coverage/`
- **Exclusions**: Test files and external libraries excluded

### Key Test Files

- `tests/conftest.py`: Comprehensive fixtures for Oracle and DBT testing
- `tests/test_basic.py`: Basic functionality tests
- `tests/test_config_advanced.py`: Configuration validation tests
- `tests/test_connections_advanced.py`: Oracle connection tests
- `tests/test_impl_advanced.py`: Implementation tests

## Configuration

### Environment Variables

The client supports environment variable configuration with `DBT_ORACLE_` prefix:

```bash
# Required Oracle connection settings
DBT_ORACLE_ORACLE_HOST=localhost
DBT_ORACLE_ORACLE_PORT=1521
DBT_ORACLE_ORACLE_SERVICE_NAME=ORCL
DBT_ORACLE_ORACLE_USERNAME=user
DBT_ORACLE_ORACLE_PASSWORD=password

# Optional performance settings
DBT_ORACLE_ORACLE_POOL_MIN=1
DBT_ORACLE_ORACLE_POOL_MAX=10
DBT_ORACLE_ORACLE_TIMEOUT=30

# DBT execution settings
DBT_ORACLE_DBT_PROJECT_DIR=.
DBT_ORACLE_DBT_PROFILES_DIR=.
DBT_ORACLE_DBT_TARGET=dev
DBT_ORACLE_DBT_THREADS=4
```

### Configuration Class Usage

```python
from flext_dbt_oracle import FlextDbtOracleConfig

# Environment-based configuration
config = FlextDbtOracleConfig()

# Access Oracle config for flext-db-oracle
oracle_config = config.get_oracle_config()

# Access Meltano config for flext-meltano
meltano_config = config.get_meltano_config()

# Validate Oracle connection
is_valid = config.validate_oracle_connection()
```

## Code Patterns

### Client Usage

Main client for orchestrating Oracle and DBT operations:

```python
from flext_dbt_oracle import FlextDbtOracleClient, FlextDbtOracleConfig

# Initialize client with configuration
config = FlextDbtOracleConfig()
client = FlextDbtOracleClient(config)

# Test Oracle connection
connection_result = client.test_oracle_connection()
if connection_result.success:
    print("Oracle connection successful")

# Extract Oracle metadata
metadata_result = client.extract_oracle_metadata(
    schema_names=["ANALYTICS"],
    object_types=["TABLES"]
)

# Run full Oracle-to-DBT pipeline
pipeline_result = client.run_full_pipeline(
    schema_names=["ANALYTICS"],
    model_names=["dim_customers", "fact_orders"]
)
```

### Error Handling

Use FLEXT core patterns with FlextResult:

```python
from flext_core import FlextResult, get_logger

logger = get_logger(__name__)

def process_oracle_data():
    try:
        # Oracle operations
        result = client.extract_oracle_metadata()
        if not result.success:
            logger.error("Metadata extraction failed: %s", result.error)
            return result
        
        return FlextResult.ok(result.data)
    except Exception as e:
        logger.exception("Unexpected error during Oracle processing")
        return FlextResult.fail(f"Processing error: {e}")
```

### Configuration Management

Comprehensive configuration with type mappings:

```python
from flext_dbt_oracle import FlextDbtOracleConfig

config = FlextDbtOracleConfig()

# Oracle-specific mappings
oracle_type = config.get_dbt_type_for_oracle_type("VARCHAR2(100)")
materialization = config.get_materialization_for_layer("staging")
schema_mapping = config.get_object_type_for_schema("tables")

# Performance configuration
perf_config = config.get_performance_config()
quality_config = config.get_oracle_quality_config()
```

## Quality Standards

### Code Quality (Strict Enforcement)

- **Linting**: Ruff with comprehensive rules enabled
- **Type Checking**: MyPy strict mode (currently has some errors in active development)
- **Security**: Bandit security scanning + pip-audit
- **Formatting**: Ruff formatter with consistent style
- **Coverage**: 90% test coverage target

### Performance Standards

- **Connection Management**: Uses flext-db-oracle connection pooling
- **Resource Management**: Proper lifecycle management through FlextResult patterns
- **Error Handling**: Comprehensive error handling and logging

### Documentation Requirements

- **Docstrings**: All public APIs have comprehensive docstrings
- **Type Hints**: Full type annotations for all functions and methods
- **Architecture**: Clear separation between Oracle operations and DBT integration

## Debugging and Troubleshooting

### Common Issues

**Connection Problems**:

```python
from flext_dbt_oracle import FlextDbtOracleClient, FlextDbtOracleConfig

config = FlextDbtOracleConfig()
client = FlextDbtOracleClient(config)

# Test Oracle connection
result = client.test_oracle_connection()
if not result.success:
    print(f"Connection failed: {result.error}")
```

**Configuration Validation**:

```bash
# Check environment variables
env | grep DBT_ORACLE_

# Validate configuration in Python
python -c "
from flext_dbt_oracle import FlextDbtOracleConfig
config = FlextDbtOracleConfig()
print('Connection valid:', config.validate_oracle_connection())
print('Oracle config:', config.get_oracle_config())
"
```

**DBT Integration Issues**:

```bash
make dbt-debug              # Debug DBT configuration
make dbt-compile            # Test DBT model compilation
```

### Logging

Enable detailed logging for debugging:

```bash
export FLEXT_LOG_LEVEL=DEBUG
export FLEXT_ENV=development
```

## Current Development Status

### ✅ Architecture Clarification - RESOLVED

**Project Identity**: flext-dbt-oracle is now clearly defined as a **DBT client integration library**, not a custom DBT adapter. This resolves previous architectural confusion.

**Current Architecture**:
- **FlextDbtOracleClient**: High-level orchestration client
- **Integration Focus**: Uses existing flext-db-oracle + flext-meltano libraries
- **Clear Boundaries**: Oracle operations via flext-db-oracle, DBT operations via flext-meltano

### 🔄 Active Development Areas

**Type Safety Improvements**:
- MyPy strict mode implementation in progress
- Some type errors remain (expected during active development)
- Target: Zero type errors before production release

**Test Coverage Enhancement**:
- Current: Working towards 90% coverage target
- Comprehensive test fixtures in place
- Integration tests with Oracle shared container setup

**Configuration System**:
- Environment variable support implemented
- Oracle-to-DBT type mapping system in place
- Performance and quality thresholds configurable

## FLEXT Ecosystem Integration

This client library integrates with the broader FLEXT ecosystem:

- **flext-core**: Provides FlextResult patterns, logging, and configuration base
- **flext-db-oracle**: Handles Oracle Database connectivity and operations
- **flext-meltano**: Provides DBT execution and model management
- **flext-observability**: Adds monitoring and metrics collection

### Key Integration Points

```python
# flext-core integration
from flext_core import FlextResult, get_logger

# flext-db-oracle integration
oracle_config = config.get_oracle_config()
oracle_api = FlextDbOracleApi(oracle_config)

# flext-meltano integration
meltano_config = config.get_meltano_config()
dbt_hub = create_dbt_hub(registry_path)
```

## Development Guidelines

### Adding New Features

1. Follow FLEXT core patterns (FlextResult, proper logging)
2. Use composition with existing FLEXT libraries (don't duplicate functionality)
3. Add comprehensive type hints and validation
4. Include unit and integration tests (90%+ coverage target)
5. Update configuration classes for new settings
6. Document functionality with comprehensive docstrings

### Extending Oracle Integration

1. Modify `FlextDbtOracleClient` class in `dbt_client.py`
2. Update configuration in `FlextDbtOracleConfig` in `dbt_config.py`
3. Add new Oracle type mappings or schema mappings as needed
4. Extend data quality or performance configuration
5. Add corresponding tests with proper fixtures

### DBT Integration Enhancement

1. Use flext-meltano `FlextDbtHub` for DBT operations
2. Avoid duplicating DBT functionality - delegate to flext-meltano
3. Focus on Oracle-specific DBT orchestration logic
4. Maintain clear separation between Oracle operations and DBT execution
