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
    
    def generate_voronoi(self, width: int = 80, height: int = 40, num_sites: int = 10) -> str:
        """Generate Voronoi diagram pattern.
        
        Args:
            width: Width of pattern
            height: Height of pattern
            num_sites: Number of Voronoi sites
            
        Returns:
            Voronoi diagram pattern
        """
        # Generate random sites
        sites = [(random.randint(0, width), random.randint(0, height)) 
                 for _ in range(num_sites)]
        
        chars = ' .:-=+*#%@'
        grid = [[' ' for _ in range(width)] for _ in range(height)]
        
        for y in range(height):
            for x in range(width):
                # Find closest site
                min_dist = float('inf')
                closest_site = 0
                
                for i, (sx, sy) in enumerate(sites):
                    dist = math.sqrt((x - sx)**2 + (y - sy)**2)
                    if dist < min_dist:
                        min_dist = dist
                        closest_site = i
                
                # Map distance to character
                max_dist = math.sqrt(width*width + height*height)
                char_idx = int((min_dist / max_dist) * (len(chars) - 1))
                grid[y][x] = chars[char_idx]
        
        return '\n'.join([''.join(row) for row in grid])
    
    def generate_perlin_noise(self, width: int = 80, height: int = 40,
                              scale: float = 0.1, octaves: int = 4) -> str:
        """Generate Perlin noise pattern.
        
        Args:
            width: Width of pattern
            height: Height of pattern
            scale: Noise scale (smaller = more detail)
            octaves: Number of octaves for fractal noise
            
        Returns:
            Perlin noise pattern
        """
        chars = ' .:-=+*#%@'
        
        def fade(t):
            return t * t * t * (t * (t * 6 - 15) + 10)
        
        def lerp(a, b, t):
            return a + t * (b - a)
        
        def grad(hash_val, x, y):
            h = hash_val & 3
            u = x if h & 2 == 0 else -x
            v = y if h & 1 == 0 else -y
            return u + v
        
        def noise(x, y):
            # Simple hash-based noise
            X = int(x) & 255
            Y = int(y) & 255
            
            xf = x - int(x)
            yf = y - int(y)
            
            u = fade(xf)
            v = fade(yf)
            
            # Hash coordinates
            a = (X + Y * 57) % 256
            b = ((X + 1) + Y * 57) % 256
            c = (X + (Y + 1) * 57) % 256
            d = ((X + 1) + (Y + 1) * 57) % 256
            
            return lerp(
                lerp(grad(a, xf, yf), grad(b, xf - 1, yf), u),
                lerp(grad(c, xf, yf - 1), grad(d, xf - 1, yf - 1), u),
                v
            )
        
        lines = []
        for y in range(height):
            line = ''
            for x in range(width):
                value = 0
                amplitude = 1
                frequency = scale
                
                for _ in range(octaves):
                    value += noise(x * frequency, y * frequency) * amplitude
                    amplitude *= 0.5
                    frequency *= 2
                
                # Normalize to 0-1
                value = (value + 1) / 2
                char_idx = int(value * (len(chars) - 1))
                line += chars[char_idx]
            
            lines.append(line)
        
        return '\n'.join(lines)
    
    def generate_reaction_diffusion(self, width: int = 80, height: int = 40,
                                    iterations: int = 50) -> str:
        """Generate reaction-diffusion pattern (Turing pattern).
        
        Args:
            width: Width of pattern
            height: Height of pattern
            iterations: Number of simulation iterations
            
        Returns:
            Reaction-diffusion pattern
        """
        # Initialize grids
        A = [[1.0 for _ in range(width)] for _ in range(height)]
        B = [[0.0 for _ in range(width)] for _ in range(height)]
        
        # Add initial seed
        center_y, center_x = height // 2, width // 2
        for y in range(max(0, center_y-5), min(height, center_y+5)):
            for x in range(max(0, center_x-5), min(width, center_x+5)):
                B[y][x] = 1.0
        
        # Parameters
        feed = 0.055
        kill = 0.062
        dt = 1.0
        Da = 1.0
        Db = 0.5
        
        chars = ' .:-=+*#%@'
        
        for _ in range(iterations):
            A_new = [row[:] for row in A]
            B_new = [row[:] for row in B]
            
            for y in range(1, height-1):
                for x in range(1, width-1):
                    # Laplacian (5-point stencil)
                    lapl_A = (A[y-1][x] + A[y+1][x] + A[y][x-1] + A[y][x+1] - 4*A[y][x]) * 0.2
                    lapl_B = (B[y-1][x] + B[y+1][x] + B[y][x-1] + B[y][x+1] - 4*B[y][x]) * 0.2
                    
                    # Reaction-diffusion equations
                    reaction = A[y][x] * B[y][x] * B[y][x]
                    A_new[y][x] = max(0, min(1, A[y][x] + (Da * lapl_A - reaction + feed * (1 - A[y][x])) * dt))
                    B_new[y][x] = max(0, min(1, B[y][x] + (Db * lapl_B + reaction - (kill + feed) * B[y][x]) * dt))
            
            A, B = A_new, B_new
        
        # Convert to ASCII
        lines = []
        for row in A:
            line = ''
            for val in row:
                char_idx = int(val * (len(chars) - 1))
                line += chars[char_idx]
            lines.append(line)
        
        return '\n'.join(lines)
    
    def generate_flow_field(self, width: int = 80, height: int = 40,
                           num_particles: int = 100, steps: int = 50) -> str:
        """Generate flow field pattern.
        
        Args:
            width: Width of pattern
            height: Height of pattern
            num_particles: Number of particles
            steps: Number of steps per particle
            
        Returns:
            Flow field pattern
        """
        grid = [[' ' for _ in range(width)] for _ in range(height)]
        
        # Create flow field using Perlin-like noise
        def flow_field(x, y):
            angle = math.sin(x * 0.1) * math.cos(y * 0.1) * math.pi * 2
            return math.cos(angle), math.sin(angle)
        
        # Trace particles
        for _ in range(num_particles):
            x = random.uniform(0, width)
            y = random.uniform(0, height)
            
            for _ in range(steps):
                ix, iy = int(x), int(y)
                
                if 0 <= ix < width and 0 <= iy < height:
                    if grid[iy][ix] == ' ':
                        grid[iy][ix] = '.'
                    elif grid[iy][ix] == '.':
                        grid[iy][ix] = ':'
                    elif grid[iy][ix] == ':':
                        grid[iy][ix] = '='
                    elif grid[iy][ix] == '=':
                        grid[iy][ix] = '+'
                    elif grid[iy][ix] == '+':
                        grid[iy][ix] = '*'
                
                # Move particle
                dx, dy = flow_field(x, y)
                x += dx * 0.5
                y += dy * 0.5
                
                # Wrap around
                x = x % width
                y = y % height
        
        return '\n'.join([''.join(row) for row in grid])
    
    def generate_parametric_curve(self, width: int = 80, height: int = 40,
                                  curve_type: str = 'butterfly') -> str:
        """Generate parametric curve pattern.
        
        Args:
            width: Width of pattern
            height: Height of pattern
            curve_type: Type of curve ('butterfly', 'rose', 'cardioid', 'lemniscate')
            
        Returns:
            Parametric curve pattern
        """
        grid = [[' ' for _ in range(width)] for _ in range(height)]
        
        steps = 2000
        
        for i in range(steps):
            t = i / steps * 2 * math.pi * 4
            
            if curve_type == 'butterfly':
                x = math.sin(t) * (math.exp(math.cos(t)) - 2 * math.cos(4*t) - math.sin(t/12)**5)
                y = math.cos(t) * (math.exp(math.cos(t)) - 2 * math.cos(4*t) - math.sin(t/12)**5)
            elif curve_type == 'rose':
                n = 5
                k = n
                x = math.cos(k * t) * math.cos(n * t)
                y = math.cos(k * t) * math.sin(n * t)
            elif curve_type == 'cardioid':
                x = 2 * math.cos(t) * (1 - math.cos(t))
                y = 2 * math.sin(t) * (1 - math.cos(t))
            elif curve_type == 'lemniscate':
                x = math.cos(t) / (1 + math.sin(t)**2)
                y = math.sin(t) * math.cos(t) / (1 + math.sin(t)**2)
            else:
                x = math.cos(t)
                y = math.sin(t)
            
            # Scale and center
            scale = min(width, height) / 4
            grid_x = int(x * scale + width / 2)
            grid_y = int(y * scale + height / 2)
            
            if 0 <= grid_x < width and 0 <= grid_y < height:
                grid[grid_y][grid_x] = '*'
        
        return '\n'.join([''.join(row) for row in grid])
    
    def generate_chaos_game(self, width: int = 80, height: int = 40,
                           num_points: int = 10000, shape: str = 'triangle') -> str:
        """Generate pattern using chaos game algorithm.
        
        Args:
            width: Width of pattern
            height: Height of pattern
            num_points: Number of points to generate
            shape: Shape type ('triangle', 'square', 'pentagon')
            
        Returns:
            Chaos game pattern
        """
        grid = [[' ' for _ in range(width)] for _ in range(height)]
        
        # Define vertices
        if shape == 'triangle':
            vertices = [
                (width // 2, 10),
                (width // 4, height - 10),
                (3 * width // 4, height - 10)
            ]
        elif shape == 'square':
            margin = 10
            vertices = [
                (margin, margin),
                (width - margin, margin),
                (width - margin, height - margin),
                (margin, height - margin)
            ]
        elif shape == 'pentagon':
            center_x, center_y = width // 2, height // 2
            radius = min(width, height) // 3
            vertices = []
            for i in range(5):
                angle = i * 2 * math.pi / 5 - math.pi / 2
                x = center_x + radius * math.cos(angle)
                y = center_y + radius * math.sin(angle)
                vertices.append((int(x), int(y)))
        else:
            vertices = [(width // 2, 10), (width // 4, height - 10), (3 * width // 4, height - 10)]
        
        # Start from random point
        x, y = random.randint(0, width), random.randint(0, height)
        
        # Ratio for Sierpinski triangle
        ratio = 0.5
        
        for _ in range(num_points):
            # Pick random vertex
            vx, vy = random.choice(vertices)
            
            # Move halfway towards vertex
            x = int(x + (vx - x) * ratio)
            y = int(y + (vy - y) * ratio)
            
            if 0 <= x < width and 0 <= y < height:
                if grid[y][x] == ' ':
                    grid[y][x] = '.'
                elif grid[y][x] == '.':
                    grid[y][x] = '*'
                elif grid[y][x] == '*':
                    grid[y][x] = '#'
        
        return '\n'.join([''.join(row) for row in grid])

