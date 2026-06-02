#  Advanced Calculator

> A command-line Python calculator with persistent history, multi-operation support, and clean input validation — built for clarity and everyday use.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Architecture](#architecture)
- [Error Handling](#error-handling)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Overview

**Advanced Calculator** is a lightweight Python CLI application that evaluates mathematical expressions, stores a persistent calculation history, and handles common input errors gracefully — all with zero external dependencies.

It supports the full range of standard arithmetic operators, multi-step expressions with parentheses, and three built-in commands (`history`, `clear`, `exit`) to manage your session. The project is intentionally simple in structure, making it an ideal reference for learning Python fundamentals such as file I/O, exception handling, and modular function design.

---

## Features

- Evaluate complex expressions — e.g. `(10 + 5) * 4 / 3 % 7`
- Supports `+`, `-`, `*`, `/`, `%` operators
- Persistent calculation history saved to a local text file
- History displayed in reverse-chronological order (most recent first)
- One-command history clearing
- Whole-number formatting — `4.0` is displayed as `4`
- Graceful handling of division by zero
- Consecutive operator detection — blocks inputs like `2++3` or `5*-3`
- No external dependencies — pure Python standard library

---

## Installation

**Requirements:** Python 3.8 or higher.

```bash
# 1. Clone the repository
git clone https://github.com/SohelMallik/Advanced-Calculator-Python.git
cd Advanced-Calculator-Python

# 2. Confirm your Python version
python --version

# 3. Run the application
python Advanced-Calculator.py
```

No virtual environment or `pip install` is needed — the project uses only Python's standard library.

---

## Usage

Once running, type a math expression or one of the three commands at the prompt.

### Arithmetic

```
Enter calculation: 25 + 75
Result: 100

Enter calculation: (3 + 5) * 2 - 10 / 5
Result: 14

Enter calculation: 17 % 5
Result: 2
```

### History Commands

```
Enter calculation: history

--- Calculation History ---
17%5 = 2
(3+5)*2-10/5 = 14
25+75 = 100
-------------------------

Enter calculation: clear
History Cleared.

Enter calculation: exit
Goodbye!
```

---

## Configuration

No environment variables or config files are required.

The only setting in the project is the history file path, defined at the top of `Advanced-Calculator.py`:

```python
history_file = "history.txt"
```

Change this value to use a different filename or directory — for example:

```python
history_file = "logs/calc_history.txt"
```

Make sure the target directory exists before running the app if you use a subdirectory.

---

## Architecture

The application is structured as five focused functions, each with a single responsibility:

| Function | Responsibility |
|---|---|
| `main()` | REPL loop — reads input and routes to the correct handler |
| `calculation(input)` | Validates and evaluates a math expression via `eval()` |
| `save_history(eq, result)` | Appends `expression = result` to the history file |
| `show_history()` | Reads the history file and prints entries newest-first |
| `clear_history()` | Overwrites the history file with an empty file |

**Execution flow:**

```
User Input
    │
    ├── "history"  →  show_history()
    ├── "clear"    →  clear_history()
    ├── "exit"     →  print goodbye & break loop
    └── expression →  strip spaces
                          │
                      consecutive operator check
                          │
                        eval()
                          │
                      format result
                          │
                      print + save_history()
```

> **Security note:** This project uses Python's built-in `eval()` for expression parsing, which is appropriate for a local CLI tool. For any web-facing or multi-user deployment, replace `eval()` with a dedicated expression parser such as the `ast` module or the [`simpleeval`](https://pypi.org/project/simpleeval/) library.

---

## Error Handling

| Scenario | Behaviour |
|---|---|
| Division by zero | Catches `ZeroDivisionError` and prints a clear message |
| Consecutive operators (`2++3`) | Detected before `eval()` is called; prints a validation error |
| Completely invalid input (`abc`) | Caught by the generic `Exception` handler |
| Missing history file | `FileNotFoundError` caught in `show_history()` |
| Whole-number float result (`4.0`) | Automatically converted to `int` before display |

---

## Testing

The project currently uses manual testing. Suggested test cases:

| Input | Expected Output |
|---|---|
| `5 + 3` | `Result: 8` |
| `10 / 0` | `Error: Division by zero not allowed.` |
| `2 ++ 3` | `Invalid input! Expression has consecutive operators.` |
| `abc` | `Invalid input! Please enter a valid math expression.` |
| `9.0 / 3` | `Result: 3` |
| `history` | Prints saved calculations newest-first |
| `clear` | Clears `history.txt` and confirms |
| `exit` | Prints `Goodbye!` and terminates |

To add automated tests in the future:

```bash
pip install pytest
pytest tests/
```

---

## Contributing

Contributions, bug reports, and feature suggestions are welcome.

```bash
# 1. Fork the repository on GitHub
# 2. Create a feature branch
git checkout -b feature/your-feature-name

# 3. Make your changes and commit
git add .
git commit -m "feat: describe your change clearly"

# 4. Push to your fork
git push origin feature/your-feature-name

# 5. Open a Pull Request on GitHub
```

Please follow [PEP 8](https://peps.python.org/pep-0008/) style guidelines. Include test cases for any new functionality, and update this README if your change affects usage or configuration.

---

## License

This project is licensed under the **MIT License** — you are free to use, modify, and distribute it with attribution.

See [LICENSE](LICENSE) for the full text.

---

## Contact

**Sohel Mallik**

- **GitHub Issues:** [Open an issue](https://github.com/SohelMallik/Fake-News-Generator-Python.git)
- **Email:** malliksohel582@gmail.com
