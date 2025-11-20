"""Configuration management for ASCII art generator."""


class Config:
    """Configuration class for ASCII art generator settings."""
    
    def __init__(self, color_enabled=False):
        """Initialize configuration.
        
        Args:
            color_enabled: Whether to enable color output
        """
        self.color_enabled = color_enabled
        self.default_width = 80
        self.default_height = 20
        
        # Character sets for image-to-ASCII conversion
        self.charsets = {
            'standard': " .:-=+*#%@",
            'detailed': " .'`^\",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$",
            'simple': " .oO@",
            'blocks': " ░▒▓█"
        }
        
        # Color codes for terminal output
        self.colors = {
            'reset': '\033[0m',
            'bold': '\033[1m',
            'red': '\033[91m',
            'green': '\033[92m',
            'yellow': '\033[93m',
            'blue': '\033[94m',
            'magenta': '\033[95m',
            'cyan': '\033[96m',
        }
    
    def get_charset(self, name='standard'):
        """Get character set by name.
        
        Args:
            name: Name of the character set
            
        Returns:
            String of characters ordered by density
        """
        return self.charsets.get(name, self.charsets['standard'])
    
    def colorize(self, text, color):
        """Apply color to text if color is enabled.
        
        Args:
            text: Text to colorize
            color: Color name
            
        Returns:
            Colorized text or original text
        """
        if not self.color_enabled:
            return text
        
        color_code = self.colors.get(color, '')
        reset_code = self.colors['reset']
        return f"{color_code}{text}{reset_code}"

