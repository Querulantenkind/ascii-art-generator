"""Image to ASCII art converter."""

from PIL import Image
from typing import Optional, Tuple


class ImageASCIIGenerator:
    """Convert images to ASCII art."""
    
    # Different character sets for different densities
    CHAR_SETS = {
        'dense': '@%#*+=-:. ',
        'medium': '@%#*+=-:. ',
        'sparse': '@#*+-:. ',
        'blocks': '█▓▒░ ',
        'simple': '#. ',
        'detailed': '@$B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,"^`\'. ',
    }
    
    def __init__(self, char_set: str = 'medium', width: int = 80, 
                 height: Optional[int] = None, invert: bool = False):
        """
        Initialize the image ASCII generator.
        
        Args:
            char_set: Character set to use ('dense', 'medium', 'sparse', 'blocks', 'simple', 'detailed')
            width: Output width in characters
            height: Output height in characters (None for auto-calculate)
            invert: Invert brightness (dark becomes light)
        """
        self.char_set = self.CHAR_SETS.get(char_set, self.CHAR_SETS['medium'])
        self.width = width
        self.height = height
        self.invert = invert
    
    def _get_char_for_brightness(self, brightness: float) -> str:
        """
        Get ASCII character based on brightness value.
        
        Args:
            brightness: Brightness value (0.0 to 1.0)
        
        Returns:
            ASCII character
        """
        if self.invert:
            brightness = 1.0 - brightness
        
        # Map brightness to character index
        index = int(brightness * (len(self.char_set) - 1))
        return self.char_set[index]
    
    def _resize_image(self, image: Image.Image) -> Image.Image:
        """
        Resize image to target dimensions while maintaining aspect ratio.
        
        Args:
            image: PIL Image object
        
        Returns:
            Resized PIL Image
        """
        aspect_ratio = image.height / image.width
        
        if self.height is None:
            # Calculate height based on aspect ratio
            self.height = int(self.width * aspect_ratio * 0.5)  # 0.5 accounts for char aspect ratio
        
        # Resize image
        return image.resize((self.width, self.height), Image.Resampling.LANCZOS)
    
    def _image_to_grayscale(self, image: Image.Image) -> Image.Image:
        """
        Convert image to grayscale.
        
        Args:
            image: PIL Image object
        
        Returns:
            Grayscale PIL Image
        """
        if image.mode != 'L':
            return image.convert('L')
        return image
    
    def generate(self, image_path: str) -> str:
        """
        Generate ASCII art from an image file.
        
        Args:
            image_path: Path to the image file
        
        Returns:
            ASCII art string
        """
        try:
            # Open and process image
            image = Image.open(image_path)
            image = self._image_to_grayscale(image)
            image = self._resize_image(image)
            
            # Convert pixels to ASCII
            pixels = image.load()
            ascii_art = []
            
            for y in range(image.height):
                line = []
                for x in range(image.width):
                    brightness = pixels[x, y] / 255.0
                    char = self._get_char_for_brightness(brightness)
                    line.append(char)
                ascii_art.append(''.join(line))
            
            return '\n'.join(ascii_art)
        
        except FileNotFoundError:
            raise FileNotFoundError(f"Image file not found: {image_path}")
        except Exception as e:
            raise Exception(f"Error processing image: {str(e)}")
    
    def set_char_set(self, char_set: str) -> bool:
        """
        Set the character set.
        
        Args:
            char_set: Character set name ('dense', 'medium', 'sparse', 'blocks', 'simple', 'detailed')
        
        Returns:
            True if set successfully, False otherwise
        """
        if char_set in self.CHAR_SETS:
            self.char_set = self.CHAR_SETS[char_set]
            return True
        return False
    
    def list_char_sets(self) -> list:
        """Return list of available character sets."""
        return list(self.CHAR_SETS.keys())

