"""Smart ASCII art generation with AI-like features."""

from typing import List, Dict, Tuple, Optional
import re


class SmartFontSelector:
    """Intelligently select the best font for given text."""
    
    def __init__(self):
        """Initialize smart font selector."""
        self.font_characteristics = {
            'standard': {'width': 'medium', 'height': 'tall', 'style': 'professional', 'readability': 'high'},
            'banner': {'width': 'wide', 'height': 'tall', 'style': 'bold', 'readability': 'medium'},
            'block': {'width': 'wide', 'height': 'medium', 'style': 'solid', 'readability': 'low'},
            'slant': {'width': 'medium', 'height': 'short', 'style': 'dynamic', 'readability': 'medium'},
            'small': {'width': 'narrow', 'height': 'short', 'style': 'compact', 'readability': 'high'},
            'bubble': {'width': 'wide', 'height': 'short', 'style': 'playful', 'readability': 'medium'},
        }
    
    def suggest_font(self, text: str, context: str = 'general', 
                    max_width: Optional[int] = None) -> List[Tuple[str, float, str]]:
        """Suggest best fonts for given text and context.
        
        Args:
            text: Text to analyze
            context: Usage context ('header', 'logo', 'banner', 'body', 'title')
            max_width: Maximum width constraint
            
        Returns:
            List of (font_name, score, reason) tuples, sorted by score
        """
        suggestions = []
        
        for font_name, characteristics in self.font_characteristics.items():
            score = 0.0
            reasons = []
            
            # Context-based scoring
            if context == 'header':
                if characteristics['style'] in ['professional', 'bold']:
                    score += 30
                    reasons.append("professional style")
                if characteristics['height'] == 'tall':
                    score += 20
                    reasons.append("tall height")
            
            elif context == 'logo':
                if characteristics['style'] in ['bold', 'solid']:
                    score += 30
                    reasons.append("bold style")
                if characteristics['readability'] == 'high':
                    score += 20
                    reasons.append("high readability")
            
            elif context == 'banner':
                if characteristics['width'] == 'wide':
                    score += 25
                    reasons.append("wide format")
                if characteristics['style'] == 'bold':
                    score += 25
                    reasons.append("bold style")
            
            elif context == 'title':
                if characteristics['height'] == 'tall':
                    score += 25
                    reasons.append("tall height")
                if characteristics['readability'] == 'high':
                    score += 25
                    reasons.append("readable")
            
            # Text length scoring
            text_length = len(text)
            if text_length <= 5:
                if characteristics['width'] == 'wide':
                    score += 15
                    reasons.append("good for short text")
            elif text_length <= 15:
                if characteristics['width'] == 'medium':
                    score += 15
                    reasons.append("good for medium text")
            else:
                if characteristics['width'] == 'narrow':
                    score += 15
                    reasons.append("good for long text")
            
            # Width constraint scoring
            if max_width:
                estimated_width = len(text) * (10 if characteristics['width'] == 'wide' else 
                                              7 if characteristics['width'] == 'medium' else 5)
                if estimated_width <= max_width:
                    score += 20
                    reasons.append("fits width constraint")
                else:
                    score -= 30
                    reasons.append("exceeds width constraint")
            
            # Character type scoring
            if text.isupper():
                if characteristics['style'] in ['bold', 'solid']:
                    score += 10
                    reasons.append("good for uppercase")
            
            if any(char.isdigit() for char in text):
                if characteristics['readability'] == 'high':
                    score += 10
                    reasons.append("clear digits")
            
            reason_text = ", ".join(reasons[:3])  # Top 3 reasons
            suggestions.append((font_name, score, reason_text))
        
        # Sort by score (descending)
        suggestions.sort(key=lambda x: x[1], reverse=True)
        
        return suggestions
    
    def get_best_font(self, text: str, context: str = 'general', 
                     max_width: Optional[int] = None) -> str:
        """Get the single best font recommendation.
        
        Args:
            text: Text to analyze
            context: Usage context
            max_width: Maximum width constraint
            
        Returns:
            Best font name
        """
        suggestions = self.suggest_font(text, context, max_width)
        return suggestions[0][0] if suggestions else 'standard'


