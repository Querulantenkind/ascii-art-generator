"""Composition system for combining multiple ASCII art elements."""

from typing import List, Tuple, Optional
from enum import Enum


class Alignment(Enum):
    """Alignment options for composition."""
    LEFT = 'left'
    CENTER = 'center'
    RIGHT = 'right'
    TOP = 'top'
    BOTTOM = 'bottom'


class Layer:
    """Represents a layer in ASCII art composition."""
    
    def __init__(self, content: str, x: int = 0, y: int = 0,
                 z_index: int = 0, opacity: float = 1.0):
        """Initialize layer.
        
        Args:
            content: ASCII art content
            x: X position
            y: Y position
            z_index: Z-index for layering
            opacity: Opacity (0.0-1.0)
        """
        self.content = content
        self.x = x
        self.y = y
        self.z_index = z_index
        self.opacity = opacity
        self.visible = True
    
    def get_lines(self) -> List[str]:
        """Get content as list of lines.
        
        Returns:
            List of lines
        """
        return self.content.split('\n')


class Composition:
    """Compose multiple ASCII art elements into a single output."""
    
    def __init__(self, width: int = 80, height: int = 40,
                 fill_char: str = ' '):
        """Initialize composition.
        
        Args:
            width: Canvas width
            height: Canvas height
            fill_char: Background fill character
        """
        self.width = width
        self.height = height
        self.fill_char = fill_char
        self.layers: List[Layer] = []
    
    def add_layer(self, content: str, x: int = 0, y: int = 0,
                  z_index: int = 0) -> Layer:
        """Add a layer to the composition.
        
        Args:
            content: ASCII art content
            x: X position
            y: Y position
            z_index: Z-index
            
        Returns:
            Created layer
        """
        layer = Layer(content, x, y, z_index)
        self.layers.append(layer)
        return layer
    
    def render(self) -> str:
        """Render the composition.
        
        Returns:
            Composed ASCII art
        """
        # Create canvas
        canvas = [[self.fill_char for _ in range(self.width)]
                  for _ in range(self.height)]
        
        # Sort layers by z-index
        sorted_layers = sorted(self.layers, key=lambda l: l.z_index)
        
        # Render each layer
        for layer in sorted_layers:
            if not layer.visible:
                continue
            
            lines = layer.get_lines()
            
            for i, line in enumerate(lines):
                y = layer.y + i
                
                if 0 <= y < self.height:
                    for j, char in enumerate(line):
                        x = layer.x + j
                        
                        if 0 <= x < self.width:
                            if char != ' ' or layer.opacity >= 1.0:
                                canvas[y][x] = char
        
        return '\n'.join([''.join(row) for row in canvas])
    
    def clear(self):
        """Clear all layers."""
        self.layers = []


