#!/bin/bash
# Installation script for ASCII Art Generator

set -e

echo "Installing ASCII Art Generator..."

# Check Python version
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "Python version: $python_version"

# Install in development mode (editable)
echo "Installing in editable mode..."
python3 -m pip install -e .

# Or install normally
# python3 -m pip install .

echo ""
echo "Installation complete!"
echo ""
echo "Available commands:"
echo "  ascii-art          - Basic CLI interface"
echo "  ascii-art-generator.py - Basic generator"
echo "  ascii-art-pro.py   - Pro version with advanced features"
echo "  ascii-art-editor.py - Interactive TUI editor"
echo ""
echo "To uninstall: pip uninstall ascii-art-generator"

