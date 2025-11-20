"""Data visualization in ASCII art - charts, graphs, and plots."""

from typing import List, Dict, Tuple, Optional
import math


class ASCIIChart:
    """Create ASCII charts and graphs."""
    
    def __init__(self):
        """Initialize ASCII chart generator."""
        self.bar_char = '█'
        self.empty_char = '░'
    
    def bar_chart(self, data: Dict[str, float], width: int = 60,
                  height: int = 20, show_values: bool = True) -> str:
        """Generate horizontal bar chart.
        
        Args:
            data: Dictionary of label: value pairs
            width: Chart width
            height: Chart height
            show_values: Show numeric values
            
        Returns:
            ASCII bar chart
        """
        if not data:
            return "No data provided"
        
        max_value = max(data.values())
        max_label_len = max(len(label) for label in data.keys())
        
        # Calculate bar width
        bar_width = width - max_label_len - 10
        
        lines = []
        lines.append("Bar Chart")
        lines.append("=" * width)
        
        for label, value in data.items():
            # Calculate bar length
            bar_length = int((value / max_value) * bar_width) if max_value > 0 else 0
            
            # Create bar
            bar = self.bar_char * bar_length
            empty = self.empty_char * (bar_width - bar_length)
            
            # Format line
            value_str = f" {value:.1f}" if show_values else ""
            line = f"{label.ljust(max_label_len)} │{bar}{empty}│{value_str}"
            lines.append(line)
        
        lines.append("=" * width)
        
        return '\n'.join(lines)
    
    def column_chart(self, data: Dict[str, float], width: int = 60,
                    height: int = 20) -> str:
        """Generate vertical column chart.
        
        Args:
            data: Dictionary of label: value pairs
            width: Chart width
            height: Chart height
            
        Returns:
            ASCII column chart
        """
        if not data:
            return "No data provided"
        
        max_value = max(data.values())
        num_cols = len(data)
        col_width = width // num_cols
        
        lines = []
        
        # Draw from top to bottom
        for row in range(height, 0, -1):
            line = ""
            threshold = (row / height) * max_value
            
            for label, value in data.items():
                if value >= threshold:
                    line += (self.bar_char * (col_width - 1)).center(col_width)
                else:
                    line += " " * col_width
            
            lines.append(line)
        
        # Add baseline
        lines.append("─" * width)
        
        # Add labels
        label_line = ""
        for label in data.keys():
            label_line += label[:col_width-1].center(col_width)
        lines.append(label_line)
        
        return '\n'.join(lines)
    
    def line_graph(self, data: List[float], width: int = 60,
                  height: int = 20, label: str = "Data") -> str:
        """Generate line graph.
        
        Args:
            data: List of values
            width: Graph width
            height: Graph height
            label: Data label
            
        Returns:
            ASCII line graph
        """
        if not data:
            return "No data provided"
        
        min_val = min(data)
        max_val = max(data)
        value_range = max_val - min_val if max_val != min_val else 1
        
        # Create grid
        grid = [[' ' for _ in range(width)] for _ in range(height)]
        
        # Plot points
        for i, value in enumerate(data):
            x = int((i / (len(data) - 1)) * (width - 1)) if len(data) > 1 else width // 2
            y = height - 1 - int(((value - min_val) / value_range) * (height - 1))
            
            if 0 <= x < width and 0 <= y < height:
                grid[y][x] = '*'
                
                # Connect points with lines
                if i > 0:
                    prev_value = data[i - 1]
                    prev_x = int(((i - 1) / (len(data) - 1)) * (width - 1))
                    prev_y = height - 1 - int(((prev_value - min_val) / value_range) * (height - 1))
                    
                    # Draw line between points
                    self._draw_line(grid, prev_x, prev_y, x, y)
        
        # Convert grid to string
        lines = [label]
        lines.append("┌" + "─" * width + "┐")
        
        for row in grid:
            lines.append("│" + ''.join(row) + "│")
        
        lines.append("└" + "─" * width + "┘")
        lines.append(f"Min: {min_val:.2f}  Max: {max_val:.2f}")
        
        return '\n'.join(lines)
    
    def _draw_line(self, grid: List[List[str]], x1: int, y1: int, 
                   x2: int, y2: int):
        """Draw line between two points using Bresenham's algorithm."""
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        sx = 1 if x1 < x2 else -1
        sy = 1 if y1 < y2 else -1
        err = dx - dy
        
        x, y = x1, y1
        
        while True:
            if 0 <= y < len(grid) and 0 <= x < len(grid[0]):
                if grid[y][x] == ' ':
                    grid[y][x] = '·'
            
            if x == x2 and y == y2:
                break
            
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x += sx
            if e2 < dx:
                err += dx
                y += sy
    
    def pie_chart(self, data: Dict[str, float], radius: int = 15) -> str:
        """Generate ASCII pie chart.
        
        Args:
            data: Dictionary of label: value pairs
            radius: Chart radius
            
        Returns:
            ASCII pie chart
        """
        if not data:
            return "No data provided"
        
        total = sum(data.values())
        size = radius * 2 + 1
        
        # Create grid
        grid = [[' ' for _ in range(size)] for _ in range(size)]
        
        # Calculate angles for each slice
        current_angle = 0
        chars = ['█', '▓', '▒', '░', '●', '○', '◆', '◇']
        
        for i, (label, value) in enumerate(data.items()):
            slice_angle = (value / total) * 360 if total > 0 else 0
            char = chars[i % len(chars)]
            
            # Fill slice
            for y in range(size):
                for x in range(size):
                    # Calculate distance from center
                    dx = x - radius
                    dy = y - radius
                    distance = math.sqrt(dx*dx + dy*dy)
                    
                    if distance <= radius:
                        # Calculate angle
                        angle = math.degrees(math.atan2(dy, dx)) + 180
                        
                        if current_angle <= angle < current_angle + slice_angle:
                            grid[y][x] = char
            
            current_angle += slice_angle
        
        # Convert to string
        lines = ["Pie Chart"]
        lines.append("=" * size)
        
        for row in grid:
            lines.append(''.join(row))
        
        lines.append("=" * size)
        
        # Add legend
        for i, (label, value) in enumerate(data.items()):
            char = chars[i % len(chars)]
            percentage = (value / total) * 100 if total > 0 else 0
            lines.append(f"{char} {label}: {value:.1f} ({percentage:.1f}%)")
        
        return '\n'.join(lines)
    
    def scatter_plot(self, x_data: List[float], y_data: List[float],
                    width: int = 60, height: int = 20,
                    label: str = "Scatter Plot") -> str:
        """Generate scatter plot.
        
        Args:
            x_data: X coordinates
            y_data: Y coordinates
            width: Plot width
            height: Plot height
            label: Plot label
            
        Returns:
            ASCII scatter plot
        """
        if not x_data or not y_data or len(x_data) != len(y_data):
            return "Invalid data"
        
        x_min, x_max = min(x_data), max(x_data)
        y_min, y_max = min(y_data), max(y_data)
        
        x_range = x_max - x_min if x_max != x_min else 1
        y_range = y_max - y_min if y_max != y_min else 1
        
        # Create grid
        grid = [[' ' for _ in range(width)] for _ in range(height)]
        
        # Plot points
        for x, y in zip(x_data, y_data):
            plot_x = int(((x - x_min) / x_range) * (width - 1))
            plot_y = height - 1 - int(((y - y_min) / y_range) * (height - 1))
            
            if 0 <= plot_x < width and 0 <= plot_y < height:
                grid[plot_y][plot_x] = '●'
        
        # Convert to string
        lines = [label]
        lines.append("┌" + "─" * width + "┐")
        
        for row in grid:
            lines.append("│" + ''.join(row) + "│")
        
        lines.append("└" + "─" * width + "┘")
        lines.append(f"X: [{x_min:.2f}, {x_max:.2f}]  Y: [{y_min:.2f}, {y_max:.2f}]")
        
        return '\n'.join(lines)
    
    def histogram(self, data: List[float], bins: int = 10,
                 width: int = 60, height: int = 20) -> str:
        """Generate histogram.
        
        Args:
            data: Data values
            bins: Number of bins
            width: Chart width
            height: Chart height
            
        Returns:
            ASCII histogram
        """
        if not data:
            return "No data provided"
        
        min_val = min(data)
        max_val = max(data)
        value_range = max_val - min_val if max_val != min_val else 1
        
        # Calculate bin edges
        bin_width = value_range / bins
        bin_counts = [0] * bins
        
        # Count values in each bin
        for value in data:
            bin_index = min(int((value - min_val) / bin_width), bins - 1)
            bin_counts[bin_index] += 1
        
        # Create bar chart of bins
        max_count = max(bin_counts) if bin_counts else 1
        
        lines = ["Histogram"]
        lines.append("=" * width)
        
        # Draw bars
        for row in range(height, 0, -1):
            line = ""
            threshold = (row / height) * max_count
            
            for count in bin_counts:
                bar_width = width // bins
                if count >= threshold:
                    line += self.bar_char * bar_width
                else:
                    line += " " * bar_width
            
            lines.append(line)
        
        lines.append("─" * width)
        
        # Add bin labels
        label_line = ""
        for i in range(bins):
            bin_start = min_val + i * bin_width
            label = f"{bin_start:.1f}"
            label_line += label[:width//bins].ljust(width//bins)
        lines.append(label_line)
        
        return '\n'.join(lines)


class ASCIITable:
    """Create formatted ASCII tables."""
    
    def __init__(self):
        """Initialize ASCII table generator."""
        pass
    
    def create_table(self, headers: List[str], rows: List[List[str]],
                    style: str = 'single') -> str:
        """Create formatted table.
        
        Args:
            headers: Column headers
            rows: Data rows
            style: Border style ('single', 'double', 'ascii')
            
        Returns:
            Formatted ASCII table
        """
        if not headers:
            return "No headers provided"
        
        # Box drawing characters
        if style == 'single':
            chars = {
                'tl': '┌', 'tr': '┐', 'bl': '└', 'br': '┘',
                'h': '─', 'v': '│', 'cross': '┼',
                'lt': '├', 'rt': '┤', 'tt': '┬', 'bt': '┴'
            }
        elif style == 'double':
            chars = {
                'tl': '╔', 'tr': '╗', 'bl': '╚', 'br': '╝',
                'h': '═', 'v': '║', 'cross': '╬',
                'lt': '╠', 'rt': '╣', 'tt': '╦', 'bt': '╩'
            }
        else:  # ascii
            chars = {
                'tl': '+', 'tr': '+', 'bl': '+', 'br': '+',
                'h': '-', 'v': '|', 'cross': '+',
                'lt': '+', 'rt': '+', 'tt': '+', 'bt': '+'
            }
        
        # Calculate column widths
        col_widths = [len(h) for h in headers]
        for row in rows:
            for i, cell in enumerate(row):
                if i < len(col_widths):
                    col_widths[i] = max(col_widths[i], len(str(cell)))
        
        # Build table
        lines = []
        
        # Top border
        line = chars['tl']
        for i, width in enumerate(col_widths):
            line += chars['h'] * (width + 2)
            if i < len(col_widths) - 1:
                line += chars['tt']
        line += chars['tr']
        lines.append(line)
        
        # Headers
        line = chars['v']
        for i, (header, width) in enumerate(zip(headers, col_widths)):
            line += f" {header.ljust(width)} "
            line += chars['v']
        lines.append(line)
        
        # Header separator
        line = chars['lt']
        for i, width in enumerate(col_widths):
            line += chars['h'] * (width + 2)
            if i < len(col_widths) - 1:
                line += chars['cross']
        line += chars['rt']
        lines.append(line)
        
        # Data rows
        for row in rows:
            line = chars['v']
            for i, (cell, width) in enumerate(zip(row, col_widths)):
                line += f" {str(cell).ljust(width)} "
                line += chars['v']
            lines.append(line)
        
        # Bottom border
        line = chars['bl']
        for i, width in enumerate(col_widths):
            line += chars['h'] * (width + 2)
            if i < len(col_widths) - 1:
                line += chars['bt']
        line += chars['br']
        lines.append(line)
        
        return '\n'.join(lines)


class ProgressVisualizer:
    """Visualize progress and metrics."""
    
    def __init__(self):
        """Initialize progress visualizer."""
        pass
    
    def progress_bar(self, current: float, total: float, width: int = 50,
                    show_percentage: bool = True, label: str = "") -> str:
        """Create progress bar.
        
        Args:
            current: Current value
            total: Total value
            width: Bar width
            show_percentage: Show percentage
            label: Optional label
            
        Returns:
            Progress bar string
        """
        percentage = (current / total) * 100 if total > 0 else 0
        filled = int((current / total) * width) if total > 0 else 0
        
        bar = '█' * filled + '░' * (width - filled)
        
        result = f"[{bar}]"
        
        if show_percentage:
            result += f" {percentage:.1f}%"
        
        if label:
            result = f"{label}: {result}"
        
        return result
    
    def gauge(self, value: float, min_val: float = 0, max_val: float = 100,
             width: int = 40, label: str = "") -> str:
        """Create gauge visualization.
        
        Args:
            value: Current value
            min_val: Minimum value
            max_val: Maximum value
            width: Gauge width
            label: Optional label
            
        Returns:
            Gauge string
        """
        value_range = max_val - min_val
        position = int(((value - min_val) / value_range) * width) if value_range > 0 else 0
        position = max(0, min(width - 1, position))
        
        gauge = ['─'] * width
        gauge[position] = '▼'
        
        result = []
        if label:
            result.append(label)
        
        result.append(''.join(gauge))
        result.append(f"{min_val}".ljust(width // 3) + 
                     f"{value:.1f}".center(width // 3) + 
                     f"{max_val}".rjust(width // 3))
        
        return '\n'.join(result)
    
    def sparkline(self, data: List[float]) -> str:
        """Create sparkline (mini line chart).
        
        Args:
            data: Data values
            
        Returns:
            Sparkline string
        """
        if not data:
            return ""
        
        min_val = min(data)
        max_val = max(data)
        value_range = max_val - min_val if max_val != min_val else 1
        
        # Unicode block characters for sparklines
        chars = ['▁', '▂', '▃', '▄', '▅', '▆', '▇', '█']
        
        sparkline = ''
        for value in data:
            index = int(((value - min_val) / value_range) * (len(chars) - 1))
            sparkline += chars[index]
        
        return sparkline

