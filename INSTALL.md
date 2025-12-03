# Installation Guide

## Quick Install

### Option 1: Install from source (recommended)

```bash
# Clone the repository
git clone https://github.com/yourusername/ascii-art-generator.git
cd ascii-art-generator

# Install in editable mode (for development)
pip install -e .

# Or install normally
pip install .
```

### Option 2: Use the installation script

```bash
chmod +x install.sh
./install.sh
```

## Global Installation

After installation, the following commands will be available globally:

- `ascii-art` - Basic CLI interface
- `ascii-art-generator` - Basic generator
- `ascii-art-pro` - Pro version with advanced features
- `ascii-art-editor` - Interactive TUI editor
- `aag` - Short alias for ascii-art-generator
- `aag-pro` - Short alias for ascii-art-pro
- `aag-editor` - Short alias for ascii-art-editor

## Optional Dependencies

Install optional features:

```bash
# Image support
pip install "ascii-art-generator[image]"

# QR code support
pip install "ascii-art-generator[qr]"

# Video support
pip install "ascii-art-generator[video]"

# All optional features
pip install "ascii-art-generator[all]"
```

## Verify Installation

```bash
# Check if commands are available
which ascii-art-generator
which ascii-art-pro
which ascii-art-editor

# Test basic functionality
ascii-art-generator text "Hello"
ascii-art-pro text "TEST" --effect shadow
```

## Uninstall

```bash
pip uninstall ascii-art-generator
```

## Development Installation

For development with editable install:

```bash
pip install -e ".[all]"
```

This allows you to edit the source code and see changes immediately without reinstalling.

