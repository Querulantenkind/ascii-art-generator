# Making ASCII Art Generator Globally Executable

## Installation Methods

### Method 1: Using pip (Recommended)

```bash
# Install in editable/development mode
pip install -e .

# Or install normally
pip install .
```

After installation, these commands will be available globally:
- `ascii-art` - Basic CLI
- `ascii-art-generator` - Basic generator  
- `ascii-art-pro` - Pro version
- `ascii-art-editor` - TUI editor
- `aag`, `aag-pro`, `aag-editor` - Short aliases

### Method 2: Direct Script Execution

The scripts are already executable:

```bash
# Make scripts executable (if needed)
chmod +x ascii_art_generator.py
chmod +x ascii_art_pro.py
chmod +x ascii_art_editor.py

# Run directly
./ascii_art_generator.py text "Hello"
./ascii_art_pro.py text "TEST" --effect shadow
./ascii_art_editor.py
```

### Method 3: Using the Installation Script

```bash
chmod +x install.sh
./install.sh
```

## Building Distribution Packages

### Create source distribution

```bash
python3 setup.py sdist
```

### Create wheel distribution

```bash
python3 setup.py bdist_wheel
```

### Install from wheel

```bash
pip install dist/ascii_art_generator-4.0.0-py3-none-any.whl
```

## Verify Installation

```bash
# Check if commands are in PATH
which ascii-art-generator
which ascii-art-pro
which ascii-art-editor

# Test commands
ascii-art-generator --help
ascii-art-pro --help
ascii-art-editor --help
```

## Uninstall

```bash
pip uninstall ascii-art-generator
```

## Troubleshooting

If commands are not found after installation:

1. Check if Python scripts directory is in PATH:
   ```bash
   echo $PATH | grep -i python
   ```

2. Find Python scripts directory:
   ```bash
   python3 -m site --user-base
   ```

3. Add to PATH (if needed):
   ```bash
   export PATH="$PATH:$(python3 -m site --user-base)/bin"
   ```

4. For system-wide installation (requires sudo):
   ```bash
   sudo pip install .
   ```

