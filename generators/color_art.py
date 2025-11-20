"""Color support for ASCII art with gradients and ANSI colors."""

from typing import Tuple, List, Optional
import math


class ColorMapper:
    """Maps colors to ANSI escape codes for terminal output."""
    
    def __init__(self):
        """Initialize color mapper."""
        self.color_mode = '256'  # '16', '256', or 'truecolor'
        
        # Basic 16 colors
        self.basic_colors = {
            'black': 0, 'red': 1, 'green': 2, 'yellow': 3,
            'blue': 4, 'magenta': 5, 'cyan': 6, 'white': 7,
            'bright_black': 8, 'bright_red': 9, 'bright_green': 10,
            'bright_yellow': 11, 'bright_blue': 12, 'bright_magenta': 13,
            'bright_cyan': 14, 'bright_white': 15
        }
    
    def rgb_to_ansi256(self, r: int, g: int, b: int) -> int:
        """Convert RGB to ANSI 256 color code.
        
        Args:
            r, g, b: RGB values (0-255)
            
        Returns:
            ANSI 256 color code
        """
        # Grayscale
        if r == g == b:
            if r < 8:
                return 16
            if r > 248:
                return 231
            return round(((r - 8) / 247) * 24) + 232
        
        # Color
        r_idx = round(r / 255 * 5)
        g_idx = round(g / 255 * 5)
        b_idx = round(b / 255 * 5)
        
        return 16 + (36 * r_idx) + (6 * g_idx) + b_idx
    
    def ansi_fg_color(self, r: int, g: int, b: int) -> str:
        """Get ANSI foreground color escape code.
        
        Args:
            r, g, b: RGB values (0-255)
            
        Returns:
            ANSI escape code
        """
        if self.color_mode == 'truecolor':
            return f'\033[38;2;{r};{g};{b}m'
        elif self.color_mode == '256':
            code = self.rgb_to_ansi256(r, g, b)
            return f'\033[38;5;{code}m'
        else:
            # Basic 16 colors - find closest
            return '\033[37m'  # Default to white
    
    def ansi_bg_color(self, r: int, g: int, b: int) -> str:
        """Get ANSI background color escape code.
        
        Args:
            r, g, b: RGB values (0-255)
            
        Returns:
            ANSI escape code
        """
        if self.color_mode == 'truecolor':
            return f'\033[48;2;{r};{g};{b}m'
        elif self.color_mode == '256':
            code = self.rgb_to_ansi256(r, g, b)
            return f'\033[48;5;{code}m'
        else:
            return '\033[40m'  # Default to black
    
    @staticmethod
    def reset() -> str:
        """Get ANSI reset code.
        
        Returns:
            ANSI reset escape code
        """
        return '\033[0m'


