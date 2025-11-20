"""Clipboard integration for easy copy/paste of ASCII art."""

import subprocess
import sys
import os
from typing import Optional, Dict, Tuple


class ClipboardManager:
    """Manage clipboard operations for ASCII art."""
    
    def __init__(self):
        """Initialize clipboard manager."""
        self.platform = sys.platform
        self._detect_clipboard_tool()
    
    def _detect_clipboard_tool(self):
        """Detect available clipboard tool."""
        self.clipboard_tool = None
        
        if self.platform == 'darwin':  # macOS
            self.clipboard_tool = 'pbcopy'
        elif self.platform == 'win32':  # Windows
            self.clipboard_tool = 'clip'
        else:  # Linux/Unix
            # Try to find available tool
            for tool in ['xclip', 'xsel', 'wl-copy']:
                if self._command_exists(tool):
                    self.clipboard_tool = tool
                    break
    
    def _command_exists(self, command: str) -> bool:
        """Check if command exists.
        
        Args:
            command: Command name
            
        Returns:
            True if command exists
        """
        try:
            subprocess.run(
                ['which', command],
                capture_output=True,
                check=True
            )
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            return False
    
    def copy(self, text: str) -> bool:
        """Copy text to clipboard.
        
        Args:
            text: Text to copy
            
        Returns:
            True if successful
        """
        if not self.clipboard_tool:
            print("⚠ No clipboard tool detected. Install xclip, xsel, or wl-copy")
            return False
        
        try:
            if self.platform == 'darwin':
                # macOS
                process = subprocess.Popen(
                    ['pbcopy'],
                    stdin=subprocess.PIPE
                )
                process.communicate(text.encode('utf-8'))
                return process.returncode == 0
            
            elif self.platform == 'win32':
                # Windows
                process = subprocess.Popen(
                    ['clip'],
                    stdin=subprocess.PIPE,
                    shell=True
                )
                process.communicate(text.encode('utf-16'))
                return process.returncode == 0
            
            else:
                # Linux/Unix
                if self.clipboard_tool == 'xclip':
                    process = subprocess.Popen(
                        ['xclip', '-selection', 'clipboard'],
                        stdin=subprocess.PIPE
                    )
                    process.communicate(text.encode('utf-8'))
                    return process.returncode == 0
                
                elif self.clipboard_tool == 'xsel':
                    process = subprocess.Popen(
                        ['xsel', '--clipboard', '--input'],
                        stdin=subprocess.PIPE
                    )
                    process.communicate(text.encode('utf-8'))
                    return process.returncode == 0
                
                elif self.clipboard_tool == 'wl-copy':
                    process = subprocess.Popen(
                        ['wl-copy'],
                        stdin=subprocess.PIPE
                    )
                    process.communicate(text.encode('utf-8'))
                    return process.returncode == 0
        
        except Exception as e:
            print(f"Error copying to clipboard: {e}")
            return False
        
        return False
    
    def paste(self) -> Optional[str]:
        """Paste text from clipboard.
        
        Returns:
            Clipboard text or None
        """
        if not self.clipboard_tool:
            print("⚠ No clipboard tool detected")
            return None
        
        try:
            if self.platform == 'darwin':
                # macOS
                result = subprocess.run(
                    ['pbpaste'],
                    capture_output=True,
                    text=True
                )
                return result.stdout if result.returncode == 0 else None
            
            elif self.platform == 'win32':
                # Windows - using PowerShell
                result = subprocess.run(
                    ['powershell', '-command', 'Get-Clipboard'],
                    capture_output=True,
                    text=True
                )
                return result.stdout if result.returncode == 0 else None
            
            else:
                # Linux/Unix
                if self.clipboard_tool == 'xclip':
                    result = subprocess.run(
                        ['xclip', '-selection', 'clipboard', '-o'],
                        capture_output=True,
                        text=True
                    )
                    return result.stdout if result.returncode == 0 else None
                
                elif self.clipboard_tool == 'xsel':
                    result = subprocess.run(
                        ['xsel', '--clipboard', '--output'],
                        capture_output=True,
                        text=True
                    )
                    return result.stdout if result.returncode == 0 else None
                
                elif self.clipboard_tool == 'wl-paste':
                    result = subprocess.run(
                        ['wl-paste'],
                        capture_output=True,
                        text=True
                    )
                    return result.stdout if result.returncode == 0 else None
        
        except Exception as e:
            print(f"Error pasting from clipboard: {e}")
            return None
        
        return None
    
    def copy_with_confirmation(self, text: str, label: str = "ASCII art") -> bool:
        """Copy text with user confirmation.
        
        Args:
            text: Text to copy
            label: Description of content
            
        Returns:
            True if successful
        """
        success = self.copy(text)
        
        if success:
            print(f"✓ {label} copied to clipboard!")
        else:
            print(f"✗ Failed to copy {label} to clipboard")
            print("\nYou can manually copy the output above.")
        
        return success
    
    def get_clipboard_info(self) -> Dict[str, any]:
        """Get clipboard system information.
        
        Returns:
            Dictionary with clipboard info
        """
        return {
            'platform': self.platform,
            'tool': self.clipboard_tool,
            'available': self.clipboard_tool is not None,
            'can_copy': self.clipboard_tool is not None,
            'can_paste': self.clipboard_tool is not None
        }
    
    def install_instructions(self) -> str:
        """Get installation instructions for clipboard tools.
        
        Returns:
            Installation instructions
        """
        if self.platform == 'darwin':
            return "Clipboard support is built-in on macOS (pbcopy/pbpaste)"
        
        elif self.platform == 'win32':
            return "Clipboard support is built-in on Windows (clip)"
        
        else:  # Linux/Unix
            return """
Clipboard support requires one of the following tools:

For X11 (most Linux):
  sudo apt install xclip    # Debian/Ubuntu
  sudo dnf install xclip    # Fedora
  sudo pacman -S xclip      # Arch

  OR

  sudo apt install xsel     # Alternative

For Wayland:
  sudo apt install wl-clipboard
  sudo dnf install wl-clipboard
  sudo pacman -S wl-clipboard

After installation, restart the application.
""".strip()