class ContentAwareScaler:
    """Scale ASCII art while preserving important details."""
    
    def __init__(self):
        """Initialize content-aware scaler."""
        pass
    
    def scale(self, ascii_art: str, target_width: int, 
             preserve_aspect: bool = True) -> str:
        """Scale ASCII art to target width.
        
        Args:
            ascii_art: Input ASCII art
            target_width: Target width
            preserve_aspect: Preserve aspect ratio
            
        Returns:
            Scaled ASCII art
        """
        lines = ascii_art.split('\n')
        
        if not lines:
            return ascii_art
        
        current_width = max(len(line) for line in lines)
        
        if current_width == target_width:
            return ascii_art
        
        if target_width > current_width:
            return self._expand(lines, target_width, preserve_aspect)
        else:
            return self._compress(lines, target_width, preserve_aspect)
    
    def _expand(self, lines: List[str], target_width: int, 
               preserve_aspect: bool) -> str:
        """Expand ASCII art."""
        current_width = max(len(line) for line in lines)
        scale_factor = target_width / current_width
        
        result = []
        for line in lines:
            expanded = ''
            for char in line:
                # Repeat character based on scale factor
                repeat_count = max(1, int(scale_factor))
                expanded += char * repeat_count
            result.append(expanded)
        
        # Expand vertically if preserving aspect
        if preserve_aspect:
            vertical_scale = int(scale_factor)
            expanded_result = []
            for line in result:
                for _ in range(vertical_scale):
                    expanded_result.append(line)
            result = expanded_result
        
        return '\n'.join(result)
    
    def _compress(self, lines: List[str], target_width: int, 
                 preserve_aspect: bool) -> str:
        """Compress ASCII art intelligently."""
        current_width = max(len(line) for line in lines)
        scale_factor = target_width / current_width
        
        result = []
        for line in lines:
            compressed = ''
            step = 1.0 / scale_factor
            pos = 0.0
            
            while int(pos) < len(line):
                compressed += line[int(pos)]
                pos += step
            
            result.append(compressed[:target_width])
        
        # Compress vertically if preserving aspect
        if preserve_aspect:
            vertical_step = 1.0 / scale_factor
            compressed_result = []
            pos = 0.0
            
            while int(pos) < len(result):
                compressed_result.append(result[int(pos)])
                pos += vertical_step
            
            result = compressed_result
        
        return '\n'.join(result)


class AutoComposer:
    """Automatically compose multiple ASCII art elements."""
    
    def __init__(self):
        """Initialize auto composer."""
        pass
    
    def auto_layout(self, elements: List[str], canvas_width: int = 100,
                   canvas_height: int = 40, style: str = 'balanced') -> str:
        """Automatically arrange elements for best visual impact.
        
        Args:
            elements: List of ASCII art elements
            canvas_width: Canvas width
            canvas_height: Canvas height
            style: Layout style ('balanced', 'hierarchical', 'flow', 'centered')
            
        Returns:
            Composed ASCII art
        """
        if not elements:
            return ''
        
        if style == 'balanced':
            return self._balanced_layout(elements, canvas_width, canvas_height)
        elif style == 'hierarchical':
            return self._hierarchical_layout(elements, canvas_width, canvas_height)
        elif style == 'flow':
            return self._flow_layout(elements, canvas_width, canvas_height)
        elif style == 'centered':
            return self._centered_layout(elements, canvas_width, canvas_height)
        else:
            return self._balanced_layout(elements, canvas_width, canvas_height)
    
    def _balanced_layout(self, elements: List[str], width: int, height: int) -> str:
        """Create balanced grid layout."""
        from generators.composition import Compositor
        
        compositor = Compositor()
        
        # Calculate optimal grid dimensions
        num_elements = len(elements)
        cols = int(num_elements ** 0.5) + 1
        
        return compositor.grid_layout(elements, cols=cols, spacing=2)
    
    def _hierarchical_layout(self, elements: List[str], width: int, height: int) -> str:
        """Create hierarchical layout (largest first)."""
        from generators.composition import Compositor
        
        compositor = Compositor()
        
        # Sort by size (largest first)
        sorted_elements = sorted(
            elements,
            key=lambda e: len(e.split('\n')) * max(len(line) for line in e.split('\n')),
            reverse=True
        )
        
        # Stack vertically with largest on top
        return compositor.vertical_concat(*sorted_elements, spacing=2)
    
    def _flow_layout(self, elements: List[str], width: int, height: int) -> str:
        """Create flowing layout."""
        from generators.composition import Compositor
        
        compositor = Compositor()
        
        # Arrange in reading order (left to right, top to bottom)
        return compositor.horizontal_concat(*elements, spacing=3)
    
    def _centered_layout(self, elements: List[str], width: int, height: int) -> str:
        """Create centered layout."""
        result = []
        
        for element in elements:
            lines = element.split('\n')
            centered_lines = []
            
            for line in lines:
                padding = (width - len(line)) // 2
                centered_lines.append(' ' * padding + line)
            
            result.extend(centered_lines)
            result.append('')  # Spacing
        
        return '\n'.join(result)


