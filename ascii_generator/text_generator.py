"""Text to ASCII art generator using various font styles."""

import pyfiglet
from typing import List, Optional


class TextASCIIGenerator:
    """Generate ASCII art from text using various font styles."""
    
    # Available font styles
    AVAILABLE_FONTS = [
        'standard', 'slant', '3-d', '3x5', '5lineoblique', 'acrobatic',
        'alligator', 'alligator2', 'alphabet', 'avatar', 'banner', 'banner3-D',
        'banner3', 'banner4', 'barbwire', 'basic', 'bell', 'big', 'bigchief',
        'binary', 'block', 'bubble', 'bulbhead', 'caligraphy', 'caligraphy2',
        'catwalk', 'chunky', 'coinstak', 'colossal', 'computer', 'contessa',
        'contrast', 'cosmic', 'cosmike', 'cricket', 'cursive', 'cyberlarge',
        'cybermedium', 'cybersmall', 'diamond', 'digital', 'doh', 'doom',
        'dotmatrix', 'drpepper', 'eftichess', 'eftifont', 'eftipiti', 'eftirobot',
        'eftitalic', 'eftiwall', 'eftiwater', 'epic', 'fender', 'fourtops',
        'fraktur', 'fuzzy', 'goofy', 'gothic', 'graffiti', 'hollywood',
        'invita', 'isometric1', 'isometric2', 'isometric3', 'isometric4',
        'italic', 'ivrit', 'jazmine', 'jerusalem', 'katakana', 'kban',
        'larry3d', 'lcd', 'lean', 'letters', 'linux', 'lockergnome',
        'madrid', 'marquee', 'maxfour', 'mike', 'mini', 'mirror', 'mnemonic',
        'morse', 'moscow', 'nancyj', 'nancyj-fancy', 'nancyj-underlined',
        'nipples', 'ntgreek', 'o8', 'ogre', 'pawp', 'peaks', 'pebbles',
        ' pepper', 'poison', 'puffy', 'pyramid', 'rectangles', 'relief',
        'relief2', 'rev', 'roman', 'rot13', 'rounded', 'rowancap', 'rozzo',
        'runic', 'runyc', 'sblood', 'script', 'serifcap', 'shadow', 'short',
        'slant', 'slide', 'slscript', 'small', 'smisome1', 'smkeyboard',
        'smscript', 'smshadow', 'smslant', 'smtengwar', 'speed', 'stampatello',
        'standard', 'starwars', 'stellar', 'stop', 'straight', 'tanja',
        'tengwar', 'term', 'thick', 'thin', 'threepoint', 'ticks', 'ticksslant',
        'tinker-toy', 'tombstone', 'trek', 'tsalagi', 'twopoint', 'univers',
        'usaflag', 'wavy', 'weird'
    ]
    
    def __init__(self, font: str = 'standard'):
        """
        Initialize the text ASCII generator.
        
        Args:
            font: Font style to use (default: 'standard')
        """
        self.font = font if font in self.AVAILABLE_FONTS else 'standard'
    
    def generate(self, text: str, width: Optional[int] = None) -> str:
        """
        Generate ASCII art from text.
        
        Args:
            text: Text to convert to ASCII art
            width: Maximum width for the output (None for auto)
        
        Returns:
            ASCII art string
        """
        try:
            figlet = pyfiglet.Figlet(font=self.font, width=width)
            return figlet.renderText(text)
        except pyfiglet.FontNotFound:
            # Fallback to standard font if specified font not found
            figlet = pyfiglet.Figlet(font='standard', width=width)
            return figlet.renderText(text)
    
    def list_fonts(self) -> List[str]:
        """Return list of available fonts."""
        return self.AVAILABLE_FONTS
    
    def set_font(self, font: str) -> bool:
        """
        Set the font style.
        
        Args:
            font: Font name to use
        
        Returns:
            True if font was set successfully, False otherwise
        """
        if font in self.AVAILABLE_FONTS:
            self.font = font
            return True
        return False

