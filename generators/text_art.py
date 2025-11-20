"""Text-to-ASCII art generator with multiple font styles."""

from typing import Optional


class TextArtGenerator:
    """Generator for converting text to ASCII art using various fonts."""
    
    def __init__(self, config):
        """Initialize text art generator.
        
        Args:
            config: Configuration object
        """
        self.config = config
        self.fonts = self._load_fonts()
    
    def _load_fonts(self):
        """Load available ASCII art fonts.
        
        Returns:
            Dictionary of font definitions
        """
        return {
            'standard': StandardFont(),
            'banner': BannerFont(),
            'block': BlockFont(),
            'slant': SlantFont(),
            'small': SmallFont(),
            'bubble': BubbleFont(),
        }
    
    def generate(self, text: str, font: str = 'standard', width: Optional[int] = None) -> str:
        """Generate ASCII art from text.
        
        Args:
            text: Input text to convert
            font: Font style to use
            width: Maximum width (optional)
            
        Returns:
            ASCII art string
        """
        if font not in self.fonts:
            font = 'standard'
        
        font_obj = self.fonts[font]
        result = font_obj.render(text)
        
        if width:
            result = self._wrap_text(result, width)
        
        return result
    
    def _wrap_text(self, text: str, width: int) -> str:
        """Wrap ASCII art to specified width.
        
        Args:
            text: ASCII art text
            width: Maximum width
            
        Returns:
            Wrapped text
        """
        lines = text.split('\n')
        wrapped_lines = []
        
        for line in lines:
            if len(line) <= width:
                wrapped_lines.append(line)
            else:
                wrapped_lines.append(line[:width])
        
        return '\n'.join(wrapped_lines)
    
    def list_fonts(self):
        """Get list of available fonts.
        
        Returns:
            List of font names
        """
        return list(self.fonts.keys())


class BaseFont:
    """Base class for ASCII art fonts."""
    
    def __init__(self):
        self.height = 1
        self.char_map = {}
    
    def render(self, text: str) -> str:
        """Render text in this font.
        
        Args:
            text: Text to render
            
        Returns:
            ASCII art string
        """
        raise NotImplementedError


class StandardFont(BaseFont):
    """Standard ASCII art font (FIGlet-style)."""
    
    def __init__(self):
        super().__init__()
        self.height = 6
        self._init_chars()
    
    def _init_chars(self):
        """Initialize character definitions."""
        self.char_map = {
            'A': [
                "   ___   ",
                "  / _ \\  ",
                " / /_\\ \\ ",
                "/  _  \\ \\",
                "\\_/ \\_/ /",
                "        "
            ],
            'B': [
                " ____  ",
                "|  _ \\ ",
                "| |_) |",
                "|  _ < ",
                "|_| \\_\\",
                "       "
            ],
            'C': [
                "  ____ ",
                " / ___|",
                "| |    ",
                "| |___ ",
                " \\____|",
                "       "
            ],
            'D': [
                " ____  ",
                "|  _ \\ ",
                "| | | |",
                "| |_| |",
                "|____/ ",
                "       "
            ],
            'E': [
                " _____ ",
                "|  ___|",
                "| |__  ",
                "|  __| ",
                "|_____|",
                "       "
            ],
            'F': [
                " _____ ",
                "|  ___|",
                "| |__  ",
                "|  __| ",
                "|_|    ",
                "       "
            ],
            'G': [
                "  ____ ",
                " / ___|",
                "| |  _ ",
                "| |_| |",
                " \\____|",
                "       "
            ],
            'H': [
                " _   _ ",
                "| | | |",
                "| |_| |",
                "|  _  |",
                "|_| |_|",
                "       "
            ],
            'I': [
                " ___ ",
                "|_ _|",
                " | | ",
                " | | ",
                "|___|",
                "     "
            ],
            'J': [
                "     _ ",
                "    | |",
                " _  | |",
                "| |_| |",
                " \\___/ ",
                "       "
            ],
            'K': [
                " _  __",
                "| |/ /",
                "| ' / ",
                "| . \\ ",
                "|_|\\_\\",
                "      "
            ],
            'L': [
                " _     ",
                "| |    ",
                "| |    ",
                "| |___ ",
                "|_____|",
                "       "
            ],
            'M': [
                " __  __ ",
                "|  \\/  |",
                "| |\\/| |",
                "| |  | |",
                "|_|  |_|",
                "        "
            ],
            'N': [
                " _   _ ",
                "| \\ | |",
                "|  \\| |",
                "| |\\  |",
                "|_| \\_|",
                "       "
            ],
            'O': [
                "  ___  ",
                " / _ \\ ",
                "| | | |",
                "| |_| |",
                " \\___/ ",
                "       "
            ],
            'P': [
                " ____  ",
                "|  _ \\ ",
                "| |_) |",
                "|  __/ ",
                "|_|    ",
                "       "
            ],
            'Q': [
                "  ___  ",
                " / _ \\ ",
                "| | | |",
                "| |_| |",
                " \\__\\_\\",
                "       "
            ],
            'R': [
                " ____  ",
                "|  _ \\ ",
                "| |_) |",
                "|  _ < ",
                "|_| \\_\\",
                "       "
            ],
            'S': [
                " ____  ",
                "/ ___| ",
                "\\___ \\ ",
                " ___) |",
                "|____/ ",
                "       "
            ],
            'T': [
                " _____ ",
                "|_   _|",
                "  | |  ",
                "  | |  ",
                "  |_|  ",
                "       "
            ],
            'U': [
                " _   _ ",
                "| | | |",
                "| | | |",
                "| |_| |",
                " \\___/ ",
                "       "
            ],
            'V': [
                "__     __",
                "\\ \\   / /",
                " \\ \\ / / ",
                "  \\ V /  ",
                "   \\_/   ",
                "         "
            ],
            'W': [
                "__        __",
                "\\ \\      / /",
                " \\ \\ /\\ / / ",
                "  \\ V  V /  ",
                "   \\_/\\_/   ",
                "            "
            ],
            'X': [
                "__  __",
                "\\ \\/ /",
                " \\  / ",
                " /  \\ ",
                "/_/\\_\\",
                "      "
            ],
            'Y': [
                "__   __",
                "\\ \\ / /",
                " \\ V / ",
                "  | |  ",
                "  |_|  ",
                "       "
            ],
            'Z': [
                " _____",
                "|__  /",
                "  / / ",
                " / /_ ",
                "/____|",
                "      "
            ],
            ' ': [
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   "
            ],
            '!': [
                " _ ",
                "| |",
                "| |",
                "|_|",
                "(_)",
                "   "
            ],
            '?': [
                " ___ ",
                "|__ \\",
                "  / /",
                " |_| ",
                " (_) ",
                "     "
            ],
        }
    
    def render(self, text: str) -> str:
        """Render text in standard font.
        
        Args:
            text: Text to render
            
        Returns:
            ASCII art string
        """
        text = text.upper()
        lines = [''] * self.height
        
        for char in text:
            if char in self.char_map:
                char_lines = self.char_map[char]
                for i in range(self.height):
                    lines[i] += char_lines[i]
            else:
                # Use space for unknown characters
                for i in range(self.height):
                    lines[i] += "   "
        
        return '\n'.join(lines)


