#!/bin/bash
# Script to run Ruff linting and formatting

echo "Running Ruff linting and formatting..."

# Check for issues and auto-fix
echo "Checking for linting issues..."
ruff check . --fix

# Format code
echo "Formatting code..."
ruff format .

echo "All done! Code is now linted and formatted."
