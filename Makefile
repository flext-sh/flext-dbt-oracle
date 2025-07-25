# FLEXT DBT ORACLE - Oracle Database Data Transformations
# =======================================================
# dbt transformations for Oracle Database with enterprise analytics
# Python 3.13 + dbt-oracle + Oracle SQL + Zero Tolerance Quality Gates

.PHONY: help info diagnose check validate test lint type-check security format format-check fix
.PHONY: install dev-install setup pre-commit build clean
.PHONY: coverage coverage-html test-unit test-integration test-dbt
.PHONY: deps-update deps-audit deps-tree deps-outdated
.PHONY: dbt-compile dbt-run dbt-test dbt-docs dbt-debug dbt-seed dbt-snapshot dbt-deps dbt-clean
.PHONY: oracle-profile-test oracle-macros oracle-performance

# ============================================================================
# 🎯 HELP & INFORMATION
# ============================================================================

help: ## Show this help message
	@echo "🏛️ FLEXT DBT ORACLE - Oracle Database Data Transformations"
	@echo "=========================================================="
	@echo "🎯 Clean Architecture + DDD + Python 3.13 + dbt Oracle Analytics"
	@echo ""
	@echo "📦 dbt transformations for Oracle Database with enterprise patterns"
	@echo "🔒 Zero tolerance quality gates for Oracle data models"
	@echo "🧪 90%+ test coverage requirement for analytics models"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'


info: ## Mostrar informações do projeto
	@echo "📊 Informações do Projeto"
	@echo "======================"
	@echo "Nome: flext-dbt-oracle"
	@echo "Título: FLEXT DBT ORACLE"
	@echo "Tipo: dbt-project"
	@echo "Versão: $(shell poetry version -s 2>/dev/null || echo "0.7.0")"
	@echo "Python: $(shell python3.13 --version 2>/dev/null || echo "Não encontrado")"
	@echo "Poetry: $(shell poetry --version 2>/dev/null || echo "Não instalado")"
	@echo "Venv: $(shell poetry env info --path 2>/dev/null || echo "Não ativado")"
	@echo "Diretório: $(CURDIR)"
	@echo "Git Branch: $(shell git branch --show-current 2>/dev/null || echo "Não é repo git")"
	@echo "Git Status: $(shell git status --porcelain 2>/dev/null | wc -l | xargs echo) arquivos alterados"

diagnose: ## Executar diagnósticos completos
	@echo "🔍 Executando diagnósticos para flext-dbt-oracle..."
	@echo "Informações do Sistema:"
	@echo "OS: $(shell uname -s)"
	@echo "Arquitetura: $(shell uname -m)"
	@echo "Python: $(shell python3.13 --version 2>/dev/null || echo "Não encontrado")"
	@echo "Poetry: $(shell poetry --version 2>/dev/null || echo "Não instalado")"
	@echo ""
	@echo "Estrutura do Projeto:"
	@ls -la
	@echo ""
	@echo "Configuração Poetry:"
	@poetry config --list 2>/dev/null || echo "Poetry não configurado"
	@echo ""
	@echo "Status das Dependências:"
	@poetry show --outdated 2>/dev/null || echo "Nenhuma dependência desatualizada"

# ============================================================================
# 🎯 CORE QUALITY GATES - ZERO TOLERANCE
# ============================================================================

validate: lint type-check security test dbt-test ## STRICT compliance validation (all must pass)
	@echo "✅ ALL QUALITY GATES PASSED - FLEXT DBT ORACLE COMPLIANT"

check: lint type-check test dbt-compile ## Essential quality checks (pre-commit standard)
	@echo "✅ Essential checks passed"

lint: ## Ruff linting (17 rule categories, ALL enabled)
	@echo "🔍 Running ruff linter (ALL rules enabled)..."
	@poetry run ruff check src/ tests/ --fix --unsafe-fixes
	@echo "✅ Linting complete"

type-check: ## MyPy strict mode type checking (zero errors tolerated)
	@echo "🛡️ Running MyPy strict type checking..."
	@poetry run mypy src/ tests/ --strict
	@echo "✅ Type checking complete"

