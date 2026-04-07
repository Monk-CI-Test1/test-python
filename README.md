# Python CI Test Project

A minimal Python project for testing GitHub Actions CI runners.

## Project Structure

```
src/        - Source modules
tests/      - Test files
setup.py    - Package setup
```

## Setup & Test

```bash
pip install -r requirements.txt
pytest tests/
pylint src/
python -m pytest --cov=src tests/
```

## CI Jobs

1. **Lint** — Black formatting, pylint validation
2. **Test** — Run pytest with coverage
3. **Build** — Setup install
4. **Code Analysis** — Pylint static analysis
5. **Performance** — Build time measurement
