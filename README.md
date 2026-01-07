---

# OpsForge

## Overview

OpsForge is a lightweight, modular Python CLI tool designed to inspect system environment details, perform basic health checks, and report system status.
The project is built using only the Python standard library and follows a clean package-based architecture suitable for learning systems programming, CLI design, and foundational DevOps/security tooling.


---

## Features

* Environment inspection (OS, Python, execution context)
* System health check with strict/non-strict modes
* Basic system status reporting
* Deterministic exit codes for automation
* Modular CLI and core separation
* Testable, package-safe imports

---

## Project Structure

```
opsforge/
├── opsforge/
│   ├── cli.py
│   ├── core/
│   │   ├── env.py
│   │   ├── health.py
│   │   ├── status.py
│   │   ├── commands.py
│   │   └── parser.py
│   ├── utils/
│   └── storage/
├── tests/
│   ├── test_basic.py
│   └── test_health.py
└── README.md
```

---

## Requirements

* Python 3.10 or higher
* No third-party libraries required

---

## Installation

Clone the repository:

```bash
git clone https://github.com/DhyaanKanoja11/opsforge.git
cd opsforge
```

No virtual environment or dependency installation is required.

---

## Usage

All commands are executed from the project root.

### Environment Information

```bash
python -m opsforge.cli env
```

JSON output:

```bash
python -m opsforge.cli env --json
```

---

### System Status

```bash
python -m opsforge.cli status
```

---

### Health Check

```bash
python -m opsforge.cli health
```

Strict mode (non-recoverable failure):

```bash
python -m opsforge.cli health --strict
```

---

## Exit Codes

| Code | Meaning            |
| ---: | ------------------ |
|    0 | Success            |
|    1 | Non-critical issue |
|    2 | Strict failure     |

These exit codes are designed for scripting and CI integration.

---

## Testing

Run tests from the project root:

```bash
python -m tests.test_basic
python -m tests.test_health
```

All tests must pass before submission or further development.

---

## Roadmap 

Planned contributions include:

* `scan` module for basic TCP port probing (standard library only)
* Enhanced system status (CPU, memory, disk)
* Logging integration
* Expanded test coverage
* Improved CLI argument parsing
---

## License

This project is released under the MIT License.

---