class GradientGenerator:
    """Generate color gradients for ASCII art."""
    
    def __init__(self):
        """Initialize gradient generator."""
        self.color_mapper = ColorMapper()
    
    def linear_gradient(self, start_color: Tuple[int, int, int],
                       end_color: Tuple[int, int, int],
                       steps: int) -> List[Tuple[int, int, int]]:
        """Generate linear gradient between two colors.
        
        Args:
            start_color: Starting RGB color
            end_color: Ending RGB color
            steps: Number of steps in gradient
            
        Returns:
            List of RGB colors
        """
        gradient = []
        
        for i in range(steps):
            t = i / (steps - 1) if steps > 1 else 0
            
            r = int(start_color[0] + (end_color[0] - start_color[0]) * t)
            g = int(start_color[1] + (end_color[1] - start_color[1]) * t)
            b = int(start_color[2] + (end_color[2] - start_color[2]) * t)
            
            gradient.append((r, g, b))
        
        return gradient
    
    def rainbow_gradient(self, steps: int) -> List[Tuple[int, int, int]]:
        """Generate rainbow gradient.
        
        Args:
            steps: Number of steps
            
        Returns:
            List of RGB colors
        """
        gradient = []
        
        for i in range(steps):
            hue = i / steps
            r, g, b = self._hsv_to_rgb(hue, 1.0, 1.0)
            gradient.append((r, g, b))
        
        return gradient
    
    def _hsv_to_rgb(self, h: float, s: float, v: float) -> Tuple[int, int, int]:
        """Convert HSV to RGB.
        
        Args:
            h: Hue (0-1)
            s: Saturation (0-1)
            v: Value (0-1)
            
        Returns:
            RGB tuple (0-255)
        """
        if s == 0.0:
            r = g = b = int(v * 255)
            return (r, g, b)
        
        i = int(h * 6.0)
        f = (h * 6.0) - i
        p = v * (1.0 - s)
        q = v * (1.0 - s * f)
        t = v * (1.0 - s * (1.0 - f))
        i = i % 6
        
        if i == 0:
            r, g, b = v, t, p
        elif i == 1:
            r, g, b = q, v, p
        elif i == 2:
            r, g, b = p, v, t
        elif i == 3:
            r, g, b = p, q, v
        elif i == 4:
            r, g, b = t, p, v
        else:
            r, g, b = v, p, q
        
        return (int(r * 255), int(g * 255), int(b * 255))
    
    def apply_gradient_to_text(self, text: str, gradient_type: str = 'rainbow') -> str:
        """Apply color gradient to text.
        
        Args:
            text: Text to colorize
            gradient_type: Type of gradient ('rainbow', 'fire', 'ocean', 'forest')
            
        Returns:
            Colorized text with ANSI codes
        """
        lines = text.split('\n')
        colored_lines = []
        
        # Calculate total characters for gradient
        total_chars = sum(len(line) for line in lines)
        
        if gradient_type == 'rainbow':
            gradient = self.rainbow_gradient(total_chars)
        elif gradient_type == 'fire':
            gradient = self.linear_gradient((255, 0, 0), (255, 255, 0), total_chars)
        elif gradient_type == 'ocean':
            gradient = self.linear_gradient((0, 100, 255), (0, 255, 255), total_chars)
        elif gradient_type == 'forest':
            gradient = self.linear_gradient((0, 100, 0), (144, 238, 144), total_chars)
        else:
            gradient = self.rainbow_gradient(total_chars)
        
        char_index = 0
        
        for line in lines:
            colored_line = ''
            for char in line:
                if char_index < len(gradient):
                    r, g, b = gradient[char_index]
                    colored_line += self.color_mapper.ansi_fg_color(r, g, b) + char
                    char_index += 1
                else:
                    colored_line += char
            
            colored_line += self.color_mapper.reset()
            colored_lines.append(colored_line)
        
        return '\n'.join(colored_lines)


class ColorImageConverter:
    """Convert images to colored ASCII art."""
    
    def __init__(self):
        """Initialize color image converter."""
        self.color_mapper = ColorMapper()
    
    def convert_to_colored_ascii(self, image_path: str, width: int = 80,
                                 charset: str = ' .:-=+*#%@') -> str:
        """Convert image to colored ASCII art.
        
        Args:
            image_path: Path to image file
            width: Width of output
            charset: Character set to use
            
        Returns:
            Colored ASCII art
        """
        try:
            from PIL import Image
        except ImportError:
            return "Error: Pillow library required for image conversion"
        
        try:
            # Load and resize image
            image = Image.open(image_path)
            
            # Calculate height maintaining aspect ratio
            aspect_ratio = image.height / image.width
            height = int(width * aspect_ratio * 0.55)
            
            # Resize
            image = image.resize((width, height))
            
            # Convert to RGB
            image = image.convert('RGB')
            
            # Generate colored ASCII
            result = []
            
            for y in range(height):
                line = ''
                for x in range(width):
                    r, g, b = image.getpixel((x, y))
                    
                    # Calculate brightness
                    brightness = (r + g + b) / 3
                    char_index = int((brightness / 255) * (len(charset) - 1))
                    char = charset[char_index]
                    
                    # Apply color
                    color_code = self.color_mapper.ansi_fg_color(r, g, b)
                    line += color_code + char
                
                line += self.color_mapper.reset()
                result.append(line)
            
            return '\n'.join(result)
        
        except Exception as e:
            return f"Error: {e}"