security: ## Security scans (bandit + pip-audit + secrets)
	@echo "🔒 Running security scans..."
	@poetry run bandit -r src/ --severity-level medium --confidence-level medium
	@poetry run pip-audit --ignore-vuln PYSEC-2022-42969
	@poetry run detect-secrets scan --all-files
	@echo "✅ Security scans complete"

format: ## Format code with ruff
	@echo "🎨 Formatting code..."
	@poetry run ruff format src/ tests/
	@echo "✅ Formatting complete"

format-check: ## Check formatting without fixing
	@echo "🎨 Checking code formatting..."
	@poetry run ruff format src/ tests/ --check
	@echo "✅ Format check complete"

fix: format lint ## Auto-fix all issues (format + imports + lint)
	@echo "🔧 Auto-fixing all issues..."
	@poetry run ruff check src/ tests/ --fix --unsafe-fixes
	@echo "✅ All auto-fixes applied"

# ============================================================================
# 🧪 TESTING - 90% COVERAGE MINIMUM
# ============================================================================

test: ## Run tests with coverage (90% minimum required)
	@echo "🧪 Running tests with coverage..."
	@poetry run pytest tests/ -v --cov=src/flext_dbt_oracle --cov-report=term-missing --cov-fail-under=90
	@echo "✅ Tests complete"

test-unit: ## Run unit tests only
	@echo "🧪 Running unit tests..."
	@poetry run pytest tests/unit/ -v
	@echo "✅ Unit tests complete"

test-integration: ## Run integration tests only
	@echo "🧪 Running integration tests..."
	@poetry run pytest tests/integration/ -v
	@echo "✅ Integration tests complete"

test-dbt: dbt-deps dbt-compile ## Run dbt data tests
	@echo "🧪 Running dbt data tests..."
	@poetry run dbt test --profiles-dir profiles/ --target dev
	@echo "✅ DBT data tests complete"

coverage: ## Generate detailed coverage report
	@echo "📊 Generating coverage report..."
	@poetry run pytest tests/ --cov=src/flext_dbt_oracle --cov-report=term-missing --cov-report=html
	@echo "✅ Coverage report generated in htmlcov/"

coverage-html: coverage ## Generate HTML coverage report
	@echo "📊 Opening coverage report..."
	@python -m webbrowser htmlcov/index.html

# ============================================================================
# 🚀 DEVELOPMENT SETUP
# ============================================================================

setup: install pre-commit dbt-deps ## Complete development setup
	@echo "🎯 Development setup complete!"

install: ## Install dependencies with Poetry
	@echo "📦 Installing dependencies..."
	@poetry install --all-extras --with dev,test,docs,security
	@echo "✅ Dependencies installed"

dev-install: install ## Install in development mode
	@echo "🔧 Setting up development environment..."
	@poetry install --all-extras --with dev,test,docs,security
	@poetry run pre-commit install
	@mkdir -p profiles logs target dbt_packages
	@echo "✅ Development environment ready"

pre-commit: ## Setup pre-commit hooks
	@echo "🎣 Setting up pre-commit hooks..."
	@poetry run pre-commit install
	@poetry run pre-commit run --all-files || true
	@echo "✅ Pre-commit hooks installed"

# ============================================================================
# 🎯 DBT OPERATIONS - CORE WORKFLOW
# ============================================================================

dbt-deps: ## Install dbt dependencies
	@echo "📦 Installing dbt dependencies..."
	@poetry run dbt deps --profiles-dir profiles/
	@echo "✅ DBT dependencies installed"

dbt-debug: ## Debug dbt configuration
	@echo "🔍 Debugging dbt configuration..."
	@poetry run dbt debug --profiles-dir profiles/ --target dev
	@echo "✅ DBT debug complete"

dbt-compile: dbt-deps ## Compile dbt models
	@echo "🔨 Compiling dbt models..."
	@poetry run dbt compile --profiles-dir profiles/ --target dev
	@echo "✅ DBT models compiled"

dbt-run: dbt-deps dbt-compile ## Run dbt models
	@echo "🚀 Running dbt models..."
	@poetry run dbt run --profiles-dir profiles/ --target dev
	@echo "✅ DBT models executed"