class StyleAnalyzer:
    """Analyze and suggest styles for ASCII art."""
    
    def __init__(self):
        """Initialize style analyzer."""
        pass
    
    def analyze_text(self, text: str) -> Dict[str, any]:
        """Analyze text to suggest appropriate styles.
        
        Args:
            text: Text to analyze
            
        Returns:
            Dictionary of style suggestions
        """
        analysis = {
            'length': len(text),
            'has_numbers': any(c.isdigit() for c in text),
            'has_special': any(not c.isalnum() and not c.isspace() for c in text),
            'is_uppercase': text.isupper(),
            'is_lowercase': text.islower(),
            'is_mixed': not text.isupper() and not text.islower(),
            'word_count': len(text.split()),
        }
        
        # Suggest effects
        effects = []
        if analysis['is_uppercase'] and analysis['length'] <= 10:
            effects.append(('3d', 'uppercase text looks great in 3D'))
            effects.append(('shadow', 'adds depth to bold text'))
        
        if analysis['word_count'] == 1 and analysis['length'] <= 8:
            effects.append(('glow', 'single words benefit from glow'))
            effects.append(('outline', 'makes short text stand out'))
        
        if analysis['length'] > 20:
            effects.append(('simple', 'keep long text simple'))
        
        analysis['suggested_effects'] = effects
        
        # Suggest colors
        colors = []
        if 'error' in text.lower() or 'fail' in text.lower():
            colors.append(('fire', 'red/orange for errors'))
        elif 'success' in text.lower() or 'pass' in text.lower():
            colors.append(('forest', 'green for success'))
        elif 'info' in text.lower() or 'data' in text.lower():
            colors.append(('ocean', 'blue for information'))
        else:
            colors.append(('rainbow', 'colorful and eye-catching'))
        
        analysis['suggested_colors'] = colors
        
        return analysis
    
    def suggest_complete_style(self, text: str, context: str = 'general') -> Dict[str, str]:
        """Suggest complete style configuration.
        
        Args:
            text: Text to style
            context: Usage context
            
        Returns:
            Complete style configuration
        """
        analysis = self.analyze_text(text)
        selector = SmartFontSelector()
        
        # Get best font
        font = selector.get_best_font(text, context)
        
        # Get best effect
        effect = analysis['suggested_effects'][0][0] if analysis['suggested_effects'] else None
        
        # Get best color
        color = analysis['suggested_colors'][0][0] if analysis['suggested_colors'] else None
        
        return {
            'font': font,
            'effect': effect,
            'color': color,
            'reasoning': {
                'font': selector.suggest_font(text, context)[0][2],
                'effect': analysis['suggested_effects'][0][1] if analysis['suggested_effects'] else 'no effect needed',
                'color': analysis['suggested_colors'][0][1] if analysis['suggested_colors'] else 'default colors'
            }
        }


class SmartGenerator:
    """High-level smart ASCII art generator."""
    
    def __init__(self):
        """Initialize smart generator."""
        self.font_selector = SmartFontSelector()
        self.style_analyzer = StyleAnalyzer()
        self.auto_composer = AutoComposer()
        self.scaler = ContentAwareScaler()
    
    def generate_smart(self, text: str, context: str = 'general',
                      max_width: Optional[int] = None,
                      apply_effects: bool = True,
                      apply_colors: bool = False) -> Tuple[str, Dict]:
        """Generate ASCII art with smart style selection.
        
        Args:
            text: Text to convert
            context: Usage context
            max_width: Maximum width
            apply_effects: Whether to apply suggested effects
            apply_colors: Whether to apply suggested colors
            
        Returns:
            Tuple of (ascii_art, metadata)
        """
        from generators.text_art import TextArtGenerator
        from generators.text_effects import TextEffects
        from generators.color_art import GradientGenerator
        from utils.config import Config
        
        # Get style suggestions
        style = self.style_analyzer.suggest_complete_style(text, context)
        
        # Generate base art
        config = Config(color_enabled=apply_colors)
        gen = TextArtGenerator(config)
        art = gen.generate(text, font=style['font'])
        
        # Apply effects if requested
        if apply_effects and style['effect']:
            effects = TextEffects()
            
            if style['effect'] == '3d':
                art = effects.add_3d_effect(art)
            elif style['effect'] == 'shadow':
                art = effects.add_shadow(art)
            elif style['effect'] == 'glow':
                art = effects.add_glow(art)
            elif style['effect'] == 'outline':
                art = effects.add_outline(art)
        
        # Apply colors if requested
        if apply_colors and style['color']:
            gradient_gen = GradientGenerator()
            art = gradient_gen.apply_gradient_to_text(art, style['color'])
        
        # Scale if needed
        if max_width:
            art = self.scaler.scale(art, max_width)
        
        # Metadata
        metadata = {
            'font': style['font'],
            'effect': style['effect'],
            'color': style['color'],
            'reasoning': style['reasoning'],
            'text_analysis': self.style_analyzer.analyze_text(text)
        }
        
        return art, metadata
    
    def generate_variations(self, text: str, count: int = 5) -> List[Tuple[str, Dict]]:
        """Generate multiple variations with different styles.
        
        Args:
            text: Text to convert
            count: Number of variations
            
        Returns:
            List of (ascii_art, metadata) tuples
        """
        from generators.text_art import TextArtGenerator
        from utils.config import Config
        
        config = Config()
        gen = TextArtGenerator(config)
        
        variations = []
        fonts = ['standard', 'banner', 'block', 'slant', 'small']
        
        for i, font in enumerate(fonts[:count]):
            art = gen.generate(text, font=font)
            metadata = {
                'font': font,
                'variation': i + 1,
                'total_variations': count
            }
            variations.append((art, metadata))
        
        return variations

