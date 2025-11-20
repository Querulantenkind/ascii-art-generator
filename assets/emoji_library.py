"""Comprehensive ASCII emoji and icon library."""

from typing import Dict, List, Optional


class EmojiLibrary:
    """ASCII emoji and icon collection."""
    
    def __init__(self):
        """Initialize emoji library."""
        self.emojis = self._load_emojis()
        self.icons = self._load_icons()
        self.symbols = self._load_symbols()
        self.decorations = self._load_decorations()
    
    def _load_emojis(self) -> Dict[str, str]:
        """Load emoji collection.
        
        Returns:
            Dictionary of emoji name to ASCII representation
        """
        return {
            # Faces - Happy
            'smile': '😊',
            'grin': '😁',
            'happy': '^_^',
            'joy': '😂',
            'laugh': 'XD',
            'love': '😍',
            'heart_eyes': '♥‿♥',
            
            # Faces - Sad/Neutral
            'sad': '😢',
            'cry': 'T_T',
            'frown': ':(',
            'neutral': '😐',
            'meh': ':|',
            'thinking': '🤔',
            'confused': '😕',
            
            # Faces - Excited
            'excited': '(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧',
            'party': '🎉',
            'celebrate': '\\(^o^)/',
            'yay': '＼(＾O＾)／',
            
            # Faces - Other
            'wink': '😉',
            'cool': '😎',
            'sunglasses': '(⌐■_■)',
            'angry': '😠',
            'rage': '(╯°□°)╯︵ ┻━┻',
            'shrug': '¯\\_(ツ)_/¯',
            'facepalm': '(>_<)',
            'sleep': '😴',
            'dead': 'x_x',
            
            # Gestures
            'thumbs_up': '👍',
            'thumbs_down': '👎',
            'ok_hand': '👌',
            'wave': '👋',
            'clap': '👏',
            'pray': '🙏',
            'muscle': '💪',
            'point_right': '☞',
            'point_left': '☜',
            'point_up': '☝',
            'point_down': '☟',
            
            # Hearts
            'heart': '♥',
            'hearts': '♥♥♥',
            'broken_heart': '💔',
            'heart_arrow': '♥→',
            'sparkling_heart': '💖',
        }
    
    def _load_icons(self) -> Dict[str, str]:
        """Load icon collection.
        
        Returns:
            Dictionary of icon name to ASCII representation
        """
        return {
            # Status
            'check': '✓',
            'checkmark': '✔',
            'cross': '✗',
            'x': '✘',
            'warning': '⚠',
            'info': 'ℹ',
            'question': '?',
            'exclamation': '!',
            'alert': '🔔',
            
            # Arrows
            'arrow_up': '↑',
            'arrow_down': '↓',
            'arrow_left': '←',
            'arrow_right': '→',
            'arrow_up_down': '↕',
            'arrow_left_right': '↔',
            'arrow_ne': '↗',
            'arrow_se': '↘',
            'arrow_sw': '↙',
            'arrow_nw': '↖',
            'double_arrow_right': '⇒',
            'double_arrow_left': '⇐',
            
            # Shapes
            'circle': '○',
            'circle_filled': '●',
            'square': '□',
            'square_filled': '■',
            'triangle': '△',
            'triangle_filled': '▲',
            'diamond': '◇',
            'diamond_filled': '◆',
            'star': '★',
            'star_empty': '☆',
            
            # Tech
            'code': '</>',
            'terminal': '$',
            'command': '>',
            'file': '📄',
            'folder': '📁',
            'folder_open': '📂',
            'document': '📃',
            'page': '📄',
            'bug': '🐛',
            'gear': '⚙',
            'wrench': '🔧',
            'hammer': '🔨',
            'lock': '🔒',
            'unlock': '🔓',
            'key': '🔑',
            
            # Media
            'play': '▶',
            'pause': '⏸',
            'stop': '⏹',
            'record': '⏺',
            'fast_forward': '⏩',
            'rewind': '⏪',
            'music': '♪',
            'note': '♫',
            
            # Weather
            'sun': '☀',
            'cloud': '☁',
            'rain': '☂',
            'umbrella': '☂',
            'snow': '❄',
            'snowflake': '❅',
            'lightning': '⚡',
            'moon': '☾',
            'star_sky': '✨',
            
            # Nature
            'tree': '🌲',
            'flower': '✿',
            'leaf': '🍃',
            'rose': '🌹',
            'tulip': '🌷',
            'plant': '🌱',
            
            # Objects
            'coffee': '☕',
            'beer': '🍺',
            'cake': '🍰',
            'pizza': '🍕',
            'book': '📖',
            'pencil': '✏',
            'pen': '✒',
            'scissors': '✂',
            'phone': '📱',
            'email': '✉',
            'mail': '📧',
            'calendar': '📅',
            'clock': '🕐',
            'hourglass': '⌛',
            'trophy': '🏆',
            'medal': '🏅',
            'gift': '🎁',
            'balloon': '🎈',
            
            # Misc
            'fire': '🔥',
            'rocket': '🚀',
            'sparkles': '✨',
            'dizzy': '💫',
            'boom': '💥',
            'zzz': '💤',
            'speech': '💬',
            'thought': '💭',
        }
    
    def _load_symbols(self) -> Dict[str, str]:
        """Load symbol collection.
        
        Returns:
            Dictionary of symbol name to ASCII representation
        """
        return {
            # Math
            'plus': '+',
            'minus': '-',
            'multiply': '×',
            'divide': '÷',
            'equals': '=',
            'not_equal': '≠',
            'less_than': '<',
            'greater_than': '>',
            'less_equal': '≤',
            'greater_equal': '≥',
            'infinity': '∞',
            'sum': '∑',
            'pi': 'π',
            'delta': 'Δ',
            'alpha': 'α',
            'beta': 'β',
            'gamma': 'γ',
            
            # Currency
            'dollar': '$',
            'euro': '€',
            'pound': '£',
            'yen': '¥',
            'cent': '¢',
            
            # Punctuation
            'bullet': '•',
            'bullet_hollow': '◦',
            'dash': '—',
            'ellipsis': '…',
            'quote_left': '"',
            'quote_right': '"',
            'apostrophe': "'",
            
            # Box Drawing
            'box_light_h': '─',
            'box_light_v': '│',
            'box_light_tl': '┌',
            'box_light_tr': '┐',
            'box_light_bl': '└',
            'box_light_br': '┘',
            'box_heavy_h': '━',
            'box_heavy_v': '┃',
            'box_double_h': '═',
            'box_double_v': '║',
            
            # Blocks
            'block_light': '░',
            'block_medium': '▒',
            'block_dark': '▓',
            'block_full': '█',
            'block_half_left': '▌',
            'block_half_right': '▐',
            'block_half_top': '▀',
            'block_half_bottom': '▄',
        }
    
    def _load_decorations(self) -> Dict[str, str]:
        """Load decorative elements.
        
        Returns:
            Dictionary of decoration patterns
        """
        return {
            'divider_simple': '─' * 60,
            'divider_double': '═' * 60,
            'divider_wave': '~' * 60,
            'divider_dots': '·' * 60,
            'divider_stars': '* ' * 30,
            'divider_flowers': '❀ ' * 30,
            'divider_hearts': '♥ ' * 30,
            
            'corner_tl': '╔',
            'corner_tr': '╗',
            'corner_bl': '╚',
            'corner_br': '╝',
            
            'border_top': '═══════════════════════════════════════',
            'border_bottom': '═══════════════════════════════════════',
            'border_left': '║',
            'border_right': '║',
        }
    
    def get(self, name: str, category: str = None) -> Optional[str]:
        """Get emoji, icon, or symbol by name.
        
        Args:
            name: Name of emoji/icon/symbol
            category: Optional category to search in
            
        Returns:
            ASCII representation or None
        """
        if category == 'emoji' or category is None:
            if name in self.emojis:
                return self.emojis[name]
        
        if category == 'icon' or category is None:
            if name in self.icons:
                return self.icons[name]
        
        if category == 'symbol' or category is None:
            if name in self.symbols:
                return self.symbols[name]
        
        if category == 'decoration' or category is None:
            if name in self.decorations:
                return self.decorations[name]
        
        return None
    
    def search(self, query: str) -> Dict[str, str]:
        """Search for emojis/icons by name.
        
        Args:
            query: Search query
            
        Returns:
            Dictionary of matching items
        """
        query = query.lower()
        results = {}
        
        for name, value in {**self.emojis, **self.icons, 
                           **self.symbols, **self.decorations}.items():
            if query in name.lower():
                results[name] = value
        
        return results
    
    def list_all(self, category: str = None) -> Dict[str, str]:
        """List all items in a category.
        
        Args:
            category: Category to list ('emoji', 'icon', 'symbol', 'decoration')
            
        Returns:
            Dictionary of items
        """
        if category == 'emoji':
            return self.emojis.copy()
        elif category == 'icon':
            return self.icons.copy()
        elif category == 'symbol':
            return self.symbols.copy()
        elif category == 'decoration':
            return self.decorations.copy()
        else:
            return {**self.emojis, **self.icons, **self.symbols, **self.decorations}
    
    def create_emoji_grid(self, category: str = None, cols: int = 8) -> str:
        """Create visual grid of emojis.
        
        Args:
            category: Category to display
            cols: Number of columns
            
        Returns:
            Formatted emoji grid
        """
        items = self.list_all(category)
        
        result = []
        result.append("=" * 80)
        result.append(f"ASCII EMOJI LIBRARY - {(category or 'ALL').upper()}".center(80))
        result.append("=" * 80)
        result.append("")
        
        item_list = list(items.items())
        
        for i in range(0, len(item_list), cols):
            row_items = item_list[i:i+cols]
            
            # Names row
            names = ' | '.join([name[:10].ljust(10) for name, _ in row_items])
            result.append(names)
            
            # Emoji row
            emojis = ' | '.join([str(emoji).center(10) for _, emoji in row_items])
            result.append(emojis)
            
            result.append('-' * 80)
        
        return '\n'.join(result)

