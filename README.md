# Page Object + Test Framework Builder

Mini Selenium + Pytest framework using Page Object Model.

## Structure
- pages/ → Page classes
- Tests/ → Test cases
- utils/ → Reusable helpers & decorator
- output/ → Logs, screenshots, summary

## Install
pip install -r requirements.txt

## Run Tests
pytest -v

## Outputs
- Screenshots: output/screenshots/
- Summary: output/framework_summary.json

Architecture: Page Object Model (POM)
Test Runner: Pytest
Design Pattern: OOP + Decorator