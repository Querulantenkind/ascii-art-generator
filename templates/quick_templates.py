"""Quick templates for instant ASCII art generation."""

from typing import Dict, Optional, List, Tuple
from datetime import datetime


class QuickTemplates:
    """One-liner templates for instant generation."""
    
    def __init__(self):
        """Initialize quick templates."""
        self.templates = self._load_quick_templates()
    
    def _load_quick_templates(self) -> Dict[str, callable]:
        """Load quick template functions.
        
        Returns:
            Dictionary of template name to generator function
        """
        return {
            'header': self.header,
            'banner': self.banner,
            'box': self.box,
            'alert': self.alert,
            'success': self.success,
            'error': self.error,
            'warning': self.warning,
            'info': self.info,
            'divider': self.divider,
            'title': self.title,
            'subtitle': self.subtitle,
            'menu': self.menu,
            'progress': self.progress,
            'loading': self.loading,
            'timestamp': self.timestamp,
            'signature': self.signature,
        }
    
    def header(self, text: str, width: int = 60) -> str:
        """Quick header template.
        
        Args:
            text: Header text
            width: Width
            
        Returns:
            Header ASCII art
        """
        return f"""
╔{'═' * (width - 2)}╗
║ {text.center(width - 4)} ║
╚{'═' * (width - 2)}╝
""".strip()
    
    def banner(self, text: str, subtitle: str = '', width: int = 60) -> str:
        """Quick banner template.
        
        Args:
            text: Main text
            subtitle: Optional subtitle
            width: Width
            
        Returns:
            Banner ASCII art
        """
        lines = [
            '╔' + '═' * (width - 2) + '╗',
            '║' + ' ' * (width - 2) + '║',
            '║ ' + text.center(width - 4) + ' ║',
        ]
        
        if subtitle:
            lines.append('║ ' + subtitle.center(width - 4) + ' ║')
        
        lines.extend([
            '║' + ' ' * (width - 2) + '║',
            '╚' + '═' * (width - 2) + '╝'
        ])
        
        return '\n'.join(lines)
    
    def box(self, content: str, title: str = '', width: int = 60) -> str:
        """Quick box template.
        
        Args:
            content: Box content
            title: Optional title
            width: Width
            
        Returns:
            Box ASCII art
        """
        lines = []
        
        if title:
            lines.append('┌─ ' + title + ' ' + '─' * (width - len(title) - 5) + '┐')
        else:
            lines.append('┌' + '─' * (width - 2) + '┐')
        
        for line in content.split('\n'):
            lines.append('│ ' + line.ljust(width - 4) + ' │')
        
        lines.append('└' + '─' * (width - 2) + '┘')
        
        return '\n'.join(lines)
    
    def alert(self, message: str, alert_type: str = 'info', width: int = 60) -> str:
        """Quick alert template.
        
        Args:
            message: Alert message
            alert_type: Type ('info', 'success', 'warning', 'error')
            width: Width
            
        Returns:
            Alert ASCII art
        """
        icons = {
            'info': 'ℹ',
            'success': '✓',
            'warning': '⚠',
            'error': '✗'
        }
        
        icon = icons.get(alert_type, 'ℹ')
        title = alert_type.upper()
        
        return f"""
┌{'─' * (width - 2)}┐
│ {icon} {title.ljust(width - 6)} │
│{' ' * (width - 2)}│
│  {message.ljust(width - 5)}│
└{'─' * (width - 2)}┘
""".strip()
    
    def success(self, message: str, width: int = 60) -> str:
        """Quick success message."""
        return self.alert(message, 'success', width)
    
    def error(self, message: str, width: int = 60) -> str:
        """Quick error message."""
        return self.alert(message, 'error', width)
    
    def warning(self, message: str, width: int = 60) -> str:
        """Quick warning message."""
        return self.alert(message, 'warning', width)
    
    def info(self, message: str, width: int = 60) -> str:
        """Quick info message."""
        return self.alert(message, 'info', width)
    
    def divider(self, text: str = '', width: int = 60, char: str = '═') -> str:
        """Quick divider template.
        
        Args:
            text: Optional divider text
            width: Width
            char: Divider character
            
        Returns:
            Divider ASCII art
        """
        if text:
            text_with_spaces = f' {text} '
            side_length = (width - len(text_with_spaces)) // 2
            return char * side_length + text_with_spaces + char * side_length
        else:
            return char * width
    
    def title(self, text: str, width: int = 60) -> str:
        """Quick title template.
        
        Args:
            text: Title text
            width: Width
            
        Returns:
            Title ASCII art
        """
        return f"""
{text.center(width)}
{'─' * width}
""".strip()
    
    def subtitle(self, text: str, width: int = 60) -> str:
        """Quick subtitle template.
        
        Args:
            text: Subtitle text
            width: Width
            
        Returns:
            Subtitle ASCII art
        """
        return f"{text.center(width)}\n{'·' * width}"
    
    def menu(self, title: str, options: List[str], width: int = 60) -> str:
        """Quick menu template.
        
        Args:
            title: Menu title
            options: List of menu options
            width: Width
            
        Returns:
            Menu ASCII art
        """
        lines = [
            '┌' + '─' * (width - 2) + '┐',
            '│ ' + title.center(width - 4) + ' │',
            '├' + '─' * (width - 2) + '┤',
        ]
        
        for i, option in enumerate(options, 1):
            lines.append(f'│  {i}. {option.ljust(width - 8)} │')
        
        lines.extend([
            '│  0. Exit' + ' ' * (width - 12) + '│',
            '└' + '─' * (width - 2) + '┘'
        ])
        
        return '\n'.join(lines)
    
    def progress(self, label: str, current: int, total: int, width: int = 50) -> str:
        """Quick progress bar template.
        
        Args:
            label: Progress label
            current: Current value
            total: Total value
            width: Bar width
            
        Returns:
            Progress bar ASCII art
        """
        percentage = (current / total * 100) if total > 0 else 0
        filled = int((current / total) * width) if total > 0 else 0
        
        bar = '█' * filled + '░' * (width - filled)
        
        return f"{label}: [{bar}] {percentage:.1f}% ({current}/{total})"
    
    def loading(self, message: str = 'Loading', width: int = 60) -> str:
        """Quick loading template.
        
        Args:
            message: Loading message
            width: Width
            
        Returns:
            Loading ASCII art
        """
        return f"""
┌{'─' * (width - 2)}┐
│{' ' * (width - 2)}│
│ {message.center(width - 4)} │
│ {'⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏'.center(width - 4)} │
│{' ' * (width - 2)}│
└{'─' * (width - 2)}┘
""".strip()
    
    def timestamp(self, label: str = '', width: int = 60) -> str:
        """Quick timestamp template.
        
        Args:
            label: Optional label
            width: Width
            
        Returns:
            Timestamp ASCII art
        """
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        if label:
            return f"┌─ {label} ─ {now} {'─' * (width - len(label) - len(now) - 7)}┐"
        else:
            return f"┌─ {now} {'─' * (width - len(now) - 4)}┐"
    
    def signature(self, author: str, date: str = None, width: int = 60) -> str:
        """Quick signature template.
        
        Args:
            author: Author name
            date: Optional date
            width: Width
            
        Returns:
            Signature ASCII art
        """
        if date is None:
            date = datetime.now().strftime("%Y-%m-%d")
        
        return f"""
{'─' * width}
Created by: {author}
Date: {date}
""".strip()
    
    def generate(self, template_name: str, *args, **kwargs) -> str:
        """Generate quick template by name.
        
        Args:
            template_name: Name of template
            *args: Positional arguments for template
            **kwargs: Keyword arguments for template
            
        Returns:
            Generated ASCII art
        """
        if template_name not in self.templates:
            raise ValueError(f"Unknown template: {template_name}")
        
        template_func = self.templates[template_name]
        return template_func(*args, **kwargs)
    
    def list_templates(self) -> List[str]:
        """List available quick templates.
        
        Returns:
            List of template names
        """
        return list(self.templates.keys())

