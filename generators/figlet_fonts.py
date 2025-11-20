"""FIGlet font loader and renderer for ASCII art.

This module provides support for loading and rendering FIGlet fonts,
which are industry-standard ASCII art fonts with extensive character sets.
"""

import os
import re
from typing import Dict, List, Optional, Tuple


class FIGletFont:
    """FIGlet font parser and renderer."""
    
    def __init__(self, font_data: str = None, font_name: str = None):
        """Initialize FIGlet font.
        
        Args:
            font_data: Raw font file content
            font_name: Name of built-in font to use
        """
        self.height = 0
        self.baseline = 0
        self.max_length = 0
        self.comment_lines = 0
        self.hardblank = '$'
        self.chars = {}
        
        if font_data:
            self._parse_font(font_data)
        elif font_name:
            self._load_builtin_font(font_name)
    
    def _parse_font(self, font_data: str):
        """Parse FIGlet font file format.
        
        Args:
            font_data: Font file content
        """
        lines = font_data.split('\n')
        
        # Parse header line
        header = lines[0]
        if header.startswith('flf2a'):
            parts = header.split()
            self.hardblank = header[5]
            self.height = int(parts[1]) if len(parts) > 1 else 0
            self.baseline = int(parts[2]) if len(parts) > 2 else 0
            self.max_length = int(parts[3]) if len(parts) > 3 else 0
            self.comment_lines = int(parts[5]) if len(parts) > 5 else 0
        
        # Skip comment lines
        current_line = 1 + self.comment_lines
        
        # Parse characters (ASCII 32-126 are required)
        for ascii_code in range(32, 127):
            char_lines = []
            for i in range(self.height):
                if current_line < len(lines):
                    line = lines[current_line]
                    # Remove end markers (@ or @@)
                    line = re.sub(r'[@]{1,2}$', '', line)
                    # Replace hardblank with space
                    line = line.replace(self.hardblank, ' ')
                    char_lines.append(line)
                    current_line += 1
            
            if char_lines:
                self.chars[chr(ascii_code)] = char_lines
    
    def _load_builtin_font(self, font_name: str):
        """Load a built-in simplified FIGlet-style font.
        
        Args:
            font_name: Name of the font
        """
        # Built-in mini FIGlet fonts
        if font_name == 'mini':
            self.height = 1
            self.chars = {chr(i): [chr(i)] for i in range(32, 127)}
        
        elif font_name == 'term':
            self.height = 3
            # Simple 3-line font
            for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                self.chars[char] = [
                    f' {char} ',
                    f'/{char}\\',
                    '   '
                ]
            self.chars[' '] = ['   ', '   ', '   ']
    
    def render(self, text: str, width: Optional[int] = None) -> str:
        """Render text using this FIGlet font.
        
        Args:
            text: Text to render
            width: Maximum width (optional)
            
        Returns:
            Rendered ASCII art
        """
        if not self.chars:
            return text
        
        lines = [''] * self.height
        
        for char in text:
            if char == '\n':
                # Handle newlines
                result = '\n'.join(lines)
                lines = [''] * self.height
                return result
            
            char_lines = self.chars.get(char, self.chars.get(' ', [' '] * self.height))
            
            for i in range(self.height):
                if i < len(char_lines):
                    lines[i] += char_lines[i]
        
        result = '\n'.join(lines)
        
        if width:
            result = self._wrap(result, width)
        
        return result
    
    def _wrap(self, text: str, width: int) -> str:
        """Wrap text to specified width.
        
        Args:
            text: Text to wrap
            width: Maximum width
            
        Returns:
            Wrapped text
        """
        lines = text.split('\n')
        wrapped = []
        
        for line in lines:
            if len(line) <= width:
                wrapped.append(line)
            else:
                wrapped.append(line[:width])
        
        return '\n'.join(wrapped)


class FIGletFontManager:
    """Manager for FIGlet fonts."""
    
    def __init__(self):
        """Initialize font manager."""
        self.fonts: Dict[str, FIGletFont] = {}
        self._load_builtin_fonts()
    
    def _load_builtin_fonts(self):
        """Load built-in fonts."""
        # Mini font
        self.fonts['mini'] = FIGletFont(font_name='mini')
        
        # Term font
        self.fonts['term'] = FIGletFont(font_name='term')
        
        # Add more built-in fonts here
        self._add_larry3d_font()
        self._add_doom_font()
    
    def _add_larry3d_font(self):
        """Add Larry3D-style font."""
        font_data = """flf2a$ 8 6 15 0 2
Larry3D-style font
$$
  $$
  $$
  $$
  $$
  $$
  $$
  $$
"""
        # This is a simplified version - in production, you'd load actual FIGlet files
        self.fonts['larry3d'] = FIGletFont(font_name='term')
    
    def _add_doom_font(self):
        """Add DOOM-style font."""
        # Simplified DOOM-style font
        self.fonts['doom'] = FIGletFont(font_name='term')
    
    def get_font(self, name: str) -> Optional[FIGletFont]:
        """Get font by name.
        
        Args:
            name: Font name
            
        Returns:
            FIGlet font or None
        """
        return self.fonts.get(name)
    
    def list_fonts(self) -> List[str]:
        """Get list of available fonts.
        
        Returns:
            List of font names
        """
        return list(self.fonts.keys())
    
    def load_font_file(self, path: str, name: str):
        """Load a FIGlet font from file.
        
        Args:
            path: Path to .flf file
            name: Name to register font as
        """
        try:
            with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                font_data = f.read()
            
            self.fonts[name] = FIGletFont(font_data=font_data)
        except Exception as e:
            print(f"Error loading font {name}: {e}")