class BannerFont(BaseFont):
    """Banner-style ASCII art font."""
    
    def __init__(self):
        super().__init__()
        self.height = 7
    
    def render(self, text: str) -> str:
        """Render text in banner font.
        
        Args:
            text: Text to render
            
        Returns:
            ASCII art string
        """
        text = text.upper()
        lines = [
            " " + "#" * (len(text) * 8 + 2),
            "#" + " " * (len(text) * 8 + 2) + "#"
        ]
        
        # Create large letters
        letter_line = "#  "
        for char in text:
            letter_line += f"  {char}  " + "  "
        letter_line += " #"
        lines.append(letter_line)
        
        lines.extend([
            "#" + " " * (len(text) * 8 + 2) + "#",
            " " + "#" * (len(text) * 8 + 2)
        ])
        
        return '\n'.join(lines)


class BlockFont(BaseFont):
    """Block-style ASCII art font using box drawing characters."""
    
    def __init__(self):
        super().__init__()
        self.height = 5
    
    def render(self, text: str) -> str:
        """Render text in block font.
        
        Args:
            text: Text to render
            
        Returns:
            ASCII art string
        """
        text = text.upper()
        lines = []
        
        for i in range(self.height):
            line = ""
            for char in text:
                if char == ' ':
                    line += "    "
                elif i == 0 or i == 4:
                    line += "████ "
                elif i == 2:
                    line += "████ "
                else:
                    line += "█  █ "
            lines.append(line)
        
        return '\n'.join(lines)


class SlantFont(BaseFont):
    """Slanted ASCII art font."""
    
    def __init__(self):
        super().__init__()
        self.height = 5
    
    def render(self, text: str) -> str:
        """Render text in slant font.
        
        Args:
            text: Text to render
            
        Returns:
            ASCII art string
        """
        text = text.upper()
        result = []
        
        for i, char in enumerate(text):
            if char == ' ':
                result.append("  ")
            else:
                result.append(f"/{char}\\")
        
        return "  " + " ".join(result)


class SmallFont(BaseFont):
    """Small ASCII art font."""
    
    def __init__(self):
        super().__init__()
        self.height = 3
    
    def render(self, text: str) -> str:
        """Render text in small font.
        
        Args:
            text: Text to render
            
        Returns:
            ASCII art string
        """
        text = text.upper()
        lines = ["", "", ""]
        
        for char in text:
            if char == ' ':
                for i in range(3):
                    lines[i] += "  "
            else:
                lines[0] += f" {char} "
                lines[1] += f"/{char}\\"
                lines[2] += "   "
        
        return '\n'.join(lines)


class BubbleFont(BaseFont):
    """Bubble-style ASCII art font."""
    
    def __init__(self):
        super().__init__()
        self.height = 3
    
    def render(self, text: str) -> str:
        """Render text in bubble font.
        
        Args:
            text: Text to render
            
        Returns:
            ASCII art string
        """
        text = text.upper()
        lines = ["", "", ""]
        
        for char in text:
            if char == ' ':
                for i in range(3):
                    lines[i] += "    "
            else:
                lines[0] += " ___ "
                lines[1] += f"( {char} )"
                lines[2] += " --- "
        
        return '\n'.join(lines)