class ClipboardHelper:
    """Helper functions for clipboard operations."""
    
    def __init__(self):
        """Initialize clipboard helper."""
        self.manager = ClipboardManager()
    
    def quick_copy(self, text: str, show_preview: bool = True,
                  preview_lines: int = 5) -> bool:
        """Quick copy with optional preview.
        
        Args:
            text: Text to copy
            show_preview: Show preview before copying
            preview_lines: Number of preview lines
            
        Returns:
            True if successful
        """
        if show_preview:
            lines = text.split('\n')
            preview = '\n'.join(lines[:preview_lines])
            
            if len(lines) > preview_lines:
                preview += f"\n... ({len(lines) - preview_lines} more lines)"
            
            print("Preview:")
            print(preview)
            print()
        
        return self.manager.copy_with_confirmation(text)
    
    def copy_and_save(self, text: str, filename: str) -> Tuple[bool, bool]:
        """Copy to clipboard and save to file.
        
        Args:
            text: Text to copy and save
            filename: Output filename
            
        Returns:
            Tuple of (copy_success, save_success)
        """
        # Copy to clipboard
        copy_success = self.manager.copy(text)
        
        # Save to file
        save_success = False
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(text)
            save_success = True
            print(f"✓ Saved to {filename}")
        except Exception as e:
            print(f"✗ Failed to save: {e}")
        
        if copy_success:
            print("✓ Copied to clipboard")
        
        return copy_success, save_success
    
    def interactive_copy(self, text: str) -> bool:
        """Interactive copy with user prompt.
        
        Args:
            text: Text to copy
            
        Returns:
            True if user chose to copy
        """
        response = input("\nCopy to clipboard? (y/n): ").strip().lower()
        
        if response == 'y':
            return self.manager.copy_with_confirmation(text)
        
        return False

