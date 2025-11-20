"""Pattern and border generator for ASCII art."""

from typing import Optional


class PatternGenerator:
    """Generator for creating ASCII patterns, borders, and decorative elements."""
    
    def __init__(self, config):
        """Initialize pattern generator.
        
        Args:
            config: Configuration object
        """
        self.config = config
        self.box_chars = {
            'single': {
                'tl': '┌', 'tr': '┐', 'bl': '└', 'br': '┘',
                'h': '─', 'v': '│', 'cross': '┼',
                'lt': '├', 'rt': '┤', 'tt': '┬', 'bt': '┴'
            },
            'double': {
                'tl': '╔', 'tr': '╗', 'bl': '╚', 'br': '╝',
                'h': '═', 'v': '║', 'cross': '╬',
                'lt': '╠', 'rt': '╣', 'tt': '╦', 'bt': '╩'
            },
            'thick': {
                'tl': '┏', 'tr': '┓', 'bl': '┗', 'br': '┛',
                'h': '━', 'v': '┃', 'cross': '╋',
                'lt': '┣', 'rt': '┫', 'tt': '┳', 'bt': '┻'
            },
            'ascii': {
                'tl': '+', 'tr': '+', 'bl': '+', 'br': '+',
                'h': '-', 'v': '|', 'cross': '+',
                'lt': '+', 'rt': '+', 'tt': '+', 'bt': '+'
            }
        }
    
    def generate(self, pattern_type: str, width: int = 60, height: int = 10,
                 style: str = 'single', **kwargs) -> str:
        """Generate ASCII pattern.
        
        Args:
            pattern_type: Type of pattern (box, border, line, diamond, wave)
            width: Width of pattern
            height: Height of pattern
            style: Border style (single, double, thick, ascii)
            **kwargs: Additional pattern-specific parameters
            
        Returns:
            ASCII art pattern string
        """
        if pattern_type == 'box':
            return self.generate_box(width, height, style)
        elif pattern_type == 'border':
            return self.generate_border(width, style)
        elif pattern_type == 'line':
            return self.generate_line(width, style, kwargs.get('line_type', 'horizontal'))
        elif pattern_type == 'diamond':
            return self.generate_diamond(width, height)
        elif pattern_type == 'wave':
            return self.generate_wave(width, height)
        else:
            return f"Unknown pattern type: {pattern_type}"
    
    def generate_box(self, width: int, height: int, style: str = 'single') -> str:
        """Generate a box pattern.
        
        Args:
            width: Width of box
            height: Height of box
            style: Border style
            
        Returns:
            Box pattern string
        """
        chars = self.box_chars.get(style, self.box_chars['single'])
        
        lines = []
        
        # Top line
        lines.append(chars['tl'] + chars['h'] * (width - 2) + chars['tr'])
        
        # Middle lines
        for _ in range(height - 2):
            lines.append(chars['v'] + ' ' * (width - 2) + chars['v'])
        
        # Bottom line
        lines.append(chars['bl'] + chars['h'] * (width - 2) + chars['br'])
        
        return '\n'.join(lines)
    
    def generate_border(self, width: int, style: str = 'single') -> str:
        """Generate a decorative border.
        
        Args:
            width: Width of border
            style: Border style
            
        Returns:
            Border string
        """
        chars = self.box_chars.get(style, self.box_chars['single'])
        
        lines = []
        
        # Top border
        lines.append(chars['tl'] + chars['h'] * (width - 2) + chars['tr'])
        lines.append(chars['v'] + ' ' * (width - 2) + chars['v'])
        
        # Title area
        title_line = chars['lt'] + chars['h'] * (width - 2) + chars['rt']
        lines.append(title_line)
        
        lines.append(chars['v'] + ' ' * (width - 2) + chars['v'])
        lines.append(chars['bl'] + chars['h'] * (width - 2) + chars['br'])
        
        return '\n'.join(lines)
    
    def generate_line(self, width: int, style: str = 'single',
                     line_type: str = 'horizontal') -> str:
        """Generate a line.
        
        Args:
            width: Width of line
            style: Line style
            line_type: 'horizontal' or 'vertical'
            
        Returns:
            Line string
        """
        chars = self.box_chars.get(style, self.box_chars['single'])
        
        if line_type == 'horizontal':
            return chars['h'] * width
        else:
            return '\n'.join([chars['v']] * width)
    
    def generate_diamond(self, width: int, height: int) -> str:
        """Generate a diamond pattern.
        
        Args:
            width: Width of pattern
            height: Height of pattern
            
        Returns:
            Diamond pattern string
        """
        lines = []
        mid = height // 2
        
        for i in range(height):
            if i <= mid:
                # Expanding part
                spaces = mid - i
                stars = (i * 2) + 1
            else:
                # Contracting part
                spaces = i - mid
                stars = ((height - i - 1) * 2) + 1
            
            # Center the pattern
            total_width = spaces + stars
            padding = (width - total_width) // 2
            
            line = ' ' * padding + ' ' * spaces + '*' * stars
            lines.append(line)
        
        return '\n'.join(lines)
    
    def generate_wave(self, width: int, height: int) -> str:
        """Generate a wave pattern.
        
        Args:
            width: Width of pattern
            height: Height of pattern
            
        Returns:
            Wave pattern string
        """
        import math
        
        lines = []
        
        for y in range(height):
            line = ''
            for x in range(width):
                # Calculate wave position
                wave_y = int((height / 2) + (height / 4) * math.sin((x / width) * 4 * math.pi))
                
                if y == wave_y:
                    line += '~'
                else:
                    line += ' '
            
            lines.append(line)
        
        return '\n'.join(lines)
    
    def generate_grid(self, width: int, height: int, cell_width: int = 5,
                     cell_height: int = 3, style: str = 'single') -> str:
        """Generate a grid pattern.
        
        Args:
            width: Number of columns
            height: Number of rows
            cell_width: Width of each cell
            cell_height: Height of each cell
            style: Border style
            
        Returns:
            Grid pattern string
        """
        chars = self.box_chars.get(style, self.box_chars['single'])
        
        lines = []
        
        # Top border
        top_line = chars['tl']
        for i in range(width):
            top_line += chars['h'] * cell_width
            if i < width - 1:
                top_line += chars['tt']
        top_line += chars['tr']
        lines.append(top_line)
        
        # Rows
        for row in range(height):
            # Cell content lines
            for _ in range(cell_height):
                content_line = chars['v']
                for col in range(width):
                    content_line += ' ' * cell_width
                    content_line += chars['v']
                lines.append(content_line)
            
            # Horizontal separator (except after last row)
            if row < height - 1:
                sep_line = chars['lt']
                for i in range(width):
                    sep_line += chars['h'] * cell_width
                    if i < width - 1:
                        sep_line += chars['cross']
                sep_line += chars['rt']
                lines.append(sep_line)
        
        # Bottom border
        bottom_line = chars['bl']
        for i in range(width):
            bottom_line += chars['h'] * cell_width
            if i < width - 1:
                bottom_line += chars['bt']
        bottom_line += chars['br']
        lines.append(bottom_line)
        
        return '\n'.join(lines)
    
    def generate_banner(self, text: str, width: int, style: str = 'double') -> str:
        """Generate a banner with text.
        
        Args:
            text: Text to display in banner
            width: Width of banner
            style: Border style
            
        Returns:
            Banner string
        """
        chars = self.box_chars.get(style, self.box_chars['double'])
        
        lines = []
        
        # Top border
        lines.append(chars['tl'] + chars['h'] * (width - 2) + chars['tr'])
        
        # Empty line
        lines.append(chars['v'] + ' ' * (width - 2) + chars['v'])
        
        # Text line (centered)
        text_padding = (width - 2 - len(text)) // 2
        text_line = chars['v'] + ' ' * text_padding + text
        text_line += ' ' * (width - 2 - text_padding - len(text)) + chars['v']
        lines.append(text_line)
        
        # Empty line
        lines.append(chars['v'] + ' ' * (width - 2) + chars['v'])
        
        # Bottom border
        lines.append(chars['bl'] + chars['h'] * (width - 2) + chars['br'])
        
        return '\n'.join(lines)

