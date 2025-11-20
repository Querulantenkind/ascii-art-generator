"""Image-to-ASCII art converter."""

from typing import Optional
import os


class ImageArtGenerator:
    """Generator for converting images to ASCII art."""
    
    def __init__(self, config):
        """Initialize image art generator.
        
        Args:
            config: Configuration object
        """
        self.config = config
    
    def generate(self, image_path: str, width: int = 80, charset: str = 'standard') -> str:
        """Convert image to ASCII art.
        
        Args:
            image_path: Path to image file
            width: Width of output ASCII art
            charset: Character set to use
            
        Returns:
            ASCII art string
        """
        try:
            from PIL import Image
        except ImportError:
            return self._generate_placeholder(
                "PIL (Pillow) not installed. Install with: pip install Pillow"
            )
        
        if not os.path.exists(image_path):
            return f"Error: Image file not found: {image_path}"
        
        try:
            # Open and process image
            image = Image.open(image_path)
            
            # Convert to grayscale
            image = image.convert('L')
            
            # Calculate height to maintain aspect ratio
            aspect_ratio = image.height / image.width
            height = int(width * aspect_ratio * 0.55)  # 0.55 to account for character height
            
            # Resize image
            image = image.resize((width, height))
            
            # Get character set
            chars = self.config.get_charset(charset)
            
            # Convert pixels to ASCII
            pixels = image.getdata()
            ascii_art = []
            
            for i in range(0, len(pixels), width):
                row = pixels[i:i+width]
                ascii_row = ''.join([self._pixel_to_char(pixel, chars) for pixel in row])
                ascii_art.append(ascii_row)
            
            return '\n'.join(ascii_art)
        
        except Exception as e:
            return f"Error processing image: {str(e)}"
    
    def _pixel_to_char(self, pixel_value: int, charset: str) -> str:
        """Convert pixel brightness to ASCII character.
        
        Args:
            pixel_value: Grayscale pixel value (0-255)
            charset: String of characters ordered by density
            
        Returns:
            ASCII character
        """
        # Map pixel value to character index
        char_index = int((pixel_value / 255) * (len(charset) - 1))
        return charset[char_index]
    
    def _generate_placeholder(self, message: str) -> str:
        """Generate a placeholder message.
        
        Args:
            message: Message to display
            
        Returns:
            Formatted message
        """
        border = "=" * len(message)
        return f"{border}\n{message}\n{border}"
    
    def generate_from_text(self, text: str, width: int = 40, height: int = 10) -> str:
        """Generate ASCII art from text (simple text-based image).
        
        Args:
            text: Text to convert
            width: Width of canvas
            height: Height of canvas
            
        Returns:
            ASCII art string
        """
        # Create a simple centered text image
        lines = []
        text_lines = text.split('\n')
        
        # Calculate vertical centering
        start_line = (height - len(text_lines)) // 2
        
        for i in range(height):
            if start_line <= i < start_line + len(text_lines):
                line_text = text_lines[i - start_line]
                # Center horizontally
                padding = (width - len(line_text)) // 2
                line = ' ' * padding + line_text + ' ' * (width - padding - len(line_text))
            else:
                line = ' ' * width
            lines.append(line)
        
        return '\n'.join(lines)

