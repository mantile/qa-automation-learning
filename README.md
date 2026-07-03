# 🚀 QA Automation Learning Roadmap

**Middle QA Automation Engineer**

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![Playwright](https://img.shields.io/badge/Playwright-1.40%2B-green.svg)](https://playwright.dev/python/)
[![Pytest](https://img.shields.io/badge/pytest-7.4%2B-orange.svg)](https://docs.pytest.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub last commit](https://img.shields.io/github/last-commit/mantile/qa-automation-learning.svg)](https://github.com/mantile/qa-automation-learning/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/mantile/qa-automation-learning.svg)](https://github.com/mantile/qa-automation-learning)
[![YouTrack](https://img.shields.io/badge/YouTrack-Whiteboard-0052CC.svg)](https://mantile.youtrack.cloud/whiteboards/500-0)
[![Tests Status](https://github.com/mantile/qa-automation-learning/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/mantile/qa-automation-learning/actions/workflows/tests.yml)
[![Allure Report](https://img.shields.io/badge/Allure-Report-1E90FF.svg)](https://github.com/mantile/qa-automation-learning/actions/workflows/allure.yml)



---

## 📖 Overview

This repository is my **personal learning roadmap and portfolio** for growing to Middle QA Automation Engineer. It contains structured learning phases, practical projects, and all the materials I'm studying.

**Core philosophy:** Not just writing tests — **designing testing ecosystems**, managing quality at the product level, and influencing the development process.

---

## 🎯 Global Goal

**Middle QA Automation Engineer** who can:

- Design scalable test frameworks from scratch
- Implement Shift-Left testing strategies
- Mentor junior engineers
- Drive quality metrics and processes

**Core Tech Stack:**
- 🐍 **Python 3.8+** — primary language
- 🎭 **Playwright** — UI automation (modern, fast, reliable)
- 🧪 **Pytest** — test framework
- 🐙 **Git & GitHub Actions** — version control & CI/CD
- 🐳 **Docker** — environment containerization
- 📊 **Allure** — beautiful test reports

---

## 📊 Current Level (Starting Point)

| Aspect | Current | Target |
| :--- | :--- | :--- |
| **Experience** | Manual QA Engineer | Middle QA Automation (~3-5 years) |
| **Python** | Basic (scripts, syntax) | Advanced (OOP, async, decorators) |
| **Testing** | Manual + test theory | Full automation framework design |
| **Tools** | Basic Git, Jira | Docker, CI/CD, Allure, Performance tools |

---

## 🌐 Test Applications for Hands-On Projects

Instead of hypothetical examples, this roadmap uses real, publicly available test websites. This ensures you're practicing with authentic applications and challenges.

| Website | Purpose | Key Features to Test |
| :--- | :--- | :--- |
| **[XYZ Bank](https://www.globalsqa.com/angularJs-protractor/BankingProject)** | Banking application simulation | Customer login, fund transfers, transaction history, account management, table interactions |
| **[Swag Labs](https://www.saucedemo.com)** | E-commerce platform (SauceDemo) | User authentication, product filtering/sorting, shopping cart, checkout process, and order validation |
| **[DemoQA](https://demoqa.com/)** | A comprehensive UI elements demo | Forms, buttons, modals, drag-and-drop, date pickers, and other complex UI interactions |
| **[Restful-Booker](https://restful-booker.herokuapp.com/apidoc/index.html)** | Hotel booking API sandbox | CRUD operations for bookings; token-based authentication; GET, POST, PUT, PATCH, DELETE methods; response validation; error handling |
| **SQLite (Local)** | Embedded test database | Practicing SQL queries, data validation, and test data setup/teardown for database-backed applications |

---

## 🗺️ Learning Roadmap

### 🧱 PHASE 1: Foundation (1–2 weeks)
**Goal:** Write Python scripts confidently and work with Git.

| Topic | Status | Resources |
| :--- | :--- | :--- |
| Testing Theory (Unit/Integration/E2E) | ✅ | [Playwright Docs](https://playwright.dev/python/) |
| Python Basics | ✅ | [Python Tutorial](https://docs.python.org/3/tutorial/) |
| Git Basics | ✅ | [GitHub Learning Lab](https://lab.github.com/) |

---

### 🎯 PHASE 2: First Automated Test (1–2 weeks)
**Goal:** Control a browser with code.

| Topic | Status | Resources |
| :--- | :--- | :--- |
| Playwright Setup | ✅ | [Playwright Installation](https://playwright.dev/python/docs/intro) |
| Locators (CSS, XPath, Text) | ✅ | [Locators Guide](https://playwright.dev/docs/locators) |
| First Test Script | ✅ | - |

**Project:** Saucedemo login tests (open page → click → verify URL)

---

### 🏗️ PHASE 3: Real Framework (3–4 weeks)
**Goal:** Build a structured, maintainable test project.

| Topic | Status | Resources |
| :--- | :--- | :--- |
| Pytest (fixtures, markers) | ✅ | [Pytest Docs](https://docs.pytest.org/) |
| Page Object Model (POM) | ✅ | [POM Guide](https://playwright.dev/docs/pom) |
| API Testing (requests) | 🔄 | [Requests Library](https://requests.readthedocs.io/) |

**Project:** Saucedemo E-commerce test framework with 10+ UI + API tests (fullrun from login to shopping finish)

---

### ⚙️ PHASE 4: CI/CD Integration (1–2 weeks)
**Goal:** Tests run automatically on every push.

| Topic | Status | Resources |
| :--- | :--- | :--- |
| GitHub Actions | 🔄 | [GitHub Actions Docs](https://docs.github.com/en/actions) |
| Parallel Execution | 🔄 | [pytest-xdist](https://pytest-xdist.readthedocs.io/) |
| Test Reports | 🔄 | [Allure Framework](https://docs.qameta.io/allure/) |

**Project:** CI pipeline with parallel tests and Allure reports

---

### 📈 PHASE 5: Scaling & Maintenance (Ongoing)
**Goal:** Deepen skills and maintain test quality.

| Topic | Status | Resources |
| :--- | :--- | :--- |
| SQL (JOIN, transactions) | 🔄 | [SQL Tutorial](https://www.w3schools.com/sql/) |
| Docker Containers | 🔄 | [Docker Curriculum](https://docker-curriculum.com/) |
| Flaky Test Analysis | 🔄 | [Playwright Trace](https://playwright.dev/docs/trace-viewer) |
| Allure Reports | 🔄 | [Allure Docs](https://docs.qameta.io/allure/) |

**Project:** Add DB checks, Allure reports, and containerization

---
### 🧱 PHASE 6: Deep Foundation
**Goal:** Understand the system as a whole, not just test cases.

| Topic | Status | Resources |
| :--- | :--- | :--- |
| Deep Understanding of Application Architecture | 🔄 | - |
| Python: From Basic to Advanced (OOP, Async, Decorators) | 🔄 | [Fluent Python](https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/) |
| Git at Team Level (Rebase, Merge, Code Review) | 🔄 | [Git Docs](https://git-scm.com/doc) |
| SQL: From SELECT to Advanced Queries (JOIN, Windows, Transactions) | 🔄 | [SQL Tutorial](https://www.w3schools.com/sql/) |
| Docker: Basic Proficiency | 🔄 | [Docker Docs](https://docs.docker.com/) |

**Project:** Set up Docker environment, write advanced SQL queries, participate in code reviews

---

### 🏗️ PHASE 7: Framework Architecture
**Goal:** Design the test framework as a standalone product.

| Topic | Status | Resources |
| :--- | :--- | :--- |
| Architectural Patterns (POM, Factory, Singleton, Chain) | 🔄 | [Design Patterns](https://refactoring.guru/design-patterns) |
| Advanced Pytest (Custom Fixtures, Plugins, Hooks) | 🔄 | [Pytest Docs](https://docs.pytest.org/) |
| API Testing at Middle Level (Contract Testing, OAuth, GraphQL) | 🔄 | [Requests Library](https://requests.readthedocs.io/) |
| Allure: Advanced Reporting (Steps, Attachments, Jira Integration) | 🔄 | [Allure Docs](https://docs.qameta.io/allure/) |
| Test Data Management (Factories, Cleanup Strategies) | 🔄 | - |

**Project:** Refactor framework with design patterns, implement contract tests, create custom Allure reports

---

### ⚙️ PHASE 8: CI/CD & Infrastructure
**Goal:** Tests are part of the development ecosystem.

| Topic | Status | Resources |
| :--- | :--- | :--- |
| Advanced CI/CD (Multi-branch, Parallel Runs, Artifacts, Triggers) | 🔄 | [GitHub Actions Docs](https://docs.github.com/en/actions) |
| Docker & Containerization (Kubernetes, docker-compose) | 🔄 | [Kubernetes Docs](https://kubernetes.io/docs/) |
| Cloud Technologies (S3, Azure Blob, BrowserStack) | 🔄 | - |
| Test Monitoring (Alerts, History, Grafana/Kibana) | 🔄 | [Grafana Docs](https://grafana.com/docs/) |

**Project:** Set up parallel execution in CI, configure alerts, implement monitoring dashboards

---

### 🎯 PHASE 9: Test Strategy & Shift-Left
**Goal:** Not just find bugs — prevent them.

| Topic | Status | Resources |
| :--- | :--- | :--- |
| Test Strategy (Test Plan, Risk-Based Testing, Tool Selection) | 🔄 | - |
| Team Collaboration (Code Review, Refinement, Pair Testing) | 🔄 | - |
| BDD (Cucumber/Behave, Gherkin) | 🔄 | [Cucumber Docs](https://cucumber.io/docs/) |
| Quality Metrics (Coverage, Flaky Rate, Execution Time) | 🔄 | - |

**Project:** Create a Test Plan, implement BDD for a project, set up quality dashboards

---

### 📈 PHASE 10: Performance & Leadership
**Goal:** Go beyond functional testing.

| Topic | Status | Resources |
| :--- | :--- | :--- |
| Performance/Load Testing (JMeter, k6) | 🔄 | [k6 Docs](https://k6.io/docs/) |
| Security Testing (OWASP ZAP, SQL Injection, XSS) | 🔄 | [OWASP ZAP Docs](https://www.zaproxy.org/docs/) |
| Maintenance & Optimization (Flaky Fixes, Speed Optimization) | 🔄 | - |
| Mentoring (Code Reviews, Workshops, Documentation) | 🔄 | - |

**Project:** Write load tests, run security scans, mentor junior engineers

---
### 📂 Repository Structure

```plaintext
qa-automation-learning/
├── .github/                        # GitHub CI/CD pipelines
├── data/                           # Test data (JSON, YAML, CSV)
├── pages/                          # Page Object Models
│   ├── BankingProject/             # POM for XYZ Bank
│   ├── Demoqa/                     # POM for DemoQA
│   └── Saucedemo/                  # POM for Swag Labs
├── reports/                        # Test reports (Allure, HTML)
├── tests/                          # All test files
│   ├── 1_2Newbee/                  # Beginner tests
│   │   └── first_tests.py
│   ├── BankingProject/             # Tests for XYZ Bank
│   ├── Demoqa/                     # Tests for DemoQA
│   ├── Saucedemo/                  # Tests for Swag Labs
│   └── utils/                      # Test-specific utilities
├── .gitignore                      # Ignored files
├── conftest.py                     # Global pytest fixtures
├── docker-compose.yml              # Docker container for tests
├── pytest.ini                      # Pytest configuration (markers, options)
├── README.md                       # Project documentation
└── requirements.txt                # Python dependencies
```
---

## 🛠️ Technologies & Tools

| Category | Tools | Purpose |
| :--- | :--- | :--- |
| **Language** | Python 3.8+ | Core programming |
| **Browser Automation** | Playwright | UI testing (Chromium, Firefox, WebKit) |
| **Test Framework** | Pytest, pytest-xdist | Test execution, parallelization |
| **API Testing** | Requests, pytest | REST API validation |
| **Reporting** | Allure, pytest-html | Beautiful test reports |
| **CI/CD** | GitHub Actions | Automatic test execution |
| **Containerization** | Docker, docker-compose | Environment isolation |
| **Version Control** | Git, GitHub | Code management |
| **Database** | SQL (PostgreSQL/MySQL) | Data validation |
| **Code Quality** | Black, flake8 | Code style and linting |

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Git
- Docker (optional, for containerized runs)

### Installation

## 🚀 Quick Start Guide
1. Clone the Repository

```bash
git clone https://github.com/mantile/qa-automation-learning.git
cd qa-automation-learning
```

2. Set Up Python Environment
```bash
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install
```
3. Create the Test Database
```bash
python create_test_db.py
```
4. Run the Automated Tests

```bash
# Run all tests
pytest

# Run tests with Allure reporting
pytest --alluredir=reports/allure-results
```
5. View the Allure Report

```bash
# Serve the Allure report locally
allure serve reports/allure-results
```

## 📚 Key Resources

- [Playwright Documentation (Python)](https://playwright.dev/python/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Allure Framework](https://docs.qameta.io/allure/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [SQLite Tutorial](https://www.sqlite.org/docs.html)

## 🤝 Connect

- **GitHub:** [github.com/mantile](https://github.com/mantile)

## 📄 License
This project is for educational purposes. Licensed under the MIT License.

## 🚀 Keep learning and building!
[![GitHub stars](https://img.shields.io/github/stars/mantile/qa-automation-learning.svg?style=social&label=Star)](https://github.com/mantile/qa-automation-learning/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/mantile/qa-automation-learning.svg?style=social&label=Fork)](https://github.com/mantile/qa-automation-learning/network/members)
[![GitHub watchers](https://img.shields.io/github/watchers/mantile/qa-automation-learning.svg?style=social&label=Watch)](https://github.com/mantile/qa-automation-learning/watchers)
[![GitHub issues](https://img.shields.io/github/issues/mantile/qa-automation-learning.svg)](https://github.com/mantile/qa-automation-learning/issues)
[![GitHub contributors](https://img.shields.io/github/contributors/mantile/qa-automation-learning.svg)](https://github.com/mantile/qa-automation-learning/graphs/contributors)
[![GitHub last commit](https://img.shields.io/github/last-commit/mantile/qa-automation-learning.svg)](https://github.com/mantile/qa-automation-learning/commits/main)
