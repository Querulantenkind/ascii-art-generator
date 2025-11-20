"""Export ASCII art to various formats: HTML, SVG, Markdown, and more."""

import html
from typing import Optional, Tuple


class HTMLExporter:
    """Export ASCII art to HTML format."""
    
    def __init__(self):
        """Initialize HTML exporter."""
        self.default_font = 'Courier New, monospace'
        self.default_bg = '#000000'
        self.default_fg = '#00ff00'
    
    def export(self, ascii_art: str, title: str = 'ASCII Art',
               font_family: str = None, bg_color: str = None,
               fg_color: str = None, font_size: int = 14) -> str:
        """Export ASCII art to HTML.
        
        Args:
            ascii_art: ASCII art content
            title: Page title
            font_family: Font family to use
            bg_color: Background color
            fg_color: Foreground color
            font_size: Font size in pixels
            
        Returns:
            HTML string
        """
        font = font_family or self.default_font
        bg = bg_color or self.default_bg
        fg = fg_color or self.default_fg
        
        # Escape HTML
        escaped_art = html.escape(ascii_art)
        
        html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{html.escape(title)}</title>
    <style>
        body {{
            background-color: {bg};
            color: {fg};
            font-family: {font};
            font-size: {font_size}px;
            padding: 20px;
            margin: 0;
        }}
        pre {{
            margin: 0;
            white-space: pre;
            line-height: 1.2;
        }}
        .ascii-art {{
            display: inline-block;
            padding: 20px;
            border: 2px solid {fg};
            border-radius: 5px;
        }}
    </style>
</head>
<body>
    <div class="ascii-art">
        <pre>{escaped_art}</pre>
    </div>
</body>
</html>"""
        
        return html_template
    
    def export_with_colors(self, ascii_art_with_ansi: str,
                          title: str = 'ASCII Art') -> str:
        """Export ASCII art with ANSI colors to HTML.
        
        Args:
            ascii_art_with_ansi: ASCII art with ANSI color codes
            title: Page title
            
        Returns:
            HTML string with colors
        """
        # Convert ANSI codes to HTML spans
        import re
        
        # Simple ANSI to HTML color mapping
        ansi_colors = {
            '30': '#000000', '31': '#ff0000', '32': '#00ff00', '33': '#ffff00',
            '34': '#0000ff', '35': '#ff00ff', '36': '#00ffff', '37': '#ffffff',
            '90': '#808080', '91': '#ff8080', '92': '#80ff80', '93': '#ffff80',
            '94': '#8080ff', '95': '#ff80ff', '96': '#80ffff', '97': '#ffffff',
        }
        
        html_content = ascii_art_with_ansi
        
        # Replace ANSI codes with HTML spans
        for code, color in ansi_colors.items():
            pattern = f'\033\\[{code}m'
            html_content = html_content.replace(pattern, f'<span style="color: {color};">')
        
        # Replace reset codes
        html_content = html_content.replace('\033[0m', '</span>')
        
        # Escape remaining HTML
        html_content = html.escape(html_content)
        
        return self.export(html_content, title)


class SVGExporter:
    """Export ASCII art to SVG format."""
    
    def __init__(self):
        """Initialize SVG exporter."""
        self.char_width = 10
        self.char_height = 16
    
    def export(self, ascii_art: str, title: str = 'ASCII Art',
               font_size: int = 14, font_family: str = 'monospace',
               fg_color: str = '#000000', bg_color: str = '#ffffff') -> str:
        """Export ASCII art to SVG.
        
        Args:
            ascii_art: ASCII art content
            title: SVG title
            font_size: Font size
            font_family: Font family
            fg_color: Foreground color
            bg_color: Background color
            
        Returns:
            SVG string
        """
        lines = ascii_art.split('\n')
        
        if not lines:
            return ''
        
        max_width = max(len(line) for line in lines) if lines else 0
        height = len(lines)
        
        svg_width = max_width * self.char_width + 40
        svg_height = height * self.char_height + 40
        
        svg_template = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{svg_width}" height="{svg_height}">
    <title>{html.escape(title)}</title>
    <rect width="100%" height="100%" fill="{bg_color}"/>
    <text x="20" y="20" font-family="{font_family}" font-size="{font_size}" fill="{fg_color}">
"""
        
        for i, line in enumerate(lines):
            y_pos = 20 + (i + 1) * self.char_height
            svg_template += f'        <tspan x="20" y="{y_pos}">{html.escape(line)}</tspan>\n'
        
        svg_template += """    </text>
</svg>"""
        
        return svg_template


