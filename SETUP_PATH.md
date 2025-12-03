# Setting Up PATH for ASCII Art Generator

## Quick Setup Guide

### Step 1: Find Your Python Scripts Directory

Run these commands to find where pip installs scripts:

```bash
# Method 1: User scripts directory
python3 -m site --user-base
# This will output something like: /home/username/.local

# The scripts are in: /home/username/.local/bin

# Method 2: System-wide scripts directory (if using sudo)
python3 -c "import sysconfig; print(sysconfig.get_path('scripts'))"
# This will output something like: /usr/local/bin
```

### Step 2: Add to PATH

#### Option A: Temporary (Current Session Only)

```bash
# For user installation
export PATH="$PATH:$HOME/.local/bin"

# Or for system installation
export PATH="$PATH:/usr/local/bin"
```

#### Option B: Permanent (Recommended)

**For Bash (default on most Linux systems):**

```bash
# Add to ~/.bashrc
echo 'export PATH="$PATH:$HOME/.local/bin"' >> ~/.bashrc

# Reload your shell configuration
source ~/.bashrc
```

**For Zsh:**

```bash
# Add to ~/.zshrc
echo 'export PATH="$PATH:$HOME/.local/bin"' >> ~/.zshrc

# Reload your shell configuration
source ~/.zshrc
```

**For Fish:**

```fish
# Add to ~/.config/fish/config.fish
echo 'set -gx PATH $PATH $HOME/.local/bin' >> ~/.config/fish/config.fish

# Reload your shell configuration
source ~/.config/fish/config.fish
```

### Step 3: Verify PATH Setup

```bash
# Check if directory is in PATH
echo $PATH | grep -o "$HOME/.local/bin"

# Or check if commands are available
which ascii-art-generator
which ascii-art-pro
which ascii-art-editor
```

### Step 4: Test Commands

```bash
# Test the commands
ascii-art-generator --help
ascii-art-pro --help
ascii-art-editor --help
```

## Alternative: Create Symbolic Links

If you prefer, you can create symbolic links in a directory already in your PATH:

```bash
# Find a directory already in PATH (usually /usr/local/bin or ~/bin)
echo $PATH

# Create ~/bin if it doesn't exist
mkdir -p ~/bin

# Add ~/bin to PATH (if not already there)
echo 'export PATH="$PATH:$HOME/bin"' >> ~/.bashrc
source ~/.bashrc

# Create symbolic links
ln -s $(pwd)/ascii_art_generator.py ~/bin/ascii-art-generator
ln -s $(pwd)/ascii_art_pro.py ~/bin/ascii-art-pro
ln -s $(pwd)/ascii_art_editor.py ~/bin/ascii-art-editor

# Make them executable
chmod +x ~/bin/ascii-art-*
```

## Quick Setup Script

Run this script to automatically set up PATH:

```bash
#!/bin/bash
# Quick PATH setup script

SCRIPTS_DIR="$HOME/.local/bin"

# Check if directory exists
if [ ! -d "$SCRIPTS_DIR" ]; then
    mkdir -p "$SCRIPTS_DIR"
fi

# Detect shell and add to appropriate config file
if [ -n "$ZSH_VERSION" ]; then
    CONFIG_FILE="$HOME/.zshrc"
elif [ -n "$BASH_VERSION" ]; then
    CONFIG_FILE="$HOME/.bashrc"
else
    CONFIG_FILE="$HOME/.profile"
fi

# Add to PATH if not already there
if ! grep -q "$SCRIPTS_DIR" "$CONFIG_FILE" 2>/dev/null; then
    echo "" >> "$CONFIG_FILE"
    echo "# Python user scripts" >> "$CONFIG_FILE"
    echo "export PATH=\"\$PATH:$SCRIPTS_DIR\"" >> "$CONFIG_FILE"
    echo "Added $SCRIPTS_DIR to $CONFIG_FILE"
    echo "Run: source $CONFIG_FILE"
else
    echo "PATH already configured in $CONFIG_FILE"
fi

# Verify
if echo $PATH | grep -q "$SCRIPTS_DIR"; then
    echo "✓ PATH is set correctly"
else
    echo "⚠ PATH not active yet. Run: source $CONFIG_FILE"
fi
```

## Troubleshooting

### Commands Not Found After Adding to PATH

1. **Reload your shell:**
   ```bash
   source ~/.bashrc  # or ~/.zshrc
   ```

2. **Or open a new terminal window**

3. **Check if scripts directory exists:**
   ```bash
   ls -la ~/.local/bin/
   ```

4. **Verify installation:**
   ```bash
   pip show ascii-art-generator
   ```

### Find Where Scripts Are Installed

```bash
# For user installation
python3 -m site --user-base
# Scripts are in: <output>/bin

# For system installation
python3 -c "import sysconfig; print(sysconfig.get_path('scripts'))"
```

### Check Current PATH

```bash
echo $PATH | tr ':' '\n' | nl
```

## System-Wide Installation (Alternative)

If you want system-wide installation (requires sudo):

```bash
sudo pip install -e .
# Scripts will be in /usr/local/bin (usually already in PATH)
```