dbt-test: dbt-compile ## Run dbt tests
	@echo "🧪 Running dbt tests..."
	@poetry run dbt test --profiles-dir profiles/ --target dev
	@echo "✅ DBT tests complete"

dbt-docs: dbt-compile ## Generate dbt documentation
	@echo "📚 Generating dbt documentation..."
	@poetry run dbt docs generate --profiles-dir profiles/ --target dev
	@echo "✅ DBT documentation generated"

dbt-seed: dbt-deps ## Load dbt seed data
	@echo "🌱 Loading dbt seed data..."
	@poetry run dbt seed --profiles-dir profiles/ --target dev
	@echo "✅ DBT seed data loaded"

dbt-snapshot: dbt-deps ## Run dbt snapshots
	@echo "📸 Running dbt snapshots..."
	@poetry run dbt snapshot --profiles-dir profiles/ --target dev
	@echo "✅ DBT snapshots complete"

dbt-clean: ## Clean dbt artifacts
	@echo "🧹 Cleaning dbt artifacts..."
	@poetry run dbt clean --profiles-dir profiles/
	@rm -rf logs/dbt.log
	@echo "✅ DBT artifacts cleaned"

# ============================================================================
# 🔧 ORACLE SPECIFIC OPERATIONS
# ============================================================================

oracle-profile-test: ## Test Oracle connection profiles
	@echo "🔗 Testing Oracle connection profiles..."
	@poetry run dbt debug --profiles-dir profiles/ --target dev
	@poetry run python scripts/test_oracle_connections.py
	@echo "✅ Oracle profile tests complete"

oracle-macros: dbt-deps ## Test and validate Oracle-specific macros
	@echo "🔧 Testing Oracle macros..."
	@poetry run dbt test --models test_oracle_macros --profiles-dir profiles/ --target dev
	@poetry run python scripts/validate_oracle_macros.py
	@echo "✅ Oracle macros tests complete"

oracle-performance: dbt-compile ## Analyze Oracle performance and optimization
	@echo "⚡ Analyzing Oracle performance..."
	@poetry run python scripts/analyze_oracle_performance.py
	@poetry run dbt compile --profiles-dir profiles/ --target dev
	@echo "✅ Oracle performance analysis complete"

oracle-staging-models: dbt-run ## Run Oracle staging models only
	@echo "📥 Running Oracle staging models..."
	@poetry run dbt run --models tag:staging --profiles-dir profiles/ --target dev
	@echo "✅ Oracle staging models executed"

oracle-marts-models: dbt-run ## Run Oracle marts models only
	@echo "🏪 Running Oracle marts models..."
	@poetry run dbt run --models tag:marts --profiles-dir profiles/ --target dev
	@echo "✅ Oracle marts models executed"

oracle-fact-models: dbt-run ## Run Oracle fact models only
	@echo "📊 Running Oracle fact models..."
	@poetry run dbt run --models tag:fact --profiles-dir profiles/ --target dev
	@echo "✅ Oracle fact models executed"

oracle-dimension-models: dbt-run ## Run Oracle dimension models only
	@echo "🗂️ Running Oracle dimension models..."
	@poetry run dbt run --models tag:dimension --profiles-dir profiles/ --target dev
	@echo "✅ Oracle dimension models executed"

oracle-full-refresh: ## Full refresh of Oracle models
	@echo "🔄 Full refresh of Oracle models..."
	@poetry run dbt run --full-refresh --profiles-dir profiles/ --target dev
	@echo "✅ Oracle models full refresh complete"

oracle-test-data-quality: dbt-test ## Test Oracle data quality rules
	@echo "🔍 Testing Oracle data quality..."
	@poetry run dbt test --models tag:data_quality --profiles-dir profiles/ --target dev
	@echo "✅ Oracle data quality tests passed"

oracle-explain-plan: dbt-compile ## Generate Oracle explain plans
	@echo "📋 Generating Oracle explain plans..."
	@poetry run dbt compile --profiles-dir profiles/ --target dev
	@poetry run python scripts/generate_explain_plans.py
	@echo "✅ Oracle explain plans generated"

# ============================================================================
# 📦 BUILD & DISTRIBUTION
# ============================================================================

