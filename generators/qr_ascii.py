"""QR Code generation in ASCII art format."""

from typing import Optional


class QRCodeASCII:
    """Generate QR codes as ASCII art."""
    
    def __init__(self):
        """Initialize QR code generator."""
        self.block_char = '█'
        self.empty_char = ' '
    
    def generate(self, data: str, version: int = 1,
                error_correction: str = 'M', scale: int = 1) -> str:
        """Generate QR code as ASCII art.
        
        Args:
            data: Data to encode
            version: QR code version (1-40)
            error_correction: Error correction level ('L', 'M', 'Q', 'H')
            scale: Scale factor for output
            
        Returns:
            ASCII QR code
        """
        try:
            import qrcode
        except ImportError:
            return self._generate_placeholder(data)
        
        # Create QR code
        qr = qrcode.QRCode(
            version=version,
            error_correction=self._get_error_correction(error_correction),
            box_size=1,
            border=2,
        )
        
        qr.add_data(data)
        qr.make(fit=True)
        
        # Get matrix
        matrix = qr.get_matrix()
        
        # Convert to ASCII
        lines = []
        for row in matrix:
            line = ''
            for cell in row:
                char = self.block_char if cell else self.empty_char
                line += char * scale
            
            # Add line multiple times for vertical scaling
            for _ in range(scale):
                lines.append(line)
        
        return '\n'.join(lines)
    
    def _get_error_correction(self, level: str):
        """Get error correction constant.
        
        Args:
            level: Error correction level
            
        Returns:
            Error correction constant
        """
        try:
            import qrcode
            
            levels = {
                'L': qrcode.constants.ERROR_CORRECT_L,
                'M': qrcode.constants.ERROR_CORRECT_M,
                'Q': qrcode.constants.ERROR_CORRECT_Q,
                'H': qrcode.constants.ERROR_CORRECT_H,
            }
            
            return levels.get(level, qrcode.constants.ERROR_CORRECT_M)
        except ImportError:
            return None
    
    def _generate_placeholder(self, data: str) -> str:
        """Generate placeholder when qrcode library not available.
        
        Args:
            data: Data that would be encoded
            
        Returns:
            Placeholder message
        """
        message = f"""
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║                      QR CODE GENERATOR                        ║
║                                                               ║
║  The 'qrcode' library is required for QR code generation.    ║
║                                                               ║
║  Install with: pip install qrcode[pil]                        ║
║                                                               ║
║  Data to encode: {data[:40]}{'...' if len(data) > 40 else ''}
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
"""
        return message.strip()
    
    def generate_with_border(self, data: str, title: str = "QR CODE",
                            **kwargs) -> str:
        """Generate QR code with decorative border.
        
        Args:
            data: Data to encode
            title: Title for the QR code
            **kwargs: Additional arguments for generate()
            
        Returns:
            QR code with border
        """
        qr_code = self.generate(data, **kwargs)
        
        lines = qr_code.split('\n')
        width = len(lines[0]) if lines else 0
        
        # Create border
        result = []
        result.append('╔' + '═' * (width + 2) + '╗')
        result.append('║ ' + title.center(width) + ' ║')
        result.append('╠' + '═' * (width + 2) + '╣')
        
        for line in lines:
            result.append('║ ' + line + ' ║')
        
        result.append('╠' + '═' * (width + 2) + '╣')
        result.append('║ ' + data[:width].center(width) + ' ║')
        result.append('╚' + '═' * (width + 2) + '╝')
        
        return '\n'.join(result)
    
    def generate_simple(self, data: str) -> str:
        """Generate simple QR code using basic ASCII.
        
        Args:
            data: Data to encode
            
        Returns:
            Simple ASCII QR code
        """
        # Use different characters for variety
        self.block_char = '#'
        self.empty_char = '.'
        
        result = self.generate(data, scale=1)
        
        # Reset to defaults
        self.block_char = '█'
        self.empty_char = ' '
        
        return result

