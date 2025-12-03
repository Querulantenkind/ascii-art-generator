#!/bin/bash
# Quick PATH setup script for ASCII Art Generator

SCRIPTS_DIR="$HOME/.local/bin"

echo "Setting up PATH for ASCII Art Generator..."
echo "Scripts directory: $SCRIPTS_DIR"

# Check if directory exists
if [ ! -d "$SCRIPTS_DIR" ]; then
    mkdir -p "$SCRIPTS_DIR"
    echo "Created directory: $SCRIPTS_DIR"
fi

# Detect shell and add to appropriate config file
if [ -n "$ZSH_VERSION" ]; then
    CONFIG_FILE="$HOME/.zshrc"
    SHELL_NAME="zsh"
elif [ -n "$BASH_VERSION" ]; then
    CONFIG_FILE="$HOME/.bashrc"
    SHELL_NAME="bash"
else
    CONFIG_FILE="$HOME/.profile"
    SHELL_NAME="sh"
fi

echo "Detected shell: $SHELL_NAME"
echo "Config file: $CONFIG_FILE"

# Add to PATH if not already there
if [ -f "$CONFIG_FILE" ] && grep -q "$SCRIPTS_DIR" "$CONFIG_FILE" 2>/dev/null; then
    echo "✓ PATH already configured in $CONFIG_FILE"
else
    echo "" >> "$CONFIG_FILE"
    echo "# Python user scripts directory" >> "$CONFIG_FILE"
    echo "export PATH=\"\$PATH:$SCRIPTS_DIR\"" >> "$CONFIG_FILE"
    echo "✓ Added $SCRIPTS_DIR to $CONFIG_FILE"
fi

# Show current PATH status
if echo $PATH | grep -q "$SCRIPTS_DIR"; then
    echo "✓ PATH is currently active"
else
    echo "⚠ PATH not active in current session"
    echo "  Run: source $CONFIG_FILE"
    echo "  Or open a new terminal"
fi

echo ""
echo "To verify installation, run:"
echo "  which ascii-art-generator"
echo "  ascii-art-generator --help"