class MarkdownExporter:
    """Export ASCII art to Markdown format."""
    
    def __init__(self):
        """Initialize Markdown exporter."""
        pass
    
    def export(self, ascii_art: str, title: str = 'ASCII Art',
               description: str = '') -> str:
        """Export ASCII art to Markdown.
        
        Args:
            ascii_art: ASCII art content
            title: Title for the markdown
            description: Optional description
            
        Returns:
            Markdown string
        """
        markdown = f"# {title}\n\n"
        
        if description:
            markdown += f"{description}\n\n"
        
        markdown += "```\n"
        markdown += ascii_art
        markdown += "\n```\n"
        
        return markdown
    
    def export_with_metadata(self, ascii_art: str, title: str,
                            author: str = '', date: str = '',
                            tags: list = None) -> str:
        """Export with metadata.
        
        Args:
            ascii_art: ASCII art content
            title: Title
            author: Author name
            date: Creation date
            tags: List of tags
            
        Returns:
            Markdown with frontmatter
        """
        markdown = "---\n"
        markdown += f"title: {title}\n"
        
        if author:
            markdown += f"author: {author}\n"
        
        if date:
            markdown += f"date: {date}\n"
        
        if tags:
            markdown += f"tags: [{', '.join(tags)}]\n"
        
        markdown += "---\n\n"
        markdown += "```\n"
        markdown += ascii_art
        markdown += "\n```\n"
        
        return markdown


class JSONExporter:
    """Export ASCII art to JSON format."""
    
    def __init__(self):
        """Initialize JSON exporter."""
        pass
    
    def export(self, ascii_art: str, metadata: dict = None) -> str:
        """Export ASCII art to JSON.
        
        Args:
            ascii_art: ASCII art content
            metadata: Optional metadata dictionary
            
        Returns:
            JSON string
        """
        import json
        
        data = {
            'content': ascii_art,
            'lines': ascii_art.split('\n'),
            'width': max(len(line) for line in ascii_art.split('\n')) if ascii_art else 0,
            'height': len(ascii_art.split('\n')),
        }
        
        if metadata:
            data['metadata'] = metadata
        
        return json.dumps(data, indent=2, ensure_ascii=False)


class ANSIExporter:
    """Export ASCII art with ANSI formatting."""
    
    def __init__(self):
        """Initialize ANSI exporter."""
        pass
    
    def export_with_box(self, ascii_art: str, title: str = '',
                       box_style: str = 'double') -> str:
        """Export with decorative ANSI box.
        
        Args:
            ascii_art: ASCII art content
            title: Optional title
            box_style: Box style ('single', 'double', 'thick')
            
        Returns:
            ASCII art with ANSI box
        """
        box_chars = {
            'single': {'tl': '┌', 'tr': '┐', 'bl': '└', 'br': '┘', 'h': '─', 'v': '│'},
            'double': {'tl': '╔', 'tr': '╗', 'bl': '╚', 'br': '╝', 'h': '═', 'v': '║'},
            'thick': {'tl': '┏', 'tr': '┓', 'bl': '┗', 'br': '┛', 'h': '━', 'v': '┃'},
        }
        
        chars = box_chars.get(box_style, box_chars['double'])
        lines = ascii_art.split('\n')
        
        if not lines:
            return ''
        
        max_width = max(len(line) for line in lines)
        
        result = []
        
        # Top border
        if title:
            title_line = chars['tl'] + chars['h'] * 2 + f' {title} ' + chars['h'] * (max_width - len(title) - 3) + chars['tr']
            result.append(title_line)
        else:
            result.append(chars['tl'] + chars['h'] * (max_width + 2) + chars['tr'])
        
        # Content
        for line in lines:
            result.append(chars['v'] + ' ' + line.ljust(max_width) + ' ' + chars['v'])
        
        # Bottom border
        result.append(chars['bl'] + chars['h'] * (max_width + 2) + chars['br'])
        
        return '\n'.join(result)


class ImageExporter:
    """Export ASCII art to image format."""
    
    def __init__(self):
        """Initialize image exporter."""
        pass
    
    def export_to_png(self, ascii_art: str, output_path: str,
                     font_size: int = 14, fg_color: Tuple[int, int, int] = (0, 255, 0),
                     bg_color: Tuple[int, int, int] = (0, 0, 0)) -> bool:
        """Export ASCII art to PNG image.
        
        Args:
            ascii_art: ASCII art content
            output_path: Output file path
            font_size: Font size
            fg_color: Foreground RGB color
            bg_color: Background RGB color
            
        Returns:
            True if successful
        """
        try:
            from PIL import Image, ImageDraw, ImageFont
        except ImportError:
            print("Error: Pillow library required for image export")
            return False
        
        try:
            lines = ascii_art.split('\n')
            
            if not lines:
                return False
            
            # Calculate image dimensions
            char_width = font_size * 0.6
            char_height = font_size * 1.2
            
            max_width = max(len(line) for line in lines)
            width = int(max_width * char_width) + 40
            height = int(len(lines) * char_height) + 40
            
            # Create image
            image = Image.new('RGB', (width, height), bg_color)
            draw = ImageDraw.Draw(image)
            
            # Try to load monospace font
            try:
                font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf', font_size)
            except:
                font = ImageFont.load_default()
            
            # Draw text
            y_offset = 20
            for line in lines:
                draw.text((20, y_offset), line, font=font, fill=fg_color)
                y_offset += char_height
            
            # Save image
            image.save(output_path)
            return True
        
        except Exception as e:
            print(f"Error exporting to PNG: {e}")
            return False