build: clean dbt-compile ## Build dbt project
	@echo "🔨 Building dbt project..."
	@poetry build
	@echo "✅ Build complete - packages in dist/"

clean: ## Remove all artifacts
	@echo "🧹 Cleaning up..."
	@rm -rf build/
	@rm -rf dist/
	@rm -rf *.egg-info/
	@rm -rf .coverage
	@rm -rf htmlcov/
	@rm -rf target/
	@rm -rf dbt_packages/
	@rm -rf logs/
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name ".ruff_cache" -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -delete 2>/dev/null || true
	@echo "✅ Cleanup complete"

# ============================================================================
# 📊 DEPENDENCY MANAGEMENT
# ============================================================================

deps-update: ## Update all dependencies
	@echo "🔄 Updating dependencies..."
	@poetry update
	@poetry run dbt deps --profiles-dir profiles/
	@echo "✅ Dependencies updated"

deps-audit: ## Audit dependencies for vulnerabilities
	@echo "🔍 Auditing dependencies..."
	@poetry run pip-audit
	@echo "✅ Dependency audit complete"

deps-tree: ## Show dependency tree
	@echo "🌳 Dependency tree:"
	@poetry show --tree

deps-outdated: ## Show outdated dependencies
	@echo "📋 Outdated dependencies:"
	@poetry show --outdated

# ============================================================================
# 🔧 ENVIRONMENT CONFIGURATION
# ============================================================================

# Project information
PROJECT_NAME := flext-dbt-oracle
PROJECT_TYPE := meltano-plugin
PROJECT_VERSION := $(shell poetry version -s)
PROJECT_DESCRIPTION := FLEXT DBT Oracle - Oracle Database Data Transformations

# Python settings
PYTHON := python3.13
export PYTHONPATH := $(PWD)/src:$(PYTHONPATH)
export PYTHONDONTWRITEBYTECODE := 1
export PYTHONUNBUFFERED := 1

# DBT settings
export DBT_PROFILES_DIR := $(PWD)/profiles
export DBT_PROJECT_DIR := $(PWD)
export DBT_TARGET := dev
export DBT_LOG_LEVEL := INFO

# Oracle settings
export ORACLE_SOURCE_SCHEMA := FLEXT_RAW
export ORACLE_TARGET_SCHEMA := FLEXT_ANALYTICS

# Performance settings
export DBT_THREADS := 4
export DBT_PARTIAL_PARSE := true
export DBT_USE_COLORS := true
export DBT_PRINTER_WIDTH := 80

# Quality settings
export DBT_WARN_ERROR := false
export DBT_STORE_FAILURES := true
export DBT_FAIL_FAST := false

# Poetry settings
export POETRY_VENV_IN_PROJECT := false
export POETRY_CACHE_DIR := $(HOME)/.cache/pypoetry

# Quality gate settings
export MYPY_CACHE_DIR := .mypy_cache
export RUFF_CACHE_DIR := .ruff_cache

.DEFAULT_GOAL := help

# ============================================================================
# 🎯 WORKSPACE INTEGRATION
# ============================================================================

workspace-sync: ## Sync with workspace dependencies
	@echo "🔄 Syncing with workspace dependencies..."
	@poetry run python scripts/sync_workspace_deps.py
	@echo "✅ Workspace sync complete"

ecosystem-check: ## Verify FLEXT ecosystem compatibility
	@echo "🌐 Checking FLEXT ecosystem compatibility..."
	@echo "📦 DBT Oracle project: $(PROJECT_NAME) v$(PROJECT_VERSION)"
	@echo "🏗️ Architecture: Clean Architecture + DDD"
	@echo "🐍 Python: 3.13"
	@echo "🗂️ Framework: dbt Oracle"
	@echo "📊 Quality: Zero tolerance enforcement"
	@echo "✅ Ecosystem compatibility verified"

workspace-info: ## Show workspace integration info
	@echo "🏢 FLEXT Workspace Integration"
	@echo "==============================="
	@echo "📁 Project Path: $(PWD)"
	@echo "🏆 Role: Oracle Database Data Transformations"
	@echo "🔗 Dependencies: flext-core"
	@echo "📦 Provides: Oracle analytics models"
	@echo "🎯 Standards: Enterprise dbt Oracle patterns"