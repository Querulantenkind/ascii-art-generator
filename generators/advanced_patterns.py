"""Advanced pattern generators: spirals, fractals, mazes, and more."""

import math
import random
from typing import List, Tuple, Set


class AdvancedPatternGenerator:
    """Generator for complex ASCII patterns."""
    
    def __init__(self):
        """Initialize advanced pattern generator."""
        pass
    
    def generate_spiral(self, size: int = 20, clockwise: bool = True) -> str:
        """Generate spiral pattern.
        
        Args:
            size: Size of the spiral
            clockwise: Direction of spiral
            
        Returns:
            Spiral pattern string
        """
        # Create grid
        grid = [[' ' for _ in range(size)] for _ in range(size)]
        
        # Start from center
        x, y = size // 2, size // 2
        dx, dy = 1, 0
        steps = 1
        step_count = 0
        turn_count = 0
        
        chars = '*#@%+=:.-'
        char_idx = 0
        
        grid[y][x] = chars[char_idx % len(chars)]
        
        for _ in range(size * size):
            for _ in range(steps):
                x += dx
                y += dy
                
                if 0 <= x < size and 0 <= y < size:
                    char_idx += 1
                    grid[y][x] = chars[char_idx % len(chars)]
            
            # Turn
            if clockwise:
                dx, dy = -dy, dx
            else:
                dx, dy = dy, -dx
            
            turn_count += 1
            if turn_count % 2 == 0:
                steps += 1
        
        return '\n'.join([''.join(row) for row in grid])
    
    def generate_mandelbrot(self, width: int = 80, height: int = 40,
                           max_iter: int = 20) -> str:
        """Generate Mandelbrot set ASCII art.
        
        Args:
            width: Width of output
            height: Height of output
            max_iter: Maximum iterations
            
        Returns:
            Mandelbrot set pattern
        """
        chars = ' .:-=+*#%@'
        
        # Mandelbrot bounds
        x_min, x_max = -2.5, 1.0
        y_min, y_max = -1.0, 1.0
        
        lines = []
        
        for row in range(height):
            line = ''
            y = y_min + (y_max - y_min) * row / height
            
            for col in range(width):
                x = x_min + (x_max - x_min) * col / width
                
                # Calculate iterations
                c = complex(x, y)
                z = 0
                iterations = 0
                
                while abs(z) <= 2 and iterations < max_iter:
                    z = z * z + c
                    iterations += 1
                
                # Map to character
                if iterations == max_iter:
                    char = chars[-1]
                else:
                    char_idx = int(iterations / max_iter * (len(chars) - 1))
                    char = chars[char_idx]
                
                line += char
            
            lines.append(line)
        
        return '\n'.join(lines)
    
    def generate_julia_set(self, width: int = 80, height: int = 40,
                          c_real: float = -0.7, c_imag: float = 0.27015,
                          max_iter: int = 20) -> str:
        """Generate Julia set ASCII art.
        
        Args:
            width: Width of output
            height: Height of output
            c_real: Real part of constant c
            c_imag: Imaginary part of constant c
            max_iter: Maximum iterations
            
        Returns:
            Julia set pattern
        """
        chars = ' .:-=+*#%@'
        
        x_min, x_max = -1.5, 1.5
        y_min, y_max = -1.0, 1.0
        
        lines = []
        c = complex(c_real, c_imag)
        
        for row in range(height):
            line = ''
            y = y_min + (y_max - y_min) * row / height
            
            for col in range(width):
                x = x_min + (x_max - x_min) * col / width
                
                z = complex(x, y)
                iterations = 0
                
                while abs(z) <= 2 and iterations < max_iter:
                    z = z * z + c
                    iterations += 1
                
                if iterations == max_iter:
                    char = chars[-1]
                else:
                    char_idx = int(iterations / max_iter * (len(chars) - 1))
                    char = chars[char_idx]
                
                line += char
            
            lines.append(line)
        
        return '\n'.join(lines)
    
    def generate_maze(self, width: int = 40, height: int = 20) -> str:
        """Generate maze using recursive backtracking.
        
        Args:
            width: Width of maze (must be odd)
            height: Height of maze (must be odd)
            
        Returns:
            Maze pattern
        """
        # Ensure odd dimensions
        width = width if width % 2 == 1 else width + 1
        height = height if height % 2 == 1 else height + 1
        
        # Initialize grid (all walls)
        grid = [['█' for _ in range(width)] for _ in range(height)]
        
        # Recursive backtracking
        def carve_path(x: int, y: int):
            grid[y][x] = ' '
            
            # Directions: right, down, left, up
            directions = [(2, 0), (0, 2), (-2, 0), (0, -2)]
            random.shuffle(directions)
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < width and 0 <= ny < height and grid[ny][nx] == '█':
                    # Carve wall between
                    grid[y + dy // 2][x + dx // 2] = ' '
                    carve_path(nx, ny)
        
        # Start from (1, 1)
        carve_path(1, 1)
        
        # Add entrance and exit
        grid[0][1] = ' '
        grid[height - 1][width - 2] = ' '
        
        return '\n'.join([''.join(row) for row in grid])
    
    def generate_sierpinski_triangle(self, order: int = 5) -> str:
        """Generate Sierpinski triangle fractal.
        
        Args:
            order: Order of fractal (depth)
            
        Returns:
            Sierpinski triangle pattern
        """
        size = 2 ** order
        lines = []
        
        for y in range(size):
            line = ' ' * (size - y - 1)
            
            for x in range(y + 1):
                # Sierpinski condition
                if (x & y) == x:
                    line += '* '
                else:
                    line += '  '
            
            lines.append(line)
        
        return '\n'.join(lines)
    
    def generate_cellular_automaton(self, width: int = 80, height: int = 40,
                                   rule: int = 30) -> str:
        """Generate cellular automaton pattern (Rule 30, 90, 110, etc.).
        
        Args:
            width: Width of pattern
            height: Height of pattern (generations)
            rule: Rule number (0-255)
            
        Returns:
            Cellular automaton pattern
        """
        # Convert rule to binary lookup table
        rule_bin = format(rule, '08b')
        lookup = {format(i, '03b'): rule_bin[7 - i] for i in range(8)}
        
        # Initialize first row
        current = ['0'] * width
        current[width // 2] = '1'
        
        lines = []
        
        for _ in range(height):
            # Convert to display characters
            line = ''.join(['█' if c == '1' else ' ' for c in current])
            lines.append(line)
            
            # Generate next generation
            next_gen = []
            for i in range(width):
                left = current[i - 1] if i > 0 else '0'
                center = current[i]
                right = current[i + 1] if i < width - 1 else '0'
                
                pattern = left + center + right
                next_gen.append(lookup[pattern])
            
            current = next_gen
        
        return '\n'.join(lines)
    
    def generate_lissajous(self, width: int = 60, height: int = 30,
                          a: int = 3, b: int = 4, delta: float = math.pi / 2) -> str:
        """Generate Lissajous curve.
        
        Args:
            width: Width of canvas
            height: Height of canvas
            a, b: Frequency parameters
            delta: Phase shift
            
        Returns:
            Lissajous curve pattern
        """
        grid = [[' ' for _ in range(width)] for _ in range(height)]
        
        steps = 1000
        
        for i in range(steps):
            t = i / steps * 2 * math.pi
            
            x = math.sin(a * t + delta)
            y = math.sin(b * t)
            
            # Map to grid coordinates
            grid_x = int((x + 1) / 2 * (width - 1))
            grid_y = int((y + 1) / 2 * (height - 1))
            
            if 0 <= grid_x < width and 0 <= grid_y < height:
                grid[grid_y][grid_x] = '*'
        
        return '\n'.join([''.join(row) for row in grid])
    
    def generate_tree(self, height: int = 15, style: str = 'pine') -> str:
        """Generate ASCII tree.
        
        Args:
            height: Height of tree
            style: Tree style ('pine', 'oak', 'palm')
            
        Returns:
            Tree pattern
        """
        if style == 'pine':
            return self._generate_pine_tree(height)
        elif style == 'oak':
            return self._generate_oak_tree(height)
        elif style == 'palm':
            return self._generate_palm_tree(height)
        else:
            return self._generate_pine_tree(height)
    
    def _generate_pine_tree(self, height: int) -> str:
        """Generate pine tree."""
        lines = []
        max_width = height * 2 + 1
        
        # Star on top
        lines.append(' ' * (max_width // 2) + '*')
        
        # Tree layers
        for i in range(height):
            width = i * 2 + 1
            padding = (max_width - width) // 2
            line = ' ' * padding + '/' + '*' * (width - 2) + '\\'
            lines.append(line)
        
        # Trunk
        trunk_width = max(3, height // 3)
        trunk_height = max(2, height // 5)
        trunk_padding = (max_width - trunk_width) // 2
        
        for _ in range(trunk_height):
            lines.append(' ' * trunk_padding + '|' * trunk_width)
        
        return '\n'.join(lines)
    
    def _generate_oak_tree(self, height: int) -> str:
        """Generate oak tree."""
        lines = []
        max_width = height * 3
        
        # Canopy
        for i in range(height // 2):
            width = (i + 1) * 4
            padding = (max_width - width) // 2
            line = ' ' * padding + '@' * width
            lines.append(line)
        
        # Trunk
        trunk_width = max(3, height // 4)
        trunk_height = height // 2
        trunk_padding = (max_width - trunk_width) // 2
        
        for _ in range(trunk_height):
            lines.append(' ' * trunk_padding + '|' * trunk_width)
        
        return '\n'.join(lines)
    
    def _generate_palm_tree(self, height: int) -> str:
        """Generate palm tree."""
        lines = []
        max_width = height * 2
        
        # Fronds
        frond_lines = [
            '    \\|/',
            '   \\\\|//',
            '  \\\\\\|///',
        ]
        
        for line in frond_lines:
            padding = (max_width - len(line)) // 2
            lines.append(' ' * padding + line)
        
        # Trunk (curved)
        trunk_height = height
        center = max_width // 2
        
        for i in range(trunk_height):
            offset = int(math.sin(i / 3) * 2)
            pos = center + offset
            line = ' ' * pos + '|'
            lines.append(line)
        
        return '\n'.join(lines)

