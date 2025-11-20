"""Text effects for ASCII art: shadows, outlines, 3D effects, and more."""

from typing import List, Tuple, Optional


class TextEffects:
    """Apply various effects to ASCII art text."""
    
    def __init__(self):
        """Initialize text effects."""
        pass
    
    def add_shadow(self, text: str, direction: str = 'bottom-right',
                   shadow_char: str = '░') -> str:
        """Add shadow effect to ASCII art.
        
        Args:
            text: Input ASCII art
            direction: Shadow direction ('bottom-right', 'bottom', 'right')
            shadow_char: Character to use for shadow
            
        Returns:
            ASCII art with shadow
        """
        lines = text.split('\n')
        
        if direction == 'bottom-right':
            # Add shadow to bottom and right
            result = []
            
            for line in lines:
                result.append(line + shadow_char)
            
            # Add bottom shadow line
            if lines:
                shadow_line = shadow_char * (len(lines[0]) + 1)
                result.append(shadow_line)
            
            return '\n'.join(result)
        
        elif direction == 'bottom':
            result = lines.copy()
            if lines:
                shadow_line = shadow_char * len(lines[0])
                result.append(shadow_line)
            return '\n'.join(result)
        
        elif direction == 'right':
            result = [line + shadow_char for line in lines]
            return '\n'.join(result)
        
        return text
    
    def add_outline(self, text: str, outline_char: str = '#',
                   thickness: int = 1) -> str:
        """Add outline around ASCII art.
        
        Args:
            text: Input ASCII art
            outline_char: Character for outline
            thickness: Outline thickness
            
        Returns:
            ASCII art with outline
        """
        lines = text.split('\n')
        
        if not lines:
            return text
        
        max_width = max(len(line) for line in lines) if lines else 0
        
        # Pad lines to same width
        padded_lines = [line.ljust(max_width) for line in lines]
        
        # Add outline
        result = []
        
        # Top border
        for _ in range(thickness):
            result.append(outline_char * (max_width + 2 * thickness))
        
        # Content with side borders
        for line in padded_lines:
            bordered_line = (outline_char * thickness) + line + (outline_char * thickness)
            result.append(bordered_line)
        
        # Bottom border
        for _ in range(thickness):
            result.append(outline_char * (max_width + 2 * thickness))
        
        return '\n'.join(result)
    
    def add_3d_effect(self, text: str, depth: int = 3,
                     direction: str = 'right') -> str:
        """Add 3D depth effect to ASCII art.
        
        Args:
            text: Input ASCII art
            depth: Depth of 3D effect
            direction: Direction of depth ('right', 'left', 'down', 'up')
            
        Returns:
            ASCII art with 3D effect
        """
        lines = text.split('\n')
        
        if direction == 'right':
            result = []
            for i, line in enumerate(lines):
                offset = min(i, depth)
                result.append(' ' * offset + line)
            return '\n'.join(result)
        
        elif direction == 'left':
            result = []
            max_offset = min(len(lines), depth)
            for i, line in enumerate(lines):
                offset = max_offset - min(i, depth)
                result.append(' ' * offset + line)
            return '\n'.join(result)
        
        elif direction == 'down':
            result = lines.copy()
            for i in range(1, min(depth + 1, len(lines))):
                result.append(lines[-1])
            return '\n'.join(result)
        
        return text
    
    def add_double_vision(self, text: str, offset: int = 3,
                         char1: str = None, char2: str = None) -> str:
        """Add double vision/glitch effect.
        
        Args:
            text: Input ASCII art
            offset: Horizontal offset between copies
            char1: Character for first copy (None = original)
            char2: Character for second copy (None = original)
            
        Returns:
            ASCII art with double vision effect
        """
        lines = text.split('\n')
        result = []
        
        for line in lines:
            # Create offset version
            offset_line = ' ' * offset + line
            
            # Merge lines
            merged = list(offset_line)
            for i, char in enumerate(line):
                if char != ' ' and i < len(merged):
                    if merged[i] == ' ':
                        merged[i] = char if char1 is None else char1
                    else:
                        merged[i] = char if char2 is None else char2
            
            result.append(''.join(merged))
        
        return '\n'.join(result)
    
    def add_mirror(self, text: str, axis: str = 'vertical') -> str:
        """Add mirror effect.
        
        Args:
            text: Input ASCII art
            axis: Mirror axis ('vertical', 'horizontal')
            
        Returns:
            Mirrored ASCII art
        """
        lines = text.split('\n')
        
        if axis == 'vertical':
            # Mirror horizontally
            result = []
            for line in lines:
                mirrored = line + '|' + line[::-1]
                result.append(mirrored)
            return '\n'.join(result)
        
        elif axis == 'horizontal':
            # Mirror vertically
            separator = '-' * len(lines[0]) if lines else ''
            mirrored_lines = lines[::-1]
            return '\n'.join(lines + [separator] + mirrored_lines)
        
        return text
    
    def add_glow(self, text: str, intensity: int = 2) -> str:
        """Add glow effect around characters.
        
        Args:
            text: Input ASCII art
            intensity: Glow intensity (radius)
            
        Returns:
            ASCII art with glow effect
        """
        lines = text.split('\n')
        
        if not lines:
            return text
        
        height = len(lines)
        width = max(len(line) for line in lines) if lines else 0
        
        # Create grid
        grid = [[' ' for _ in range(width + intensity * 2)] 
                for _ in range(height + intensity * 2)]
        
        # Place original text
        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                if char != ' ':
                    grid[y + intensity][x + intensity] = char
                    
                    # Add glow around it
                    for dy in range(-intensity, intensity + 1):
                        for dx in range(-intensity, intensity + 1):
                            ny, nx = y + intensity + dy, x + intensity + dx
                            if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]):
                                if grid[ny][nx] == ' ':
                                    distance = abs(dx) + abs(dy)
                                    if distance <= intensity:
                                        grid[ny][nx] = '·' if distance == intensity else '∙'
        
        return '\n'.join([''.join(row) for row in grid])
    
    def add_wave_distortion(self, text: str, amplitude: int = 2,
                           frequency: float = 0.5) -> str:
        """Add wave distortion effect.
        
        Args:
            text: Input ASCII art
            amplitude: Wave amplitude
            frequency: Wave frequency
            
        Returns:
            Distorted ASCII art
        """
        import math
        
        lines = text.split('\n')
        result = []
        
        for i, line in enumerate(lines):
            offset = int(amplitude * math.sin(i * frequency))
            distorted = ' ' * abs(offset) + line if offset >= 0 else line
            result.append(distorted)
        
        return '\n'.join(result)
    
    def add_perspective(self, text: str, vanishing_point: str = 'bottom') -> str:
        """Add perspective effect.
        
        Args:
            text: Input ASCII art
            vanishing_point: Vanishing point location ('bottom', 'top')
            
        Returns:
            ASCII art with perspective
        """
        lines = text.split('\n')
        result = []
        
        total_lines = len(lines)
        
        for i, line in enumerate(lines):
            if vanishing_point == 'bottom':
                scale = 1 - (i / total_lines) * 0.5
            else:
                scale = 0.5 + (i / total_lines) * 0.5
            
            new_length = max(1, int(len(line) * scale))
            
            if new_length < len(line):
                # Compress line
                step = len(line) / new_length
                compressed = ''.join([line[int(j * step)] for j in range(new_length)])
                result.append(compressed)
            else:
                result.append(line)
        
        return '\n'.join(result)
    
    def add_emboss(self, text: str) -> str:
        """Add emboss effect.
        
        Args:
            text: Input ASCII art
            
        Returns:
            Embossed ASCII art
        """
        lines = text.split('\n')
        result = []
        
        for i, line in enumerate(lines):
            embossed = ''
            for j, char in enumerate(line):
                if char != ' ':
                    # Add highlight and shadow
                    if j > 0 and line[j-1] == ' ':
                        embossed += '▓'
                    elif j < len(line) - 1 and line[j+1] == ' ':
                        embossed += '░'
                    else:
                        embossed += char
                else:
                    embossed += char
            result.append(embossed)
        
        return '\n'.join(result)
    
    def add_neon(self, text: str) -> str:
        """Add neon sign effect.
        
        Args:
            text: Input ASCII art
            
        Returns:
            Neon-style ASCII art
        """
        lines = text.split('\n')
        result = []
        
        for line in lines:
            neon = ''
            for char in line:
                if char != ' ':
                    # Replace with neon-style characters
                    neon += '█'
                else:
                    neon += ' '
            result.append(neon)
        
        return '\n'.join(result)
    
    def add_ascii_border_art(self, text: str, style: str = 'stars') -> str:
        """Add decorative border with ASCII art.
        
        Args:
            text: Input text
            style: Border style ('stars', 'flowers', 'arrows')
            
        Returns:
            Text with decorative border
        """
        lines = text.split('\n')
        
        if not lines:
            return text
        
        max_width = max(len(line) for line in lines)
        
        if style == 'stars':
            top_bottom = '* ' * ((max_width + 4) // 2)
            side = '* '
        elif style == 'flowers':
            top_bottom = '❀ ' * ((max_width + 4) // 2)
            side = '❀ '
        elif style == 'arrows':
            top_bottom = '» ' * ((max_width + 4) // 2)
            side = '» '
        else:
            top_bottom = '* ' * ((max_width + 4) // 2)
            side = '* '
        
        result = [top_bottom]
        
        for line in lines:
            result.append(side + line.ljust(max_width) + ' ' + side.strip())
        
        result.append(top_bottom)
        
        return '\n'.join(result)