class Compositor:
    """Advanced composition operations."""
    
    def __init__(self):
        """Initialize compositor."""
        pass
    
    def horizontal_concat(self, *arts: str, spacing: int = 2,
                         alignment: Alignment = Alignment.TOP) -> str:
        """Concatenate ASCII arts horizontally.
        
        Args:
            *arts: ASCII art strings to concatenate
            spacing: Space between elements
            alignment: Vertical alignment
            
        Returns:
            Concatenated ASCII art
        """
        if not arts:
            return ''
        
        # Split into lines
        all_lines = [art.split('\n') for art in arts]
        
        # Find max height
        max_height = max(len(lines) for lines in all_lines)
        
        # Pad lines based on alignment
        padded_lines = []
        for lines in all_lines:
            width = max(len(line) for line in lines) if lines else 0
            
            if alignment == Alignment.TOP:
                padded = lines + [' ' * width] * (max_height - len(lines))
            elif alignment == Alignment.BOTTOM:
                padded = [' ' * width] * (max_height - len(lines)) + lines
            else:  # CENTER
                top_pad = (max_height - len(lines)) // 2
                bottom_pad = max_height - len(lines) - top_pad
                padded = [' ' * width] * top_pad + lines + [' ' * width] * bottom_pad
            
            # Ensure all lines have same width
            padded = [line.ljust(width) for line in padded]
            padded_lines.append(padded)
        
        # Concatenate horizontally
        result = []
        for i in range(max_height):
            line = (' ' * spacing).join([lines[i] for lines in padded_lines])
            result.append(line)
        
        return '\n'.join(result)
    
    def vertical_concat(self, *arts: str, spacing: int = 1,
                       alignment: Alignment = Alignment.LEFT) -> str:
        """Concatenate ASCII arts vertically.
        
        Args:
            *arts: ASCII art strings to concatenate
            spacing: Space between elements
            alignment: Horizontal alignment
            
        Returns:
            Concatenated ASCII art
        """
        if not arts:
            return ''
        
        # Find max width
        all_lines = [art.split('\n') for art in arts]
        max_width = max(
            max(len(line) for line in lines) if lines else 0
            for lines in all_lines
        )
        
        result = []
        
        for i, lines in enumerate(all_lines):
            # Add lines with alignment
            for line in lines:
                if alignment == Alignment.LEFT:
                    result.append(line.ljust(max_width))
                elif alignment == Alignment.RIGHT:
                    result.append(line.rjust(max_width))
                else:  # CENTER
                    padding = (max_width - len(line)) // 2
                    result.append(' ' * padding + line)
            
            # Add spacing (except after last element)
            if i < len(all_lines) - 1:
                result.extend([' ' * max_width] * spacing)
        
        return '\n'.join(result)
    
    def overlay(self, background: str, foreground: str,
                x: int = 0, y: int = 0, transparent_char: str = ' ') -> str:
        """Overlay one ASCII art on another.
        
        Args:
            background: Background ASCII art
            foreground: Foreground ASCII art
            x: X offset for foreground
            y: Y offset for foreground
            transparent_char: Character to treat as transparent
            
        Returns:
            Overlaid ASCII art
        """
        bg_lines = background.split('\n')
        fg_lines = foreground.split('\n')
        
        # Create mutable canvas
        canvas = [list(line) for line in bg_lines]
        
        # Overlay foreground
        for i, fg_line in enumerate(fg_lines):
            canvas_y = y + i
            
            if 0 <= canvas_y < len(canvas):
                for j, char in enumerate(fg_line):
                    canvas_x = x + j
                    
                    if 0 <= canvas_x < len(canvas[canvas_y]):
                        if char != transparent_char:
                            canvas[canvas_y][canvas_x] = char
        
        return '\n'.join([''.join(line) for line in canvas])
    
    def grid_layout(self, arts: List[str], cols: int,
                   cell_width: int = None, cell_height: int = None,
                   spacing: int = 2) -> str:
        """Arrange ASCII arts in a grid layout.
        
        Args:
            arts: List of ASCII art strings
            cols: Number of columns
            cell_width: Width of each cell (auto if None)
            cell_height: Height of each cell (auto if None)
            spacing: Space between cells
            
        Returns:
            Grid layout ASCII art
        """
        if not arts:
            return ''
        
        rows = (len(arts) + cols - 1) // cols
        
        # Calculate cell dimensions if not provided
        if cell_width is None:
            cell_width = max(
                max(len(line) for line in art.split('\n'))
                for art in arts
            )
        
        if cell_height is None:
            cell_height = max(len(art.split('\n')) for art in arts)
        
        result = []
        
        for row in range(rows):
            # Collect arts for this row
            row_arts = []
            for col in range(cols):
                idx = row * cols + col
                if idx < len(arts):
                    row_arts.append(arts[idx])
                else:
                    row_arts.append(' ' * cell_width)
            
            # Pad each art to cell dimensions
            padded_row_arts = []
            for art in row_arts:
                lines = art.split('\n')
                
                # Pad height
                while len(lines) < cell_height:
                    lines.append('')
                
                # Pad width
                padded_lines = [line.ljust(cell_width) for line in lines]
                padded_row_arts.append('\n'.join(padded_lines))
            
            # Concatenate horizontally
            row_result = self.horizontal_concat(*padded_row_arts, spacing=spacing)
            result.append(row_result)
        
        # Join rows vertically
        return '\n'.join(result)
    
    def frame(self, content: str, title: str = '',
             style: str = 'double', padding: int = 1) -> str:
        """Add a frame around ASCII art.
        
        Args:
            content: ASCII art content
            title: Optional title
            style: Frame style
            padding: Internal padding
            
        Returns:
            Framed ASCII art
        """
        from generators.pattern_art import PatternGenerator
        from utils.config import Config
        
        lines = content.split('\n')
        
        if not lines:
            return ''
        
        max_width = max(len(line) for line in lines)
        
        # Add padding
        padded_lines = []
        for _ in range(padding):
            padded_lines.append(' ' * max_width)
        
        for line in lines:
            padded_lines.append(' ' * padding + line.ljust(max_width) + ' ' * padding)
        
        for _ in range(padding):
            padded_lines.append(' ' * max_width)
        
        # Create frame
        pattern_gen = PatternGenerator(Config())
        
        frame_width = max_width + padding * 2 + 2
        frame_height = len(padded_lines) + 2
        
        box_chars = pattern_gen.box_chars.get(style, pattern_gen.box_chars['double'])
        
        result = []
        
        # Top
        if title:
            top = box_chars['tl'] + box_chars['h'] * 2 + f' {title} '
            top += box_chars['h'] * (frame_width - len(title) - 5) + box_chars['tr']
            result.append(top)
        else:
            result.append(box_chars['tl'] + box_chars['h'] * (frame_width - 2) + box_chars['tr'])
        
        # Content
        for line in padded_lines:
            result.append(box_chars['v'] + line + box_chars['v'])
        
        # Bottom
        result.append(box_chars['bl'] + box_chars['h'] * (frame_width - 2) + box_chars['br'])
        
        return '\n'.join(result)
    
    def split_screen(self, left: str, right: str,
                    divider: str = '│') -> str:
        """Create split-screen layout.
        
        Args:
            left: Left side ASCII art
            right: Right side ASCII art
            divider: Divider character
            
        Returns:
            Split-screen ASCII art
        """
        left_lines = left.split('\n')
        right_lines = right.split('\n')
        
        max_height = max(len(left_lines), len(right_lines))
        left_width = max(len(line) for line in left_lines) if left_lines else 0
        right_width = max(len(line) for line in right_lines) if right_lines else 0
        
        # Pad lines
        left_padded = left_lines + [' ' * left_width] * (max_height - len(left_lines))
        right_padded = right_lines + [' ' * right_width] * (max_height - len(right_lines))
        
        result = []
        for i in range(max_height):
            left_line = left_padded[i].ljust(left_width)
            right_line = right_padded[i].ljust(right_width)
            result.append(f"{left_line} {divider} {right_line}")
        
        return '\n'.join(result)

