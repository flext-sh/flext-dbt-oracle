# FLEXT-DBT-Oracle


<!-- TOC START -->
- [🚀 Key Features](#-key-features)
- [📦 Installation](#-installation)
- [🛠️ Usage](#-usage)
  - [Parallel Query Configuration](#parallel-query-configuration)
  - [Applying Oracle Hints](#applying-oracle-hints)
  - [Partition Management](#partition-management)
- [🏗️ Architecture](#-architecture)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
<!-- TOC END -->

[![dbt 1.6+](https://img.shields.io/badge/dbt-1.6+-orange.svg)](https://getdbt.com)
[![Oracle Database](https://img.shields.io/badge/Oracle-19c%2B-red.svg)](https://www.oracle.com/database/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

**FLEXT-DBT-Oracle** is a specialized dbt adapter designed for optimal performance on Oracle platforms. It provides native connectivity, parallel execution support, and data warehouse features tailored for Oracle Database environments (19c+).

Part of the [FLEXT](https://github.com/flext-sh/flext) ecosystem.

## 🚀 Key Features

- **Native Optimization**: Custom macros for Oracle CBO (Cost-Based Optimizer) hints and query tuning.
- **Parallel Execution**: Leverage Oracle's Parallel Query features directly from your dbt configurations.
- **Connection Pooling**: Enterprise-grade connection management for high-concurrency dbt runs.
- **Partitioning Support**: Easily define partition strategies (`RANGE`, `LIST`, `HASH`) in your model config.
- **Materialized Views**: Robust support for Oracle Materialized Views (MViews) with refresh capabilities.
- **Bulk Loading**: Optimized data loading patterns (`APPEND` hints) for large datasets.

## 📦 Installation

To use in your dbt project, add to your `packages.yml`:

```yaml
packages:
  - git: "https://github.com/organization/flext.git"
    subdirectory: "flext-dbt-oracle"
    revision: "main" 
```

Run dependencies:

```bash
dbt deps
```

## 🛠️ Usage

### Parallel Query Configuration

Boost performance on large fact tables:

```yaml
# dbt_project.yml
models:
  my_project:
    marts:
      finance:
        +materialized: table
        +oracle_parallel_degree: 8  # Use 8 parallel threads
        +oracle_compress: 'BASIC'
```

### Applying Oracle Hints

Optimize critical queries with direct optimizer hints:

```sql
{{ config(
    materialized='incremental',
    unique_key='transaction_id',
    oracle_hint='/*+ APPEND PARALLEL(4) */'
) }}

SELECT *
FROM {{ source('raw', 'transactions') }}
WHERE transaction_date > (SELECT MAX(transaction_date) FROM {{ this }})
```

### Partition Management

Define effective partitioning strategies for historical data:

```sql
{{ config(
    materialized='table',
    oracle_partition_by="RANGE(transaction_date) INTERVAL(NUMTOYMINTERVAL(1, 'MONTH'))",
    oracle_subpartition_by="HASH(customer_id) SUBPARTITIONS 16"
) }}

SELECT ...
```

## 🏗️ Architecture

FLEXT-DBT-Oracle extends standard dbt functionality:

- **Adapter Layer**: Custom implementation of `dbt-core` adapter interface for `cx_Oracle` / `python-oracledb`.
- **Macro Layer**: Specialized Jinja macros for DDL generation and query optimization.
- **Connection Layer**: Advanced connection pooling and session management.

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](docs/development.md) for details on testing against local Oracle containers and improving adapter features.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
